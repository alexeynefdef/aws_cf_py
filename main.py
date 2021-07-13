from datetime import date

import boto3

today = date.today()

message = {
    "date": today.strftime("%d/%m/%Y")
}

client = boto3.client(
    "lambda",
    region_name="eu-central-1",
    aws_access_key_id='',
    aws_secret_access_key='')

for i in range (10):

    response = client.invoke(
        FunctionName='',
        InvocationType='Event',
        LogType='Tail'
    )
