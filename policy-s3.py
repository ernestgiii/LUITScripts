#!/usr/bin/env python3

# Setting an s3 policy using boto3
import boto3
import json
s3_resource=boto3.client("s3")
s3_resource.put_bucket_policy(Bucket="breezypythonbucketv2",Policy='bucket_policy')
s3_resource.put_bucket_policy
bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': f'arn:aws:s3:::breezypthonbucketv2/*'
    }]
}

bucket_policy=json.dumps(bucket_policy)
s3 = boto3.client('s3')
s3_resource.put_bucket_policy(Bucket="breezypythonbucketv2", Policy=bucket_policy)
