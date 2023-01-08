# RDS Read Replica using CFN

https://awstut.com/en/2023/01/09/rds-read-replica-using-cfn-en/

# Architecture

![fa-111-diagram](https://user-images.githubusercontent.com/84276199/211221936-b5216aa0-3705-4eee-9101-5d213d9558f8.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-111.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-111/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-111 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-111/fa-111.yaml \
--capabilities CAPABILITY_IAM
```
