# S3 Lifecycle Rules – Delete expired objects

https://awstut.com/en/2023/01/03/s3-lifecycle-rules-delete-expired-objects-en/

# Architecture

![fa-108-diagram](https://user-images.githubusercontent.com/84276199/210352133-90791c21-91ff-45a1-bf1f-6d580c96dd55.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-108.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-108/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-108 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-108/fa-108.yaml \
--capabilities CAPABILITY_IAM
```
