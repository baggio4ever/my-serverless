import json
from datetime import datetime
import boto3
from boto3.dynamodb.conditions import Key,Attr


def what_time_is_it_now(event, context):
    if "headers" in event:
        origin = event["headers"]["origin"]  # どこから聞かれても返せるように
    else:
        origin = ""
    dt = datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f')

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('dev-loglogs3')

    message = dt + " Lambdaでログってやるぜ"

    table.put_item(
        Item={
            "user_id": "hirayama",
            "created_at": dt,
            "message": message
        }
    )

    body = {
        "datetime": dt,
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
