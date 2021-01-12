# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Account']


class Account(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Allows management of a [Google Cloud Platform service account](https://cloud.google.com/compute/docs/access/service-accounts)

        > **Warning:**  If you delete and recreate a service account, you must reapply any IAM roles that it had before.

        > Creation of service accounts is eventually consistent, and that can lead to
        errors when you try to apply ACLs to service accounts immediately after
        creation.

        ## Example Usage

        This snippet creates a service account in a project.

        ```python
        import pulumi
        import pulumi_gcp as gcp

        service_account = gcp.service_account.Account("serviceAccount",
            account_id="service-account-id",
            display_name="Service Account")
        ```

        ## Import

        Service accounts can be imported using their URI, e.g.

        ```sh
         $ pulumi import gcp:serviceAccount/account:Account my_sa projects/my-project/serviceAccounts/my-sa@my-project.iam.gserviceaccount.com
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account id that is used to generate the service
               account email address and a stable unique id. It is unique within a project,
               must be 6-30 characters long, and match the regular expression `a-z`
               to comply with RFC1035. Changing this forces a new service account to be created.
        :param pulumi.Input[str] description: A text description of the service account.
               Must be less than or equal to 256 UTF-8 bytes.
        :param pulumi.Input[str] display_name: The display name for the service account.
               Can be updated without creating a new resource.
        :param pulumi.Input[str] project: The ID of the project that the service account will be created in.
               Defaults to the provider project configuration.
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

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__['account_id'] = account_id
            __props__['description'] = description
            __props__['display_name'] = display_name
            __props__['project'] = project
            __props__['email'] = None
            __props__['name'] = None
            __props__['unique_id'] = None
        super(Account, __self__).__init__(
            'gcp:serviceAccount/account:Account',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            email: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            unique_id: Optional[pulumi.Input[str]] = None) -> 'Account':
        """
        Get an existing Account resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account id that is used to generate the service
               account email address and a stable unique id. It is unique within a project,
               must be 6-30 characters long, and match the regular expression `a-z`
               to comply with RFC1035. Changing this forces a new service account to be created.
        :param pulumi.Input[str] description: A text description of the service account.
               Must be less than or equal to 256 UTF-8 bytes.
        :param pulumi.Input[str] display_name: The display name for the service account.
               Can be updated without creating a new resource.
        :param pulumi.Input[str] email: The e-mail address of the service account. This value
               should be referenced from any `organizations.getIAMPolicy` data sources
               that would grant the service account privileges.
        :param pulumi.Input[str] name: The fully-qualified name of the service account.
        :param pulumi.Input[str] project: The ID of the project that the service account will be created in.
               Defaults to the provider project configuration.
        :param pulumi.Input[str] unique_id: The unique id of the service account.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["account_id"] = account_id
        __props__["description"] = description
        __props__["display_name"] = display_name
        __props__["email"] = email
        __props__["name"] = name
        __props__["project"] = project
        __props__["unique_id"] = unique_id
        return Account(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The account id that is used to generate the service
        account email address and a stable unique id. It is unique within a project,
        must be 6-30 characters long, and match the regular expression `a-z`
        to comply with RFC1035. Changing this forces a new service account to be created.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A text description of the service account.
        Must be less than or equal to 256 UTF-8 bytes.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name for the service account.
        Can be updated without creating a new resource.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        The e-mail address of the service account. This value
        should be referenced from any `organizations.getIAMPolicy` data sources
        that would grant the service account privileges.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The fully-qualified name of the service account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project that the service account will be created in.
        Defaults to the provider project configuration.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> pulumi.Output[str]:
        """
        The unique id of the service account.
        """
        return pulumi.get(self, "unique_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

