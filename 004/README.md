# Four ways to initialize Linux instance

https://awstut.com/en/2021/12/11/four-ways-to-initialize-a-linux-instance/

# Architecture

![fa-004-diagram](https://user-images.githubusercontent.com/84276199/188314790-3bcb00b8-1138-4ad2-a86c-5c5ddc4b5dd9.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-004.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-004/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-004 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-004/fa-004.yaml \
--capabilities CAPABILITY_IAM
```
