#!/usr/bin/env python3.7
# We're creating an SQS Queue
import boto3 

sqs = boto3.client('sqs')
response = sqs.create_queue(
    QueueName='Week15ProjectQueue',
    Attributes={
        'DelaySeconds': '30',
        'MessageRetentionPeriod': '86400'
    }
)

print(response['QueueUrl']) 



