# Email notification of EventBridge event data via SNS

https://awstut.com/en/2022/12/17/email-notification-of-eventbridge-event-data-via-sns-en/

# Architecture

![fa-102-diagram](https://user-images.githubusercontent.com/84276199/209410973-da36988c-8696-4dca-bd84-0e5d005b1003.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-102.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

```yaml
Parameters:
  MailAddress:
    Type: String
    Default: mail@example.com
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-102/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-102 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-102/fa-102.yaml \
--capabilities CAPABILITY_IAM
```
