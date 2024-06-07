# Install the AWS IoT Device Client on the Raspberry Pi registered in Systems Manager

https://awstut.com/en/2024/06/08/install-the-aws-iot-device-client-on-the-raspberry-pi-registered-in-systems-manager-en/

# Architecture

![fa-153-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/91b17353-cbf6-4fb0-b2c6-2b4e762266a0)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-153.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-153/ --recursive
```

## CloudFormation Stack Creation 1

```bash
aws cloudformation create-stack \
--stack-name fa-153-01 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-153/fa-153-01.yaml \
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
--stack-name fa-153-02 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-153/fa-153-02.yaml \
--capabilities CAPABILITY_IAM
```
