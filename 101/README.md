# Email notifications via SNS when resources are changed using AWS Config

https://awstut.com/en/2022/12/11/email-notifications-via-sns-when-resources-are-changed-using-aws-config-en/

# Architecture

![fa-101-diagram](https://user-images.githubusercontent.com/84276199/209410863-014b704b-c9f2-4250-abae-e18b70c1b78e.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-101.yaml.

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
aws s3 cp . s3://my-bucket/fa-101/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-101 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-101/fa-101.yaml \
--capabilities CAPABILITY_IAM
```
