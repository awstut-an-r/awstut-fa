# EC2 Auto Scaling – Target tracking scaling based on CPU utilization

https://awstut.com/en/2022/02/20/ec2-auto-scaling-target-tracking-policy-cpu-utilization-2/

# Architecture

![fa-026-diagram](https://user-images.githubusercontent.com/84276199/200161851-fb72b1ac-6ebb-415f-8aa0-6cc9ca251a9a.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-026.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-026/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-026 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-026/fa-026.yaml \
--capabilities CAPABILITY_IAM
```
