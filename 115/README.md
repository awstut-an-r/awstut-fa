# AWS-PatchAsgInstance to patch instances in the AutoScaling group in turn

https://awstut.com/en/2023/02/05/aws-patchasginstance-to-patch-instances-in-the-autoscaling-group-in-turn-en/

# Architecture

![fa-115-diagram](https://user-images.githubusercontent.com/84276199/216809079-0fd53606-63dc-468e-a8dd-9cc22f7d101f.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-105.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-105/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-105 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-105/fa-105.yaml \
--capabilities CAPABILITY_IAM
```
