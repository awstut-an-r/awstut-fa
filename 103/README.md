# Email notification via SNS of AWS Config data matching EventBridge rules

https://awstut.com/en/2022/12/18/email-notification-via-sns-of-aws-config-data-matching-eventbridge-rules-en/

# Architecture

![fa-103-diagram](https://user-images.githubusercontent.com/84276199/209411069-2db3c966-b389-4407-b6a2-6166fa77222b.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-103.yaml.

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
aws s3 cp . s3://my-bucket/fa-103/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-103 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-103/fa-103.yaml \
--capabilities CAPABILITY_IAM
```
