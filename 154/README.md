# Create AWS IoT client certificate using CloudFormation custom resource

https://awstut.com/en/2024/03/24/create-aws-iot-client-certificate-using-cloudformation-custom-resource-en/

# Architecture

![fa-154-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/ce28514d-6393-44e2-8de9-a4361797f834)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-154.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-154/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-154 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-154/fa-154.yaml \
--capabilities CAPABILITY_IAM
```
