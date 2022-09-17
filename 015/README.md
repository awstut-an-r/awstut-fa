# Install CloudWatch Agent on Linux and collect data

https://awstut.com/en/2021/12/28/install-cloudwatch-agent-on-linux-and-collect-data/

# Architecture

![fa-015-diagram](https://user-images.githubusercontent.com/84276199/190858871-2f465fe2-8be1-4214-8472-fc997ff4f4f9.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-015.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-015/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-015 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-015/fa-015.yaml \
--capabilities CAPABILITY_IAM
```
