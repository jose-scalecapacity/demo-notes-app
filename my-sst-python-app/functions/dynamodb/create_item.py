import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('my-sst-table')  

def handler(event, context):
    table.put_item(
        Item={
            'id': '123',
            'name': 'Example Item'
        }
    )