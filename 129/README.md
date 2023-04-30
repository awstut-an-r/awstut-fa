# Automatically push test images to ECR using CFN custom resources and CodeBuild

https://awstut.com/en/2023/04/30/automatically-push-test-images-to-ecr-using-cfn-custom-resources-and-codebuild-en/

# Architecture

![fa-129-diagram](https://user-images.githubusercontent.com/84276199/235342847-9f1acab9-9452-45a5-b00b-a69fc3e1adc9.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-129.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-129/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-129 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-129/fa-129.yaml \
--capabilities CAPABILITY_IAM
```
