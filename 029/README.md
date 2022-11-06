# Forwarding traffic to multiple target groups with path-based routing in ALB

https://awstut.com/en/2022/02/23/forwarding-traffic-to-multiple-target-groups-with-path-based-routing-in-alb/

# Architecture

![fa-029-diagram](https://user-images.githubusercontent.com/84276199/200164680-a04684e7-a0b8-4e33-9ffa-e2e463c3105f.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-029.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-029/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-029 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-029/fa-029.yaml \
--capabilities CAPABILITY_IAM
```
