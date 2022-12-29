#!/usr/bin/env python3.7

# We're creating a script to delete dynamo db table

import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('videogamecollectionDB')

table.delete()
