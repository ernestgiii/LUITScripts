#!/usr/bin/env python3.7

# We're removing vpc

import boto3

client=boto3.client("ec2")

response = client.delete_vpc(
    VpcId= 'vpc-0d4f733c934b42993',
    )
response 