# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetUserAssignedIdentityResult',
    'AwaitableGetUserAssignedIdentityResult',
    'get_user_assigned_identity',
]

warnings.warn("""azure.core.getUserAssignedIdentity has been deprecated in favor of azure.authorization.getUserAssignedIdentity""", DeprecationWarning)

@pulumi.output_type
class GetUserAssignedIdentityResult:
    """
    A collection of values returned by getUserAssignedIdentity.
    """
    def __init__(__self__, client_id=None, id=None, location=None, name=None, principal_id=None, resource_group_name=None, tags=None):
        if client_id and not isinstance(client_id, str):
            raise TypeError("Expected argument 'client_id' to be a str")
        pulumi.set(__self__, "client_id", client_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if principal_id and not isinstance(principal_id, str):
            raise TypeError("Expected argument 'principal_id' to be a str")
        pulumi.set(__self__, "principal_id", principal_id)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        The Client ID of the User Assigned Identity.
        """
        return pulumi.get(self, "client_id")

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
        The Azure location where the User Assigned Identity exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The Service Principal ID of the User Assigned Identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags assigned to the User Assigned Identity.
        """
        return pulumi.get(self, "tags")


class AwaitableGetUserAssignedIdentityResult(GetUserAssignedIdentityResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserAssignedIdentityResult(
            client_id=self.client_id,
            id=self.id,
            location=self.location,
            name=self.name,
            principal_id=self.principal_id,
            resource_group_name=self.resource_group_name,
            tags=self.tags)


def get_user_assigned_identity(name: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserAssignedIdentityResult:
    """
    Use this data source to access information about an existing User Assigned Identity.

    ## Example Usage
    ### Reference An Existing)

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.authorization.get_user_assigned_identity(name="name_of_user_assigned_identity",
        resource_group_name="name_of_resource_group")
    pulumi.export("uaiClientId", example.client_id)
    pulumi.export("uaiPrincipalId", example.principal_id)
    ```


    :param str name: The name of the User Assigned Identity.
    :param str resource_group_name: The name of the Resource Group in which the User Assigned Identity exists.
    """
    pulumi.log.warn("get_user_assigned_identity is deprecated: azure.core.getUserAssignedIdentity has been deprecated in favor of azure.authorization.getUserAssignedIdentity")
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:core/getUserAssignedIdentity:getUserAssignedIdentity', __args__, opts=opts, typ=GetUserAssignedIdentityResult).value

    return AwaitableGetUserAssignedIdentityResult(
        client_id=__ret__.client_id,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        principal_id=__ret__.principal_id,
        resource_group_name=__ret__.resource_group_name,
        tags=__ret__.tags)
