# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['User']


class User(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_license_type: Optional[pulumi.Input[str]] = None,
                 licensing_source: Optional[pulumi.Input[str]] = None,
                 origin: Optional[pulumi.Input[str]] = None,
                 origin_id: Optional[pulumi.Input[str]] = None,
                 principal_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a user entitlement within Azure DevOps.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        user = azuredevops.User("user", principal_name="foo@contoso.com")
        ```
        ## Relevant Links

        - [Azure DevOps Service REST API 5.1 - User Entitlements - Add](https://docs.microsoft.com/en-us/rest/api/azure/devops/memberentitlementmanagement/user%20entitlements/add?view=azure-devops-rest-5.1)

        ## PAT Permissions Required

        - **Member Entitlement Management**: Read & Write

        ## Import

        The resources allows the import via the UUID of a user entitlement or by using the principal name of a user owning an entitlement.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_license_type: Type of Account License. Valid values: `advanced`, `earlyAdopter`, `express`, `none`, `professional`, or `stakeholder`. Defaults to `express`. In addition the value `basic` is allowed which is an alias for `express` and reflects the name of the `express` license used in the Azure DevOps web interface.
        :param pulumi.Input[str] licensing_source: The source of the licensing (e.g. Account. MSDN etc.) Valid values: `account` (Default), `auto`, `msdn`, `none`, `profile`, `trail`
        :param pulumi.Input[str] origin: The type of source provider for the origin identifier.
        :param pulumi.Input[str] origin_id: The unique identifier from the system of origin. Typically a sid, object id or Guid. e.g. Used for member of other tenant on Azure Active Directory.
        :param pulumi.Input[str] principal_name: The principal name is the PrincipalName of a graph member from the source provider. Usually, e-mail address.
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

            __props__['account_license_type'] = account_license_type
            __props__['licensing_source'] = licensing_source
            __props__['origin'] = origin
            __props__['origin_id'] = origin_id
            __props__['principal_name'] = principal_name
            __props__['descriptor'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azuredevops:Entitlement/user:User")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(User, __self__).__init__(
            'azuredevops:index/user:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_license_type: Optional[pulumi.Input[str]] = None,
            descriptor: Optional[pulumi.Input[str]] = None,
            licensing_source: Optional[pulumi.Input[str]] = None,
            origin: Optional[pulumi.Input[str]] = None,
            origin_id: Optional[pulumi.Input[str]] = None,
            principal_name: Optional[pulumi.Input[str]] = None) -> 'User':
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_license_type: Type of Account License. Valid values: `advanced`, `earlyAdopter`, `express`, `none`, `professional`, or `stakeholder`. Defaults to `express`. In addition the value `basic` is allowed which is an alias for `express` and reflects the name of the `express` license used in the Azure DevOps web interface.
        :param pulumi.Input[str] descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the user graph subject.
        :param pulumi.Input[str] licensing_source: The source of the licensing (e.g. Account. MSDN etc.) Valid values: `account` (Default), `auto`, `msdn`, `none`, `profile`, `trail`
        :param pulumi.Input[str] origin: The type of source provider for the origin identifier.
        :param pulumi.Input[str] origin_id: The unique identifier from the system of origin. Typically a sid, object id or Guid. e.g. Used for member of other tenant on Azure Active Directory.
        :param pulumi.Input[str] principal_name: The principal name is the PrincipalName of a graph member from the source provider. Usually, e-mail address.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["account_license_type"] = account_license_type
        __props__["descriptor"] = descriptor
        __props__["licensing_source"] = licensing_source
        __props__["origin"] = origin
        __props__["origin_id"] = origin_id
        __props__["principal_name"] = principal_name
        return User(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountLicenseType")
    def account_license_type(self) -> pulumi.Output[Optional[str]]:
        """
        Type of Account License. Valid values: `advanced`, `earlyAdopter`, `express`, `none`, `professional`, or `stakeholder`. Defaults to `express`. In addition the value `basic` is allowed which is an alias for `express` and reflects the name of the `express` license used in the Azure DevOps web interface.
        """
        return pulumi.get(self, "account_license_type")

    @property
    @pulumi.getter
    def descriptor(self) -> pulumi.Output[str]:
        """
        The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the user graph subject.
        """
        return pulumi.get(self, "descriptor")

    @property
    @pulumi.getter(name="licensingSource")
    def licensing_source(self) -> pulumi.Output[Optional[str]]:
        """
        The source of the licensing (e.g. Account. MSDN etc.) Valid values: `account` (Default), `auto`, `msdn`, `none`, `profile`, `trail`
        """
        return pulumi.get(self, "licensing_source")

    @property
    @pulumi.getter
    def origin(self) -> pulumi.Output[str]:
        """
        The type of source provider for the origin identifier.
        """
        return pulumi.get(self, "origin")

    @property
    @pulumi.getter(name="originId")
    def origin_id(self) -> pulumi.Output[str]:
        """
        The unique identifier from the system of origin. Typically a sid, object id or Guid. e.g. Used for member of other tenant on Azure Active Directory.
        """
        return pulumi.get(self, "origin_id")

    @property
    @pulumi.getter(name="principalName")
    def principal_name(self) -> pulumi.Output[str]:
        """
        The principal name is the PrincipalName of a graph member from the source provider. Usually, e-mail address.
        """
        return pulumi.get(self, "principal_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

