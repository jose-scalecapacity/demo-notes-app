import boto3
from boto3 import botocore
from typing import Any, Dict

def handler(event: Dict[str, Any], context) -> Dict[str, Any]:
  """Uploads a file to a temporary S3 bucket."""

  # Extract the uploaded file data from the event
  try:
    file_data = event['body']
    filename = event['filename']  # Assuming filename is also provided in the event
  except KeyError:
    return {
      "statusCode": 400,
      "body": "Missing required fields: 'body' or 'filename'"
    }

  # Create a temporary S3 bucket name (replace with your naming convention)
  bucket_name = f"my-temporary-bucket-{context.aws_request_id}"

  # Create S3 client
  s3_client = boto3.client('s3')

  # Create the temporary S3 bucket
  try:
    s3_client.create_bucket(Bucket=bucket_name)
  except botocore.exceptions.ClientError as e:
    error_message = str(e)
    if 'BucketAlreadyOwnedByYou' in error_message:
      # Handle scenario where bucket already exists (optional)
      pass
    else:
      return {
        "statusCode": 500,
        "body": f"Error creating S3 bucket: {error_message}"
      }

  # Upload the file to the S3 bucket
  try:
    s3_client.put_object(Body=file_data, Bucket=bucket_name, Key=filename)
  except botocore.exceptions.ClientError as e:
    return {
      "statusCode": 500,
      "body": f"Error uploading file to S3: {str(e)}"
    }

  # Success message with temporary S3 bucket name for reference
  return {
    "statusCode": 200,
    "body": f"File uploaded successfully to temporary S3 bucket: {bucket_name}"
  }