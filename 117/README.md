# Using CodePipeline to build CI/CD environment for CloudFormation

https://awstut.com/en/2023/02/11/using-codepipeline-to-build-cicd-environment-for-cloudformation-en/

# Architecture

![fa-117-diagram](https://user-images.githubusercontent.com/84276199/218216998-1ee0d4ae-2ffc-425a-a5ef-b446f5d022dc.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-117.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-117/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-117 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-117/fa-117.yaml \
--capabilities CAPABILITY_IAM
```
