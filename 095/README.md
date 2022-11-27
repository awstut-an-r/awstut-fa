# Try EBS Multi-Attach

https://awstut.com/en/2022/11/23/try-ebs-multi-attach-en/

# Architecture

![fa-095-diagram](https://user-images.githubusercontent.com/84276199/204133342-617499ef-131a-46f4-8cdf-fb0da1650732.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-095.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-095/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-095 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-095/fa-095.yaml \
--capabilities CAPABILITY_IAM
```
