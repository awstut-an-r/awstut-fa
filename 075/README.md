# Use CodePipeline to trigger CodeCommit pushes to push images to ECR

https://awstut.com/en/2022/08/14/use-codepipeline-to-trigger-codecommit-pushes-to-push-images-to-ecr-en/

# Architecture

![fa-075-diagram](https://user-images.githubusercontent.com/84276199/204114691-6b9e24e5-7f47-4f4e-bf1b-b1eb5598d31d.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-075.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp ./templates s3://my-bucket/fa-075/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-075 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-075/fa-075.yaml \
--capabilities CAPABILITY_IAM
```
