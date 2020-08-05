import json
import os, boto3
import uuid
import time
from datetime import datetime
from secret_config import SPOTIFY_AUTH
from botocore.vendored import requests

from botocore.exceptions import ClientError

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
TRACK_TABLE_NAME = os.environ['TRACK_TABLE_NAME']
STATUS_TABLE_NAME = os.environ['STATUS_TABLE_NAME']
track_table = dynamodb.Table(TRACK_TABLE_NAME)
status_table = dynamodb.Table(STATUS_TABLE_NAME)


class CloudPlayer():
    def __get_timestamp(elem):
        return elem['timestamp']

    def __count_tracks(self):
        return track_table.item_count

    def __timeleft(self):
        # TODO use real track and player information
        return self.__count_tracks() * (3 * 60)

    @staticmethod
    def get_tracklist_uris(self):
        return_list = []
        # Scan items in table
        try:
            response = track_table.scan()
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            track_list = response['Items']

            track_list.sort(key=self.__get_timestamp, reverse=False)

            for i in track_list:
                return_list.append(i['track_uri'])

        return return_list

    @staticmethod
    def remove_from_tracklist(self, track_played_uri: str):
        track_table.delete_item(Key={'track_uri': track_played_uri})

    @staticmethod
    def reset_skipped_status(self):
        status_table.put_item(
            Item={
                'status_key': 'skip',
                'status_value': False,
            })

    @staticmethod
    def wish_track(self, track_uri: str, username: str):
        track_table.put_item(
            Item={
                'id': str(uuid.uuid4()),
                'track_uri': track_uri,
                'username': username,
                'timestamp': int(time.mktime(datetime.now().timetuple()))
            }
        )
        track_count = self.__count_tracks()
        timeleft = self.__timeleft()

        return track_count, timeleft

    @staticmethod
    def search(search_text: str):
        # get token
        token_response = requests.post('https://accounts.spotify.com/api/token', headers={
            'Authorization': 'Basic {}'.format(SPOTIFY_AUTH['base64basicAuth'])},
                                       data={'grant_type': 'client_credentials'})
        token = "Bearer " + json.loads(token_response.text)["access_token"]

        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': token}

        type = 'track'
        market = 'DE'
        limit = '10'
        offset = '0'

        payload = {'q': search_text, 'type': type, 'market': market, 'limit': limit, 'offset': offset}
        # example search query "https://api.spotify.com/v1/search?q=eminem%20stan&type=track&market=DE&limit=10&offset=0"
        search_response = requests.get("https://api.spotify.com/v1/search", headers=headers, params=payload)

        r_tracks = json.loads(search_response.text)["tracks"]["items"]
        tracks = []
        # simplify track from response
        for r_track in r_tracks:
            track = {}
            track["uri"] = r_track["uri"]
            track["artist"] = ""
            for r_artist in r_track["artists"]:
                track["artist"] = track["artist"] + r_artist["name"] + ", "
            track["artist"] = track["artist"][:-2]
            track["name"] = r_track["name"]
            track["popularity"] = r_track["popularity"]
            track["length"] = r_track["duration_ms"]
            track["image"] = (r_track["album"]["images"][0]["url"])
            tracks.append(track)

        return tracks

        def get_status():
            status_response = {}

            # defaults
            return_status = {'play': True, 'skip': False, 'volume': 50, 'track_list': []}

            status_table = dynamodb.Table(STATUS_TABLE_NAME)

            # Scan items in table
            try:
                response = status_table.scan()
            except ClientError as e:
                print(e.response['Error']['Message'])
            else:
                status_response = dict(response['Items'])

                # overwrite defaults with return values
                return_status.update(status_response)
            return return_status

        def set_status(status_param):
            allowed_status_keys = ['play', 'skip', 'volume']
            status_response = {}

            # filtering parameters with list comprehension to assure only allowed parameters are passed
            status_param_verified = dict(
                [[status_key, status_param[status_key]] for status_key in allowed_status_keys if
                 status_key in status_param])

            # get current state
            status_current = get_status()

            # use current status settings as default if not part in params (e.g. if only volume has been sent as
            # parameter)
            status_param_verified.update(status_current)

            status_table = dynamodb.Table(STATUS_TABLE_NAME)

            for status_key, status_value in status_param_verified:
                status_table.put_item(
                    Item={
                        'status_key': status_key,
                        'status_value': status_value
                    }
                )

            return get_status()
