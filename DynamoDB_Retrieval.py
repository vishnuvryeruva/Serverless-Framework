import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('planets')

def lambda_handler(event, context):
    table.put_item(
        Item = {
            'id': 'pluto',
            'temp': 'extreme cold'
        }
    )
    response = 'Item added'
    return {
        'statusCode': 200,
        'body': response
    }
