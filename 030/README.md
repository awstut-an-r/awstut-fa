# Scaling based on custom metrics (memory) – Linux

https://awstut.com/en/2022/03/05/scaling-based-on-custom-metrics-memory-linux/

# Architecture

![fa-030-diagram](https://user-images.githubusercontent.com/84276199/200165060-1551caaf-3f0d-4de6-9a99-04e3dbad6908.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-030.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-030/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-030 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-030/fa-030.yaml \
--capabilities CAPABILITY_IAM
```
