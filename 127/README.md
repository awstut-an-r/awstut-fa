# Using Amazon ECS Exec to access ECS (Fargate) containers in private subnet

https://awstut.com/en/2023/05/03/using-amazon-ecs-exec-to-access-ecs-fargate-containers-in-private-subnet-en/

# Architecture

![fa-127-diagram](https://user-images.githubusercontent.com/84276199/235791276-75565f08-e0ad-4e68-bb60-01908ca56b53.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-127.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-127/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-127 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-127/fa-127.yaml \
--capabilities CAPABILITY_IAM
```
