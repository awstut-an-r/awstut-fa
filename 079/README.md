# Define action in CodePipeline calls Lambda function to change desired number of Fargate tasks

https://awstut.com/en/2022/08/28/define-action-in-codepipeline-calls-lambda-function-to-change-desired-number-of-fargate-tasks-en/

# Architecture

![fa-079-diagram](https://user-images.githubusercontent.com/84276199/204129682-6fee2d71-77c2-40d4-834a-9ec554ebcaf4.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-079.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp ./templates s3://my-bucket/fa-079/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-079 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-079/fa-079.yaml \
--capabilities CAPABILITY_IAM
```
