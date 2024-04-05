import base64
import boto3
import uuid

from multipart import MultipartParser

# from boto3 import ClientError #TODO: throws error; probably version issue
from typing import Any, Dict


def handler(event, context):
  """Uploads a file to a temporary S3 bucket."""

  bucket_name = f"sst-tmp-bkt-{uuid.uuid4()}"

  s3_client = boto3.client('s3')

  # TODO: Either figure out how to PUT a not base64 encoded package or
  #       figure out how to extract the filename from the decoded package.

  # file_data = event['body']
  # filename = 'temp_file'

  return event

  # # Generate a unique bucket name using uuid
  # bucket_name = f"sst-tmp-bkt-{uuid.uuid4()}"

  # # Create S3 client
  # # TODO: Temporary credentials while permissions are sorted out
  # try:
  #   s3_client = boto3.client('s3')

  # except Exception as e: #TODO: Temp fix to possible version issue
  # # except ClientError as e:
  #     return {
  #       "statusCode": 500,
  #       "body": f"Error creating S3 client: {str(e)}"
  #     }
  
  # # Create the bucket (specify region if needed)
  # try:
  #   s3_client.create_bucket(Bucket=bucket_name)
       
  # except Exception as e:
  #   return f"Error creating bucket: {str(e)}"

  # # Uploads a file to the specified S3 bucket.
  # try:
  #   s3_client.put_object(Body=file_data, Bucket=bucket_name, Key=filename)

  # except Exception as e:
  #   return {
  #     "statusCode": 500,
  #     "body": f"Error uploading file to S3: {str(e)}"
  #   }

  # # Success message
  # return {
  #   "statusCode": 200,
  #   "body": f"File uploaded successfully to temporary S3 bucket: {bucket_name}"
  # }