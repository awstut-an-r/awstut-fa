# Backup to S3 every time you push to CodeCommit

https://awstut.com/en/2023/07/15/backup-to-s3-every-time-you-push-to-codecommit-en/

# Architecture

![fa-136-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/7433c3a7-2b1b-4ddd-a60c-4f39b3d59a50)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-136.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-136/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-136 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-136/fa-136.yaml \
--capabilities CAPABILITY_IAM
```
