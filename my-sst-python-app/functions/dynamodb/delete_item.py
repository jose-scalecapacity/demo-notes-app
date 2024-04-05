import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('my-sst-table')

def handler(event, context):
    try:
        # Assuming your primary key is named 'id'
        item_id = event.get('pathParameters', {}).get('id')  

        if not item_id:
            return {
                'statusCode': 400,
                'body': 'Please provide an item ID.'
            }

        table.delete_item(
            Key={'id': item_id}
        )

        return {
            'statusCode': 200,
            'body': 'Item deleted successfully.' 
        }

    except Exception as e:
        print(repr(e))
        return {
            'statusCode': 500,
            'body': 'An error occurred while deleting the item.'
        }