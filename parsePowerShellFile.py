import json
import boto3
import re

class FileNotFound(Exception): pass
class ErrorResponse(Exception): pass

def lambda_handler(event, context):
    s3Client = boto3.resource('s3')
    print(event)
    try:
        psFile = s3Client.Object(event['Bucket'], event['Key'])
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            raise FileNotFound("The File Was Not Found")
        else:
            raise ErrorResponse(e.response['Error'])
    body = psFile.get()['Body'].read().decode('utf-8')
    body = re.sub(re.compile("/\*.*?\*/",re.DOTALL ), "", body)
    body = re.sub(re.compile("#.*?\n"), "", body)
    list = []
    for line in body.splitlines():
        if line.rstrip():
            list.append(line)
    return {
        'psCommand': list
    }
