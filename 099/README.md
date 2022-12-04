# Integrating two Lambda functions using EventBridge

https://awstut.com/en/2022/12/05/integrating-two-lambda-functions-using-eventbridge-en/

# Architecture

![fa-099-diagram](https://user-images.githubusercontent.com/84276199/205519882-5e21f71a-2b87-4b73-a896-b274aa165c81.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-099.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-099/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-099 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-099/fa-099.yaml \
--capabilities CAPABILITY_IAM
```
