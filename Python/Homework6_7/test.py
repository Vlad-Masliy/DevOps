import os
import boto3
import logging
from botocore.exceptions import ClientError
import json


ses = boto3.client('ses')
sns = boto3.client('sns')
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    write_to_dynamodb(table_name = 'Python_Homework_7', name = 'Download_files', message = 'file xx aploaded to s3 at time')
    send_email(source_mail = 'vladyslav.maslii@nure.ua',destination_mail = 'vlad.maslii2019@gmail.com', message = 'file x aploaded to s3 at time')
    send_sms(phone_number = '+380965956540',message = 'file xx aploaded to s3 at time')


def write_to_dynamodb(table_name, name, message):
    table = dynamodb.Table(table_name)
    table.update_item(
        Key={
                name:message,
            }
    )


def send_email(destination_mail, source_mail, message):
    ses.send_email(
        Destination={
            'ToAddresses': [destination_mail],
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': message,
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'aws notification',
            },
        },
        Source=source_mail,
    )


def send_sms(phone_number,message):
    sns.publish(
        PhoneNumber=phone_number,
        Message=message
    )
