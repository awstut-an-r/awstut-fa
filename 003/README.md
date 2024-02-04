# Accessing Linux instance via SSM Session Manager

https://awstut.com/en/2021/12/11/accessing-a-linux-instance-via-ssm-session-manager/

# Architecture

![fa-003-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/42540b90-56ed-4adc-a46d-5ad53bb5007a)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-003.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-003/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-003 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-003/fa-003.yaml \
--capabilities CAPABILITY_IAM
```
