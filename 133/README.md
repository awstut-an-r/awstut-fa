# Introduction to Amplify with CloudFormation

https://awstut.com/en/2023/06/17/introduction-to-amplify-with-cloudformation-en/

# Architecture

![fa-133-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/c6e83b70-79c1-4787-94c1-8af0dc05c997)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-133.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-133/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-133 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-133/fa-133.yaml \
--capabilities CAPABILITY_IAM
```
