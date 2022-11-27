# Create Sorry content for ALB and Fargate(ECS) pattern

https://awstut.com/en/2022/10/02/create-sorry-content-for-alb-and-fargateecs-pattern-en/

# Architecture

![fa-086-diagram](https://user-images.githubusercontent.com/84276199/204131552-454c85e6-3f29-4f12-98ac-166618e2e8bd.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-086.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp ./templates s3://my-bucket/fa-086/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-086 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-086/fa-086.yaml \
--capabilities CAPABILITY_IAM
```
