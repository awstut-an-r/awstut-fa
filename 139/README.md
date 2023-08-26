# Mix on-demand/spot instances in EC2 Auto Scaling Group

https://awstut.com/en/2023/08/27/mix-on-demand-spot-instances-in-ec2-auto-scaling-group-en/

# Architecture

![fa-139-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/4ed7b23d-0299-40b3-a0aa-01bad6abc862)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-139.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-139/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-139 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-139/fa-139.yaml \
--capabilities CAPABILITY_IAM
```
