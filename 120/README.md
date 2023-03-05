# Use EventBridge to execute Step Functions periodically

https://awstut.com/en/2023/03/05/use-eventbridge-to-execute-step-functions-periodically-en/

# Architecture

![fa-120-diagram](https://user-images.githubusercontent.com/84276199/222956131-df1fc242-f90e-461a-93dc-10daa68f54d3.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-120.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-120/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-120 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-120/fa-120.yaml \
--capabilities CAPABILITY_IAM
```
