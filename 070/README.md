# Email notification via CloudWatch Alarm when ECS CPU usage exceeds threshold

https://awstut.com/en/2022/08/11/email-notification-via-cloudwatch-alarm-when-ecs-cpu-usage-exceeds-threshold-en/

# Architecture

![fa-070-diagram](https://user-images.githubusercontent.com/84276199/204089326-68687bab-aeea-4135-972a-23d89037aa70.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-070.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-070/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-070 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-070/fa-070.yaml \
--capabilities CAPABILITY_IAM
```
