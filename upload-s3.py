#!/usr/bin/env python3.7

#Uploading Files to S3 Bucket

import boto3
s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="beach.jpg",
    Bucket="breezypythonbucket",
    Key="beach.jpg")
    