# Create yum Repository in S3 and Access from Private Subnet

https://awstut.com/en/2022/03/19/create-yum-repository-in-s3-and-access-from-private-subnet/

# Architecture

![fa-031-diagram](https://user-images.githubusercontent.com/84276199/200165585-ae4620c4-c30f-4a5a-99bf-76de0bd0eba4.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-031.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-031/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-031 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-031/fa-031.yaml \
--capabilities CAPABILITY_IAM
```
