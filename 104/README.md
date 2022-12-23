# Email notification via SNS when Nocompliant resources are detected by AWS Config

https://awstut.com/en/2022/12/24/email-notification-via-sns-when-nocompliant-resources-are-detected-by-aws-config-en/

# Architecture

![fa-104-diagram](https://user-images.githubusercontent.com/84276199/209410616-8b930c69-1a80-4c9b-afc5-b79219500dfa.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-104.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-104/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-104 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-104/fa-104.yaml \
--capabilities CAPABILITY_IAM
```
