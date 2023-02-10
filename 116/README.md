# Set up a Maintenance Window to schedule SSM Patch Manager

https://awstut.com/en/2023/02/05/set-up-maintenance-window-to-schedule-ssm-patch-manager-en/

# Architecture

![fa-116-diagram](https://user-images.githubusercontent.com/84276199/216806333-db765539-53af-465c-9a68-f9aaa2d29b3c.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-116.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-116/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-116 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-116/fa-116.yaml \
--capabilities CAPABILITY_IAM
```
