# Connect your Raspberry Pi to AWS IoT Core using the AWS IoT Device SDK

https://awstut.com/en/2024/07/27/connect-your-raspberry-pi-to-aws-iot-core-using-the-aws-iot-device-sdk-en/

# Architecture

![fa-157-diagram](https://github.com/user-attachments/assets/b218b7b9-8317-4221-b762-254e8e8ae8d0)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-157.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-157/ --recursive
```

## CloudFormation Stack Creation 1

```bash
aws cloudformation create-stack \
--stack-name fa-157-01 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-157/fa-157-01.yaml \
--capabilities CAPABILITY_IAM
```

 ## Raspberry Pi Setting up

```bash
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install libc6:armhf
mkdir /tmp/ssm
curl https://amazon-ssm-ap-northeast-1.s3.ap-northeast-1.amazonaws.com/latest/debian_arm/ssm-setup-cli -o /tmp/ssm/ssm-setup-cli
sudo chmod +x /tmp/ssm/ssm-setup-cli
sudo /tmp/ssm/ssm-setup-cli -register -activation-code "[activation-code]" -activation-id "[activation-id]" -region "ap-northeast-1"
```

## CloudFormation Stack Creation 2

```bash
aws cloudformation create-stack \
--stack-name fa-157-02 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-157/fa-157-02.yaml \
--capabilities CAPABILITY_IAM
```
