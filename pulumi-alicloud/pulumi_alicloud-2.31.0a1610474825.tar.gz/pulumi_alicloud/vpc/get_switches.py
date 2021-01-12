# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'GetSwitchesResult',
    'AwaitableGetSwitchesResult',
    'get_switches',
]

@pulumi.output_type
class GetSwitchesResult:
    """
    A collection of values returned by getSwitches.
    """
    def __init__(__self__, cidr_block=None, id=None, ids=None, is_default=None, name_regex=None, names=None, output_file=None, resource_group_id=None, tags=None, vpc_id=None, vswitches=None, zone_id=None):
        if cidr_block and not isinstance(cidr_block, str):
            raise TypeError("Expected argument 'cidr_block' to be a str")
        pulumi.set(__self__, "cidr_block", cidr_block)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if is_default and not isinstance(is_default, bool):
            raise TypeError("Expected argument 'is_default' to be a bool")
        pulumi.set(__self__, "is_default", is_default)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if resource_group_id and not isinstance(resource_group_id, str):
            raise TypeError("Expected argument 'resource_group_id' to be a str")
        pulumi.set(__self__, "resource_group_id", resource_group_id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        pulumi.set(__self__, "vpc_id", vpc_id)
        if vswitches and not isinstance(vswitches, list):
            raise TypeError("Expected argument 'vswitches' to be a list")
        pulumi.set(__self__, "vswitches", vswitches)
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[str]:
        """
        CIDR block of the VSwitch.
        """
        return pulumi.get(self, "cidr_block")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        A list of VSwitch IDs.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[bool]:
        """
        Whether the VSwitch is the default one in the region.
        """
        return pulumi.get(self, "is_default")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of VSwitch names.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[str]:
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Any]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[str]:
        """
        ID of the VPC that owns the VSwitch.
        """
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter
    def vswitches(self) -> Sequence['outputs.GetSwitchesVswitchResult']:
        """
        A list of VSwitches. Each element contains the following attributes:
        """
        return pulumi.get(self, "vswitches")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[str]:
        """
        ID of the availability zone where the VSwitch is located.
        """
        return pulumi.get(self, "zone_id")


class AwaitableGetSwitchesResult(GetSwitchesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSwitchesResult(
            cidr_block=self.cidr_block,
            id=self.id,
            ids=self.ids,
            is_default=self.is_default,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            resource_group_id=self.resource_group_id,
            tags=self.tags,
            vpc_id=self.vpc_id,
            vswitches=self.vswitches,
            zone_id=self.zone_id)


def get_switches(cidr_block: Optional[str] = None,
                 ids: Optional[Sequence[str]] = None,
                 is_default: Optional[bool] = None,
                 name_regex: Optional[str] = None,
                 output_file: Optional[str] = None,
                 resource_group_id: Optional[str] = None,
                 tags: Optional[Mapping[str, Any]] = None,
                 vpc_id: Optional[str] = None,
                 zone_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSwitchesResult:
    """
    This data source provides a list of VSwitches owned by an Alibaba Cloud account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    config = pulumi.Config()
    name = config.get("name")
    if name is None:
        name = "vswitchDatasourceName"
    default_zones = alicloud.get_zones()
    vpc = alicloud.vpc.Network("vpc", cidr_block="172.16.0.0/16")
    vswitch = alicloud.vpc.Switch("vswitch",
        availability_zone=default_zones.zones[0].id,
        cidr_block="172.16.0.0/24",
        vpc_id=vpc.id)
    default_switches = vswitch.name.apply(lambda name: alicloud.vpc.get_switches(name_regex=name))
    ```


    :param str cidr_block: Filter results by a specific CIDR block. For example: "172.16.0.0/12".
    :param Sequence[str] ids: A list of VSwitch IDs.
    :param bool is_default: Indicate whether the VSwitch is created by the system.
    :param str name_regex: A regex string to filter results by name.
    :param str resource_group_id: The Id of resource group which VSWitch belongs.
    :param Mapping[str, Any] tags: A mapping of tags to assign to the resource.
    :param str vpc_id: ID of the VPC that owns the VSwitch.
    :param str zone_id: The availability zone of the VSwitch.
    """
    __args__ = dict()
    __args__['cidrBlock'] = cidr_block
    __args__['ids'] = ids
    __args__['isDefault'] = is_default
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['resourceGroupId'] = resource_group_id
    __args__['tags'] = tags
    __args__['vpcId'] = vpc_id
    __args__['zoneId'] = zone_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:vpc/getSwitches:getSwitches', __args__, opts=opts, typ=GetSwitchesResult).value

    return AwaitableGetSwitchesResult(
        cidr_block=__ret__.cidr_block,
        id=__ret__.id,
        ids=__ret__.ids,
        is_default=__ret__.is_default,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        output_file=__ret__.output_file,
        resource_group_id=__ret__.resource_group_id,
        tags=__ret__.tags,
        vpc_id=__ret__.vpc_id,
        vswitches=__ret__.vswitches,
        zone_id=__ret__.zone_id)
