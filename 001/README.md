# Attach instances in private subnet to ELB

https://awstut.com/en/2021/12/11/attaching-instances-in-private-subnet-to-elb/

# Architecture

![fa-001-diagram](https://user-images.githubusercontent.com/84276199/188146332-4695ffb2-1ee1-4e9c-89ab-2d8f8ea5a672.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-001.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-001/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-001 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-001/fa-001.yaml \
--capabilities CAPABILITY_IAM
```
