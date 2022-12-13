# We're launching an s3 bucket in python using boto3
import boto3

aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("breezypythonbucketv2")
response = bucket.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
    
)

print(response)