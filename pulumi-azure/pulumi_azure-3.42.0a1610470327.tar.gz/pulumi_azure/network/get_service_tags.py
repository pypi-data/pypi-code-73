# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetServiceTagsResult',
    'AwaitableGetServiceTagsResult',
    'get_service_tags',
]

@pulumi.output_type
class GetServiceTagsResult:
    """
    A collection of values returned by getServiceTags.
    """
    def __init__(__self__, address_prefixes=None, id=None, location=None, location_filter=None, service=None):
        if address_prefixes and not isinstance(address_prefixes, list):
            raise TypeError("Expected argument 'address_prefixes' to be a list")
        pulumi.set(__self__, "address_prefixes", address_prefixes)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if location_filter and not isinstance(location_filter, str):
            raise TypeError("Expected argument 'location_filter' to be a str")
        pulumi.set(__self__, "location_filter", location_filter)
        if service and not isinstance(service, str):
            raise TypeError("Expected argument 'service' to be a str")
        pulumi.set(__self__, "service", service)

    @property
    @pulumi.getter(name="addressPrefixes")
    def address_prefixes(self) -> Sequence[str]:
        """
        List of address prefixes for the service type (and optionally a specific region).
        """
        return pulumi.get(self, "address_prefixes")

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
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="locationFilter")
    def location_filter(self) -> Optional[str]:
        return pulumi.get(self, "location_filter")

    @property
    @pulumi.getter
    def service(self) -> str:
        return pulumi.get(self, "service")


class AwaitableGetServiceTagsResult(GetServiceTagsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceTagsResult(
            address_prefixes=self.address_prefixes,
            id=self.id,
            location=self.location,
            location_filter=self.location_filter,
            service=self.service)


def get_service_tags(location: Optional[str] = None,
                     location_filter: Optional[str] = None,
                     service: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceTagsResult:
    """
    Use this data source to access information about Service Tags.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.network.get_service_tags(location="westcentralus",
        service="AzureKeyVault",
        location_filter="northeurope")
    pulumi.export("addressPrefixes", data["azurerm_service_tags"]["example"]["address_prefixes"])
    ```


    :param str location: The Azure Region where the Service Tags exists. This value is not used to filter the results but for specifying the region to request. For filtering by region use `location_filter` instead.  More information can be found here: [Service Tags URL parameters](https://docs.microsoft.com/en-us/rest/api/virtualnetwork/servicetags/list#uri-parameters).
    :param str location_filter: Changes the scope of the service tags. Can be any value that is also valid for `location`. If this field is empty then all address prefixes are considered instead of only location specific ones.
    :param str service: The type of the service for which address prefixes will be fetched. Available service tags can be found here: [Available service tags](https://docs.microsoft.com/en-us/azure/virtual-network/service-tags-overview#available-service-tags).
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['locationFilter'] = location_filter
    __args__['service'] = service
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:network/getServiceTags:getServiceTags', __args__, opts=opts, typ=GetServiceTagsResult).value

    return AwaitableGetServiceTagsResult(
        address_prefixes=__ret__.address_prefixes,
        id=__ret__.id,
        location=__ret__.location,
        location_filter=__ret__.location_filter,
        service=__ret__.service)
