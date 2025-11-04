from aws_cdk import (
    Stack,
    aws_s3,
    aws_lambda as lambda_,
aws_s3_notifications as s3n,
)
from aws_cdk.aws_lambda_python_alpha import PythonFunction
from constructs import Construct

class LibraryInfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "InfraQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        # AWS Lambda to do the sending of the messages
        # S3 bucket for uploading the CSV file containing the information
        # a User Group, for people who are allowed to upload
        # some Users to go into that group
        # the connection between the S3 bucket and the Lambda
        # the Lambda has to listen for changes to the S3 bucket

        # the bucket into which things are uploaded
        bucket = aws_s3.Bucket(self, 'library-comms-info-bucket')

        # the Lambda function that's going to do the processing
        lambda_function = PythonFunction(
            self,
            "text-users",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="handler",
            entry="src",
            index="index.py"

        )

        # Give Lambda permissions to read objects from the bucket
        bucket.grant_read(lambda_function)

        # Trigger Lambda when object created in S3 bucket
        notification = s3n.LambdaDestination(lambda_function)
        bucket.add_event_notification(aws_s3.EventType.OBJECT_CREATED, notification)
