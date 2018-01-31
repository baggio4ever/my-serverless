import json


def hello(event, context):
    if "headers" in event:
        origin = event["headers"]["origin"]  # どこから聞かれても返せるように
    else:
        origin = ""
    body = {
        "message": "Hello,Serverless!!",
        "input": event
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
