import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('my-sst-table')

def handler(event, context):
    try:
        # Assuming your primary key is named 'id'
        item_id = event.get('pathParameters', {}).get('id')  
        data = json.loads(event.get('body', '{}'))  # Parse update data from request body

        if not item_id or not data:
            return {
                'statusCode': 400,
                'body': 'Please provide an item ID and update data.'
            }

        # Build the UpdateExpression and ExpressionAttributeValues
        update_expression = 'SET '
        expression_attribute_values = {}
        for key, value in data.items():
            update_expression += f'{key} = :{key}, '
            expression_attribute_values[f':{key}'] = value
        update_expression = update_expression[:-2]  # Remove trailing comma

        response = table.update_item(
            Key={'id': item_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues='UPDATED_NEW'  # Returns the updated attributes
        )

        return {
            'statusCode': 200,
            'body': json.dumps(response['Attributes'])  
        }

    except Exception as e:
        print(repr(e))
        return {
            'statusCode': 500,
            'body': 'An error occurred while updating the item.'
        }