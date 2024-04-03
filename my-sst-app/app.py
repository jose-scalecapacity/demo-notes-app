from aws_cdk import core as cdk
from aws_cdk.aws_apigateway import Api, ApiRoute, HttpMethod
from aws_cdk.aws_s3 import Bucket
from aws_cdk.aws_dynamodb import Attribute, AttributeType, Table
from aws_cdk import aws_transcribe as TranscriptionJob

class MySSTApp(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define S3 bucket
        self.bucket = Bucket(self, "MyBucket",
                             removal_policy=cdk.RemovalPolicy.DESTROY)

        # Define DynamoDB table
        self.table = Table(self, "MyTable",
                           partition_key=Attribute(name="id", type=AttributeType.STRING),
                           removal_policy=cdk.RemovalPolicy.DESTROY)

        # Define TranscriptionJob for asynchronous transcription processing
        self.transcription_job = TranscriptionJob(self, "MyTranscriptionJob",
                                                 bucket=self.bucket,
                                                 # ... other transcription job options
                                                 removal_policy=cdk.RemovalPolicy.DESTROY)

        # Grant access to S3 bucket and DynamoDB table from your Lambda functions
        # (code for Lambda function integration will be added later)

        api = Api(self, "MyApi",
          # ... other API options

          routes=[
              ApiRoute(path="/upload", handler="functions/upload.handler", http_method=HttpMethod.POST),
              ApiRoute(path="/transcribe/{id}", handler="functions/transcribe.handler", http_method=HttpMethod.GET),
          ])

        # Grant API Gateway access to S3 and DynamoDB (already defined in previous step)
        api.attach_permissions([self.bucket, self.table])
