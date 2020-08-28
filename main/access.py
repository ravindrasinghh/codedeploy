import boto3
import os
import sys

terraform_operation = sys.argv[1]
account = sys.argv[2]
sts_connection = boto3.client('sts')
role_arns = {
    "dev" : "arn:aws:iam::659604645969:role/Account-B-role"
}
print(role_arns[account])
account_tokens = sts_connection.assume_role(
    RoleArn=role_arns[account],
    RoleSessionName="session_of_account"
)
os.environ["AWS_ACCESS_KEY_ID"] = account_tokens['Credentials']['AccessKeyId']
os.environ["AWS_SECRET_ACCESS_KEY"] = account_tokens['Credentials']['SecretAccessKey']
print(account_tokens['Credentials']['AccessKeyId'])
print(account_tokens['Credentials']['SecretAccessKey'])

client = boto3.client(
        's3',
        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
    )
print(client.list_buckets())

os.system("terraform init")
if terraform_operation == "plan":
    os.system("terraform plan")
else:
    os.system("terraform apply -auto-approve")
