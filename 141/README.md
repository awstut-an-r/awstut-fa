# Introduction to Elastic Beanstalk with CloudFormation

https://awstut.com/en/2023/10/01/introduction-to-elastic-beanstalk-with-cloudformation-en/

# Architecture

![fa-141-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/798cc1e9-26fb-4105-8e10-d3c87b0d99ad)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-141.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-141/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-141 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-141/fa-141.yaml \
--capabilities CAPABILITY_IAM
```
