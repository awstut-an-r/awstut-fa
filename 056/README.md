# AppSync – DataSource: OpenSearch

https://awstut.com/en/2022/06/12/appsync-datasource-opensearch-en/

# Architecture

![fa-056-diagram](https://user-images.githubusercontent.com/84276199/204078351-2a68c8df-725f-4805-a8a2-fcb2784bfeff.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-056.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Prepare OpenSearch document

```bash
cat <<EOF > bulk_movies.json
{ "index" : { "_index": "movies", "_id" : "2" } }
{"director": "Frankenheimer, John", "genre": ["Drama", "Mystery", "Thriller", "Crime"], "year": 1962, "actor": ["Lansbury, Angela", "Sinatra, Frank", "Leigh, Janet", "Harvey, Laurence", "Silva, Henry", "Frees, Paul", "Gregory, James", "Bissell, Whit", "McGiver, John", "Parrish, Leslie", "Edwards, James", "Flowers, Bess", "Dhiegh, Khigh", "Payne, Julie", "Kleeb, Helen", "Gray, Joe", "Nalder, Reggie", "Stevens, Bert", "Masters, Michael", "Lowell, Tom"], "title": "The Manchurian Candidate"}
{ "index" : { "_index": "movies", "_id" : "3" } }
{"director": "Baird, Stuart", "genre": ["Action", "Crime", "Thriller"], "year": 1998, "actor": ["Downey Jr., Robert", "Jones, Tommy Lee", "Snipes, Wesley", "Pantoliano, Joe", "Jacob, Ir\u00e8ne", "Nelligan, Kate", "Roebuck, Daniel", "Malahide, Patrick", "Richardson, LaTanya", "Wood, Tom", "Kosik, Thomas", "Stellate, Nick", "Minkoff, Robert", "Brown, Spitfire", "Foster, Reese", "Spielbauer, Bruce", "Mukherji, Kevin", "Cray, Ed", "Fordham, David", "Jett, Charlie"], "title": "U.S. Marshals"}
{ "index" : { "_index": "movies", "_id" : "4" } }
{"director": "Ray, Nicholas", "genre": ["Drama", "Romance"], "year": 1955, "actor": ["Hopper, Dennis", "Wood, Natalie", "Dean, James", "Mineo, Sal", "Backus, Jim", "Platt, Edward", "Ray, Nicholas", "Hopper, William", "Allen, Corey", "Birch, Paul", "Hudson, Rochelle", "Doran, Ann", "Hicks, Chuck", "Leigh, Nelson", "Williams, Robert", "Wessel, Dick", "Bryar, Paul", "Sessions, Almira", "McMahon, David", "Peters Jr., House"], "title": "Rebel Without a Cause"}
EOF

aws s3 cp bulk_movies.json s3://awstut-bucket/fa-056/
```

https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsgupload-data.html

## Prepare Lambda Function Package

```bash
zip deploy1.zip lambda/function1/index.py

aws s3 cp deploy1.zip s3://my-bucket/fa-056/

zip deploy2.zip lambda/function2/index.py

aws s3 cp deploy2.zip s3://my-bucket/fa-056/
```

## Prepare Lambda Layer Package

```bash
sudo pip3 install requests -t python

sudo pip3 install requests-aws4auth -t python

sudo pip3 install --pre gql[all] -t python

[cfnresponse.py]

zip -r layer.zip python

aws s3 cp layer.zip s3://my-bucket/fa-055/
```

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-lambda-function-code-cfnresponsemodule.html

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-056/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-056 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-056/fa-056.yaml \
--capabilities CAPABILITY_IAM
```
