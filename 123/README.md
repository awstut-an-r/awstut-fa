# Use EventBridge and Lambda to deliver CloudWatch custom metrics on a regular basis

https://awstut.com/en/2023/04/02/use-eventbridge-and-lambda-to-deliver-cloudwatch-custom-metrics-on-a-regular-basis-en/

# Architecture

![fa-123-diagram](https://user-images.githubusercontent.com/84276199/229326844-cf1313c1-1500-44fa-8ed9-39d3bbd40243.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-123.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-123/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-123 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-123/fa-123.yaml \
--capabilities CAPABILITY_IAM
```
