# Use CFN's WaitCondition to wait for the Lambda deploy package to build

https://awstut.com/en/2023/09/16/use-cfns-waitcondition-to-wait-for-the-lambda-deploy-package-to-build-en/

# Architecture

![fa-142-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/70aefde3-06d9-44e5-9f02-73ac60b43793)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-142.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-142/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-142 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-142/fa-142.yaml \
--capabilities CAPABILITY_IAM
```
