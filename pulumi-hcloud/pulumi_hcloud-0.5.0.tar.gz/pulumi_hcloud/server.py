# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Server']


class Server(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backups: Optional[pulumi.Input[bool]] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 image: Optional[pulumi.Input[str]] = None,
                 iso: Optional[pulumi.Input[str]] = None,
                 keep_disk: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerNetworkArgs']]]]] = None,
                 rescue: Optional[pulumi.Input[str]] = None,
                 server_type: Optional[pulumi.Input[str]] = None,
                 ssh_keys: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 user_data: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Import

        Servers can be imported using the server `id`

        ```sh
         $ pulumi import hcloud:index/server:Server myserver <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] backups: Enable or disable backups.
        :param pulumi.Input[str] datacenter: The datacenter name to create the server in.
        :param pulumi.Input[str] image: Name or ID of the image the server is created from.
        :param pulumi.Input[str] iso: ID or Name of an ISO image to mount.
        :param pulumi.Input[bool] keep_disk: If true, do not upgrade the disk. This allows downgrading the server type later.
        :param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs) should be created with.
        :param pulumi.Input[str] location: The location name to create the server in. `nbg1`, `fsn1` or `hel1`
        :param pulumi.Input[str] name: Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).
        :param pulumi.Input[str] rescue: Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
        :param pulumi.Input[str] server_type: Name of the server type this server should be created with.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ssh_keys: SSH key IDs or names which should be injected into the server at creation time
        :param pulumi.Input[str] user_data: Cloud-Init user data to use during server creation
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

            __props__['backups'] = backups
            __props__['datacenter'] = datacenter
            if image is None:
                raise TypeError("Missing required property 'image'")
            __props__['image'] = image
            __props__['iso'] = iso
            __props__['keep_disk'] = keep_disk
            __props__['labels'] = labels
            __props__['location'] = location
            __props__['name'] = name
            __props__['networks'] = networks
            __props__['rescue'] = rescue
            if server_type is None:
                raise TypeError("Missing required property 'server_type'")
            __props__['server_type'] = server_type
            __props__['ssh_keys'] = ssh_keys
            __props__['user_data'] = user_data
            __props__['backup_window'] = None
            __props__['ipv4_address'] = None
            __props__['ipv6_address'] = None
            __props__['ipv6_network'] = None
            __props__['status'] = None
        super(Server, __self__).__init__(
            'hcloud:index/server:Server',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            backup_window: Optional[pulumi.Input[str]] = None,
            backups: Optional[pulumi.Input[bool]] = None,
            datacenter: Optional[pulumi.Input[str]] = None,
            image: Optional[pulumi.Input[str]] = None,
            ipv4_address: Optional[pulumi.Input[str]] = None,
            ipv6_address: Optional[pulumi.Input[str]] = None,
            ipv6_network: Optional[pulumi.Input[str]] = None,
            iso: Optional[pulumi.Input[str]] = None,
            keep_disk: Optional[pulumi.Input[bool]] = None,
            labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerNetworkArgs']]]]] = None,
            rescue: Optional[pulumi.Input[str]] = None,
            server_type: Optional[pulumi.Input[str]] = None,
            ssh_keys: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            status: Optional[pulumi.Input[str]] = None,
            user_data: Optional[pulumi.Input[str]] = None) -> 'Server':
        """
        Get an existing Server resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backup_window: (string) The backup window of the server, if enabled.
        :param pulumi.Input[bool] backups: Enable or disable backups.
        :param pulumi.Input[str] datacenter: The datacenter name to create the server in.
        :param pulumi.Input[str] image: Name or ID of the image the server is created from.
        :param pulumi.Input[str] ipv4_address: (string) The IPv4 address.
        :param pulumi.Input[str] ipv6_address: (string) The first IPv6 address of the assigned network.
        :param pulumi.Input[str] ipv6_network: (string) The IPv6 network.
        :param pulumi.Input[str] iso: ID or Name of an ISO image to mount.
        :param pulumi.Input[bool] keep_disk: If true, do not upgrade the disk. This allows downgrading the server type later.
        :param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs) should be created with.
        :param pulumi.Input[str] location: The location name to create the server in. `nbg1`, `fsn1` or `hel1`
        :param pulumi.Input[str] name: Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).
        :param pulumi.Input[str] rescue: Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
        :param pulumi.Input[str] server_type: Name of the server type this server should be created with.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ssh_keys: SSH key IDs or names which should be injected into the server at creation time
        :param pulumi.Input[str] status: (string) The status of the server.
        :param pulumi.Input[str] user_data: Cloud-Init user data to use during server creation
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["backup_window"] = backup_window
        __props__["backups"] = backups
        __props__["datacenter"] = datacenter
        __props__["image"] = image
        __props__["ipv4_address"] = ipv4_address
        __props__["ipv6_address"] = ipv6_address
        __props__["ipv6_network"] = ipv6_network
        __props__["iso"] = iso
        __props__["keep_disk"] = keep_disk
        __props__["labels"] = labels
        __props__["location"] = location
        __props__["name"] = name
        __props__["networks"] = networks
        __props__["rescue"] = rescue
        __props__["server_type"] = server_type
        __props__["ssh_keys"] = ssh_keys
        __props__["status"] = status
        __props__["user_data"] = user_data
        return Server(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backupWindow")
    def backup_window(self) -> pulumi.Output[str]:
        """
        (string) The backup window of the server, if enabled.
        """
        return pulumi.get(self, "backup_window")

    @property
    @pulumi.getter
    def backups(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable or disable backups.
        """
        return pulumi.get(self, "backups")

    @property
    @pulumi.getter
    def datacenter(self) -> pulumi.Output[str]:
        """
        The datacenter name to create the server in.
        """
        return pulumi.get(self, "datacenter")

    @property
    @pulumi.getter
    def image(self) -> pulumi.Output[str]:
        """
        Name or ID of the image the server is created from.
        """
        return pulumi.get(self, "image")

    @property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> pulumi.Output[str]:
        """
        (string) The IPv4 address.
        """
        return pulumi.get(self, "ipv4_address")

    @property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> pulumi.Output[str]:
        """
        (string) The first IPv6 address of the assigned network.
        """
        return pulumi.get(self, "ipv6_address")

    @property
    @pulumi.getter(name="ipv6Network")
    def ipv6_network(self) -> pulumi.Output[str]:
        """
        (string) The IPv6 network.
        """
        return pulumi.get(self, "ipv6_network")

    @property
    @pulumi.getter
    def iso(self) -> pulumi.Output[Optional[str]]:
        """
        ID or Name of an ISO image to mount.
        """
        return pulumi.get(self, "iso")

    @property
    @pulumi.getter(name="keepDisk")
    def keep_disk(self) -> pulumi.Output[Optional[bool]]:
        """
        If true, do not upgrade the disk. This allows downgrading the server type later.
        """
        return pulumi.get(self, "keep_disk")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        User-defined labels (key-value pairs) should be created with.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location name to create the server in. `nbg1`, `fsn1` or `hel1`
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def networks(self) -> pulumi.Output[Optional[Sequence['outputs.ServerNetwork']]]:
        return pulumi.get(self, "networks")

    @property
    @pulumi.getter
    def rescue(self) -> pulumi.Output[Optional[str]]:
        """
        Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
        """
        return pulumi.get(self, "rescue")

    @property
    @pulumi.getter(name="serverType")
    def server_type(self) -> pulumi.Output[str]:
        """
        Name of the server type this server should be created with.
        """
        return pulumi.get(self, "server_type")

    @property
    @pulumi.getter(name="sshKeys")
    def ssh_keys(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        SSH key IDs or names which should be injected into the server at creation time
        """
        return pulumi.get(self, "ssh_keys")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        (string) The status of the server.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="userData")
    def user_data(self) -> pulumi.Output[Optional[str]]:
        """
        Cloud-Init user data to use during server creation
        """
        return pulumi.get(self, "user_data")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

