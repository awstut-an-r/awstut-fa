# 3 parterns to create Lambda with CloudFormation (S3/Inline/Container)

https://awstut.com/en/2022/02/02/3-parterns-to-create-lambda-with-cloudformation-s3-inline-container/

# Architecture

![fa-020-diagram](https://user-images.githubusercontent.com/84276199/191955310-99449822-3d08-4842-8172-0e83cd1dc080.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-020.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-020/ --recursive
```

## CloudFormation Stack Creation

### Create ECR stack

```bash
aws cloudformation create-stack \
--stack-name fa-020-s3-and-ecr \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-020-s3-and-ecr.yaml
```

### Upload Lambda Function Code to S3 Bucket

```bash
zip deploy_package.zip *
aws s3 cp deploy_package.zip s3://fa-020-bucket
```

### Push Image to ECR Repository

```bash
aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin [account-id].dkr.ecr.ap-northeast-1.amazonaws.com

docker build -t fa-020-repository .

docker tag fa-020-repository:latest [account-id].dkr.ecr.ap-northeast-1.amazonaws.com/fa-020-repository:latest

docker push [account-id].dkr.ecr.ap-northeast-1.amazonaws.com/fa-020-repository:latest
```

### Create other stacks

```bash
aws cloudformation create-stack \
--stack-name fa-020 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-020/fa-020.yaml \
--capabilities CAPABILITY_IAM
```
