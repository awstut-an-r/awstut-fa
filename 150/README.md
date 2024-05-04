# Execute CodeBuild within Step Functions

https://awstut.com/en/2024/05/05/execute-codebuild-within-step-functions-en/

# Architecture

![fa-150-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/17b71075-ae25-4127-b7b3-18f3a6a8144b)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-150.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-150/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-150 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-150/fa-150.yaml \
--capabilities CAPABILITY_IAM
```
