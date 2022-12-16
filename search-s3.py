#!/usr/bin/env python3.7

# Searching for s3 buckets 
import boto3

resource=boto3.resource
resource=boto3.resource("s3")
bucket_list=list(resource.buckets.all())

len(bucket_list)

for bucket in resource.buckets.all():
    print(bucket.name)