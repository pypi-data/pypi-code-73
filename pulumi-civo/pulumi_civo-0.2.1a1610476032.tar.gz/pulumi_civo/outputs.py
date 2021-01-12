# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = [
    'KubernetesClusterInstalledApplication',
    'KubernetesClusterInstance',
    'LoadBalancerBackend',
    'GetInstancesFilterResult',
    'GetInstancesInstanceResult',
    'GetInstancesSizeFilterResult',
    'GetInstancesSizeSizeResult',
    'GetInstancesSizeSortResult',
    'GetInstancesSortResult',
    'GetKubernetesClusterInstalledApplicationResult',
    'GetKubernetesClusterInstanceResult',
    'GetKubernetesVersionFilterResult',
    'GetKubernetesVersionSortResult',
    'GetKubernetesVersionVersionResult',
    'GetLoadBalancerBackendResult',
    'GetTemplateFilterResult',
    'GetTemplateSortResult',
    'GetTemplateTemplateResult',
]

@pulumi.output_type
class KubernetesClusterInstalledApplication(dict):
    def __init__(__self__, *,
                 application: Optional[str] = None,
                 category: Optional[str] = None,
                 installed: Optional[bool] = None,
                 version: Optional[str] = None):
        """
        :param str application: The name of the application
        :param str category: The category of the application
        :param bool installed: if installed or not
        :param str version: The version of the application
        """
        if application is not None:
            pulumi.set(__self__, "application", application)
        if category is not None:
            pulumi.set(__self__, "category", category)
        if installed is not None:
            pulumi.set(__self__, "installed", installed)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def application(self) -> Optional[str]:
        """
        The name of the application
        """
        return pulumi.get(self, "application")

    @property
    @pulumi.getter
    def category(self) -> Optional[str]:
        """
        The category of the application
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def installed(self) -> Optional[bool]:
        """
        if installed or not
        """
        return pulumi.get(self, "installed")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        The version of the application
        """
        return pulumi.get(self, "version")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class KubernetesClusterInstance(dict):
    def __init__(__self__, *,
                 cpu_cores: Optional[int] = None,
                 created_at: Optional[str] = None,
                 disk_gb: Optional[int] = None,
                 firewall_id: Optional[str] = None,
                 hostname: Optional[str] = None,
                 public_ip: Optional[str] = None,
                 ram_mb: Optional[int] = None,
                 region: Optional[str] = None,
                 size: Optional[str] = None,
                 status: Optional[str] = None,
                 tags: Optional[Sequence[str]] = None):
        """
        :param int cpu_cores: Total cpu of the inatance.
        :param str created_at: The date where the Kubernetes cluster was create.
        :param int disk_gb: The size of the disk.
        :param str firewall_id: The firewall id assigned to the instance
        :param str hostname: The hostname of the instance.
        :param str public_ip: The public ip of the instances, only available if the instances is the master
        :param int ram_mb: Total ram of the instance.
        :param str region: The region where instance are.
        :param str size: The size of the instance.
        :param str status: The status of Kubernetes cluster.
               * `ready` -If the Kubernetes cluster is ready.
        :param Sequence[str] tags: A space separated list of tags, to be used freely as required.
        """
        if cpu_cores is not None:
            pulumi.set(__self__, "cpu_cores", cpu_cores)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if disk_gb is not None:
            pulumi.set(__self__, "disk_gb", disk_gb)
        if firewall_id is not None:
            pulumi.set(__self__, "firewall_id", firewall_id)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if public_ip is not None:
            pulumi.set(__self__, "public_ip", public_ip)
        if ram_mb is not None:
            pulumi.set(__self__, "ram_mb", ram_mb)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="cpuCores")
    def cpu_cores(self) -> Optional[int]:
        """
        Total cpu of the inatance.
        """
        return pulumi.get(self, "cpu_cores")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The date where the Kubernetes cluster was create.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="diskGb")
    def disk_gb(self) -> Optional[int]:
        """
        The size of the disk.
        """
        return pulumi.get(self, "disk_gb")

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> Optional[str]:
        """
        The firewall id assigned to the instance
        """
        return pulumi.get(self, "firewall_id")

    @property
    @pulumi.getter
    def hostname(self) -> Optional[str]:
        """
        The hostname of the instance.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> Optional[str]:
        """
        The public ip of the instances, only available if the instances is the master
        """
        return pulumi.get(self, "public_ip")

    @property
    @pulumi.getter(name="ramMb")
    def ram_mb(self) -> Optional[int]:
        """
        Total ram of the instance.
        """
        return pulumi.get(self, "ram_mb")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        """
        The region where instance are.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def size(self) -> Optional[str]:
        """
        The size of the instance.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of Kubernetes cluster.
        * `ready` -If the Kubernetes cluster is ready.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[str]]:
        """
        A space separated list of tags, to be used freely as required.
        """
        return pulumi.get(self, "tags")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class LoadBalancerBackend(dict):
    def __init__(__self__, *,
                 instance_id: str,
                 port: int,
                 protocol: str):
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> str:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def port(self) -> int:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        return pulumi.get(self, "protocol")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetInstancesFilterResult(dict):
    def __init__(__self__, *,
                 key: str,
                 values: Sequence[str]):
        """
        :param str key: Filter the Instances by this key. This may be one of '`id`, `hostname`, `public_ip`, `private_ip`,
               `pseudo_ip`, `size`, `cpu_cores`, `ram_mb`, `disk_gb`, `template` or `created_at`.
        :param Sequence[str] values: A list of values to match against the `key` field. Only retrieves Instances
               where the `key` field takes on one or more of the values provided here.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Filter the Instances by this key. This may be one of '`id`, `hostname`, `public_ip`, `private_ip`,
        `pseudo_ip`, `size`, `cpu_cores`, `ram_mb`, `disk_gb`, `template` or `created_at`.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        A list of values to match against the `key` field. Only retrieves Instances
        where the `key` field takes on one or more of the values provided here.
        """
        return pulumi.get(self, "values")


@pulumi.output_type
class GetInstancesInstanceResult(dict):
    def __init__(__self__, *,
                 cpu_cores: int,
                 created_at: str,
                 disk_gb: int,
                 firewall_id: str,
                 hostname: str,
                 id: str,
                 initial_password: str,
                 initial_user: str,
                 network_id: str,
                 notes: str,
                 private_ip: str,
                 pseudo_ip: str,
                 public_ip: str,
                 ram_mb: int,
                 reverse_dns: str,
                 script: str,
                 size: str,
                 sshkey_id: str,
                 status: str,
                 tags: Sequence[str],
                 template: str):
        """
        :param int cpu_cores: Total cpu of the inatance.
        :param str created_at: The date of creation of the instance
        :param int disk_gb: The size of the disk.
        :param str firewall_id: The ID of the firewall used.
        :param str hostname: The Instance hostname.
        :param str id: The ID of the Instance.
        :param str initial_password: Instance initial password
        :param str initial_user: The name of the initial user created on the server.
        :param str network_id: This will be the ID of the network.
        :param str notes: The notes of the instance.
        :param str private_ip: The private ip.
        :param str pseudo_ip: Is the ip that is used to route the public ip from the internet to the instance using NAT
        :param str public_ip: The public ip.
        :param int ram_mb: Total ram of the instance.
        :param str reverse_dns: A fully qualified domain name.
        :param str script: the contents of a script uploaded
        :param str size: The name of the size.
        :param str sshkey_id: The ID SSH.
        :param str status: The status of the instance
        :param Sequence[str] tags: An optional list of tags
        :param str template: The ID for the template to used to build the instance.
        """
        pulumi.set(__self__, "cpu_cores", cpu_cores)
        pulumi.set(__self__, "created_at", created_at)
        pulumi.set(__self__, "disk_gb", disk_gb)
        pulumi.set(__self__, "firewall_id", firewall_id)
        pulumi.set(__self__, "hostname", hostname)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "initial_password", initial_password)
        pulumi.set(__self__, "initial_user", initial_user)
        pulumi.set(__self__, "network_id", network_id)
        pulumi.set(__self__, "notes", notes)
        pulumi.set(__self__, "private_ip", private_ip)
        pulumi.set(__self__, "pseudo_ip", pseudo_ip)
        pulumi.set(__self__, "public_ip", public_ip)
        pulumi.set(__self__, "ram_mb", ram_mb)
        pulumi.set(__self__, "reverse_dns", reverse_dns)
        pulumi.set(__self__, "script", script)
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "sshkey_id", sshkey_id)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "tags", tags)
        pulumi.set(__self__, "template", template)

    @property
    @pulumi.getter(name="cpuCores")
    def cpu_cores(self) -> int:
        """
        Total cpu of the inatance.
        """
        return pulumi.get(self, "cpu_cores")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The date of creation of the instance
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="diskGb")
    def disk_gb(self) -> int:
        """
        The size of the disk.
        """
        return pulumi.get(self, "disk_gb")

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> str:
        """
        The ID of the firewall used.
        """
        return pulumi.get(self, "firewall_id")

    @property
    @pulumi.getter
    def hostname(self) -> str:
        """
        The Instance hostname.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Instance.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="initialPassword")
    def initial_password(self) -> str:
        """
        Instance initial password
        """
        return pulumi.get(self, "initial_password")

    @property
    @pulumi.getter(name="initialUser")
    def initial_user(self) -> str:
        """
        The name of the initial user created on the server.
        """
        return pulumi.get(self, "initial_user")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> str:
        """
        This will be the ID of the network.
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter
    def notes(self) -> str:
        """
        The notes of the instance.
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> str:
        """
        The private ip.
        """
        return pulumi.get(self, "private_ip")

    @property
    @pulumi.getter(name="pseudoIp")
    def pseudo_ip(self) -> str:
        """
        Is the ip that is used to route the public ip from the internet to the instance using NAT
        """
        return pulumi.get(self, "pseudo_ip")

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> str:
        """
        The public ip.
        """
        return pulumi.get(self, "public_ip")

    @property
    @pulumi.getter(name="ramMb")
    def ram_mb(self) -> int:
        """
        Total ram of the instance.
        """
        return pulumi.get(self, "ram_mb")

    @property
    @pulumi.getter(name="reverseDns")
    def reverse_dns(self) -> str:
        """
        A fully qualified domain name.
        """
        return pulumi.get(self, "reverse_dns")

    @property
    @pulumi.getter
    def script(self) -> str:
        """
        the contents of a script uploaded
        """
        return pulumi.get(self, "script")

    @property
    @pulumi.getter
    def size(self) -> str:
        """
        The name of the size.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="sshkeyId")
    def sshkey_id(self) -> str:
        """
        The ID SSH.
        """
        return pulumi.get(self, "sshkey_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the instance
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        """
        An optional list of tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def template(self) -> str:
        """
        The ID for the template to used to build the instance.
        """
        return pulumi.get(self, "template")


