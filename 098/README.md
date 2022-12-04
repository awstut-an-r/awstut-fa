# Check resource change history in AWS Config

https://awstut.com/en/2022/12/04/check-resource-change-history-in-aws-config-en/

# Architecture

![fa-098-diagram](https://user-images.githubusercontent.com/84276199/205490860-349e92af-dae9-4208-8a00-d615fa0627ce.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-098.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-098/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-098 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-098/fa-098.yaml \
--capabilities CAPABILITY_IAM
```
