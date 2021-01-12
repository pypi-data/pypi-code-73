# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['GroupMembership']


class GroupMembership(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages group membership within Azure DevOps.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        project = azuredevops.Project("project")
        user = azuredevops.User("user", principal_name="foo@contoso.com")
        group = project.id.apply(lambda id: azuredevops.get_group(project_id=id,
            name="Build Administrators"))
        membership = azuredevops.GroupMembership("membership",
            group=group.descriptor,
            members=[user.descriptor])
        ```
        ## Relevant Links

        - [Azure DevOps Service REST API 5.1 - Memberships](https://docs.microsoft.com/en-us/rest/api/azure/devops/graph/memberships?view=azure-devops-rest-5.0)

        ## PAT Permissions Required

        - **Deployment Groups**: Read & Manage

        ## Import

        Not supported.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group: The descriptor of the group being managed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: A list of user or group descriptors that will become members of the group.
               > NOTE: It's possible to define group members both within the `GroupMembership resource` via the members block and by using the `Group` resource. However it's not possible to use both methods to manage group members, since there'll be conflicts.
        :param pulumi.Input[str] mode: The mode how the resource manages group members.
               - `mode == add`: the resource will ensure that all specified members will be part of the referenced group
               - `mode == overwrite`: the resource will replace all existing members with the members specified within the `members` block
               > NOTE: To clear all members from a group, specify an empty list of descriptors in the `members` attribute and set the `mode` member to `overwrite`.
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

            if group is None and not opts.urn:
                raise TypeError("Missing required property 'group'")
            __props__['group'] = group
            if members is None and not opts.urn:
                raise TypeError("Missing required property 'members'")
            __props__['members'] = members
            __props__['mode'] = mode
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azuredevops:Identities/groupMembership:GroupMembership")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(GroupMembership, __self__).__init__(
            'azuredevops:index/groupMembership:GroupMembership',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            group: Optional[pulumi.Input[str]] = None,
            members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            mode: Optional[pulumi.Input[str]] = None) -> 'GroupMembership':
        """
        Get an existing GroupMembership resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group: The descriptor of the group being managed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: A list of user or group descriptors that will become members of the group.
               > NOTE: It's possible to define group members both within the `GroupMembership resource` via the members block and by using the `Group` resource. However it's not possible to use both methods to manage group members, since there'll be conflicts.
        :param pulumi.Input[str] mode: The mode how the resource manages group members.
               - `mode == add`: the resource will ensure that all specified members will be part of the referenced group
               - `mode == overwrite`: the resource will replace all existing members with the members specified within the `members` block
               > NOTE: To clear all members from a group, specify an empty list of descriptors in the `members` attribute and set the `mode` member to `overwrite`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["group"] = group
        __props__["members"] = members
        __props__["mode"] = mode
        return GroupMembership(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def group(self) -> pulumi.Output[str]:
        """
        The descriptor of the group being managed.
        """
        return pulumi.get(self, "group")

    @property
    @pulumi.getter
    def members(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of user or group descriptors that will become members of the group.
        > NOTE: It's possible to define group members both within the `GroupMembership resource` via the members block and by using the `Group` resource. However it's not possible to use both methods to manage group members, since there'll be conflicts.
        """
        return pulumi.get(self, "members")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[str]]:
        """
        The mode how the resource manages group members.
        - `mode == add`: the resource will ensure that all specified members will be part of the referenced group
        - `mode == overwrite`: the resource will replace all existing members with the members specified within the `members` block
        > NOTE: To clear all members from a group, specify an empty list of descriptors in the `members` attribute and set the `mode` member to `overwrite`.
        """
        return pulumi.get(self, "mode")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