@pulumi.output_type
class GetInstancesSizeFilterResult(dict):
    def __init__(__self__, *,
                 key: str,
                 values: Sequence[str]):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")


@pulumi.output_type
class GetInstancesSizeSizeResult(dict):
    def __init__(__self__, *,
                 cpu_cores: int,
                 description: str,
                 disk_gb: int,
                 name: str,
                 nice_name: str,
                 ram_mb: int,
                 selectable: bool):
        pulumi.set(__self__, "cpu_cores", cpu_cores)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "disk_gb", disk_gb)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "nice_name", nice_name)
        pulumi.set(__self__, "ram_mb", ram_mb)
        pulumi.set(__self__, "selectable", selectable)

    @property
    @pulumi.getter(name="cpuCores")
    def cpu_cores(self) -> int:
        return pulumi.get(self, "cpu_cores")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="diskGb")
    def disk_gb(self) -> int:
        return pulumi.get(self, "disk_gb")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="niceName")
    def nice_name(self) -> str:
        return pulumi.get(self, "nice_name")

    @property
    @pulumi.getter(name="ramMb")
    def ram_mb(self) -> int:
        return pulumi.get(self, "ram_mb")

    @property
    @pulumi.getter
    def selectable(self) -> bool:
        return pulumi.get(self, "selectable")


