#!/usr/bin/env python3.7

import boto3

ec2 = boto3.resource('ec2')

#instance = ec2.create_instances(
    #ImageId='ami-0b0dcb5067f052a63',
    #MinCount=3,
    #MaxCount=3,
    #InstanceType='t2.micro',
   # )
#print(instance)

# We'll be stopping our instances now 

ec2.Instance('i-06ee3df3958780598').stop()
ec2.Instance('i-06663687c94affc1a').stop()
ec2.Instance('i-094209236835c2c7b').stop()