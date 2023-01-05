# RDS Multi-AZ deployment using CFN

https://awstut.com/en/2023/01/05/rds-multi-az-deployment-using-cfn-en/

# Architecture

![fa-110-diagram](https://user-images.githubusercontent.com/84276199/210733565-611f1f49-627f-4cb9-8109-b60f4287a6f4.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-110.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-110/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-110 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-110/fa-110.yaml \
--capabilities CAPABILITY_IAM
```
