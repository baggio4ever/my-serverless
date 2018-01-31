import json


def byebye(event, context):
    if "headers" in event:
        origin = event["headers"]["origin"]  # どこから聞かれても返せるように
    else:
        origin = ""
    body = {
        "message": "Bye!,Serverless!!",
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
