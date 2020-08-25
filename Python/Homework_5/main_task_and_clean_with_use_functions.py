import boto3
import json
from botocore.exceptions import ClientError
import logging


iam = boto3.client('iam')
iamr = boto3.resource('iam')
logging.basicConfig(level=logging.INFO, format='')


def create_group (GroupName, PolicyArn):
    try:
        iamr.create_group(
            GroupName = GroupName
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            logging.info(f'Group {GroupName} already exists.')
        else:
            raise

    iam.attach_group_policy(
        GroupName= GroupName,
        PolicyArn= PolicyArn,
    )

def delete_group (GroupName, PolicyArn):
    group = iamr.Group(GroupName)
    try: 
        iam.detach_group_policy(
            GroupName= GroupName,
            PolicyArn= PolicyArn,
        )
        group.delete(GroupName)
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchEntity':
            logging.info(f'Group {GroupName} not exists.')
        else:
            raise

def create_user (UserName, GroupName):
    user = iamr.User(UserName)
    try:
        user.create(
            UserName = UserName
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            logging.info(f'User {UserName} already exists.')
        else:
            raise

    user.add_group(
        GroupName= GroupName,
    )

def create_key(UserName):
    access_key_pair = iam.create_access_key(
        UserName = UserName
    )
    return access_key_pair['AccessKey']['AccessKeyId']

def delete_key(UserName, access_key_id):

    iam.delete_access_key(
        UserName = UserName,
        AccessKeyId = access_key_id
    )
    
def attach_policy_user (UserName, PolicyArn):
    user = iamr.User(UserName) 
    user.attach_policy(
        UserName = UserName,
        PolicyArn = PolicyArn,
    )

def delete_user (UserName, GroupName):
    user = iamr.User(UserName)
    try:
        user.remove_group(
            GroupName=GroupName,
        )
        user.delete(
            UserName=UserName
            )
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchEntity':
            logging.info(f'User {UserName} not exists.')
        else:
            raise

def detach_policy_user (UserName, PolicyArn):
    user = iamr.User(UserName)
    try: 
        user.detach_policy(
            UserName = UserName,
            PolicyArn = PolicyArn,
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchEntity':
            logging.info(f'User {UserName} not exists.')
        else:
            raise
   
def create_role (RoleName, ServiceName):
    assume_role_policy_document = json.dumps({
        "Version": "2012-10-17",
        "Statement": [
            {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                ServiceName,
                ]        
            },
            "Action": "sts:AssumeRole",
            }
        ]
    })
    try:
        iam.create_role(
            RoleName = RoleName,
            AssumeRolePolicyDocument = assume_role_policy_document
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            logging.info(f'Role {RoleName} already exists.')
        else:
            raise

def attach_policy(RoleName, PolicyArn):
    role = iamr.Role(RoleName)
    role.attach_policy(
        RoleName = RoleName,
        PolicyArn = PolicyArn
    )

def detach_policy (RoleName, PolicyArn):
    role = iamr.Role(RoleName)
    try:
        role.detach_policy(
            RoleName = RoleName,
            PolicyArn = PolicyArn
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchEntity':
            logging.info(f'Role {RoleName} not exists.')
        raise   

def delete_role (RoleName):
    role = iamr.Role(RoleName)
    try:
        role.delete(RoleName)
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchEntity':
            logging.info(f'Role {RoleName} not exists.')
        raise

""" Create Groups """

create_group('Developers', 'arn:aws:iam::aws:policy/AmazonS3FullAccess' )
create_group('DevOps', 'arn:aws:iam::aws:policy/AdministratorAccess' )
create_group('ReadOnly', 'arn:aws:iam::aws:policy/ReadOnlyAccess' )

# """ Create Users """

create_user('Standard', 'ReadOnly')
create_user('Service', 'ReadOnly')
create_user('Admin', 'ReadOnly')
key_id = create_key('Service')
attach_policy_user ('Admin', 'arn:aws:iam::aws:policy/IAMUserSSHKeys')

# """ Create Roles """

create_role ('content_backup', 'iam.amazonaws.com')
attach_policy ('content_backup', 'arn:aws:iam::aws:policy/AmazonS3FullAccess' )
attach_policy ('content_backup', 'arn:aws:iam::aws:policy/AmazonGlacierFullAccess' )
create_role ('IAM_keys_rotation', 'iam.amazonaws.com')
attach_policy ('IAM_keys_rotation', 'arn:aws:iam::aws:policy/IAMUserChangePassword' )
attach_policy ('IAM_keys_rotation', 'arn:aws:iam::aws:policy/IAMUserSSHKeys' )
create_role ('downloading_files', 'iam.amazonaws.com')
attach_policy ('downloading_files', 'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess' )

"""Uncomment for delete"""
""" Delete Users """

delete_key('Service', key_id)
detach_policy_user ('Admin', 'arn:aws:iam::aws:policy/IAMUserSSHKeys')
delete_user('Standard', 'ReadOnly')
delete_user('Service', 'ReadOnly')
delete_user('Admin', 'ReadOnly')

""" Delete Groups """

delete_group('Developers', 'arn:aws:iam::aws:policy/AmazonS3FullAccess' )
delete_group('DevOps', 'arn:aws:iam::aws:policy/AdministratorAccess' )
delete_group('ReadOnly', 'arn:aws:iam::aws:policy/ReadOnlyAccess' )

""" Delete Roles """

detach_policy ('content_backup', 'arn:aws:iam::aws:policy/AmazonS3FullAccess' )
detach_policy ('content_backup', 'arn:aws:iam::aws:policy/AmazonGlacierFullAccess' )
delete_role ('content_backup')
detach_policy ('IAM_keys_rotation', 'arn:aws:iam::aws:policy/IAMUserChangePassword' )
detach_policy ('IAM_keys_rotation', 'arn:aws:iam::aws:policy/IAMUserSSHKeys' )
delete_role ('IAM_keys_rotation')
detach_policy ('downloading_files', 'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess' )
delete_role ('downloading_files')
