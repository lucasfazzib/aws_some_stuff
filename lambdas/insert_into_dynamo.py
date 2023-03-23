import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('People')
    try:
        # Insercao, pode haver mais transofrmacao aaqui..
        response = table.put_item(
          Item=event)
        return "Done"
    except:
        raise
    