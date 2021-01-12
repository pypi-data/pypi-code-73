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

__all__ = ['VpnGateway']


class VpnGateway(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bgp_settings: Optional[pulumi.Input[pulumi.InputType['VpnGatewayBgpSettingsArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scale_unit: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a VPN Gateway within a Virtual Hub, which enables Site-to-Site communication.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            address_spaces=["10.0.0.0/16"])
        example_virtual_wan = azure.network.VirtualWan("exampleVirtualWan",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        example_virtual_hub = azure.network.VirtualHub("exampleVirtualHub",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            virtual_wan_id=example_virtual_wan.id,
            address_prefix="10.0.1.0/24")
        example_vpn_gateway = azure.network.VpnGateway("exampleVpnGateway",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            virtual_hub_id=example_virtual_hub.id)
        ```

        ## Import

        VPN Gateways can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/vpnGateway:VpnGateway gateway1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Network/vpnGateways/gateway1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['VpnGatewayBgpSettingsArgs']] bgp_settings: A `bgp_settings` block as defined below.
        :param pulumi.Input[str] location: The Azure location where this VPN Gateway should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The Name which should be used for this VPN Gateway. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group in which this VPN Gateway should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[int] scale_unit: The Scale Unit for this VPN Gateway. Defaults to `1`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the VPN Gateway.
        :param pulumi.Input[str] virtual_hub_id: The ID of the Virtual Hub within which this VPN Gateway should be created. Changing this forces a new resource to be created.
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

            __props__['bgp_settings'] = bgp_settings
            __props__['location'] = location
            __props__['name'] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['scale_unit'] = scale_unit
            __props__['tags'] = tags
            if virtual_hub_id is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_hub_id'")
            __props__['virtual_hub_id'] = virtual_hub_id
        super(VpnGateway, __self__).__init__(
            'azure:network/vpnGateway:VpnGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bgp_settings: Optional[pulumi.Input[pulumi.InputType['VpnGatewayBgpSettingsArgs']]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            scale_unit: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            virtual_hub_id: Optional[pulumi.Input[str]] = None) -> 'VpnGateway':
        """
        Get an existing VpnGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['VpnGatewayBgpSettingsArgs']] bgp_settings: A `bgp_settings` block as defined below.
        :param pulumi.Input[str] location: The Azure location where this VPN Gateway should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The Name which should be used for this VPN Gateway. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group in which this VPN Gateway should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[int] scale_unit: The Scale Unit for this VPN Gateway. Defaults to `1`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the VPN Gateway.
        :param pulumi.Input[str] virtual_hub_id: The ID of the Virtual Hub within which this VPN Gateway should be created. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["bgp_settings"] = bgp_settings
        __props__["location"] = location
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["scale_unit"] = scale_unit
        __props__["tags"] = tags
        __props__["virtual_hub_id"] = virtual_hub_id
        return VpnGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bgpSettings")
    def bgp_settings(self) -> pulumi.Output['outputs.VpnGatewayBgpSettings']:
        """
        A `bgp_settings` block as defined below.
        """
        return pulumi.get(self, "bgp_settings")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The Azure location where this VPN Gateway should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The Name which should be used for this VPN Gateway. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The Name of the Resource Group in which this VPN Gateway should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="scaleUnit")
    def scale_unit(self) -> pulumi.Output[Optional[int]]:
        """
        The Scale Unit for this VPN Gateway. Defaults to `1`.
        """
        return pulumi.get(self, "scale_unit")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the VPN Gateway.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="virtualHubId")
    def virtual_hub_id(self) -> pulumi.Output[str]:
        """
        The ID of the Virtual Hub within which this VPN Gateway should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "virtual_hub_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

