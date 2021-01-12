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

__all__ = ['Table']


class Table(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acls: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableAclArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Table within an Azure Storage Account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_table = azure.storage.Table("exampleTable", storage_account_name=example_account.name)
        ```

        ## Import

        Table's within a Storage Account can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:storage/table:Table table1 "https://example.table.core.windows.net/Tables('replace-with-table-name')"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableAclArgs']]]] acls: One or more `acl` blocks as defined below.
        :param pulumi.Input[str] name: The name of the storage table. Must be unique within the storage account the table is located.
        :param pulumi.Input[str] storage_account_name: Specifies the storage account in which to create the storage table.
               Changing this forces a new resource to be created.
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

            __props__['acls'] = acls
            __props__['name'] = name
            if storage_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_name'")
            __props__['storage_account_name'] = storage_account_name
        super(Table, __self__).__init__(
            'azure:storage/table:Table',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            acls: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableAclArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            storage_account_name: Optional[pulumi.Input[str]] = None) -> 'Table':
        """
        Get an existing Table resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableAclArgs']]]] acls: One or more `acl` blocks as defined below.
        :param pulumi.Input[str] name: The name of the storage table. Must be unique within the storage account the table is located.
        :param pulumi.Input[str] storage_account_name: Specifies the storage account in which to create the storage table.
               Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["acls"] = acls
        __props__["name"] = name
        __props__["storage_account_name"] = storage_account_name
        return Table(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def acls(self) -> pulumi.Output[Optional[Sequence['outputs.TableAcl']]]:
        """
        One or more `acl` blocks as defined below.
        """
        return pulumi.get(self, "acls")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the storage table. Must be unique within the storage account the table is located.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> pulumi.Output[str]:
        """
        Specifies the storage account in which to create the storage table.
        Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "storage_account_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

