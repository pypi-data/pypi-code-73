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

__all__ = ['Cluster']


class Cluster(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ClusterIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 size_gb: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        !> **Important** Due to capacity constraints, Microsoft requires you to pre-register your subscription IDs before you are allowed to create a Log Analytics cluster. Contact Microsoft, or open a support request to register your subscription IDs.

        > **Note:** Log Analytics Clusters are subject to 14-day soft delete policy. Clusters created with the same resource group & name as a previously deleted cluster will be recovered rather than creating anew.

        Manages a Log Analytics Cluster.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_cluster = azure.loganalytics.Cluster("exampleCluster",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            identity=azure.loganalytics.ClusterIdentityArgs(
                type="SystemAssigned",
            ))
        ```

        ## Import

        Log Analytics Clusters can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:loganalytics/cluster:Cluster example /subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/group1/providers/Microsoft.OperationalInsights/clusters/cluster1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ClusterIdentityArgs']] identity: A `identity` block as defined below. Changing this forces a new Log Analytics Cluster to be created.
        :param pulumi.Input[str] location: The Azure Region where the Log Analytics Cluster should exist. Changing this forces a new Log Analytics Cluster to be created.
        :param pulumi.Input[str] name: The name which should be used for this Log Analytics Cluster. Changing this forces a new Log Analytics Cluster to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Log Analytics Cluster should exist. Changing this forces a new Log Analytics Cluster to be created.
        :param pulumi.Input[int] size_gb: The capacity of the Log Analytics Cluster specified in GB/day. Defaults to 1000.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Log Analytics Cluster.
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

            if identity is None and not opts.urn:
                raise TypeError("Missing required property 'identity'")
            __props__['identity'] = identity
            __props__['location'] = location
            __props__['name'] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['size_gb'] = size_gb
            __props__['tags'] = tags
            __props__['cluster_id'] = None
        super(Cluster, __self__).__init__(
            'azure:loganalytics/cluster:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            identity: Optional[pulumi.Input[pulumi.InputType['ClusterIdentityArgs']]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            size_gb: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The GUID of the cluster.
        :param pulumi.Input[pulumi.InputType['ClusterIdentityArgs']] identity: A `identity` block as defined below. Changing this forces a new Log Analytics Cluster to be created.
        :param pulumi.Input[str] location: The Azure Region where the Log Analytics Cluster should exist. Changing this forces a new Log Analytics Cluster to be created.
        :param pulumi.Input[str] name: The name which should be used for this Log Analytics Cluster. Changing this forces a new Log Analytics Cluster to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Log Analytics Cluster should exist. Changing this forces a new Log Analytics Cluster to be created.
        :param pulumi.Input[int] size_gb: The capacity of the Log Analytics Cluster specified in GB/day. Defaults to 1000.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Log Analytics Cluster.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cluster_id"] = cluster_id
        __props__["identity"] = identity
        __props__["location"] = location
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["size_gb"] = size_gb
        __props__["tags"] = tags
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The GUID of the cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output['outputs.ClusterIdentity']:
        """
        A `identity` block as defined below. Changing this forces a new Log Analytics Cluster to be created.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The Azure Region where the Log Analytics Cluster should exist. Changing this forces a new Log Analytics Cluster to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Log Analytics Cluster. Changing this forces a new Log Analytics Cluster to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the Log Analytics Cluster should exist. Changing this forces a new Log Analytics Cluster to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> pulumi.Output[Optional[int]]:
        """
        The capacity of the Log Analytics Cluster specified in GB/day. Defaults to 1000.
        """
        return pulumi.get(self, "size_gb")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags which should be assigned to the Log Analytics Cluster.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

