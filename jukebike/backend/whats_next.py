from __future__ import print_function
import json
from player_utils import CloudPlayer


def handler(event, context):
    print(event)
    query_parameters = event.get("queryStringParameters")
    print(query_parameters)
    if query_parameters:
        track_played = query_parameters.get('trackPlayed')
        if track_played:
            CloudPlayer.remove_from_tracklist(track_played)

        track_skipped = query_parameters.get('trackSkipped')
        if track_skipped:
            CloudPlayer.reset_skipped_status()

        return_list = CloudPlayer.getTrackListURIs()

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(return_list)
    }
