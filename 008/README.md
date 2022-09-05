# Attaching EBS to Linux Instance

https://awstut.com/en/2021/12/12/attaching-ebs-to-linux-instance/

# Architecture

![fa-008-diagram](https://user-images.githubusercontent.com/84276199/188453415-a6572913-d712-4bb7-a5d5-1fb63bbf5854.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-008.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-008/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-008 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-008/fa-008.yaml \
--capabilities CAPABILITY_IAM
```
