# Create ECS (Fargate) in Private Subnet

https://awstut.com/en/2022/07/24/create-ecs-fargate-in-private-subnet-en/

# Architecture

![fa-068-diagram](https://user-images.githubusercontent.com/84276199/204088869-15426049-ebe7-4831-bb3c-3aebd3cbcbe2.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-068.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-068/ --recursive
```

## CloudFormation Stack Creation

### ECR Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-068-ecr \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-068/fa-068-ecr.yaml
```

### Rest Stacks Creation

```bash
aws cloudformation create-stack \
--stack-name fa-068 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-068/fa-068.yaml \
--capabilities CAPABILITY_IAM
```
