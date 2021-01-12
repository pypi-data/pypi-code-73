# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetServiceResult',
    'AwaitableGetServiceResult',
    'get_service',
]

@pulumi.output_type
class GetServiceResult:
    """
    A collection of values returned by getService.
    """
    def __init__(__self__, id=None, location=None, name=None, resource_group_name=None, sku_name=None, subnet_id=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if sku_name and not isinstance(sku_name, str):
            raise TypeError("Expected argument 'sku_name' to be a str")
        pulumi.set(__self__, "sku_name", sku_name)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Azure location where the resource exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> str:
        """
        The sku name of database migration service.
        """
        return pulumi.get(self, "sku_name")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        The ID of the virtual subnet resource to which the database migration service exists.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags to assigned to the resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetServiceResult(GetServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceResult(
            id=self.id,
            location=self.location,
            name=self.name,
            resource_group_name=self.resource_group_name,
            sku_name=self.sku_name,
            subnet_id=self.subnet_id,
            tags=self.tags)


def get_service(name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceResult:
    """
    Use this data source to access information about an existing Database Migration Service.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.databasemigration.get_service(name="example-dms",
        resource_group_name="example-rg")
    pulumi.export("azurermDmsId", example.id)
    ```


    :param str name: Specify the name of the database migration service.
    :param str resource_group_name: Specifies the Name of the Resource Group within which the database migration service exists
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:databasemigration/getService:getService', __args__, opts=opts, typ=GetServiceResult).value

    return AwaitableGetServiceResult(
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        resource_group_name=__ret__.resource_group_name,
        sku_name=__ret__.sku_name,
        subnet_id=__ret__.subnet_id,
        tags=__ret__.tags)
