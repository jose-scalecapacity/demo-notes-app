import json
import boto3

def lambda_handler(event, context):
  # Get the file ID from the path parameter
  file_id = event['pathParameters']['id']

  # Access DynamoDB client
  dynamodb_client = boto3.client('dynamodb')

  # Get the transcript URL (or relevant data) from DynamoDB
  response = dynamodb_client.get_item(TableName="MyTable", Key={"id": {"S": file_id}})

  # Check if item exists
  if 'Item' not in response:
      return {
          'statusCode': 404,
          'body': f"File with ID: {file_id} not found."
      }

  # Extract the transcript URL (or relevant data)
  item = response['Item']
  transcript_url = item.get('transcript', {}).get('S')

  # You can optionally check if the transcript is already available
  # and avoid unnecessary calls to Transcribe if it exists.

  # (Optional) Retrieve the transcript from Transcribe (if not stored in DynamoDB)
  # uncomment this section and configure the logic for retrieving the transcript
  # transcribe_client = boto3.client('transcribe')
  # transcript_url = None  # replace with logic to get transcript from Transcribe

  return {
      'statusCode': 200,
      'body': f"Transcript URL: {transcript_url}" if transcript_url else "Transcript not available yet."
  }