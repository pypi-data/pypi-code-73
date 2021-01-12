from os.path import abspath, dirname

from setuptools import setup

LONG_DESCRIPTION = open(dirname(abspath(__file__)) + "/README.md", "r").read()


setup(
    name="boto3-stubs",
    version="1.16.53.0",
    packages=["boto3-stubs"],
    url="https://github.com/vemel/mypy_boto3_builder",
    license="MIT License",
    author="Vlad Emelianov",
    author_email="vlad.emelianov.nz@gmail.com",
    description="Type annotations for boto3 1.16.53, generated by mypy-boto3-buider 4.3.1",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Typing :: Typed",
    ],
    keywords="boto3 type-annotations boto3-stubs mypy mypy-stubs typeshed autocomplete auto-generated",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    package_data={"boto3-stubs": ["py.typed", "*.pyi", "*/*.pyi"]},
    python_requires=">=3.6",
    project_urls={
        "Documentation": "https://mypy-boto3-builder.readthedocs.io/en/latest/",
        "Source": "https://github.com/vemel/mypy_boto3_builder",
        "Tracker": "https://github.com/vemel/mypy_boto3_builder/issues",
    },
    install_requires=[
        "typing_extensions; python_version < '3.8'",
    ],
    extras_require={
        "all": [
            "mypy-boto3-accessanalyzer==1.16.53.0",
            "mypy-boto3-acm==1.16.53.0",
            "mypy-boto3-acm-pca==1.16.53.0",
            "mypy-boto3-alexaforbusiness==1.16.53.0",
            "mypy-boto3-amp==1.16.53.0",
            "mypy-boto3-amplify==1.16.53.0",
            "mypy-boto3-amplifybackend==1.16.53.0",
            "mypy-boto3-apigateway==1.16.53.0",
            "mypy-boto3-apigatewaymanagementapi==1.16.53.0",
            "mypy-boto3-apigatewayv2==1.16.53.0",
            "mypy-boto3-appconfig==1.16.53.0",
            "mypy-boto3-appflow==1.16.53.0",
            "mypy-boto3-appintegrations==1.16.53.0",
            "mypy-boto3-application-autoscaling==1.16.53.0",
            "mypy-boto3-application-insights==1.16.53.0",
            "mypy-boto3-appmesh==1.16.53.0",
            "mypy-boto3-appstream==1.16.53.0",
            "mypy-boto3-appsync==1.16.53.0",
            "mypy-boto3-athena==1.16.53.0",
            "mypy-boto3-auditmanager==1.16.53.0",
            "mypy-boto3-autoscaling==1.16.53.0",
            "mypy-boto3-autoscaling-plans==1.16.53.0",
            "mypy-boto3-backup==1.16.53.0",
            "mypy-boto3-batch==1.16.53.0",
            "mypy-boto3-braket==1.16.53.0",
            "mypy-boto3-budgets==1.16.53.0",
            "mypy-boto3-ce==1.16.53.0",
            "mypy-boto3-chime==1.16.53.0",
            "mypy-boto3-cloud9==1.16.53.0",
            "mypy-boto3-clouddirectory==1.16.53.0",
            "mypy-boto3-cloudformation==1.16.53.0",
            "mypy-boto3-cloudfront==1.16.53.0",
            "mypy-boto3-cloudhsm==1.16.53.0",
            "mypy-boto3-cloudhsmv2==1.16.53.0",
            "mypy-boto3-cloudsearch==1.16.53.0",
            "mypy-boto3-cloudsearchdomain==1.16.53.0",
            "mypy-boto3-cloudtrail==1.16.53.0",
            "mypy-boto3-cloudwatch==1.16.53.0",
            "mypy-boto3-codeartifact==1.16.53.0",
            "mypy-boto3-codebuild==1.16.53.0",
            "mypy-boto3-codecommit==1.16.53.0",
            "mypy-boto3-codedeploy==1.16.53.0",
            "mypy-boto3-codeguru-reviewer==1.16.53.0",
            "mypy-boto3-codeguruprofiler==1.16.53.0",
            "mypy-boto3-codepipeline==1.16.53.0",
            "mypy-boto3-codestar==1.16.53.0",
            "mypy-boto3-codestar-connections==1.16.53.0",
            "mypy-boto3-codestar-notifications==1.16.53.0",
            "mypy-boto3-cognito-identity==1.16.53.0",
            "mypy-boto3-cognito-idp==1.16.53.0",
            "mypy-boto3-cognito-sync==1.16.53.0",
            "mypy-boto3-comprehend==1.16.53.0",
            "mypy-boto3-comprehendmedical==1.16.53.0",
            "mypy-boto3-compute-optimizer==1.16.53.0",
            "mypy-boto3-config==1.16.53.0",
            "mypy-boto3-connect==1.16.53.0",
            "mypy-boto3-connect-contact-lens==1.16.53.0",
            "mypy-boto3-connectparticipant==1.16.53.0",
            "mypy-boto3-cur==1.16.53.0",
            "mypy-boto3-customer-profiles==1.16.53.0",
            "mypy-boto3-databrew==1.16.53.0",
            "mypy-boto3-dataexchange==1.16.53.0",
            "mypy-boto3-datapipeline==1.16.53.0",
            "mypy-boto3-datasync==1.16.53.0",
            "mypy-boto3-dax==1.16.53.0",
            "mypy-boto3-detective==1.16.53.0",
            "mypy-boto3-devicefarm==1.16.53.0",
            "mypy-boto3-devops-guru==1.16.53.0",
            "mypy-boto3-directconnect==1.16.53.0",
            "mypy-boto3-discovery==1.16.53.0",
            "mypy-boto3-dlm==1.16.53.0",
            "mypy-boto3-dms==1.16.53.0",
            "mypy-boto3-docdb==1.16.53.0",
            "mypy-boto3-ds==1.16.53.0",
            "mypy-boto3-dynamodb==1.16.53.0",
            "mypy-boto3-dynamodbstreams==1.16.53.0",
            "mypy-boto3-ebs==1.16.53.0",
            "mypy-boto3-ec2==1.16.53.0",
            "mypy-boto3-ec2-instance-connect==1.16.53.0",
            "mypy-boto3-ecr==1.16.53.0",
            "mypy-boto3-ecr-public==1.16.53.0",
            "mypy-boto3-ecs==1.16.53.0",
            "mypy-boto3-efs==1.16.53.0",
            "mypy-boto3-eks==1.16.53.0",
            "mypy-boto3-elastic-inference==1.16.53.0",
            "mypy-boto3-elasticache==1.16.53.0",
            "mypy-boto3-elasticbeanstalk==1.16.53.0",
            "mypy-boto3-elastictranscoder==1.16.53.0",
            "mypy-boto3-elb==1.16.53.0",
            "mypy-boto3-elbv2==1.16.53.0",
            "mypy-boto3-emr==1.16.53.0",
            "mypy-boto3-emr-containers==1.16.53.0",
            "mypy-boto3-es==1.16.53.0",
            "mypy-boto3-events==1.16.53.0",
            "mypy-boto3-firehose==1.16.53.0",
            "mypy-boto3-fms==1.16.53.0",
            "mypy-boto3-forecast==1.16.53.0",
            "mypy-boto3-forecastquery==1.16.53.0",
            "mypy-boto3-frauddetector==1.16.53.0",
            "mypy-boto3-fsx==1.16.53.0",
            "mypy-boto3-gamelift==1.16.53.0",
            "mypy-boto3-glacier==1.16.53.0",
            "mypy-boto3-globalaccelerator==1.16.53.0",
            "mypy-boto3-glue==1.16.53.0",
            "mypy-boto3-greengrass==1.16.53.0",
            "mypy-boto3-greengrassv2==1.16.53.0",
            "mypy-boto3-groundstation==1.16.53.0",
            "mypy-boto3-guardduty==1.16.53.0",
            "mypy-boto3-health==1.16.53.0",
            "mypy-boto3-healthlake==1.16.53.0",
            "mypy-boto3-honeycode==1.16.53.0",
            "mypy-boto3-iam==1.16.53.0",
            "mypy-boto3-identitystore==1.16.53.0",
            "mypy-boto3-imagebuilder==1.16.53.0",
            "mypy-boto3-importexport==1.16.53.0",
            "mypy-boto3-inspector==1.16.53.0",
            "mypy-boto3-iot==1.16.53.0",
            "mypy-boto3-iot-data==1.16.53.0",
            "mypy-boto3-iot-jobs-data==1.16.53.0",
            "mypy-boto3-iot1click-devices==1.16.53.0",
            "mypy-boto3-iot1click-projects==1.16.53.0",
            "mypy-boto3-iotanalytics==1.16.53.0",
            "mypy-boto3-iotdeviceadvisor==1.16.53.0",
            "mypy-boto3-iotevents==1.16.53.0",
            "mypy-boto3-iotevents-data==1.16.53.0",
            "mypy-boto3-iotfleethub==1.16.53.0",
            "mypy-boto3-iotsecuretunneling==1.16.53.0",
            "mypy-boto3-iotsitewise==1.16.53.0",
            "mypy-boto3-iotthingsgraph==1.16.53.0",
            "mypy-boto3-iotwireless==1.16.53.0",
            "mypy-boto3-ivs==1.16.53.0",
            "mypy-boto3-kafka==1.16.53.0",
            "mypy-boto3-kendra==1.16.53.0",
            "mypy-boto3-kinesis==1.16.53.0",
            "mypy-boto3-kinesis-video-archived-media==1.16.53.0",
            "mypy-boto3-kinesis-video-media==1.16.53.0",
            "mypy-boto3-kinesis-video-signaling==1.16.53.0",
            "mypy-boto3-kinesisanalytics==1.16.53.0",
            "mypy-boto3-kinesisanalyticsv2==1.16.53.0",
            "mypy-boto3-kinesisvideo==1.16.53.0",
            "mypy-boto3-kms==1.16.53.0",
            "mypy-boto3-lakeformation==1.16.53.0",
            "mypy-boto3-lambda==1.16.53.0",
            "mypy-boto3-lex-models==1.16.53.0",
            "mypy-boto3-lex-runtime==1.16.53.0",
            "mypy-boto3-license-manager==1.16.53.0",
            "mypy-boto3-lightsail==1.16.53.0",
            "mypy-boto3-location==1.16.53.0",
            "mypy-boto3-logs==1.16.53.0",
            "mypy-boto3-lookoutvision==1.16.53.0",
            "mypy-boto3-machinelearning==1.16.53.0",
            "mypy-boto3-macie==1.16.53.0",
            "mypy-boto3-macie2==1.16.53.0",
            "mypy-boto3-managedblockchain==1.16.53.0",
            "mypy-boto3-marketplace-catalog==1.16.53.0",
            "mypy-boto3-marketplace-entitlement==1.16.53.0",
            "mypy-boto3-marketplacecommerceanalytics==1.16.53.0",
            "mypy-boto3-mediaconnect==1.16.53.0",
            "mypy-boto3-mediaconvert==1.16.53.0",
            "mypy-boto3-medialive==1.16.53.0",
            "mypy-boto3-mediapackage==1.16.53.0",
            "mypy-boto3-mediapackage-vod==1.16.53.0",
            "mypy-boto3-mediastore==1.16.53.0",
            "mypy-boto3-mediastore-data==1.16.53.0",
            "mypy-boto3-mediatailor==1.16.53.0",
            "mypy-boto3-meteringmarketplace==1.16.53.0",
            "mypy-boto3-mgh==1.16.53.0",
            "mypy-boto3-migrationhub-config==1.16.53.0",
            "mypy-boto3-mobile==1.16.53.0",
            "mypy-boto3-mq==1.16.53.0",
            "mypy-boto3-mturk==1.16.53.0",
            "mypy-boto3-mwaa==1.16.53.0",
            "mypy-boto3-neptune==1.16.53.0",
            "mypy-boto3-network-firewall==1.16.53.0",
            "mypy-boto3-networkmanager==1.16.53.0",
            "mypy-boto3-opsworks==1.16.53.0",
            "mypy-boto3-opsworkscm==1.16.53.0",
            "mypy-boto3-organizations==1.16.53.0",
            "mypy-boto3-outposts==1.16.53.0",
            "mypy-boto3-personalize==1.16.53.0",
            "mypy-boto3-personalize-events==1.16.53.0",
            "mypy-boto3-personalize-runtime==1.16.53.0",
            "mypy-boto3-pi==1.16.53.0",
            "mypy-boto3-pinpoint==1.16.53.0",
            "mypy-boto3-pinpoint-email==1.16.53.0",
            "mypy-boto3-pinpoint-sms-voice==1.16.53.0",
            "mypy-boto3-polly==1.16.53.0",
            "mypy-boto3-pricing==1.16.53.0",
            "mypy-boto3-qldb==1.16.53.0",
            "mypy-boto3-qldb-session==1.16.53.0",
            "mypy-boto3-quicksight==1.16.53.0",
            "mypy-boto3-ram==1.16.53.0",
            "mypy-boto3-rds==1.16.53.0",
            "mypy-boto3-rds-data==1.16.53.0",
            "mypy-boto3-redshift==1.16.53.0",
            "mypy-boto3-redshift-data==1.16.53.0",
            "mypy-boto3-rekognition==1.16.53.0",
            "mypy-boto3-resource-groups==1.16.53.0",
            "mypy-boto3-resourcegroupstaggingapi==1.16.53.0",
            "mypy-boto3-robomaker==1.16.53.0",
            "mypy-boto3-route53==1.16.53.0",
            "mypy-boto3-route53domains==1.16.53.0",
            "mypy-boto3-route53resolver==1.16.53.0",
            "mypy-boto3-s3==1.16.53.0",
            "mypy-boto3-s3control==1.16.53.0",
            "mypy-boto3-s3outposts==1.16.53.0",
            "mypy-boto3-sagemaker==1.16.53.0",
            "mypy-boto3-sagemaker-a2i-runtime==1.16.53.0",
            "mypy-boto3-sagemaker-edge==1.16.53.0",
            "mypy-boto3-sagemaker-featurestore-runtime==1.16.53.0",
            "mypy-boto3-sagemaker-runtime==1.16.53.0",
            "mypy-boto3-savingsplans==1.16.53.0",
            "mypy-boto3-schemas==1.16.53.0",
            "mypy-boto3-sdb==1.16.53.0",
            "mypy-boto3-secretsmanager==1.16.53.0",
            "mypy-boto3-securityhub==1.16.53.0",
            "mypy-boto3-serverlessrepo==1.16.53.0",
            "mypy-boto3-service-quotas==1.16.53.0",
            "mypy-boto3-servicecatalog==1.16.53.0",
            "mypy-boto3-servicecatalog-appregistry==1.16.53.0",
            "mypy-boto3-servicediscovery==1.16.53.0",
            "mypy-boto3-ses==1.16.53.0",
            "mypy-boto3-sesv2==1.16.53.0",
            "mypy-boto3-shield==1.16.53.0",
            "mypy-boto3-signer==1.16.53.0",
            "mypy-boto3-sms==1.16.53.0",
            "mypy-boto3-sms-voice==1.16.53.0",
            "mypy-boto3-snowball==1.16.53.0",
            "mypy-boto3-sns==1.16.53.0",
            "mypy-boto3-sqs==1.16.53.0",
            "mypy-boto3-ssm==1.16.53.0",
            "mypy-boto3-sso==1.16.53.0",
            "mypy-boto3-sso-admin==1.16.53.0",
            "mypy-boto3-sso-oidc==1.16.53.0",
            "mypy-boto3-stepfunctions==1.16.53.0",
            "mypy-boto3-storagegateway==1.16.53.0",
            "mypy-boto3-sts==1.16.53.0",
            "mypy-boto3-support==1.16.53.0",
            "mypy-boto3-swf==1.16.53.0",
            "mypy-boto3-synthetics==1.16.53.0",
            "mypy-boto3-textract==1.16.53.0",
            "mypy-boto3-timestream-query==1.16.53.0",
            "mypy-boto3-timestream-write==1.16.53.0",
            "mypy-boto3-transcribe==1.16.53.0",
            "mypy-boto3-transfer==1.16.53.0",
            "mypy-boto3-translate==1.16.53.0",
            "mypy-boto3-waf==1.16.53.0",
            "mypy-boto3-waf-regional==1.16.53.0",
            "mypy-boto3-wafv2==1.16.53.0",
            "mypy-boto3-wellarchitected==1.16.53.0",
            "mypy-boto3-workdocs==1.16.53.0",
            "mypy-boto3-worklink==1.16.53.0",
            "mypy-boto3-workmail==1.16.53.0",
            "mypy-boto3-workmailmessageflow==1.16.53.0",
            "mypy-boto3-workspaces==1.16.53.0",
            "mypy-boto3-xray==1.16.53.0",
        ],
        "essential": [
            "mypy-boto3-cloudformation==1.16.53.0",
            "mypy-boto3-dynamodb==1.16.53.0",
            "mypy-boto3-ec2==1.16.53.0",
            "mypy-boto3-lambda==1.16.53.0",
            "mypy-boto3-rds==1.16.53.0",
            "mypy-boto3-s3==1.16.53.0",
            "mypy-boto3-sqs==1.16.53.0",
        ],
        "accessanalyzer": ["mypy-boto3-accessanalyzer==1.16.53.0"],
        "acm": ["mypy-boto3-acm==1.16.53.0"],
        "acm-pca": ["mypy-boto3-acm-pca==1.16.53.0"],
        "alexaforbusiness": ["mypy-boto3-alexaforbusiness==1.16.53.0"],
        "amp": ["mypy-boto3-amp==1.16.53.0"],
        "amplify": ["mypy-boto3-amplify==1.16.53.0"],
        "amplifybackend": ["mypy-boto3-amplifybackend==1.16.53.0"],
        "apigateway": ["mypy-boto3-apigateway==1.16.53.0"],
        "apigatewaymanagementapi": ["mypy-boto3-apigatewaymanagementapi==1.16.53.0"],
        "apigatewayv2": ["mypy-boto3-apigatewayv2==1.16.53.0"],
        "appconfig": ["mypy-boto3-appconfig==1.16.53.0"],
        "appflow": ["mypy-boto3-appflow==1.16.53.0"],
        "appintegrations": ["mypy-boto3-appintegrations==1.16.53.0"],
        "application-autoscaling": ["mypy-boto3-application-autoscaling==1.16.53.0"],
        "application-insights": ["mypy-boto3-application-insights==1.16.53.0"],
        "appmesh": ["mypy-boto3-appmesh==1.16.53.0"],
        "appstream": ["mypy-boto3-appstream==1.16.53.0"],
        "appsync": ["mypy-boto3-appsync==1.16.53.0"],
        "athena": ["mypy-boto3-athena==1.16.53.0"],
        "auditmanager": ["mypy-boto3-auditmanager==1.16.53.0"],
        "autoscaling": ["mypy-boto3-autoscaling==1.16.53.0"],
        "autoscaling-plans": ["mypy-boto3-autoscaling-plans==1.16.53.0"],
        "backup": ["mypy-boto3-backup==1.16.53.0"],
        "batch": ["mypy-boto3-batch==1.16.53.0"],
        "braket": ["mypy-boto3-braket==1.16.53.0"],
        "budgets": ["mypy-boto3-budgets==1.16.53.0"],
        "ce": ["mypy-boto3-ce==1.16.53.0"],
        "chime": ["mypy-boto3-chime==1.16.53.0"],
        "cloud9": ["mypy-boto3-cloud9==1.16.53.0"],
        "clouddirectory": ["mypy-boto3-clouddirectory==1.16.53.0"],
        "cloudformation": ["mypy-boto3-cloudformation==1.16.53.0"],
        "cloudfront": ["mypy-boto3-cloudfront==1.16.53.0"],
        "cloudhsm": ["mypy-boto3-cloudhsm==1.16.53.0"],
        "cloudhsmv2": ["mypy-boto3-cloudhsmv2==1.16.53.0"],
        "cloudsearch": ["mypy-boto3-cloudsearch==1.16.53.0"],
        "cloudsearchdomain": ["mypy-boto3-cloudsearchdomain==1.16.53.0"],
        "cloudtrail": ["mypy-boto3-cloudtrail==1.16.53.0"],
        "cloudwatch": ["mypy-boto3-cloudwatch==1.16.53.0"],
        "codeartifact": ["mypy-boto3-codeartifact==1.16.53.0"],
        "codebuild": ["mypy-boto3-codebuild==1.16.53.0"],
        "codecommit": ["mypy-boto3-codecommit==1.16.53.0"],
        "codedeploy": ["mypy-boto3-codedeploy==1.16.53.0"],
        "codeguru-reviewer": ["mypy-boto3-codeguru-reviewer==1.16.53.0"],
        "codeguruprofiler": ["mypy-boto3-codeguruprofiler==1.16.53.0"],
        "codepipeline": ["mypy-boto3-codepipeline==1.16.53.0"],
        "codestar": ["mypy-boto3-codestar==1.16.53.0"],
        "codestar-connections": ["mypy-boto3-codestar-connections==1.16.53.0"],
        "codestar-notifications": ["mypy-boto3-codestar-notifications==1.16.53.0"],
        "cognito-identity": ["mypy-boto3-cognito-identity==1.16.53.0"],
        "cognito-idp": ["mypy-boto3-cognito-idp==1.16.53.0"],
        "cognito-sync": ["mypy-boto3-cognito-sync==1.16.53.0"],
        "comprehend": ["mypy-boto3-comprehend==1.16.53.0"],
        "comprehendmedical": ["mypy-boto3-comprehendmedical==1.16.53.0"],
        "compute-optimizer": ["mypy-boto3-compute-optimizer==1.16.53.0"],
        "config": ["mypy-boto3-config==1.16.53.0"],
        "connect": ["mypy-boto3-connect==1.16.53.0"],
        "connect-contact-lens": ["mypy-boto3-connect-contact-lens==1.16.53.0"],
        "connectparticipant": ["mypy-boto3-connectparticipant==1.16.53.0"],
        "cur": ["mypy-boto3-cur==1.16.53.0"],
        "customer-profiles": ["mypy-boto3-customer-profiles==1.16.53.0"],
        "databrew": ["mypy-boto3-databrew==1.16.53.0"],
        "dataexchange": ["mypy-boto3-dataexchange==1.16.53.0"],
        "datapipeline": ["mypy-boto3-datapipeline==1.16.53.0"],
        "datasync": ["mypy-boto3-datasync==1.16.53.0"],
        "dax": ["mypy-boto3-dax==1.16.53.0"],
        "detective": ["mypy-boto3-detective==1.16.53.0"],
        "devicefarm": ["mypy-boto3-devicefarm==1.16.53.0"],
        "devops-guru": ["mypy-boto3-devops-guru==1.16.53.0"],
        "directconnect": ["mypy-boto3-directconnect==1.16.53.0"],
        "discovery": ["mypy-boto3-discovery==1.16.53.0"],
        "dlm": ["mypy-boto3-dlm==1.16.53.0"],
        "dms": ["mypy-boto3-dms==1.16.53.0"],
        "docdb": ["mypy-boto3-docdb==1.16.53.0"],
        "ds": ["mypy-boto3-ds==1.16.53.0"],
        "dynamodb": ["mypy-boto3-dynamodb==1.16.53.0"],
        "dynamodbstreams": ["mypy-boto3-dynamodbstreams==1.16.53.0"],
        "ebs": ["mypy-boto3-ebs==1.16.53.0"],
        "ec2": ["mypy-boto3-ec2==1.16.53.0"],
        "ec2-instance-connect": ["mypy-boto3-ec2-instance-connect==1.16.53.0"],
        "ecr": ["mypy-boto3-ecr==1.16.53.0"],
        "ecr-public": ["mypy-boto3-ecr-public==1.16.53.0"],
        "ecs": ["mypy-boto3-ecs==1.16.53.0"],
        "efs": ["mypy-boto3-efs==1.16.53.0"],
        "eks": ["mypy-boto3-eks==1.16.53.0"],
        "elastic-inference": ["mypy-boto3-elastic-inference==1.16.53.0"],
        "elasticache": ["mypy-boto3-elasticache==1.16.53.0"],
        "elasticbeanstalk": ["mypy-boto3-elasticbeanstalk==1.16.53.0"],
        "elastictranscoder": ["mypy-boto3-elastictranscoder==1.16.53.0"],
        "elb": ["mypy-boto3-elb==1.16.53.0"],
        "elbv2": ["mypy-boto3-elbv2==1.16.53.0"],
        "emr": ["mypy-boto3-emr==1.16.53.0"],
        "emr-containers": ["mypy-boto3-emr-containers==1.16.53.0"],
        "es": ["mypy-boto3-es==1.16.53.0"],
        "events": ["mypy-boto3-events==1.16.53.0"],
        "firehose": ["mypy-boto3-firehose==1.16.53.0"],
        "fms": ["mypy-boto3-fms==1.16.53.0"],
        "forecast": ["mypy-boto3-forecast==1.16.53.0"],
        "forecastquery": ["mypy-boto3-forecastquery==1.16.53.0"],
        "frauddetector": ["mypy-boto3-frauddetector==1.16.53.0"],
        "fsx": ["mypy-boto3-fsx==1.16.53.0"],
        "gamelift": ["mypy-boto3-gamelift==1.16.53.0"],
        "glacier": ["mypy-boto3-glacier==1.16.53.0"],
        "globalaccelerator": ["mypy-boto3-globalaccelerator==1.16.53.0"],
        "glue": ["mypy-boto3-glue==1.16.53.0"],
        "greengrass": ["mypy-boto3-greengrass==1.16.53.0"],
        "greengrassv2": ["mypy-boto3-greengrassv2==1.16.53.0"],
        "groundstation": ["mypy-boto3-groundstation==1.16.53.0"],
        "guardduty": ["mypy-boto3-guardduty==1.16.53.0"],
        "health": ["mypy-boto3-health==1.16.53.0"],
        "healthlake": ["mypy-boto3-healthlake==1.16.53.0"],
        "honeycode": ["mypy-boto3-honeycode==1.16.53.0"],
        "iam": ["mypy-boto3-iam==1.16.53.0"],
        "identitystore": ["mypy-boto3-identitystore==1.16.53.0"],
        "imagebuilder": ["mypy-boto3-imagebuilder==1.16.53.0"],
        "importexport": ["mypy-boto3-importexport==1.16.53.0"],
        "inspector": ["mypy-boto3-inspector==1.16.53.0"],
        "iot": ["mypy-boto3-iot==1.16.53.0"],
        "iot-data": ["mypy-boto3-iot-data==1.16.53.0"],
        "iot-jobs-data": ["mypy-boto3-iot-jobs-data==1.16.53.0"],
        "iot1click-devices": ["mypy-boto3-iot1click-devices==1.16.53.0"],
        "iot1click-projects": ["mypy-boto3-iot1click-projects==1.16.53.0"],
        "iotanalytics": ["mypy-boto3-iotanalytics==1.16.53.0"],
        "iotdeviceadvisor": ["mypy-boto3-iotdeviceadvisor==1.16.53.0"],
        "iotevents": ["mypy-boto3-iotevents==1.16.53.0"],
        "iotevents-data": ["mypy-boto3-iotevents-data==1.16.53.0"],
        "iotfleethub": ["mypy-boto3-iotfleethub==1.16.53.0"],
        "iotsecuretunneling": ["mypy-boto3-iotsecuretunneling==1.16.53.0"],
        "iotsitewise": ["mypy-boto3-iotsitewise==1.16.53.0"],
        "iotthingsgraph": ["mypy-boto3-iotthingsgraph==1.16.53.0"],
        "iotwireless": ["mypy-boto3-iotwireless==1.16.53.0"],
        "ivs": ["mypy-boto3-ivs==1.16.53.0"],
        "kafka": ["mypy-boto3-kafka==1.16.53.0"],
        "kendra": ["mypy-boto3-kendra==1.16.53.0"],
        "kinesis": ["mypy-boto3-kinesis==1.16.53.0"],
        "kinesis-video-archived-media": ["mypy-boto3-kinesis-video-archived-media==1.16.53.0"],
        "kinesis-video-media": ["mypy-boto3-kinesis-video-media==1.16.53.0"],
        "kinesis-video-signaling": ["mypy-boto3-kinesis-video-signaling==1.16.53.0"],
        "kinesisanalytics": ["mypy-boto3-kinesisanalytics==1.16.53.0"],
        "kinesisanalyticsv2": ["mypy-boto3-kinesisanalyticsv2==1.16.53.0"],
        "kinesisvideo": ["mypy-boto3-kinesisvideo==1.16.53.0"],
        "kms": ["mypy-boto3-kms==1.16.53.0"],
        "lakeformation": ["mypy-boto3-lakeformation==1.16.53.0"],
        "lambda": ["mypy-boto3-lambda==1.16.53.0"],
        "lex-models": ["mypy-boto3-lex-models==1.16.53.0"],
        "lex-runtime": ["mypy-boto3-lex-runtime==1.16.53.0"],
        "license-manager": ["mypy-boto3-license-manager==1.16.53.0"],
        "lightsail": ["mypy-boto3-lightsail==1.16.53.0"],
        "location": ["mypy-boto3-location==1.16.53.0"],
        "logs": ["mypy-boto3-logs==1.16.53.0"],
        "lookoutvision": ["mypy-boto3-lookoutvision==1.16.53.0"],
        "machinelearning": ["mypy-boto3-machinelearning==1.16.53.0"],
        "macie": ["mypy-boto3-macie==1.16.53.0"],
        "macie2": ["mypy-boto3-macie2==1.16.53.0"],
        "managedblockchain": ["mypy-boto3-managedblockchain==1.16.53.0"],
        "marketplace-catalog": ["mypy-boto3-marketplace-catalog==1.16.53.0"],
        "marketplace-entitlement": ["mypy-boto3-marketplace-entitlement==1.16.53.0"],
        "marketplacecommerceanalytics": ["mypy-boto3-marketplacecommerceanalytics==1.16.53.0"],
        "mediaconnect": ["mypy-boto3-mediaconnect==1.16.53.0"],
        "mediaconvert": ["mypy-boto3-mediaconvert==1.16.53.0"],
        "medialive": ["mypy-boto3-medialive==1.16.53.0"],
        "mediapackage": ["mypy-boto3-mediapackage==1.16.53.0"],
        "mediapackage-vod": ["mypy-boto3-mediapackage-vod==1.16.53.0"],
        "mediastore": ["mypy-boto3-mediastore==1.16.53.0"],
        "mediastore-data": ["mypy-boto3-mediastore-data==1.16.53.0"],
        "mediatailor": ["mypy-boto3-mediatailor==1.16.53.0"],
        "meteringmarketplace": ["mypy-boto3-meteringmarketplace==1.16.53.0"],
        "mgh": ["mypy-boto3-mgh==1.16.53.0"],
        "migrationhub-config": ["mypy-boto3-migrationhub-config==1.16.53.0"],
        "mobile": ["mypy-boto3-mobile==1.16.53.0"],
        "mq": ["mypy-boto3-mq==1.16.53.0"],
        "mturk": ["mypy-boto3-mturk==1.16.53.0"],
        "mwaa": ["mypy-boto3-mwaa==1.16.53.0"],
        "neptune": ["mypy-boto3-neptune==1.16.53.0"],
        "network-firewall": ["mypy-boto3-network-firewall==1.16.53.0"],
        "networkmanager": ["mypy-boto3-networkmanager==1.16.53.0"],
        "opsworks": ["mypy-boto3-opsworks==1.16.53.0"],
        "opsworkscm": ["mypy-boto3-opsworkscm==1.16.53.0"],
        "organizations": ["mypy-boto3-organizations==1.16.53.0"],
        "outposts": ["mypy-boto3-outposts==1.16.53.0"],
        "personalize": ["mypy-boto3-personalize==1.16.53.0"],
        "personalize-events": ["mypy-boto3-personalize-events==1.16.53.0"],
        "personalize-runtime": ["mypy-boto3-personalize-runtime==1.16.53.0"],
        "pi": ["mypy-boto3-pi==1.16.53.0"],
        "pinpoint": ["mypy-boto3-pinpoint==1.16.53.0"],
        "pinpoint-email": ["mypy-boto3-pinpoint-email==1.16.53.0"],
        "pinpoint-sms-voice": ["mypy-boto3-pinpoint-sms-voice==1.16.53.0"],
        "polly": ["mypy-boto3-polly==1.16.53.0"],
        "pricing": ["mypy-boto3-pricing==1.16.53.0"],
        "qldb": ["mypy-boto3-qldb==1.16.53.0"],
        "qldb-session": ["mypy-boto3-qldb-session==1.16.53.0"],
        "quicksight": ["mypy-boto3-quicksight==1.16.53.0"],
        "ram": ["mypy-boto3-ram==1.16.53.0"],
        "rds": ["mypy-boto3-rds==1.16.53.0"],
        "rds-data": ["mypy-boto3-rds-data==1.16.53.0"],
        "redshift": ["mypy-boto3-redshift==1.16.53.0"],
        "redshift-data": ["mypy-boto3-redshift-data==1.16.53.0"],
        "rekognition": ["mypy-boto3-rekognition==1.16.53.0"],
        "resource-groups": ["mypy-boto3-resource-groups==1.16.53.0"],
        "resourcegroupstaggingapi": ["mypy-boto3-resourcegroupstaggingapi==1.16.53.0"],
        "robomaker": ["mypy-boto3-robomaker==1.16.53.0"],
        "route53": ["mypy-boto3-route53==1.16.53.0"],
        "route53domains": ["mypy-boto3-route53domains==1.16.53.0"],
        "route53resolver": ["mypy-boto3-route53resolver==1.16.53.0"],
        "s3": ["mypy-boto3-s3==1.16.53.0"],
        "s3control": ["mypy-boto3-s3control==1.16.53.0"],
        "s3outposts": ["mypy-boto3-s3outposts==1.16.53.0"],
        "sagemaker": ["mypy-boto3-sagemaker==1.16.53.0"],
        "sagemaker-a2i-runtime": ["mypy-boto3-sagemaker-a2i-runtime==1.16.53.0"],
        "sagemaker-edge": ["mypy-boto3-sagemaker-edge==1.16.53.0"],
        "sagemaker-featurestore-runtime": ["mypy-boto3-sagemaker-featurestore-runtime==1.16.53.0"],
        "sagemaker-runtime": ["mypy-boto3-sagemaker-runtime==1.16.53.0"],
        "savingsplans": ["mypy-boto3-savingsplans==1.16.53.0"],
        "schemas": ["mypy-boto3-schemas==1.16.53.0"],
        "sdb": ["mypy-boto3-sdb==1.16.53.0"],
        "secretsmanager": ["mypy-boto3-secretsmanager==1.16.53.0"],
        "securityhub": ["mypy-boto3-securityhub==1.16.53.0"],
        "serverlessrepo": ["mypy-boto3-serverlessrepo==1.16.53.0"],
        "service-quotas": ["mypy-boto3-service-quotas==1.16.53.0"],
        "servicecatalog": ["mypy-boto3-servicecatalog==1.16.53.0"],
        "servicecatalog-appregistry": ["mypy-boto3-servicecatalog-appregistry==1.16.53.0"],
        "servicediscovery": ["mypy-boto3-servicediscovery==1.16.53.0"],
        "ses": ["mypy-boto3-ses==1.16.53.0"],
        "sesv2": ["mypy-boto3-sesv2==1.16.53.0"],
        "shield": ["mypy-boto3-shield==1.16.53.0"],
        "signer": ["mypy-boto3-signer==1.16.53.0"],
        "sms": ["mypy-boto3-sms==1.16.53.0"],
        "sms-voice": ["mypy-boto3-sms-voice==1.16.53.0"],
        "snowball": ["mypy-boto3-snowball==1.16.53.0"],
        "sns": ["mypy-boto3-sns==1.16.53.0"],
        "sqs": ["mypy-boto3-sqs==1.16.53.0"],
        "ssm": ["mypy-boto3-ssm==1.16.53.0"],
        "sso": ["mypy-boto3-sso==1.16.53.0"],
        "sso-admin": ["mypy-boto3-sso-admin==1.16.53.0"],
        "sso-oidc": ["mypy-boto3-sso-oidc==1.16.53.0"],
        "stepfunctions": ["mypy-boto3-stepfunctions==1.16.53.0"],
        "storagegateway": ["mypy-boto3-storagegateway==1.16.53.0"],
        "sts": ["mypy-boto3-sts==1.16.53.0"],
        "support": ["mypy-boto3-support==1.16.53.0"],
        "swf": ["mypy-boto3-swf==1.16.53.0"],
        "synthetics": ["mypy-boto3-synthetics==1.16.53.0"],
        "textract": ["mypy-boto3-textract==1.16.53.0"],
        "timestream-query": ["mypy-boto3-timestream-query==1.16.53.0"],
        "timestream-write": ["mypy-boto3-timestream-write==1.16.53.0"],
        "transcribe": ["mypy-boto3-transcribe==1.16.53.0"],
        "transfer": ["mypy-boto3-transfer==1.16.53.0"],
        "translate": ["mypy-boto3-translate==1.16.53.0"],
        "waf": ["mypy-boto3-waf==1.16.53.0"],
        "waf-regional": ["mypy-boto3-waf-regional==1.16.53.0"],
        "wafv2": ["mypy-boto3-wafv2==1.16.53.0"],
        "wellarchitected": ["mypy-boto3-wellarchitected==1.16.53.0"],
        "workdocs": ["mypy-boto3-workdocs==1.16.53.0"],
        "worklink": ["mypy-boto3-worklink==1.16.53.0"],
        "workmail": ["mypy-boto3-workmail==1.16.53.0"],
        "workmailmessageflow": ["mypy-boto3-workmailmessageflow==1.16.53.0"],
        "workspaces": ["mypy-boto3-workspaces==1.16.53.0"],
        "xray": ["mypy-boto3-xray==1.16.53.0"],
    },
    zip_safe=False,
)
