# Measure CPU idle time for Fargate container using CloudWatch Metric Math

https://awstut.com/en/2022/08/11/measure-cpu-idle-time-for-fargate-container-using-cloudwatch-metric-math-en/

# Architecture

![fa-073-diagram](https://user-images.githubusercontent.com/84276199/204114018-9dbf472e-3200-4348-a6ab-2364b1252ba3.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-073.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-073/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-073 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-073/fa-073.yaml \
--capabilities CAPABILITY_IAM
```
