# Introduction to Fargate with CloudFormation

https://awstut.com/en/2022/01/25/introduction-to-fargate-with-cloudformation/

# Architecture

![fa-018-diagram](https://user-images.githubusercontent.com/84276199/190931404-d2cacdf3-98c6-4e7d-887b-91ede36de44e.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-018.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-018/ --recursive
```

## CloudFormation Stack Creation

### Create ECR stack

```bash
aws cloudformation create-stack \
--stack-name fa-018-ecr \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-018/fa-018-ecr.yaml
```

### Create other stacks

```bash
aws cloudformation create-stack \
--stack-name fa-018 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-018/fa-018.yaml \
--capabilities CAPABILITY_IAM
```
