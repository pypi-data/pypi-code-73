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

__all__ = ['LaunchTemplate']


class LaunchTemplate(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_release_time: Optional[pulumi.Input[str]] = None,
                 data_disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LaunchTemplateDataDiskArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 image_id: Optional[pulumi.Input[str]] = None,
                 image_owner_alias: Optional[pulumi.Input[str]] = None,
                 instance_charge_type: Optional[pulumi.Input[str]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 internet_charge_type: Optional[pulumi.Input[str]] = None,
                 internet_max_bandwidth_in: Optional[pulumi.Input[int]] = None,
                 internet_max_bandwidth_out: Optional[pulumi.Input[int]] = None,
                 io_optimized: Optional[pulumi.Input[str]] = None,
                 key_pair_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_interfaces: Optional[pulumi.Input[pulumi.InputType['LaunchTemplateNetworkInterfacesArgs']]] = None,
                 network_type: Optional[pulumi.Input[str]] = None,
                 ram_role_name: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 security_enhancement_strategy: Optional[pulumi.Input[str]] = None,
                 security_group_id: Optional[pulumi.Input[str]] = None,
                 spot_price_limit: Optional[pulumi.Input[float]] = None,
                 spot_strategy: Optional[pulumi.Input[str]] = None,
                 system_disk_category: Optional[pulumi.Input[str]] = None,
                 system_disk_description: Optional[pulumi.Input[str]] = None,
                 system_disk_name: Optional[pulumi.Input[str]] = None,
                 system_disk_size: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 userdata: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 vswitch_id: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an ECS Launch Template resource.

        For information about Launch Template and how to use it, see [Launch Template](https://www.alibabacloud.com/help/doc-detail/73916.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        images = alicloud.ecs.get_images(owners="system")
        instances = alicloud.ecs.get_instances()
        template = alicloud.ecs.LaunchTemplate("template",
            description="test1",
            image_id=images.images[0].id,
            host_name="tf-test-host",
            instance_charge_type="PrePaid",
            instance_name="tf-instance-name",
            instance_type=instances.instances[0].instance_type,
            internet_charge_type="PayByBandwidth",
            internet_max_bandwidth_in=5,
            internet_max_bandwidth_out=0,
            io_optimized="none",
            key_pair_name="test-key-pair",
            ram_role_name="xxxxx",
            network_type="vpc",
            security_enhancement_strategy="Active",
            spot_price_limit=5,
            spot_strategy="SpotWithPriceLimit",
            security_group_id="sg-zxcvj0lasdf102350asdf9a",
            system_disk_category="cloud_ssd",
            system_disk_description="test disk",
            system_disk_name="hello",
            system_disk_size=40,
            resource_group_id="rg-zkdfjahg9zxncv0",
            userdata="xxxxxxxxxxxxxx",
            vswitch_id="sw-ljkngaksdjfj0nnasdf",
            vpc_id="vpc-asdfnbg0as8dfk1nb2",
            zone_id="beijing-a",
            tags={
                "tag1": "hello",
                "tag2": "world",
            },
            network_interfaces=alicloud.ecs.LaunchTemplateNetworkInterfacesArgs(
                name="eth0",
                description="hello1",
                primary_ip="10.0.0.2",
                security_group_id="xxxx",
                vswitch_id="xxxxxxx",
            ),
            data_disks=[
                alicloud.ecs.LaunchTemplateDataDiskArgs(
                    name="disk1",
                    description="test1",
                ),
                alicloud.ecs.LaunchTemplateDataDiskArgs(
                    name="disk2",
                    description="test2",
                ),
            ])
        ```

        ## Import

        Launch Template can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ecs/launchTemplate:LaunchTemplate lt lt-abc1234567890000
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auto_release_time: Instance auto release time. The time is presented using the ISO8601 standard and in UTC time. The format is  YYYY-MM-DDTHH:MM:SSZ.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LaunchTemplateDataDiskArgs']]]] data_disks: The list of data disks created with instance.
        :param pulumi.Input[str] description: The description of the data disk.
        :param pulumi.Input[str] host_name: Instance host name.It cannot start or end with a period (.) or a hyphen (-) and it cannot have two or more consecutive periods (.) or hyphens (-).For Windows: The host name can be [2, 15] characters in length. It can contain A-Z, a-z, numbers, periods (.), and hyphens (-). It cannot only contain numbers. For other operating systems: The host name can be [2, 64] characters in length. It can be segments separated by periods (.). It can contain A-Z, a-z, numbers, and hyphens (-).
        :param pulumi.Input[str] image_id: Image ID.
        :param pulumi.Input[str] instance_charge_type: Billing methods. Optional values:
               - PrePaid: Monthly, or annual subscription. Make sure that your registered credit card is invalid or you have insufficient balance in your PayPal account. Otherwise, InvalidPayMethod error may occur.
               - PostPaid: Pay-As-You-Go.
        :param pulumi.Input[str] instance_name: The name of the instance. The name is a string of 2 to 128 characters. It must begin with an English or a Chinese character. It can contain A-Z, a-z, Chinese characters, numbers, periods (.), colons (:), underscores (_), and hyphens (-).
        :param pulumi.Input[str] instance_type: Instance type. For more information, call resource_alicloud_instances to obtain the latest instance type list.
        :param pulumi.Input[str] internet_charge_type: Internet bandwidth billing method. Optional values: `PayByTraffic` | `PayByBandwidth`.
        :param pulumi.Input[int] internet_max_bandwidth_in: The maximum inbound bandwidth from the Internet network, measured in Mbit/s. Value range: [1, 200].
        :param pulumi.Input[int] internet_max_bandwidth_out: Maximum outbound bandwidth from the Internet, its unit of measurement is Mbit/s. Value range: [0, 100].
        :param pulumi.Input[str] io_optimized: Whether it is an I/O-optimized instance or not. Optional values:
               - none
               - optimized
        :param pulumi.Input[str] key_pair_name: The name of the key pair.
               - Ignore this parameter for Windows instances. It is null by default. Even if you enter this parameter, only the  Password content is used.
               - The password logon method for Linux instances is set to forbidden upon initialization.
        :param pulumi.Input[str] name: The name of the data disk.
        :param pulumi.Input[pulumi.InputType['LaunchTemplateNetworkInterfacesArgs']] network_interfaces: The list of network interfaces created with instance.
        :param pulumi.Input[str] network_type: Network type of the instance. Value options: `classic` | `vpc`.
        :param pulumi.Input[str] ram_role_name: The RAM role name of the instance. You can use the RAM API ListRoles to query instance RAM role names.
        :param pulumi.Input[str] security_enhancement_strategy: Whether or not to activate the security enhancement feature and install network security software free of charge. Optional values: Active | Deactive.
        :param pulumi.Input[str] security_group_id: The security group ID must be one in the same VPC.
        :param pulumi.Input[float] spot_price_limit: -(Optional) 	Sets the maximum hourly instance price. Supports up to three decimal places.
        :param pulumi.Input[str] spot_strategy: The spot strategy for a Pay-As-You-Go instance. This parameter is valid and required only when InstanceChargeType is set to PostPaid. Value range:
               - NoSpot: Normal Pay-As-You-Go instance.
               - SpotWithPriceLimit: Sets the maximum price for a spot instance.
               - SpotAsPriceGo: The system automatically calculates the price. The maximum value is the Pay-As-You-Go price.
        :param pulumi.Input[str] system_disk_category: The category of the system disk. System disk type. Optional values:
               - cloud: Basic cloud disk.
               - cloud_efficiency: Ultra cloud disk.
               - cloud_ssd: SSD cloud Disks.
               - ephemeral_ssd: local SSD Disks
               - cloud_essd: ESSD cloud Disks.
        :param pulumi.Input[str] system_disk_description: System disk description. It cannot begin with http:// or https://.
        :param pulumi.Input[str] system_disk_name: System disk name. The name is a string of 2 to 128 characters. It must begin with an English or a Chinese character. It can contain A-Z, a-z, Chinese characters, numbers, periods (.), colons (:), underscores (_), and hyphens (-).
        :param pulumi.Input[int] system_disk_size: Size of the system disk, measured in GB. Value range: [20, 500].
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
               - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
               - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
        :param pulumi.Input[str] userdata: User data of the instance, which is Base64-encoded. Size of the raw data cannot exceed 16 KB.
        :param pulumi.Input[str] vswitch_id: The VSwitch ID for ENI. The instance must be in the same zone of the same VPC network as the ENI, but they may belong to different VSwitches.
        :param pulumi.Input[str] zone_id: The zone ID of the instance.
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

            __props__['auto_release_time'] = auto_release_time
            __props__['data_disks'] = data_disks
            __props__['description'] = description
            __props__['host_name'] = host_name
            __props__['image_id'] = image_id
            __props__['image_owner_alias'] = image_owner_alias
            __props__['instance_charge_type'] = instance_charge_type
            __props__['instance_name'] = instance_name
            __props__['instance_type'] = instance_type
            __props__['internet_charge_type'] = internet_charge_type
            __props__['internet_max_bandwidth_in'] = internet_max_bandwidth_in
            __props__['internet_max_bandwidth_out'] = internet_max_bandwidth_out
            __props__['io_optimized'] = io_optimized
            __props__['key_pair_name'] = key_pair_name
            __props__['name'] = name
            __props__['network_interfaces'] = network_interfaces
            __props__['network_type'] = network_type
            __props__['ram_role_name'] = ram_role_name
            __props__['resource_group_id'] = resource_group_id
            __props__['security_enhancement_strategy'] = security_enhancement_strategy
            __props__['security_group_id'] = security_group_id
            __props__['spot_price_limit'] = spot_price_limit
            __props__['spot_strategy'] = spot_strategy
            __props__['system_disk_category'] = system_disk_category
            __props__['system_disk_description'] = system_disk_description
            __props__['system_disk_name'] = system_disk_name
            __props__['system_disk_size'] = system_disk_size
            __props__['tags'] = tags
            __props__['userdata'] = userdata
            __props__['vpc_id'] = vpc_id
            __props__['vswitch_id'] = vswitch_id
            __props__['zone_id'] = zone_id
        super(LaunchTemplate, __self__).__init__(
            'alicloud:ecs/launchTemplate:LaunchTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auto_release_time: Optional[pulumi.Input[str]] = None,
            data_disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LaunchTemplateDataDiskArgs']]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            host_name: Optional[pulumi.Input[str]] = None,
            image_id: Optional[pulumi.Input[str]] = None,
            image_owner_alias: Optional[pulumi.Input[str]] = None,
            instance_charge_type: Optional[pulumi.Input[str]] = None,
            instance_name: Optional[pulumi.Input[str]] = None,
            instance_type: Optional[pulumi.Input[str]] = None,
            internet_charge_type: Optional[pulumi.Input[str]] = None,
            internet_max_bandwidth_in: Optional[pulumi.Input[int]] = None,
            internet_max_bandwidth_out: Optional[pulumi.Input[int]] = None,
            io_optimized: Optional[pulumi.Input[str]] = None,
            key_pair_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_interfaces: Optional[pulumi.Input[pulumi.InputType['LaunchTemplateNetworkInterfacesArgs']]] = None,
            network_type: Optional[pulumi.Input[str]] = None,
            ram_role_name: Optional[pulumi.Input[str]] = None,
            resource_group_id: Optional[pulumi.Input[str]] = None,
            security_enhancement_strategy: Optional[pulumi.Input[str]] = None,
            security_group_id: Optional[pulumi.Input[str]] = None,
            spot_price_limit: Optional[pulumi.Input[float]] = None,
            spot_strategy: Optional[pulumi.Input[str]] = None,
            system_disk_category: Optional[pulumi.Input[str]] = None,
            system_disk_description: Optional[pulumi.Input[str]] = None,
            system_disk_name: Optional[pulumi.Input[str]] = None,
            system_disk_size: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            userdata: Optional[pulumi.Input[str]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None,
            vswitch_id: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'LaunchTemplate':
        """
        Get an existing LaunchTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auto_release_time: Instance auto release time. The time is presented using the ISO8601 standard and in UTC time. The format is  YYYY-MM-DDTHH:MM:SSZ.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LaunchTemplateDataDiskArgs']]]] data_disks: The list of data disks created with instance.
        :param pulumi.Input[str] description: The description of the data disk.
        :param pulumi.Input[str] host_name: Instance host name.It cannot start or end with a period (.) or a hyphen (-) and it cannot have two or more consecutive periods (.) or hyphens (-).For Windows: The host name can be [2, 15] characters in length. It can contain A-Z, a-z, numbers, periods (.), and hyphens (-). It cannot only contain numbers. For other operating systems: The host name can be [2, 64] characters in length. It can be segments separated by periods (.). It can contain A-Z, a-z, numbers, and hyphens (-).
        :param pulumi.Input[str] image_id: Image ID.
        :param pulumi.Input[str] instance_charge_type: Billing methods. Optional values:
               - PrePaid: Monthly, or annual subscription. Make sure that your registered credit card is invalid or you have insufficient balance in your PayPal account. Otherwise, InvalidPayMethod error may occur.
               - PostPaid: Pay-As-You-Go.
        :param pulumi.Input[str] instance_name: The name of the instance. The name is a string of 2 to 128 characters. It must begin with an English or a Chinese character. It can contain A-Z, a-z, Chinese characters, numbers, periods (.), colons (:), underscores (_), and hyphens (-).
        :param pulumi.Input[str] instance_type: Instance type. For more information, call resource_alicloud_instances to obtain the latest instance type list.
        :param pulumi.Input[str] internet_charge_type: Internet bandwidth billing method. Optional values: `PayByTraffic` | `PayByBandwidth`.
        :param pulumi.Input[int] internet_max_bandwidth_in: The maximum inbound bandwidth from the Internet network, measured in Mbit/s. Value range: [1, 200].
        :param pulumi.Input[int] internet_max_bandwidth_out: Maximum outbound bandwidth from the Internet, its unit of measurement is Mbit/s. Value range: [0, 100].
        :param pulumi.Input[str] io_optimized: Whether it is an I/O-optimized instance or not. Optional values:
               - none
               - optimized
        :param pulumi.Input[str] key_pair_name: The name of the key pair.
               - Ignore this parameter for Windows instances. It is null by default. Even if you enter this parameter, only the  Password content is used.
               - The password logon method for Linux instances is set to forbidden upon initialization.
        :param pulumi.Input[str] name: The name of the data disk.
        :param pulumi.Input[pulumi.InputType['LaunchTemplateNetworkInterfacesArgs']] network_interfaces: The list of network interfaces created with instance.
        :param pulumi.Input[str] network_type: Network type of the instance. Value options: `classic` | `vpc`.
        :param pulumi.Input[str] ram_role_name: The RAM role name of the instance. You can use the RAM API ListRoles to query instance RAM role names.
        :param pulumi.Input[str] security_enhancement_strategy: Whether or not to activate the security enhancement feature and install network security software free of charge. Optional values: Active | Deactive.
        :param pulumi.Input[str] security_group_id: The security group ID must be one in the same VPC.
        :param pulumi.Input[float] spot_price_limit: -(Optional) 	Sets the maximum hourly instance price. Supports up to three decimal places.
        :param pulumi.Input[str] spot_strategy: The spot strategy for a Pay-As-You-Go instance. This parameter is valid and required only when InstanceChargeType is set to PostPaid. Value range:
               - NoSpot: Normal Pay-As-You-Go instance.
               - SpotWithPriceLimit: Sets the maximum price for a spot instance.
               - SpotAsPriceGo: The system automatically calculates the price. The maximum value is the Pay-As-You-Go price.
        :param pulumi.Input[str] system_disk_category: The category of the system disk. System disk type. Optional values:
               - cloud: Basic cloud disk.
               - cloud_efficiency: Ultra cloud disk.
               - cloud_ssd: SSD cloud Disks.
               - ephemeral_ssd: local SSD Disks
               - cloud_essd: ESSD cloud Disks.
        :param pulumi.Input[str] system_disk_description: System disk description. It cannot begin with http:// or https://.
        :param pulumi.Input[str] system_disk_name: System disk name. The name is a string of 2 to 128 characters. It must begin with an English or a Chinese character. It can contain A-Z, a-z, Chinese characters, numbers, periods (.), colons (:), underscores (_), and hyphens (-).
        :param pulumi.Input[int] system_disk_size: Size of the system disk, measured in GB. Value range: [20, 500].
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
               - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
               - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
        :param pulumi.Input[str] userdata: User data of the instance, which is Base64-encoded. Size of the raw data cannot exceed 16 KB.
        :param pulumi.Input[str] vswitch_id: The VSwitch ID for ENI. The instance must be in the same zone of the same VPC network as the ENI, but they may belong to different VSwitches.
        :param pulumi.Input[str] zone_id: The zone ID of the instance.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["auto_release_time"] = auto_release_time
        __props__["data_disks"] = data_disks
        __props__["description"] = description
        __props__["host_name"] = host_name
        __props__["image_id"] = image_id
        __props__["image_owner_alias"] = image_owner_alias
        __props__["instance_charge_type"] = instance_charge_type
        __props__["instance_name"] = instance_name
        __props__["instance_type"] = instance_type
        __props__["internet_charge_type"] = internet_charge_type
        __props__["internet_max_bandwidth_in"] = internet_max_bandwidth_in
        __props__["internet_max_bandwidth_out"] = internet_max_bandwidth_out
        __props__["io_optimized"] = io_optimized
        __props__["key_pair_name"] = key_pair_name
        __props__["name"] = name
        __props__["network_interfaces"] = network_interfaces
        __props__["network_type"] = network_type
        __props__["ram_role_name"] = ram_role_name
        __props__["resource_group_id"] = resource_group_id
        __props__["security_enhancement_strategy"] = security_enhancement_strategy
        __props__["security_group_id"] = security_group_id
        __props__["spot_price_limit"] = spot_price_limit
        __props__["spot_strategy"] = spot_strategy
        __props__["system_disk_category"] = system_disk_category
        __props__["system_disk_description"] = system_disk_description
        __props__["system_disk_name"] = system_disk_name
        __props__["system_disk_size"] = system_disk_size
        __props__["tags"] = tags
        __props__["userdata"] = userdata
        __props__["vpc_id"] = vpc_id
        __props__["vswitch_id"] = vswitch_id
        __props__["zone_id"] = zone_id
        return LaunchTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoReleaseTime")
    def auto_release_time(self) -> pulumi.Output[Optional[str]]:
        """
        Instance auto release time. The time is presented using the ISO8601 standard and in UTC time. The format is  YYYY-MM-DDTHH:MM:SSZ.
        """
        return pulumi.get(self, "auto_release_time")

    @property
    @pulumi.getter(name="dataDisks")
    def data_disks(self) -> pulumi.Output[Optional[Sequence['outputs.LaunchTemplateDataDisk']]]:
        """
        The list of data disks created with instance.
        """
        return pulumi.get(self, "data_disks")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the data disk.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[Optional[str]]:
        """
        Instance host name.It cannot start or end with a period (.) or a hyphen (-) and it cannot have two or more consecutive periods (.) or hyphens (-).For Windows: The host name can be [2, 15] characters in length. It can contain A-Z, a-z, numbers, periods (.), and hyphens (-). It cannot only contain numbers. For other operating systems: The host name can be [2, 64] characters in length. It can be segments separated by periods (.). It can contain A-Z, a-z, numbers, and hyphens (-).
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> pulumi.Output[Optional[str]]:
        """
        Image ID.
        """
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter(name="imageOwnerAlias")
    def image_owner_alias(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "image_owner_alias")

    @property
    @pulumi.getter(name="instanceChargeType")
    def instance_charge_type(self) -> pulumi.Output[Optional[str]]:
        """
        Billing methods. Optional values:
        - PrePaid: Monthly, or annual subscription. Make sure that your registered credit card is invalid or you have insufficient balance in your PayPal account. Otherwise, InvalidPayMethod error may occur.
        - PostPaid: Pay-As-You-Go.
        """
        return pulumi.get(self, "instance_charge_type")

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the instance. The name is a string of 2 to 128 characters. It must begin with an English or a Chinese character. It can contain A-Z, a-z, Chinese characters, numbers, periods (.), colons (:), underscores (_), and hyphens (-).
        """
        return pulumi.get(self, "instance_name")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[Optional[str]]:
        """
        Instance type. For more information, call resource_alicloud_instances to obtain the latest instance type list.
        """
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="internetChargeType")
    def internet_charge_type(self) -> pulumi.Output[Optional[str]]:
        """
        Internet bandwidth billing method. Optional values: `PayByTraffic` | `PayByBandwidth`.
        """
        return pulumi.get(self, "internet_charge_type")

    @property
    @pulumi.getter(name="internetMaxBandwidthIn")
    def internet_max_bandwidth_in(self) -> pulumi.Output[int]:
        """
        The maximum inbound bandwidth from the Internet network, measured in Mbit/s. Value range: [1, 200].
        """
        return pulumi.get(self, "internet_max_bandwidth_in")

    @property
    @pulumi.getter(name="internetMaxBandwidthOut")
    def internet_max_bandwidth_out(self) -> pulumi.Output[Optional[int]]:
        """
        Maximum outbound bandwidth from the Internet, its unit of measurement is Mbit/s. Value range: [0, 100].
        """
        return pulumi.get(self, "internet_max_bandwidth_out")

    @property
    @pulumi.getter(name="ioOptimized")
    def io_optimized(self) -> pulumi.Output[Optional[str]]:
        """
        Whether it is an I/O-optimized instance or not. Optional values:
        - none
        - optimized
        """
        return pulumi.get(self, "io_optimized")

    @property
    @pulumi.getter(name="keyPairName")
    def key_pair_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the key pair.
        - Ignore this parameter for Windows instances. It is null by default. Even if you enter this parameter, only the  Password content is used.
        - The password logon method for Linux instances is set to forbidden upon initialization.
        """
        return pulumi.get(self, "key_pair_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the data disk.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> pulumi.Output[Optional['outputs.LaunchTemplateNetworkInterfaces']]:
        """
        The list of network interfaces created with instance.
        """
        return pulumi.get(self, "network_interfaces")

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> pulumi.Output[Optional[str]]:
        """
        Network type of the instance. Value options: `classic` | `vpc`.
        """
        return pulumi.get(self, "network_type")

    @property
    @pulumi.getter(name="ramRoleName")
    def ram_role_name(self) -> pulumi.Output[Optional[str]]:
        """
        The RAM role name of the instance. You can use the RAM API ListRoles to query instance RAM role names.
        """
        return pulumi.get(self, "ram_role_name")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter(name="securityEnhancementStrategy")
    def security_enhancement_strategy(self) -> pulumi.Output[Optional[str]]:
        """
        Whether or not to activate the security enhancement feature and install network security software free of charge. Optional values: Active | Deactive.
        """
        return pulumi.get(self, "security_enhancement_strategy")

    @property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> pulumi.Output[Optional[str]]:
        """
        The security group ID must be one in the same VPC.
        """
        return pulumi.get(self, "security_group_id")

    @property
    @pulumi.getter(name="spotPriceLimit")
    def spot_price_limit(self) -> pulumi.Output[Optional[float]]:
        """
        -(Optional) 	Sets the maximum hourly instance price. Supports up to three decimal places.
        """
        return pulumi.get(self, "spot_price_limit")

    @property
    @pulumi.getter(name="spotStrategy")
    def spot_strategy(self) -> pulumi.Output[Optional[str]]:
        """
        The spot strategy for a Pay-As-You-Go instance. This parameter is valid and required only when InstanceChargeType is set to PostPaid. Value range:
        - NoSpot: Normal Pay-As-You-Go instance.
        - SpotWithPriceLimit: Sets the maximum price for a spot instance.
        - SpotAsPriceGo: The system automatically calculates the price. The maximum value is the Pay-As-You-Go price.
        """
        return pulumi.get(self, "spot_strategy")

    @property
    @pulumi.getter(name="systemDiskCategory")
    def system_disk_category(self) -> pulumi.Output[Optional[str]]:
        """
        The category of the system disk. System disk type. Optional values:
        - cloud: Basic cloud disk.
        - cloud_efficiency: Ultra cloud disk.
        - cloud_ssd: SSD cloud Disks.
        - ephemeral_ssd: local SSD Disks
        - cloud_essd: ESSD cloud Disks.
        """
        return pulumi.get(self, "system_disk_category")

    @property
    @pulumi.getter(name="systemDiskDescription")
    def system_disk_description(self) -> pulumi.Output[Optional[str]]:
        """
        System disk description. It cannot begin with http:// or https://.
        """
        return pulumi.get(self, "system_disk_description")

    @property
    @pulumi.getter(name="systemDiskName")
    def system_disk_name(self) -> pulumi.Output[Optional[str]]:
        """
        System disk name. The name is a string of 2 to 128 characters. It must begin with an English or a Chinese character. It can contain A-Z, a-z, Chinese characters, numbers, periods (.), colons (:), underscores (_), and hyphens (-).
        """
        return pulumi.get(self, "system_disk_name")

    @property
    @pulumi.getter(name="systemDiskSize")
    def system_disk_size(self) -> pulumi.Output[Optional[int]]:
        """
        Size of the system disk, measured in GB. Value range: [20, 500].
        """
        return pulumi.get(self, "system_disk_size")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
        - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def userdata(self) -> pulumi.Output[Optional[str]]:
        """
        User data of the instance, which is Base64-encoded. Size of the raw data cannot exceed 16 KB.
        """
        return pulumi.get(self, "userdata")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="vswitchId")
    def vswitch_id(self) -> pulumi.Output[Optional[str]]:
        """
        The VSwitch ID for ENI. The instance must be in the same zone of the same VPC network as the ENI, but they may belong to different VSwitches.
        """
        return pulumi.get(self, "vswitch_id")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[Optional[str]]:
        """
        The zone ID of the instance.
        """
        return pulumi.get(self, "zone_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

