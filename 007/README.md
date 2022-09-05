# Accessing Windows instance via SSM Session Manager

https://awstut.com/en/2021/12/11/accessing-a-windows-instance-via-ssm-session-manager/

# Architecture

![fa-007-diagram](https://user-images.githubusercontent.com/84276199/188451006-049e1f72-a340-4458-8f92-1a5b4517e0ff.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-007.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-007/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-007 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-007/fa-007.yaml \
--capabilities CAPABILITY_IAM
```
