# Build Elastic Beanstalk ALB environment using CloudFormation

https://awstut.com/en/2023/10/07/build-elastic-beanstalk-alb-environment-using-cloudformation-en/

# Architecture

![fa-143-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/55872b50-0d60-418b-bba9-c4357bf9ef4d)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-143.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-143/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-143 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-143/fa-143.yaml \
--capabilities CAPABILITY_IAM
```
