# On SSL between ALB and EC2 using Self-Signed Certificate

https://awstut.com/en/2022/02/13/on-ssl-between-alb-and-ec2-using-self-signed-certificate-2/

# Architecture

![fa-024-diagram](https://user-images.githubusercontent.com/84276199/200160789-ea77b7ce-dbc4-4050-900d-ff4817fec6cf.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Register domain name

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar.html

## Tempalte File Modification

Modify the following locations in fa-024.yaml.

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

## Prepare Ansible Playbook

```bash
zip -r playbook.zip *

aws s3 cp playbook.zip s3://my-bucket/fa-024/
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-024/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-024 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-024/fa-024.yaml \
--capabilities CAPABILITY_IAM
```
