# CodeBuild – Lambda Version

https://awstut.com/en/2024/05/04/codebuild-lambda-version-en/

# Architecture

![fa-149-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/64f9e26a-6392-4f22-918a-5111a6c16d8b)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-149.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-149/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-149 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-149/fa-149.yaml \
--capabilities CAPABILITY_IAM
```
