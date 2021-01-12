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

__all__ = ['InstanceGroup']


class InstanceGroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instances: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 named_ports: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceGroupNamedPortArgs']]]]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a group of dissimilar Compute Engine virtual machine instances.
        For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/#unmanaged_instance_groups)
        and [API](https://cloud.google.com/compute/docs/reference/latest/instanceGroups)

        ## Example Usage
        ### Empty Instance Group

        ```python
        import pulumi
        import pulumi_gcp as gcp

        test = gcp.compute.InstanceGroup("test",
            description="Test instance group",
            zone="us-central1-a",
            network=google_compute_network["default"]["id"])
        ```
        ### Example Usage - With instances and named ports

        ```python
        import pulumi
        import pulumi_gcp as gcp

        webservers = gcp.compute.InstanceGroup("webservers",
            description="Test instance group",
            instances=[
                google_compute_instance["test"]["id"],
                google_compute_instance["test2"]["id"],
            ],
            named_ports=[
                gcp.compute.InstanceGroupNamedPortArgs(
                    name="http",
                    port=8080,
                ),
                gcp.compute.InstanceGroupNamedPortArgs(
                    name="https",
                    port=8443,
                ),
            ],
            zone="us-central1-a")
        ```
        ### Example Usage - Recreating an instance group in use
        Recreating an instance group that's in use by another resource will give a
        `resourceInUseByAnotherResource` error. Use `lifecycle.create_before_destroy`
        as shown in this example to avoid this type of error.

        ```python
        import pulumi
        import pulumi_gcp as gcp

        debian_image = gcp.compute.get_image(family="debian-9",
            project="debian-cloud")
        staging_vm = gcp.compute.Instance("stagingVm",
            machine_type="e2-medium",
            zone="us-central1-c",
            boot_disk=gcp.compute.InstanceBootDiskArgs(
                initialize_params=gcp.compute.InstanceBootDiskInitializeParamsArgs(
                    image=debian_image.self_link,
                ),
            ),
            network_interfaces=[gcp.compute.InstanceNetworkInterfaceArgs(
                network="default",
            )])
        staging_group = gcp.compute.InstanceGroup("stagingGroup",
            zone="us-central1-c",
            instances=[staging_vm.id],
            named_ports=[
                gcp.compute.InstanceGroupNamedPortArgs(
                    name="http",
                    port=8080,
                ),
                gcp.compute.InstanceGroupNamedPortArgs(
                    name="https",
                    port=8443,
                ),
            ])
        staging_health = gcp.compute.HttpsHealthCheck("stagingHealth", request_path="/health_check")
        staging_service = gcp.compute.BackendService("stagingService",
            port_name="https",
            protocol="HTTPS",
            backends=[gcp.compute.BackendServiceBackendArgs(
                group=staging_group.id,
            )],
            health_checks=[staging_health.id])
        ```

        ## Import

        Instance group can be imported using the `zone` and `name` with an optional `project`, e.g.

        ```sh
         $ pulumi import gcp:compute/instanceGroup:InstanceGroup webservers us-central1-a/terraform-webservers
        ```

        ```sh
         $ pulumi import gcp:compute/instanceGroup:InstanceGroup webservers big-project/us-central1-a/terraform-webservers
        ```

        ```sh
         $ pulumi import gcp:compute/instanceGroup:InstanceGroup webservers projects/big-project/zones/us-central1-a/instanceGroups/terraform-webservers
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: An optional textual description of the instance
               group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] instances: List of instances in the group. They should be given
               as either self_link or id. When adding instances they must all be in the same
               network and zone as the instance group.
        :param pulumi.Input[str] name: The name which the port will be mapped to.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceGroupNamedPortArgs']]]] named_ports: The named port configuration. See the section below
               for details on configuration.
        :param pulumi.Input[str] network: The URL of the network the instance group is in. If
               this is different from the network where the instances are in, the creation
               fails. Defaults to the network where the instances are in (if neither
               `network` nor `instances` is specified, this field will be blank).
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[str] zone: The zone that this instance group should be created in.
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
            __props__['instances'] = instances
            __props__['name'] = name
            __props__['named_ports'] = named_ports
            __props__['network'] = network
            __props__['project'] = project
            __props__['zone'] = zone
            __props__['self_link'] = None
            __props__['size'] = None
        super(InstanceGroup, __self__).__init__(
            'gcp:compute/instanceGroup:InstanceGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            instances: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            named_ports: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceGroupNamedPortArgs']]]]] = None,
            network: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[int]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'InstanceGroup':
        """
        Get an existing InstanceGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: An optional textual description of the instance
               group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] instances: List of instances in the group. They should be given
               as either self_link or id. When adding instances they must all be in the same
               network and zone as the instance group.
        :param pulumi.Input[str] name: The name which the port will be mapped to.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceGroupNamedPortArgs']]]] named_ports: The named port configuration. See the section below
               for details on configuration.
        :param pulumi.Input[str] network: The URL of the network the instance group is in. If
               this is different from the network where the instances are in, the creation
               fails. Defaults to the network where the instances are in (if neither
               `network` nor `instances` is specified, this field will be blank).
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        :param pulumi.Input[int] size: The number of instances in the group.
        :param pulumi.Input[str] zone: The zone that this instance group should be created in.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["instances"] = instances
        __props__["name"] = name
        __props__["named_ports"] = named_ports
        __props__["network"] = network
        __props__["project"] = project
        __props__["self_link"] = self_link
        __props__["size"] = size
        __props__["zone"] = zone
        return InstanceGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional textual description of the instance
        group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def instances(self) -> pulumi.Output[Sequence[str]]:
        """
        List of instances in the group. They should be given
        as either self_link or id. When adding instances they must all be in the same
        network and zone as the instance group.
        """
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which the port will be mapped to.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namedPorts")
    def named_ports(self) -> pulumi.Output[Optional[Sequence['outputs.InstanceGroupNamedPort']]]:
        """
        The named port configuration. See the section below
        for details on configuration.
        """
        return pulumi.get(self, "named_ports")

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output[str]:
        """
        The URL of the network the instance group is in. If
        this is different from the network where the instances are in, the creation
        fails. Defaults to the network where the instances are in (if neither
        `network` nor `instances` is specified, this field will be blank).
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs. If it
        is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[int]:
        """
        The number of instances in the group.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        The zone that this instance group should be created in.
        """
        return pulumi.get(self, "zone")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

