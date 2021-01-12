# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Group']


class Group(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 is_cluster: Optional[pulumi.Input[bool]] = None,
                 parent_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The description of a dynamic collection of monitored resources. Each group
        has a filter that is matched against monitored resources and their
        associated metadata. If a group's filter matches an available monitored
        resource, then that resource is a member of that group.

        To get more information about Group, see:

        * [API documentation](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/monitoring/groups/)

        ## Example Usage
        ### Monitoring Group Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        basic = gcp.monitoring.Group("basic",
            display_name="tf-test MonitoringGroup",
            filter="resource.metadata.region=\"europe-west2\"")
        ```
        ### Monitoring Group Subgroup

        ```python
        import pulumi
        import pulumi_gcp as gcp

        parent = gcp.monitoring.Group("parent",
            display_name="tf-test MonitoringParentGroup",
            filter="resource.metadata.region=\"europe-west2\"")
        subgroup = gcp.monitoring.Group("subgroup",
            display_name="tf-test MonitoringSubGroup",
            filter="resource.metadata.region=\"europe-west2\"",
            parent_name=parent.name)
        ```

        ## Import

        Group can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:monitoring/group:Group default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: A user-assigned name for this group, used only for display
               purposes.
        :param pulumi.Input[str] filter: The filter used to determine which monitored resources
               belong to this group.
        :param pulumi.Input[bool] is_cluster: If true, the members of this group are considered to be a
               cluster. The system can perform additional analysis on
               groups that are clusters.
        :param pulumi.Input[str] parent_name: The name of the group's parent, if it has one. The format is
               "projects/{project_id_or_number}/groups/{group_id}". For
               groups with no parent, parentName is the empty string, "".
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

            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__['display_name'] = display_name
            if filter is None and not opts.urn:
                raise TypeError("Missing required property 'filter'")
            __props__['filter'] = filter
            __props__['is_cluster'] = is_cluster
            __props__['parent_name'] = parent_name
            __props__['project'] = project
            __props__['name'] = None
        super(Group, __self__).__init__(
            'gcp:monitoring/group:Group',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            filter: Optional[pulumi.Input[str]] = None,
            is_cluster: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parent_name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None) -> 'Group':
        """
        Get an existing Group resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: A user-assigned name for this group, used only for display
               purposes.
        :param pulumi.Input[str] filter: The filter used to determine which monitored resources
               belong to this group.
        :param pulumi.Input[bool] is_cluster: If true, the members of this group are considered to be a
               cluster. The system can perform additional analysis on
               groups that are clusters.
        :param pulumi.Input[str] name: A unique identifier for this group. The format is "projects/{project_id_or_number}/groups/{group_id}".
        :param pulumi.Input[str] parent_name: The name of the group's parent, if it has one. The format is
               "projects/{project_id_or_number}/groups/{group_id}". For
               groups with no parent, parentName is the empty string, "".
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["display_name"] = display_name
        __props__["filter"] = filter
        __props__["is_cluster"] = is_cluster
        __props__["name"] = name
        __props__["parent_name"] = parent_name
        __props__["project"] = project
        return Group(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        A user-assigned name for this group, used only for display
        purposes.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filter(self) -> pulumi.Output[str]:
        """
        The filter used to determine which monitored resources
        belong to this group.
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter(name="isCluster")
    def is_cluster(self) -> pulumi.Output[Optional[bool]]:
        """
        If true, the members of this group are considered to be a
        cluster. The system can perform additional analysis on
        groups that are clusters.
        """
        return pulumi.get(self, "is_cluster")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique identifier for this group. The format is "projects/{project_id_or_number}/groups/{group_id}".
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parentName")
    def parent_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the group's parent, if it has one. The format is
        "projects/{project_id_or_number}/groups/{group_id}". For
        groups with no parent, parentName is the empty string, "".
        """
        return pulumi.get(self, "parent_name")

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

