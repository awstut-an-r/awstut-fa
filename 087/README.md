# EC2 Auto Scaling – Simple Scaling based on CPU utilization

https://awstut.com/en/2022/10/09/ec2-auto-scaling-simple-scaling-based-on-cpu-utilization/

# Architecture

![fa-087-diagram](https://user-images.githubusercontent.com/84276199/204131787-d17485b2-33a8-40ef-83e3-39ce4be58f23.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-087.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-087/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-087 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-087/fa-087.yaml \
--capabilities CAPABILITY_IAM
```
