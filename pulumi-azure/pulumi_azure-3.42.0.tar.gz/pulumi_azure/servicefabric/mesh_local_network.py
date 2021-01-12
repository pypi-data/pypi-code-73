# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['MeshLocalNetwork']


class MeshLocalNetwork(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_address_prefix: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Service Fabric Mesh Local Network.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_mesh_local_network = azure.servicefabric.MeshLocalNetwork("exampleMeshLocalNetwork",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            network_address_prefix="10.0.0.0/22")
        ```

        ## Import

        Service Fabric Mesh Local Network can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:servicefabric/meshLocalNetwork:MeshLocalNetwork network1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.ServiceFabricMesh/networks/network1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of this Service Fabric Mesh Local Network.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Service Fabric Mesh Local Network should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Service Fabric Mesh Local Network. Changing this forces a new resource to be created.
        :param pulumi.Input[str] network_address_prefix: The address space for the local container network.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group in which the Service Fabric Mesh Local Network exists. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
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

            __props__['description'] = description
            __props__['location'] = location
            __props__['name'] = name
            if network_address_prefix is None and not opts.urn:
                raise TypeError("Missing required property 'network_address_prefix'")
            __props__['network_address_prefix'] = network_address_prefix
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['tags'] = tags
        super(MeshLocalNetwork, __self__).__init__(
            'azure:servicefabric/meshLocalNetwork:MeshLocalNetwork',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_address_prefix: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'MeshLocalNetwork':
        """
        Get an existing MeshLocalNetwork resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of this Service Fabric Mesh Local Network.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Service Fabric Mesh Local Network should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Service Fabric Mesh Local Network. Changing this forces a new resource to be created.
        :param pulumi.Input[str] network_address_prefix: The address space for the local container network.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group in which the Service Fabric Mesh Local Network exists. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["location"] = location
        __props__["name"] = name
        __props__["network_address_prefix"] = network_address_prefix
        __props__["resource_group_name"] = resource_group_name
        __props__["tags"] = tags
        return MeshLocalNetwork(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of this Service Fabric Mesh Local Network.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the Azure Region where the Service Fabric Mesh Local Network should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Service Fabric Mesh Local Network. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkAddressPrefix")
    def network_address_prefix(self) -> pulumi.Output[str]:
        """
        The address space for the local container network.
        """
        return pulumi.get(self, "network_address_prefix")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group in which the Service Fabric Mesh Local Network exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

