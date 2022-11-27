# ECR Lifecycle Policy to automatically delete outdated images

https://awstut.com/en/2022/08/21/ecr-lifecycle-policy-to-automatically-delete-outdated-images-2/

# Architecture

![fa-077-diagram](https://user-images.githubusercontent.com/84276199/204116260-2f833295-1ae6-4de6-8ec2-f21afe8b13cf.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-077.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp ./templates s3://my-bucket/fa-077/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-077 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-077/fa-077.yaml \
--capabilities CAPABILITY_IAM
```
