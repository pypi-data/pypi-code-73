# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Topic']


class Topic(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kms_key_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 message_storage_policy: Optional[pulumi.Input[pulumi.InputType['TopicMessageStoragePolicyArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        A named resource to which messages are sent by publishers.

        To get more information about Topic, see:

        * [API documentation](https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics)
        * How-to Guides
            * [Managing Topics](https://cloud.google.com/pubsub/docs/admin#managing_topics)

        > **Note:** You can retrieve the email of the Google Managed Pub/Sub Service Account used for forwarding
        by using the `projects.ServiceIdentity` resource.

        ## Example Usage
        ### Pubsub Topic Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.pubsub.Topic("example", labels={
            "foo": "bar",
        })
        ```
        ### Pubsub Topic Cmek

        ```python
        import pulumi
        import pulumi_gcp as gcp

        key_ring = gcp.kms.KeyRing("keyRing", location="global")
        crypto_key = gcp.kms.CryptoKey("cryptoKey", key_ring=key_ring.id)
        example = gcp.pubsub.Topic("example", kms_key_name=crypto_key.id)
        ```
        ### Pubsub Topic Geo Restricted

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.pubsub.Topic("example", message_storage_policy=gcp.pubsub.TopicMessageStoragePolicyArgs(
            allowed_persistence_regions=["europe-west3"],
        ))
        ```

        ## Import

        Topic can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:pubsub/topic:Topic default projects/{{project}}/topics/{{name}}
        ```

        ```sh
         $ pulumi import gcp:pubsub/topic:Topic default {{project}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:pubsub/topic:Topic default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] kms_key_name: The resource name of the Cloud KMS CryptoKey to be used to protect access
               to messages published on this topic. Your project's PubSub service account
               (`service-{{PROJECT_NUMBER}}@gcp-sa-pubsub.iam.gserviceaccount.com`) must have
               `roles/cloudkms.cryptoKeyEncrypterDecrypter` to use this feature.
               The expected format is `projects/*/locations/*/keyRings/*/cryptoKeys/*`
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: A set of key/value label pairs to assign to this Topic.
        :param pulumi.Input[pulumi.InputType['TopicMessageStoragePolicyArgs']] message_storage_policy: Policy constraining the set of Google Cloud Platform regions where
               messages published to the topic may be stored. If not present, then no
               constraints are in effect.
               Structure is documented below.
        :param pulumi.Input[str] name: Name of the topic.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['kms_key_name'] = kms_key_name
            __props__['labels'] = labels
            __props__['message_storage_policy'] = message_storage_policy
            __props__['name'] = name
            __props__['project'] = project
        super(Topic, __self__).__init__(
            'gcp:pubsub/topic:Topic',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            kms_key_name: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            message_storage_policy: Optional[pulumi.Input[pulumi.InputType['TopicMessageStoragePolicyArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None) -> 'Topic':
        """
        Get an existing Topic resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] kms_key_name: The resource name of the Cloud KMS CryptoKey to be used to protect access
               to messages published on this topic. Your project's PubSub service account
               (`service-{{PROJECT_NUMBER}}@gcp-sa-pubsub.iam.gserviceaccount.com`) must have
               `roles/cloudkms.cryptoKeyEncrypterDecrypter` to use this feature.
               The expected format is `projects/*/locations/*/keyRings/*/cryptoKeys/*`
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: A set of key/value label pairs to assign to this Topic.
        :param pulumi.Input[pulumi.InputType['TopicMessageStoragePolicyArgs']] message_storage_policy: Policy constraining the set of Google Cloud Platform regions where
               messages published to the topic may be stored. If not present, then no
               constraints are in effect.
               Structure is documented below.
        :param pulumi.Input[str] name: Name of the topic.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["kms_key_name"] = kms_key_name
        __props__["labels"] = labels
        __props__["message_storage_policy"] = message_storage_policy
        __props__["name"] = name
        __props__["project"] = project
        return Topic(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Output[Optional[str]]:
        """
        The resource name of the Cloud KMS CryptoKey to be used to protect access
        to messages published on this topic. Your project's PubSub service account
        (`service-{{PROJECT_NUMBER}}@gcp-sa-pubsub.iam.gserviceaccount.com`) must have
        `roles/cloudkms.cryptoKeyEncrypterDecrypter` to use this feature.
        The expected format is `projects/*/locations/*/keyRings/*/cryptoKeys/*`
        """
        return pulumi.get(self, "kms_key_name")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A set of key/value label pairs to assign to this Topic.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="messageStoragePolicy")
    def message_storage_policy(self) -> pulumi.Output['outputs.TopicMessageStoragePolicy']:
        """
        Policy constraining the set of Google Cloud Platform regions where
        messages published to the topic may be stored. If not present, then no
        constraints are in effect.
        Structure is documented below.
        """
        return pulumi.get(self, "message_storage_policy")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the topic.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

