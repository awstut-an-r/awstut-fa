# Introduction to X-Ray – Tracing incoming requests for Fargate container

https://awstut.com/en/2022/08/13/introduction-to-x-ray-tracing-incoming-requests-for-fargate-container-en/

# Architecture

![fa-074-diagram](https://user-images.githubusercontent.com/84276199/204114340-4ac9e338-bac2-4fd2-893e-4c096016b53b.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-074.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-074/ --recursive
```

## ECR Stack Creation and RCR Repository Preparation

```bash
aws cloudformation create-stack --stack-name fa-074-ecr --template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-074/fa-074-ecr.yaml

aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin [account-id].dkr.ecr.ap-northeast-1.amazonaws.com

docker build -t fa-074 .

docker tag fa-074:latest [account-id].dkr.ecr.ap-northeast-1.amazonaws.com/fa-074:latest

docker push [account-id].dkr.ecr.ap-northeast-1.amazonaws.com/fa-074:latest
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-074 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-074/fa-074.yaml \
--capabilities CAPABILITY_IAM
```
