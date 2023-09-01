# Loop in Step Functions until the condition is satisfied

https://awstut.com/en/2023/09/02/loop-in-step-functions-until-the-condition-is-satisfied-en/

# Architecture

![fa-140-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/bb948a86-2455-418d-b7e3-7351e2a18090)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-140.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-140/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-140 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-140/fa-140.yaml \
--capabilities CAPABILITY_IAM
```
