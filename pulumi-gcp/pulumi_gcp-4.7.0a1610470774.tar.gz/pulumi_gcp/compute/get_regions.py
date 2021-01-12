# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetRegionsResult',
    'AwaitableGetRegionsResult',
    'get_regions',
]

@pulumi.output_type
class GetRegionsResult:
    """
    A collection of values returned by getRegions.
    """
    def __init__(__self__, id=None, names=None, project=None, status=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of regions available in the given project
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")


class AwaitableGetRegionsResult(GetRegionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegionsResult(
            id=self.id,
            names=self.names,
            project=self.project,
            status=self.status)


def get_regions(project: Optional[str] = None,
                status: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRegionsResult:
    """
    Provides access to available Google Compute regions for a given project.
    See more about [regions and zones](https://cloud.google.com/compute/docs/regions-zones/) in the upstream docs.

    ```python
    import pulumi
    import pulumi_gcp as gcp

    available = gcp.compute.get_regions()
    cluster = []
    for range in [{"value": i} for i in range(0, len(available.names))]:
        cluster.append(gcp.compute.Subnetwork(f"cluster-{range['value']}",
            ip_cidr_range=f"10.36.{range['value']}.0/24",
            network="my-network",
            region=available.names[range["value"]]))
    ```


    :param str project: Project from which to list available regions. Defaults to project declared in the provider.
    :param str status: Allows to filter list of regions based on their current status. Status can be either `UP` or `DOWN`.
           Defaults to no filtering (all available regions - both `UP` and `DOWN`).
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['status'] = status
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('gcp:compute/getRegions:getRegions', __args__, opts=opts, typ=GetRegionsResult).value

    return AwaitableGetRegionsResult(
        id=__ret__.id,
        names=__ret__.names,
        project=__ret__.project,
        status=__ret__.status)
