import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "aws-cdk.aws-codeguruprofiler",
    "version": "1.84.0",
    "description": "The CDK Construct Library for AWS::CodeGuruProfiler",
    "license": "Apache-2.0",
    "url": "https://github.com/aws/aws-cdk",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/aws/aws-cdk.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_cdk.aws_codeguruprofiler",
        "aws_cdk.aws_codeguruprofiler._jsii"
    ],
    "package_data": {
        "aws_cdk.aws_codeguruprofiler._jsii": [
            "aws-codeguruprofiler@1.84.0.jsii.tgz"
        ],
        "aws_cdk.aws_codeguruprofiler": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.aws-iam==1.84.0",
        "aws-cdk.core==1.84.0",
        "constructs>=3.2.0, <4.0.0",
        "jsii>=1.15.0, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved",
        "Framework :: AWS CDK",
        "Framework :: AWS CDK :: 1"
    ]
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