@pulumi.output_type
class GetInstancesSizeSortResult(dict):
    def __init__(__self__, *,
                 key: str,
                 direction: Optional[str] = None):
        pulumi.set(__self__, "key", key)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        return pulumi.get(self, "direction")


@pulumi.output_type
class GetInstancesSortResult(dict):
    def __init__(__self__, *,
                 key: str,
                 direction: Optional[str] = None):
        """
        :param str key: Sort the Instance by this key. This may be one of `id`, `hostname`, `public_ip`, `private_ip`,
               `pseudo_ip`, `size`, `cpu_cores`, `ram_mb`, `disk_gb`, `template` or `created_at`.
        :param str direction: The sort direction. This may be either `asc` or `desc`.
        """
        pulumi.set(__self__, "key", key)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Sort the Instance by this key. This may be one of `id`, `hostname`, `public_ip`, `private_ip`,
        `pseudo_ip`, `size`, `cpu_cores`, `ram_mb`, `disk_gb`, `template` or `created_at`.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        """
        The sort direction. This may be either `asc` or `desc`.
        """
        return pulumi.get(self, "direction")


@pulumi.output_type
class GetKubernetesClusterInstalledApplicationResult(dict):
    def __init__(__self__, *,
                 application: str,
                 category: str,
                 installed: bool,
                 version: str):
        """
        :param str application: The name of the application
        :param str category: The category of the application
        :param bool installed: if installed or not
        :param str version: The version of the application
        """
        pulumi.set(__self__, "application", application)
        pulumi.set(__self__, "category", category)
        pulumi.set(__self__, "installed", installed)
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def application(self) -> str:
        """
        The name of the application
        """
        return pulumi.get(self, "application")

    @property
    @pulumi.getter
    def category(self) -> str:
        """
        The category of the application
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def installed(self) -> bool:
        """
        if installed or not
        """
        return pulumi.get(self, "installed")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        The version of the application
        """
        return pulumi.get(self, "version")


