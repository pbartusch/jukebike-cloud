
import json

# TODO one config method for whole cloud setup
from player_utils import CloudPlayer


# TODO: create lambda deployment package for depencencies instead of using deprecated: botocore.venored requests

def handler(event, context):
    search_text = event["queryStringParameters"]['input']

    tracks = CloudPlayer.search(search_text)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(tracks)
    };
