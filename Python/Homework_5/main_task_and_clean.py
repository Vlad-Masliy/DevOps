import boto3
import json


iam = boto3.client('iam')
iamr = boto3.resource('iam')

""" Create Groups """

DevelopersGroup = iamr.Group('Developers')
DevOpsGroup = iamr.Group('DevOps')
ReadOnlyGroup = iamr.Group('ReadOnly')

iamr.create_group(
    GroupName = 'Developers'
)

response = iam.attach_group_policy(
    GroupName='Developers',
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess',
)

iamr.create_group(
    GroupName='DevOps'
)

response = iam.attach_group_policy(
    GroupName='DevOps',
    PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess',
)

iamr.create_group(
    GroupName='ReadOnly'
)

response = iam.attach_group_policy(
    GroupName='ReadOnly',
    PolicyArn='arn:aws:iam::aws:policy/ReadOnlyAccess',
)

""" Create Users """

user1 = iamr.User('Standart')
user2 = iamr.User('Service')
user3 = iamr.User('Admin')

user = user1.create('Standart')
user = user2.create('Service')
user = user3.create('Admin')

response = user1.add_group(
    GroupName='ReadOnly',
)

response = user2.add_group(
    GroupName='ReadOnly',
)

response = user3.add_group(
    GroupName='ReadOnly',
)

access_key_pair = iam.create_access_key(
    UserName ='Service'
)

response = user3.attach_policy(
    UserName ='Admin',
    PolicyArn = 'arn:aws:iam::aws:policy/IAMUserSSHKeys',
)

""" Create Roles """

ContentBackupRole = iamr.Role('content_backup')
IamKeysRotationRole = iamr.Role('IAM_keys_rotation')
DownloadingFilesRole = iamr.Role('downloading_files')

assume_role_policy_document = json.dumps({
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Principal": {
            "Service": [
              "iam.amazonaws.com",
              "s3.amazonaws.com",
            ]        
        },
        "Action": "sts:AssumeRole",
        }
    ]
})

iam.create_role(
    RoleName = "content_backup",
    AssumeRolePolicyDocument = assume_role_policy_document
)

response = ContentBackupRole.attach_policy(
    RoleName ='content_backup',
    PolicyArn = 'arn:aws:iam::aws:policy/AmazonS3FullAccess',
)

response = ContentBackupRole.attach_policy(
    RoleName ='content_backup',
    PolicyArn = 'arn:aws:iam::aws:policy/AmazonGlacierFullAccess',
)

iam.create_role(
    RoleName = "IAM_keys_rotation",
    AssumeRolePolicyDocument = assume_role_policy_document
)

response = IamKeysRotationRole.attach_policy(
    RoleName ='IAM_keys_rotation',
    PolicyArn = 'arn:aws:iam::aws:policy/IAMUserChangePassword',
)

response = IamKeysRotationRole.attach_policy(
    RoleName ='IAM_keys_rotation',
    PolicyArn = 'arn:aws:iam::aws:policy/IAMUserSSHKeys',
)

role = iam.create_role(
    RoleName = "downloading_files",
    AssumeRolePolicyDocument = assume_role_policy_document
)

response = DownloadingFilesRole.attach_policy(
    RoleName ='downloading_files',
    PolicyArn = 'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess',
)

""" Uncomment for delete created resources """

""" Delete Users """

# response = user1.remove_group(
#     GroupName='ReadOnly',
# )

# response = user1.delete('Standart')

# response = user2.remove_group(
#     GroupName='ReadOnly',
# )

# response = iam.delete_access_key(
#     UserName='Service',
#     AccessKeyId = access_key_pair['AccessKey']['AccessKeyId']
# )

# response = user2.delete('Service',)

# response = user3.remove_group(
#     GroupName='ReadOnly',
# )

# response = user3.detach_policy(
#     UserName ='Admin',
#     PolicyArn='arn:aws:iam::aws:policy/IAMUserSSHKeys',
# )

# response = user3.delete('Admin')

# """Delete Groups """

# response = iam.detach_group_policy(
#     GroupName='Developers',
#     PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess',
# )

# response = DevelopersGroup.delete('Developers')

# response = iam.detach_group_policy(
#     GroupName='DevOps',
#     PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess',
# )

# response = DevOpsGroup.delete('DevOps')

# response = iam.detach_group_policy(
#     GroupName='ReadOnly',
#     PolicyArn='arn:aws:iam::aws:policy/ReadOnlyAccess',
# )

# response = ReadOnlyGroup.delete('ReadOnly')

# """Delete Roles """

# response = ContentBackupRole.detach_policy(
#     RoleName ='content_backup',
#     PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess'
# )

# response = ContentBackupRole.detach_policy(
#     RoleName ='content_backup',
#     PolicyArn='arn:aws:iam::aws:policy/AmazonGlacierFullAccess'
# )

# response = ContentBackupRole.delete('content_backup')

# response = IamKeysRotationRole.detach_policy(
#     RoleName ='IAM_keys_rotation',
#     PolicyArn='arn:aws:iam::aws:policy/IAMUserChangePassword'
# )

# response = IamKeysRotationRole.detach_policy(
#     RoleName ='IAM_keys_rotation',
#     PolicyArn='arn:aws:iam::aws:policy/IAMUserSSHKeys'
# )

# response = IamKeysRotationRole.delete('IAM_keys_rotation')

# response = DownloadingFilesRole.detach_policy(
#     RoleName = "downloading_files",
#     PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
# )

# response = DownloadingFilesRole.delete('downloading_files')
