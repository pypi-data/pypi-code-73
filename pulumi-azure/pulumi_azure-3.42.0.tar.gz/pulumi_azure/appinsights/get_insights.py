# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetInsightsResult',
    'AwaitableGetInsightsResult',
    'get_insights',
]

@pulumi.output_type
class GetInsightsResult:
    """
    A collection of values returned by getInsights.
    """
    def __init__(__self__, app_id=None, application_type=None, connection_string=None, id=None, instrumentation_key=None, location=None, name=None, resource_group_name=None, retention_in_days=None, tags=None):
        if app_id and not isinstance(app_id, str):
            raise TypeError("Expected argument 'app_id' to be a str")
        pulumi.set(__self__, "app_id", app_id)
        if application_type and not isinstance(application_type, str):
            raise TypeError("Expected argument 'application_type' to be a str")
        pulumi.set(__self__, "application_type", application_type)
        if connection_string and not isinstance(connection_string, str):
            raise TypeError("Expected argument 'connection_string' to be a str")
        pulumi.set(__self__, "connection_string", connection_string)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instrumentation_key and not isinstance(instrumentation_key, str):
            raise TypeError("Expected argument 'instrumentation_key' to be a str")
        pulumi.set(__self__, "instrumentation_key", instrumentation_key)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if retention_in_days and not isinstance(retention_in_days, int):
            raise TypeError("Expected argument 'retention_in_days' to be a int")
        pulumi.set(__self__, "retention_in_days", retention_in_days)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> str:
        """
        The App ID associated with this Application Insights component.
        """
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter(name="applicationType")
    def application_type(self) -> str:
        """
        The type of the component.
        """
        return pulumi.get(self, "application_type")

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> str:
        """
        The connection string of the Application Insights component. (Sensitive)
        """
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instrumentationKey")
    def instrumentation_key(self) -> str:
        """
        The instrumentation key of the Application Insights component.
        """
        return pulumi.get(self, "instrumentation_key")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The Azure location where the component exists.
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
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> int:
        """
        The retention period in days.
        """
        return pulumi.get(self, "retention_in_days")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Tags applied to the component.
        """
        return pulumi.get(self, "tags")


class AwaitableGetInsightsResult(GetInsightsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInsightsResult(
            app_id=self.app_id,
            application_type=self.application_type,
            connection_string=self.connection_string,
            id=self.id,
            instrumentation_key=self.instrumentation_key,
            location=self.location,
            name=self.name,
            resource_group_name=self.resource_group_name,
            retention_in_days=self.retention_in_days,
            tags=self.tags)


def get_insights(name: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInsightsResult:
    """
    Use this data source to access information about an existing Application Insights component.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.appinsights.get_insights(name="production",
        resource_group_name="networking")
    pulumi.export("applicationInsightsInstrumentationKey", example.instrumentation_key)
    ```


    :param str name: Specifies the name of the Application Insights component.
    :param str resource_group_name: Specifies the name of the resource group the Application Insights component is located in.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:appinsights/getInsights:getInsights', __args__, opts=opts, typ=GetInsightsResult).value

    return AwaitableGetInsightsResult(
        app_id=__ret__.app_id,
        application_type=__ret__.application_type,
        connection_string=__ret__.connection_string,
        id=__ret__.id,
        instrumentation_key=__ret__.instrumentation_key,
        location=__ret__.location,
        name=__ret__.name,
        resource_group_name=__ret__.resource_group_name,
        retention_in_days=__ret__.retention_in_days,
        tags=__ret__.tags)
