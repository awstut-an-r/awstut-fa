# Create AWS IoT rules and republish MQTT messages

https://awstut.com/en/2024/08/10/use-cloudformation-to-specify-sms-short-message-as-the-destination-for-sns-notifications-en/

# Architecture

![fa-159-diagram](https://github.com/user-attachments/assets/fe291df0-d096-4114-98e2-606b0b3e0ef6)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-159.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-159/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-159 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-159/fa-159.yaml \
--capabilities CAPABILITY_IAM
```
