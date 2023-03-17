# Use EventBridge rule to run SSM Automation runbook periodically

https://awstut.com/en/2023/03/18/use-eventbridge-rule-to-run-ssm-automation-runbook-periodically-en/

# Architecture

![fa-122-diagram](https://user-images.githubusercontent.com/84276199/226046455-7a843e6f-3af0-4747-b4dc-45c2b5802d19.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-122.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-122/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-122 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-122/fa-122.yaml \
--capabilities CAPABILITY_IAM
```
