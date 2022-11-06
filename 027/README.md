# Four Predefined Metrics for EC2 Auto Scaling Target Tracking Policy

https://awstut.com/en/2022/02/28/four-predefined-metrics-for-ec2-auto-scaling-target-tracking-policy/

# Architecture

![fa-027-diagram](https://user-images.githubusercontent.com/84276199/200162998-bc54382f-9228-49e8-a333-9c784a3508c6.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-027.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-027/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-027 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-027/fa-027.yaml \
--capabilities CAPABILITY_IAM
```
