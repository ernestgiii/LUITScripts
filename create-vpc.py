#!/usr/bin/env python3.7

import boto3

# Creating a VPC
client=boto3.client("ec2")
client.create_vpc(CidrBlock='10.0.0.0/24')

