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

__all__ = ['RoleDefinition']


class RoleDefinition(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assignable_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoleDefinitionPermissionArgs']]]]] = None,
                 role_definition_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a custom Role Definition, used to assign Roles to Users/Principals. See ['Understand role definitions'](https://docs.microsoft.com/en-us/azure/role-based-access-control/role-definitions) in the Azure documentation for more details.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        primary = azure.core.get_subscription()
        example = azure.authorization.RoleDefinition("example",
            scope=primary.id,
            description="This is a custom role created",
            permissions=[azure.authorization.RoleDefinitionPermissionArgs(
                actions=["*"],
                not_actions=[],
            )],
            assignable_scopes=[primary.id])
        ```

        ## Import

        Role Definitions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:authorization/roleDefinition:RoleDefinition example "/subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Authorization/roleDefinitions/00000000-0000-0000-0000-000000000000|/subscriptions/00000000-0000-0000-0000-000000000000"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] assignable_scopes: One or more assignable scopes for this Role Definition, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`.
        :param pulumi.Input[str] description: A description of the Role Definition.
        :param pulumi.Input[str] name: The name of the Role Definition. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoleDefinitionPermissionArgs']]]] permissions: A `permissions` block as defined below.
        :param pulumi.Input[str] role_definition_id: A unique UUID/GUID which identifies this role - one will be generated if not specified. Changing this forces a new resource to be created.
        :param pulumi.Input[str] scope: The scope at which the Role Definition applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`. It is recommended to use the first entry of the `assignable_scopes`. Changing this forces a new resource to be created.
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

            __props__['assignable_scopes'] = assignable_scopes
            __props__['description'] = description
            __props__['name'] = name
            if permissions is None and not opts.urn:
                raise TypeError("Missing required property 'permissions'")
            __props__['permissions'] = permissions
            __props__['role_definition_id'] = role_definition_id
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__['scope'] = scope
            __props__['role_definition_resource_id'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure:role/definition:Definition")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(RoleDefinition, __self__).__init__(
            'azure:authorization/roleDefinition:RoleDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            assignable_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoleDefinitionPermissionArgs']]]]] = None,
            role_definition_id: Optional[pulumi.Input[str]] = None,
            role_definition_resource_id: Optional[pulumi.Input[str]] = None,
            scope: Optional[pulumi.Input[str]] = None) -> 'RoleDefinition':
        """
        Get an existing RoleDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] assignable_scopes: One or more assignable scopes for this Role Definition, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`.
        :param pulumi.Input[str] description: A description of the Role Definition.
        :param pulumi.Input[str] name: The name of the Role Definition. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoleDefinitionPermissionArgs']]]] permissions: A `permissions` block as defined below.
        :param pulumi.Input[str] role_definition_id: A unique UUID/GUID which identifies this role - one will be generated if not specified. Changing this forces a new resource to be created.
        :param pulumi.Input[str] role_definition_resource_id: The Azure Resource Manager ID for the resource.
        :param pulumi.Input[str] scope: The scope at which the Role Definition applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`. It is recommended to use the first entry of the `assignable_scopes`. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["assignable_scopes"] = assignable_scopes
        __props__["description"] = description
        __props__["name"] = name
        __props__["permissions"] = permissions
        __props__["role_definition_id"] = role_definition_id
        __props__["role_definition_resource_id"] = role_definition_resource_id
        __props__["scope"] = scope
        return RoleDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assignableScopes")
    def assignable_scopes(self) -> pulumi.Output[Sequence[str]]:
        """
        One or more assignable scopes for this Role Definition, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`.
        """
        return pulumi.get(self, "assignable_scopes")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the Role Definition.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Role Definition. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Sequence['outputs.RoleDefinitionPermission']]:
        """
        A `permissions` block as defined below.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> pulumi.Output[str]:
        """
        A unique UUID/GUID which identifies this role - one will be generated if not specified. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "role_definition_id")

    @property
    @pulumi.getter(name="roleDefinitionResourceId")
    def role_definition_resource_id(self) -> pulumi.Output[str]:
        """
        The Azure Resource Manager ID for the resource.
        """
        return pulumi.get(self, "role_definition_resource_id")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[str]:
        """
        The scope at which the Role Definition applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`. It is recommended to use the first entry of the `assignable_scopes`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "scope")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

