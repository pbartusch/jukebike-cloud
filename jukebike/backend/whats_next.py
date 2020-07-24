from __future__ import print_function
import json, boto3, os
from botocore.exceptions import ClientError

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# set environment variable
TRACK_TABLE_NAME = os.environ['TRACK_TABLE_NAME']

def get_timestamp(elem):
    return elem['timestamp']

def handler(event, context):
    table = dynamodb.Table(TRACK_TABLE_NAME)
    print(event)
    query_parameters = event.get("queryStringParameters")
    print(query_parameters)
    if query_parameters:
        track_played = query_parameters.get('trackPlayed')
        if track_played:
            response = table.delete_item(Key={'track_uri': track_played})

    # Scan items in table
    try:
        response = table.scan()
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        #TODO: refactor list operations
        #for i in response['Items']:
        track_list = response['Items']

        track_list.sort(key=get_timestamp)

        return_list = []
        for i in track_list:
            return_list.append(i['track_uri'])

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(return_list)
    }
