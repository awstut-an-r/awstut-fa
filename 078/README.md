# Delete ECR images using CloudFormation Custom Resources

https://awstut.com/en/2022/08/27/delete-ecr-images-using-cloudformation-custom-resources-en/

# Architecture

![fa-078-diagram](https://user-images.githubusercontent.com/84276199/204116346-3f3466aa-7330-4246-b497-b805b65ac23a.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-078.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp ./templates s3://my-bucket/fa-078/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-078 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-078/fa-078.yaml \
--capabilities CAPABILITY_IAM
```
