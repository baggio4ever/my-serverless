import json
from datetime import datetime
import boto3
from boto3.dynamodb.conditions import Key,Attr


def get_log(event, context):
    if event["headers"] is not None:
        if "origin" in event["headers"]:
            origin = event["headers"]["origin"]  # どこから聞かれても返せるように
        else:
            origin = ""
    else:
        origin = ""

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('dev-loglogs3')

    if( event["queryStringParameters"] is not None ):
        params = event["queryStringParameters"]
        user_id = params["user_id"]
        if user_id is not None:
#            user_id = event["queryStringParameters"]["user_id"]
            response = table.query(
                KeyConditionExpression=Key('user_id').eq( user_id )&Key('created_at').begins_with('2018/01')
            )
            items = response['Items']
        else:
            items = ["a","b"]
    else:
        items = ["x","Z"]

#    yy = json.loads(event["queryStringParameters"])

#    user_id = yy["user_id"]

#    user_id = json.loads(event["user_id"]);

#    response = table.query(
#        KeyConditionExpression=Key('user_id').eq( user_id )
#    )
#    items = response['Items']


    body = {
        "logs": items,
        "input": event,
        "origin":origin
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            "Access-Control-Allow-Origin":origin
        }
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
