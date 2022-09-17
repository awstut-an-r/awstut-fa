# Deliver VPC Flow Logs to S3/CloudWatch Logs

https://awstut.com/en/2021/12/25/deliver-vpc-flow-logs-to-s3-cloudwatch-logs/

# Architecture

![fa-014-diagram](https://user-images.githubusercontent.com/84276199/190858740-7d00064f-a159-4e15-bc04-193f63cae471.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-014.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-014/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-014 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-014/fa-014.yaml \
--capabilities CAPABILITY_IAM
```
