from __future__ import print_function
import json
from player_utils import CloudPlayer


def handler(event, context):
    print(event)
    http_method = event.get("httpMethod")

    if http_method == "GET":
        status_list = CloudPlayer.get_status()
    elif http_method == "POST":
        status_param = json.loads(event["body"])
        status_list = CloudPlayer.set_status(status_param)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(status_list)
    }
