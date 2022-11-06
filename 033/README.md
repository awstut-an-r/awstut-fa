# Amazon Linux 2 How to Connect to RDS – ALL Engines

https://awstut.com/en/2022/03/21/amazon-linux-2-how-to-connect-to-rds-all-engines/

# Architecture

![fa-033-diagram](https://user-images.githubusercontent.com/84276199/200166104-eb8d2d6e-acdb-48ed-a7b0-b889405c5727.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-033.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-033/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-033 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-033/fa-033.yaml \
--capabilities CAPABILITY_IAM
```
