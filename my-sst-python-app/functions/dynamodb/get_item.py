import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('my-sst-table')

def handler(event, context):
    try:
        # Assuming your primary key is named 'id'
        item_id = event.get('pathParameters', {}).get('id')  # Extract item ID from API path (if applicable)

        if not item_id:
            return {
                'statusCode': 400,
                'body': 'Please provide an item ID.'
            }

        response = table.get_item(Key={'id': item_id})
        item = response.get('Item')

        if item:
            return {
                'statusCode': 200,
                'body': json.dumps(item)
            }
        else:
            return {
                'statusCode': 404,
                'body': 'Item not found.'
            }

    except Exception as e:
        print(repr(e))
        return {
            'statusCode': 500,
            'body': 'An error occurred while fetching the item.'
        }
