# Attach Fargate in private subnet to ALB

https://awstut.com/en/2022/01/29/attach-fargate-in-private-subnet-to-elb-2/

# Architecture

![fa-019-diagram](https://user-images.githubusercontent.com/84276199/190933113-1a8c4edf-87f4-4e26-a4c9-df0a63b70b00.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-019.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-019/ --recursive
```

## CloudFormation Stack Creation

### Create ECR stack

```bash
aws cloudformation create-stack \
--stack-name fa-019-ecr \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-019/fa-010-ecr.yaml
```

### Push Image to ECR Repository

```bash
aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin [account-id].dkr.ecr.ap-northeast-1.amazonaws.com

docker build -t fa-019 .

docker tag fa-019:latest [account-id].dkr.ecr.ap-northeast-1.amazonaws.com/fa-019:latest

docker push [account-id].dkr.ecr.ap-northeast-1.amazonaws.com/fa-019:latest
```

### Create other stacks

```bash
aws cloudformation create-stack \
--stack-name fa-019 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-019/fa-019.yaml \
--capabilities CAPABILITY_IAM
```