@pulumi.output_type
class GetKubernetesClusterInstanceResult(dict):
    def __init__(__self__, *,
                 cpu_cores: int,
                 created_at: str,
                 disk_gb: int,
                 firewall_id: str,
                 hostname: str,
                 public_ip: str,
                 ram_mb: int,
                 region: str,
                 size: str,
                 status: str,
                 tags: Sequence[str]):
        """
        :param int cpu_cores: Total cpu of the inatance.
        :param str created_at: The date where the Kubernetes cluster was create.
        :param int disk_gb: The size of the disk.
        :param str firewall_id: The firewall id assigned to the instance
        :param str hostname: The hostname of the instance.
        :param str public_ip: The public ip of the instances, only available if the instances is the master
        :param int ram_mb: Total ram of the instance
        :param str region: The region where instance are.
        :param str size: The size of the instance.
        :param str status: The status of Kubernetes cluster.
               * `ready` -If the Kubernetes cluster is ready.
        :param Sequence[str] tags: The tag of the instances
        """
        pulumi.set(__self__, "cpu_cores", cpu_cores)
        pulumi.set(__self__, "created_at", created_at)
        pulumi.set(__self__, "disk_gb", disk_gb)
        pulumi.set(__self__, "firewall_id", firewall_id)
        pulumi.set(__self__, "hostname", hostname)
        pulumi.set(__self__, "public_ip", public_ip)
        pulumi.set(__self__, "ram_mb", ram_mb)
        pulumi.set(__self__, "region", region)
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="cpuCores")
    def cpu_cores(self) -> int:
        """
        Total cpu of the inatance.
        """
        return pulumi.get(self, "cpu_cores")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The date where the Kubernetes cluster was create.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="diskGb")
    def disk_gb(self) -> int:
        """
        The size of the disk.
        """
        return pulumi.get(self, "disk_gb")

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> str:
        """
        The firewall id assigned to the instance
        """
        return pulumi.get(self, "firewall_id")

    @property
    @pulumi.getter
    def hostname(self) -> str:
        """
        The hostname of the instance.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> str:
        """
        The public ip of the instances, only available if the instances is the master
        """
        return pulumi.get(self, "public_ip")

    @property
    @pulumi.getter(name="ramMb")
    def ram_mb(self) -> int:
        """
        Total ram of the instance
        """
        return pulumi.get(self, "ram_mb")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        The region where instance are.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def size(self) -> str:
        """
        The size of the instance.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of Kubernetes cluster.
        * `ready` -If the Kubernetes cluster is ready.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        """
        The tag of the instances
        """
        return pulumi.get(self, "tags")


@pulumi.output_type
class GetKubernetesVersionFilterResult(dict):
    def __init__(__self__, *,
                 key: str,
                 values: Sequence[str]):
        """
        :param str key: Filter the sizes by this key. This may be one of `version`,
               `label`, `type`, `default`.
        :param Sequence[str] values: Only retrieves the version which keys has value that matches
               one of the values provided here.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Filter the sizes by this key. This may be one of `version`,
        `label`, `type`, `default`.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        Only retrieves the version which keys has value that matches
        one of the values provided here.
        """
        return pulumi.get(self, "values")


@pulumi.output_type
class GetKubernetesVersionSortResult(dict):
    def __init__(__self__, *,
                 key: str,
                 direction: Optional[str] = None):
        """
        :param str key: Sort the sizes by this key. This may be one of `version`.
        :param str direction: The sort direction. This may be either `asc` or `desc`.
        """
        pulumi.set(__self__, "key", key)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Sort the sizes by this key. This may be one of `version`.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        """
        The sort direction. This may be either `asc` or `desc`.
        """
        return pulumi.get(self, "direction")


