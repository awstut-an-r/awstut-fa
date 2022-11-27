# EC2 Auto Scaling – step scaling based on CPU utilization

https://awstut.com/en/2022/10/10/ec2-auto-scaling-step-scaling-based-on-cpu-utilization-en/

# Architecture

![fa-088-diagram](https://user-images.githubusercontent.com/84276199/204131904-2bbb92c3-6c85-46a4-90d3-1a25216ad6c3.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-088.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-088/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-088 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-088/fa-088.yaml \
--capabilities CAPABILITY_IAM
```
