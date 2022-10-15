# Registering ALB to Route 53 and Accessing with Your Own Domain

https://awstut.com/en/2022/02/11/registering-alb-to-route-53-and-accessing-with-your-own-domain-2/

# Architecture

![fa-022-diagram](https://user-images.githubusercontent.com/84276199/195983226-6f4cdc47-678f-4bce-9d0c-6ac6f2b5c82b.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Register domain name

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar.html

## Tempalte File Modification

Modify the following locations in fa-022.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
    
  ALBHostedZoneId:
    Type: String
    Default: [alb-hosted-zone-id]
    
  DomainName:
    Type: String
    Default: [domain-name]
    
  HostedZoneId:
    Type: String
    Default: [hosted-zone-id]
```

Check the HostedZoneId of ALB at the following page.

https://docs.aws.amazon.com/general/latest/gr/elb.html

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-022/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-022 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-022/fa-022.yaml \
--capabilities CAPABILITY_IAM
```