@pulumi.output_type
class GetKubernetesVersionVersionResult(dict):
    def __init__(__self__, *,
                 default: bool,
                 label: str,
                 type: str,
                 version: str):
        """
        :param bool default: If is the default version used in all cluster.
        :param str label: The label of this version.
        :param str type: The type of the version can be `stable`, `legacy` etc...
        :param str version: A version of the kubernetes.
        """
        pulumi.set(__self__, "default", default)
        pulumi.set(__self__, "label", label)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def default(self) -> bool:
        """
        If is the default version used in all cluster.
        """
        return pulumi.get(self, "default")

    @property
    @pulumi.getter
    def label(self) -> str:
        """
        The label of this version.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the version can be `stable`, `legacy` etc...
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        A version of the kubernetes.
        """
        return pulumi.get(self, "version")


@pulumi.output_type
class GetLoadBalancerBackendResult(dict):
    def __init__(__self__, *,
                 instance_id: str,
                 port: int,
                 protocol: str):
        """
        :param str instance_id: The instance id
        :param int port: The port set in the configuration.
        :param str protocol: The protocol used in the configuration.
        """
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> str:
        """
        The instance id
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def port(self) -> int:
        """
        The port set in the configuration.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        The protocol used in the configuration.
        """
        return pulumi.get(self, "protocol")


@pulumi.output_type
class GetTemplateFilterResult(dict):
    def __init__(__self__, *,
                 key: str,
                 values: Sequence[str]):
        """
        :param str key: Filter the sizes by this key. This may be one of `code`,
               `name`.
        :param Sequence[str] values: Only retrieves the template which keys has value that matches
               one of the values provided here.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Filter the sizes by this key. This may be one of `code`,
        `name`.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        Only retrieves the template which keys has value that matches
        one of the values provided here.
        """
        return pulumi.get(self, "values")


@pulumi.output_type
class GetTemplateSortResult(dict):
    def __init__(__self__, *,
                 key: str,
                 direction: Optional[str] = None):
        """
        :param str key: Sort the sizes by this key. This may be one of `code`, 
               `name`.
        :param str direction: The sort direction. This may be either `asc` or `desc`.
        """
        pulumi.set(__self__, "key", key)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Sort the sizes by this key. This may be one of `code`, 
        `name`.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        """
        The sort direction. This may be either `asc` or `desc`.
        """
        return pulumi.get(self, "direction")


@pulumi.output_type
class GetTemplateTemplateResult(dict):
    def __init__(__self__, *,
                 cloud_config: str,
                 code: str,
                 default_username: str,
                 description: str,
                 id: str,
                 image_id: str,
                 name: str,
                 short_description: str,
                 volume_id: str):
        """
        :param str cloud_config: Commonly referred to as 'user-data', this is a customisation script that is run after
               the instance is first booted.
        :param str code: A unqiue, alphanumerical, short, human readable code for the template.
        :param str default_username: The default username to suggest that the user creates
        :param str description: A multi-line description of the template, in Markdown format
        :param str id: The id of the template
        :param str image_id: The Image ID of any default template or the ID of another template.
        :param str name: A short human readable name for the template
        :param str short_description: A one line description of the template
        :param str volume_id: The ID of a bootable volume, either owned by you or global.
        """
        pulumi.set(__self__, "cloud_config", cloud_config)
        pulumi.set(__self__, "code", code)
        pulumi.set(__self__, "default_username", default_username)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "image_id", image_id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "short_description", short_description)
        pulumi.set(__self__, "volume_id", volume_id)

    @property
    @pulumi.getter(name="cloudConfig")
    def cloud_config(self) -> str:
        """
        Commonly referred to as 'user-data', this is a customisation script that is run after
        the instance is first booted.
        """
        return pulumi.get(self, "cloud_config")

    @property
    @pulumi.getter
    def code(self) -> str:
        """
        A unqiue, alphanumerical, short, human readable code for the template.
        """
        return pulumi.get(self, "code")

    @property
    @pulumi.getter(name="defaultUsername")
    def default_username(self) -> str:
        """
        The default username to suggest that the user creates
        """
        return pulumi.get(self, "default_username")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A multi-line description of the template, in Markdown format
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the template
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> str:
        """
        The Image ID of any default template or the ID of another template.
        """
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A short human readable name for the template
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="shortDescription")
    def short_description(self) -> str:
        """
        A one line description of the template
        """
        return pulumi.get(self, "short_description")

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> str:
        """
        The ID of a bootable volume, either owned by you or global.
        """
        return pulumi.get(self, "volume_id")


