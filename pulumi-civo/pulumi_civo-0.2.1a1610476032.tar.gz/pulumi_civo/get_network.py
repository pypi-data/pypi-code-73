# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = [
    'GetNetworkResult',
    'AwaitableGetNetworkResult',
    'get_network',
]

@pulumi.output_type
class GetNetworkResult:
    """
    A collection of values returned by getNetwork.
    """
    def __init__(__self__, cidr=None, default=None, id=None, label=None, name=None, region=None):
        if cidr and not isinstance(cidr, str):
            raise TypeError("Expected argument 'cidr' to be a str")
        pulumi.set(__self__, "cidr", cidr)
        if default and not isinstance(default, bool):
            raise TypeError("Expected argument 'default' to be a bool")
        pulumi.set(__self__, "default", default)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if label and not isinstance(label, str):
            raise TypeError("Expected argument 'label' to be a str")
        pulumi.set(__self__, "label", label)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter
    def cidr(self) -> str:
        """
        The block ip assigned to the network.
        """
        return pulumi.get(self, "cidr")

    @property
    @pulumi.getter
    def default(self) -> bool:
        """
        If is the default network.
        """
        return pulumi.get(self, "default")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        A unique ID that can be used to identify and reference a Network.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def label(self) -> Optional[str]:
        """
        The label used in the configuration.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the network.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        The region where the network was create.
        """
        return pulumi.get(self, "region")


class AwaitableGetNetworkResult(GetNetworkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkResult(
            cidr=self.cidr,
            default=self.default,
            id=self.id,
            label=self.label,
            name=self.name,
            region=self.region)


def get_network(id: Optional[str] = None,
                label: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkResult:
    """
    Use this data source to access information about an existing resource.

    :param str id: The unique identifier of an existing Network.
    :param str label: The name of an existing Network.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['label'] = label
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('civo:index/getNetwork:getNetwork', __args__, opts=opts, typ=GetNetworkResult).value

    return AwaitableGetNetworkResult(
        cidr=__ret__.cidr,
        default=__ret__.default,
        id=__ret__.id,
        label=__ret__.label,
        name=__ret__.name,
        region=__ret__.region)
