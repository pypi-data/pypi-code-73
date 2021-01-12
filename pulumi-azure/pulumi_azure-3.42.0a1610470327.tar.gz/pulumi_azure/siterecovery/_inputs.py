# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'ReplicatedVMManagedDiskArgs',
    'ReplicatedVMNetworkInterfaceArgs',
]

@pulumi.input_type
class ReplicatedVMManagedDiskArgs:
    def __init__(__self__, *,
                 disk_id: pulumi.Input[str],
                 staging_storage_account_id: pulumi.Input[str],
                 target_disk_type: pulumi.Input[str],
                 target_replica_disk_type: pulumi.Input[str],
                 target_resource_group_id: pulumi.Input[str]):
        """
        :param pulumi.Input[str] disk_id: Id of disk that should be replicated.
        :param pulumi.Input[str] staging_storage_account_id: Storage account that should be used for caching.
        :param pulumi.Input[str] target_disk_type: What type should the disk be when a failover is done.
        :param pulumi.Input[str] target_replica_disk_type: What type should the disk be that holds the replication data.
        :param pulumi.Input[str] target_resource_group_id: Resource group disk should belong to when a failover is done.
        """
        pulumi.set(__self__, "disk_id", disk_id)
        pulumi.set(__self__, "staging_storage_account_id", staging_storage_account_id)
        pulumi.set(__self__, "target_disk_type", target_disk_type)
        pulumi.set(__self__, "target_replica_disk_type", target_replica_disk_type)
        pulumi.set(__self__, "target_resource_group_id", target_resource_group_id)

    @property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> pulumi.Input[str]:
        """
        Id of disk that should be replicated.
        """
        return pulumi.get(self, "disk_id")

    @disk_id.setter
    def disk_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "disk_id", value)

    @property
    @pulumi.getter(name="stagingStorageAccountId")
    def staging_storage_account_id(self) -> pulumi.Input[str]:
        """
        Storage account that should be used for caching.
        """
        return pulumi.get(self, "staging_storage_account_id")

    @staging_storage_account_id.setter
    def staging_storage_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "staging_storage_account_id", value)

    @property
    @pulumi.getter(name="targetDiskType")
    def target_disk_type(self) -> pulumi.Input[str]:
        """
        What type should the disk be when a failover is done.
        """
        return pulumi.get(self, "target_disk_type")

    @target_disk_type.setter
    def target_disk_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_disk_type", value)

    @property
    @pulumi.getter(name="targetReplicaDiskType")
    def target_replica_disk_type(self) -> pulumi.Input[str]:
        """
        What type should the disk be that holds the replication data.
        """
        return pulumi.get(self, "target_replica_disk_type")

    @target_replica_disk_type.setter
    def target_replica_disk_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_replica_disk_type", value)

    @property
    @pulumi.getter(name="targetResourceGroupId")
    def target_resource_group_id(self) -> pulumi.Input[str]:
        """
        Resource group disk should belong to when a failover is done.
        """
        return pulumi.get(self, "target_resource_group_id")

    @target_resource_group_id.setter
    def target_resource_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_resource_group_id", value)


@pulumi.input_type
class ReplicatedVMNetworkInterfaceArgs:
    def __init__(__self__, *,
                 source_network_interface_id: Optional[pulumi.Input[str]] = None,
                 target_static_ip: Optional[pulumi.Input[str]] = None,
                 target_subnet_name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] source_network_interface_id: Id source network interface.
        :param pulumi.Input[str] target_static_ip: Static IP to assign when a failover is done.
        :param pulumi.Input[str] target_subnet_name: Name of the subnet to to use when a failover is done.
        """
        if source_network_interface_id is not None:
            pulumi.set(__self__, "source_network_interface_id", source_network_interface_id)
        if target_static_ip is not None:
            pulumi.set(__self__, "target_static_ip", target_static_ip)
        if target_subnet_name is not None:
            pulumi.set(__self__, "target_subnet_name", target_subnet_name)

    @property
    @pulumi.getter(name="sourceNetworkInterfaceId")
    def source_network_interface_id(self) -> Optional[pulumi.Input[str]]:
        """
        Id source network interface.
        """
        return pulumi.get(self, "source_network_interface_id")

    @source_network_interface_id.setter
    def source_network_interface_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_network_interface_id", value)

    @property
    @pulumi.getter(name="targetStaticIp")
    def target_static_ip(self) -> Optional[pulumi.Input[str]]:
        """
        Static IP to assign when a failover is done.
        """
        return pulumi.get(self, "target_static_ip")

    @target_static_ip.setter
    def target_static_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_static_ip", value)

    @property
    @pulumi.getter(name="targetSubnetName")
    def target_subnet_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the subnet to to use when a failover is done.
        """
        return pulumi.get(self, "target_subnet_name")

    @target_subnet_name.setter
    def target_subnet_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_subnet_name", value)


