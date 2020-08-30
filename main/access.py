import boto3
import os
import sys

terraform_operation = sys.argv[1]
account = sys.argv[2]

sts_connection = boto3.client('sts')

role_arns = {
    "dev" : "arn:aws:iam::659604645969:role/Account-B-role"
}

account_tokens = sts_connection.assume_role(
    RoleArn=role_arns[account],
    RoleSessionName="session_of_account"
)

os.environ["AWS_ACCESS_KEY_ID"] = account_tokens['Credentials']['AccessKeyId']
os.environ["AWS_SECRET_ACCESS_KEY"] = account_tokens['Credentials']['SecretAccessKey']
os.environ["AWS_SESSION_TOKEN"] = account_tokens['Credentials']['SessionToken']

os.system("terraform init")

if terraform_operation == "plan":
    os.system("terraform plan")
elif terraform_operation == "apply":
    os.system("terraform apply -auto-approve")
else:
    print("Invalid Input")

    
