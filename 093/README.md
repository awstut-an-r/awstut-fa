# Use CFN custom resource to obtain NLB private address and set it as the source of the security group

https://awstut.com/en/2022/10/30/use-cfn-custom-resource-to-obtain-nlb-private-address-and-set-it-as-the-source-of-the-security-group-en/

# Architecture

![fa-093-diagram](https://user-images.githubusercontent.com/84276199/204132835-03ba5f6b-d1bc-48dc-ae91-0f1c437bccf0.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-093.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-093/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-093 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-093/fa-093.yaml \
--capabilities CAPABILITY_IAM
```
