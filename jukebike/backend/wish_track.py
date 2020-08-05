from __future__ import print_function
import json
from player_utils import CloudPlayer


def handler(event, context):
    print(event)
    body = json.loads(event["body"])
    track_uri = body["trackUri"]
    username = body['username']

    #wish track
    queue_position, seconds_to_wait = CloudPlayer.wish_track(track_uri, username)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps({
            'status': 'OK',
            'queuePosition': queue_position,
            'secondsToWait': seconds_to_wait
        })
    }
