from typing import Iterator

import boto3
import csv
from message import create_message


def handler(event, context):
    s3 = boto3.resource('s3')

    # get the details of the thing that was just created in S3
    detail = event['Records'][0]['s3']
    bucket_name: str = detail['bucket']['name']
    object_name: str = detail['object']['key']

    # get the actual thing that was just created
    csv_file = s3.Object(bucket_name=bucket_name, key=object_name)
    response = csv_file.get()
    data = response['Body'].read()

    # read the data into dictionaries using csv library
    rows: Iterator[dict[str, str]] = csv.DictReader(data.decode().splitlines())

    # iterate over each row and process it
    for row in rows:
        print(create_message(row))
        # process_row(row)
