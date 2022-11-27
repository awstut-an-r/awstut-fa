# Setup Approval Action in CodePipeline

https://awstut.com/en/2022/09/03/setup-approval-action-in-codepipeline-en/

# Architecture

![fa-080-diagram](https://user-images.githubusercontent.com/84276199/204129829-9fb40a94-e137-47cf-a371-ee4b65356aab.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-080.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp ./templates s3://my-bucket/fa-080/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-080 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-080/fa-080.yaml \
--capabilities CAPABILITY_IAM
```
