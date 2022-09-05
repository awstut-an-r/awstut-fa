# Four ways to attach EBS to Windows instance

https://awstut.com/en/2021/12/12/attaching-ebs-to-a-windows-instance/

# Architecture

![fa-009-diagram](https://user-images.githubusercontent.com/84276199/188455268-c8e2394e-9aee-447f-8dfa-83f0ecd4c082.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-009.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-009/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-009 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-009/fa-009.yaml \
--capabilities CAPABILITY_IAM
```
