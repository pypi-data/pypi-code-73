# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['RouterInterface']


class RouterInterface(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 interconnect_attachment: Optional[pulumi.Input[str]] = None,
                 ip_range: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 router: Optional[pulumi.Input[str]] = None,
                 vpn_tunnel: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Cloud Router interface. For more information see
        [the official documentation](https://cloud.google.com/compute/docs/cloudrouter)
        and
        [API](https://cloud.google.com/compute/docs/reference/latest/routers).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gcp as gcp

        foobar = gcp.compute.RouterInterface("foobar",
            ip_range="169.254.1.1/30",
            region="us-central1",
            router="router-1",
            vpn_tunnel="tunnel-1")
        ```

        ## Import

        Router interfaces can be imported using the `region`, `router`, and `name`, e.g.

        ```sh
         $ pulumi import gcp:compute/routerInterface:RouterInterface foobar us-central1/router-1/interface-1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] interconnect_attachment: The name or resource link to the
               VLAN interconnect for this interface. Changing this forces a new interface to
               be created. Only one of `vpn_tunnel` and `interconnect_attachment` can be
               specified.
        :param pulumi.Input[str] ip_range: IP address and range of the interface. The IP range must be
               in the RFC3927 link-local IP space. Changing this forces a new interface to be created.
        :param pulumi.Input[str] name: A unique name for the interface, required by GCE. Changing
               this forces a new interface to be created.
        :param pulumi.Input[str] project: The ID of the project in which this interface's router belongs. If it
               is not provided, the provider project is used. Changing this forces a new interface to be created.
        :param pulumi.Input[str] region: The region this interface's router sits in. If not specified,
               the project region will be used. Changing this forces a new interface to be
               created.
        :param pulumi.Input[str] router: The name of the router this interface will be attached to.
               Changing this forces a new interface to be created.
        :param pulumi.Input[str] vpn_tunnel: The name or resource link to the VPN tunnel this
               interface will be linked to. Changing this forces a new interface to be created. Only
               one of `vpn_tunnel` and `interconnect_attachment` can be specified.
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

            __props__['interconnect_attachment'] = interconnect_attachment
            __props__['ip_range'] = ip_range
            __props__['name'] = name
            __props__['project'] = project
            __props__['region'] = region
            if router is None and not opts.urn:
                raise TypeError("Missing required property 'router'")
            __props__['router'] = router
            __props__['vpn_tunnel'] = vpn_tunnel
        super(RouterInterface, __self__).__init__(
            'gcp:compute/routerInterface:RouterInterface',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            interconnect_attachment: Optional[pulumi.Input[str]] = None,
            ip_range: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            router: Optional[pulumi.Input[str]] = None,
            vpn_tunnel: Optional[pulumi.Input[str]] = None) -> 'RouterInterface':
        """
        Get an existing RouterInterface resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] interconnect_attachment: The name or resource link to the
               VLAN interconnect for this interface. Changing this forces a new interface to
               be created. Only one of `vpn_tunnel` and `interconnect_attachment` can be
               specified.
        :param pulumi.Input[str] ip_range: IP address and range of the interface. The IP range must be
               in the RFC3927 link-local IP space. Changing this forces a new interface to be created.
        :param pulumi.Input[str] name: A unique name for the interface, required by GCE. Changing
               this forces a new interface to be created.
        :param pulumi.Input[str] project: The ID of the project in which this interface's router belongs. If it
               is not provided, the provider project is used. Changing this forces a new interface to be created.
        :param pulumi.Input[str] region: The region this interface's router sits in. If not specified,
               the project region will be used. Changing this forces a new interface to be
               created.
        :param pulumi.Input[str] router: The name of the router this interface will be attached to.
               Changing this forces a new interface to be created.
        :param pulumi.Input[str] vpn_tunnel: The name or resource link to the VPN tunnel this
               interface will be linked to. Changing this forces a new interface to be created. Only
               one of `vpn_tunnel` and `interconnect_attachment` can be specified.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["interconnect_attachment"] = interconnect_attachment
        __props__["ip_range"] = ip_range
        __props__["name"] = name
        __props__["project"] = project
        __props__["region"] = region
        __props__["router"] = router
        __props__["vpn_tunnel"] = vpn_tunnel
        return RouterInterface(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="interconnectAttachment")
    def interconnect_attachment(self) -> pulumi.Output[Optional[str]]:
        """
        The name or resource link to the
        VLAN interconnect for this interface. Changing this forces a new interface to
        be created. Only one of `vpn_tunnel` and `interconnect_attachment` can be
        specified.
        """
        return pulumi.get(self, "interconnect_attachment")

    @property
    @pulumi.getter(name="ipRange")
    def ip_range(self) -> pulumi.Output[Optional[str]]:
        """
        IP address and range of the interface. The IP range must be
        in the RFC3927 link-local IP space. Changing this forces a new interface to be created.
        """
        return pulumi.get(self, "ip_range")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique name for the interface, required by GCE. Changing
        this forces a new interface to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which this interface's router belongs. If it
        is not provided, the provider project is used. Changing this forces a new interface to be created.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region this interface's router sits in. If not specified,
        the project region will be used. Changing this forces a new interface to be
        created.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def router(self) -> pulumi.Output[str]:
        """
        The name of the router this interface will be attached to.
        Changing this forces a new interface to be created.
        """
        return pulumi.get(self, "router")

    @property
    @pulumi.getter(name="vpnTunnel")
    def vpn_tunnel(self) -> pulumi.Output[Optional[str]]:
        """
        The name or resource link to the VPN tunnel this
        interface will be linked to. Changing this forces a new interface to be created. Only
        one of `vpn_tunnel` and `interconnect_attachment` can be specified.
        """
        return pulumi.get(self, "vpn_tunnel")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

