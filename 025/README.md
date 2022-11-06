# Ansible on Private Subnet

https://awstut.com/en/2022/02/13/ansible-on-private-subnet-2/

# Architecture

![fa-025-diagram](https://user-images.githubusercontent.com/84276199/200161354-cb8c0b2b-a099-423c-b071-d0a139c147df.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-025.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Prepare Ansible Playbook

```bash
zip -r playbook.zip *

aws s3 cp playbook.zip s3://my-bucket/fa-025/
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-025/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-025 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-025/fa-025.yaml \
--capabilities CAPABILITY_IAM
```
