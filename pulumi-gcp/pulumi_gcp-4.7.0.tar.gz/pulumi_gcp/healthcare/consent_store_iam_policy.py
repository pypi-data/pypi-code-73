# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['ConsentStoreIamPolicy']


class ConsentStoreIamPolicy(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 consent_store_id: Optional[pulumi.Input[str]] = None,
                 dataset: Optional[pulumi.Input[str]] = None,
                 policy_data: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Import

        For all import syntaxes, the "resource in question" can take any of the following forms* {{dataset}}/consentStores/{{name}} * {{name}} Any variables not passed in the import command will be taken from the provider configuration. Cloud Healthcare consentstore IAM resources can be imported using the resource identifiers, role, and member. IAM member imports use space-delimited identifiersthe resource in question, the role, and the member identity, e.g.

        ```sh
         $ pulumi import gcp:healthcare/consentStoreIamPolicy:ConsentStoreIamPolicy editor "{{dataset}}/consentStores/{{consent_store}} roles/viewer user:jane@example.com"
        ```

         IAM binding imports use space-delimited identifiersthe resource in question and the role, e.g.

        ```sh
         $ pulumi import gcp:healthcare/consentStoreIamPolicy:ConsentStoreIamPolicy editor "{{dataset}}/consentStores/{{consent_store}} roles/viewer"
        ```

         IAM policy imports use the identifier of the resource in question, e.g.

        ```sh
         $ pulumi import gcp:healthcare/consentStoreIamPolicy:ConsentStoreIamPolicy editor {{dataset}}/consentStores/{{consent_store}}
        ```

         -> **Custom Roles**If you're importing a IAM resource with a custom role, make sure to use the

        full name of the custom role, e.g. `[projects/my-project|organizations/my-org]/roles/my-custom-role`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] consent_store_id: Used to find the parent resource to bind the IAM policy to
        :param pulumi.Input[str] dataset: Identifies the dataset addressed by this request. Must be in the format
               'projects/{project}/locations/{location}/datasets/{dataset}'
               Used to find the parent resource to bind the IAM policy to
        :param pulumi.Input[str] policy_data: The policy data generated by
               a `organizations.getIAMPolicy` data source.
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

            if consent_store_id is None and not opts.urn:
                raise TypeError("Missing required property 'consent_store_id'")
            __props__['consent_store_id'] = consent_store_id
            if dataset is None and not opts.urn:
                raise TypeError("Missing required property 'dataset'")
            __props__['dataset'] = dataset
            if policy_data is None and not opts.urn:
                raise TypeError("Missing required property 'policy_data'")
            __props__['policy_data'] = policy_data
            __props__['etag'] = None
        super(ConsentStoreIamPolicy, __self__).__init__(
            'gcp:healthcare/consentStoreIamPolicy:ConsentStoreIamPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            consent_store_id: Optional[pulumi.Input[str]] = None,
            dataset: Optional[pulumi.Input[str]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            policy_data: Optional[pulumi.Input[str]] = None) -> 'ConsentStoreIamPolicy':
        """
        Get an existing ConsentStoreIamPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] consent_store_id: Used to find the parent resource to bind the IAM policy to
        :param pulumi.Input[str] dataset: Identifies the dataset addressed by this request. Must be in the format
               'projects/{project}/locations/{location}/datasets/{dataset}'
               Used to find the parent resource to bind the IAM policy to
        :param pulumi.Input[str] etag: (Computed) The etag of the IAM policy.
        :param pulumi.Input[str] policy_data: The policy data generated by
               a `organizations.getIAMPolicy` data source.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["consent_store_id"] = consent_store_id
        __props__["dataset"] = dataset
        __props__["etag"] = etag
        __props__["policy_data"] = policy_data
        return ConsentStoreIamPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="consentStoreId")
    def consent_store_id(self) -> pulumi.Output[str]:
        """
        Used to find the parent resource to bind the IAM policy to
        """
        return pulumi.get(self, "consent_store_id")

    @property
    @pulumi.getter
    def dataset(self) -> pulumi.Output[str]:
        """
        Identifies the dataset addressed by this request. Must be in the format
        'projects/{project}/locations/{location}/datasets/{dataset}'
        Used to find the parent resource to bind the IAM policy to
        """
        return pulumi.get(self, "dataset")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        (Computed) The etag of the IAM policy.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> pulumi.Output[str]:
        """
        The policy data generated by
        a `organizations.getIAMPolicy` data source.
        """
        return pulumi.get(self, "policy_data")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

