# Introduction to ElastiCache with CFN – Redis(Cluster Disabled)

https://awstut.com/en/2022/07/23/introduction-to-elasticache-with-cfn-redis-cluster-disabled-en/

# Architecture

![fa-063-diagram](https://user-images.githubusercontent.com/84276199/204087159-fc80d8b3-bce4-4c17-a198-99c559f5e64e.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-063.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-063/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-063 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-063/fa-063.yaml \
--capabilities CAPABILITY_IAM
```
