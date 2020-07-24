from botocore.vendored import requests
import json

# TODO one config method for whole cloud setup
from secret_config import SPOTIFY_AUTH

# TODO: create lambda deployment package for depencencies instead of using deprecated: botocore.venored requests
# TODO: create a track class? same as spotify.track class?

def handler(event, context):
    # get token
    token_response = requests.post('https://accounts.spotify.com/api/token', headers={
        'Authorization': 'Basic {}'.format(SPOTIFY_AUTH['base64basicAuth'])},
                                   data={'grant_type': 'client_credentials'})
    token = "Bearer " + json.loads(token_response.text)["access_token"]

    headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': token}

    search_text = event["queryStringParameters"]['input']
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

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(tracks)
    };
