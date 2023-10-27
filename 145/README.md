# Introduction to EC2 Image Builder using CloudFormation

https://awstut.com/en/2023/10/28/introduction-to-ec2-image-builder-using-cloudformation-en/

# Architecture

![fa-145-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/c6ce61c6-585a-4f92-92c2-da758e80bdbe)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-145.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-145/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-145 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-145/fa-145.yaml \
--capabilities CAPABILITY_IAM
```
