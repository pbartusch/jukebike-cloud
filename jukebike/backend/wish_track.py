from __future__ import print_function
import json, boto3, os, uuid
import time
from datetime import datetime

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# set environment variable
TRACK_TABLE_NAME = os.environ['TRACK_TABLE_NAME']


def handler(event, context):
    print(event)
    body = json.loads(event["body"])
    print(body)
    track_uri = body["trackUri"]
    print(track_uri)
    username = body['username']

    track_table = dynamodb.Table(TRACK_TABLE_NAME)
    # put item in table
    response = track_table.put_item(
        Item={
            'id': str(uuid.uuid4()),
            'track_uri': track_uri,
            'username' : username,
            'timestamp' : int(time.mktime(datetime.now().timetuple()))
        }
    )
    print(TRACK_TABLE_NAME)
    print("PutItem succeeded:")

    # get info for the user
    # TODO use real track and player information
    queuePosition = track_table.item_count
    # multiply with guessed average of 3:00 minutes per track
    secondsToWait = queuePosition * (3*60)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps({
            'status': 'OK',
            'queuePosition': queuePosition,
            'secondsToWait': secondsToWait
        })
    }
