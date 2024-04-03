import json
import boto3
import uuid

def lambda_handler(event, context):
  # Get uploaded file data from the event
  record = json.loads(event['body'])
  s3_file = record['Records'][0]['s3']
  bucket_name = s3_file['bucket']['name']
  file_key = s3_file['object']['key']

  # Access S3 client
  s3_client = boto3.client('s3')

  # Download the uploaded file from S3 (optional)
  # You can download the file and process it locally if needed.
  # downloaded_file = s3_client.get_object(Bucket=bucket_name, Key=file_key)['Body'].read()

  # Generate a unique ID (replace with your preferred ID generation logic)
  file_id = str(uuid.uuid4())

  # Store the file URL (or any relevant data) in DynamoDB
  dynamodb_client = boto3.client('dynamodb')
  dynamodb_client.put_item(TableName="MyTable", Item={
      "id": {"S": file_id},
      "audioUrl": {"S": f"s3://{bucket_name}/{file_key}"},
      # Add other relevant data fields if needed (e.g., transcript)
  })

  # Start an asynchronous transcription job (optional)
  # You can uncomment this section and configure the transcription job parameters
  # transcribe_client = boto3.client('transcribe')
  # transcribe_client.start_transcription_job(
  #     TranscriptionJobName=f"transcription_{file_id}",
  #     Media={'MediaFileUri': f's3://{bucket_name}/{file_key}'},
  #     # ... other transcription job options
  # )

  return {
      'statusCode': 200,
      'body': f"File uploaded successfully! ID: {file_id}"
  }