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
    'GetAppServiceResult',
    'AwaitableGetAppServiceResult',
    'get_app_service',
]

@pulumi.output_type
class GetAppServiceResult:
    """
    A collection of values returned by getAppService.
    """
    def __init__(__self__, app_service_plan_id=None, app_settings=None, client_affinity_enabled=None, client_cert_enabled=None, connection_strings=None, custom_domain_verification_id=None, default_site_hostname=None, enabled=None, https_only=None, id=None, location=None, name=None, outbound_ip_address_lists=None, outbound_ip_addresses=None, possible_outbound_ip_address_lists=None, possible_outbound_ip_addresses=None, resource_group_name=None, site_configs=None, site_credentials=None, source_controls=None, tags=None):
        if app_service_plan_id and not isinstance(app_service_plan_id, str):
            raise TypeError("Expected argument 'app_service_plan_id' to be a str")
        pulumi.set(__self__, "app_service_plan_id", app_service_plan_id)
        if app_settings and not isinstance(app_settings, dict):
            raise TypeError("Expected argument 'app_settings' to be a dict")
        pulumi.set(__self__, "app_settings", app_settings)
        if client_affinity_enabled and not isinstance(client_affinity_enabled, bool):
            raise TypeError("Expected argument 'client_affinity_enabled' to be a bool")
        pulumi.set(__self__, "client_affinity_enabled", client_affinity_enabled)
        if client_cert_enabled and not isinstance(client_cert_enabled, bool):
            raise TypeError("Expected argument 'client_cert_enabled' to be a bool")
        pulumi.set(__self__, "client_cert_enabled", client_cert_enabled)
        if connection_strings and not isinstance(connection_strings, list):
            raise TypeError("Expected argument 'connection_strings' to be a list")
        pulumi.set(__self__, "connection_strings", connection_strings)
        if custom_domain_verification_id and not isinstance(custom_domain_verification_id, str):
            raise TypeError("Expected argument 'custom_domain_verification_id' to be a str")
        pulumi.set(__self__, "custom_domain_verification_id", custom_domain_verification_id)
        if default_site_hostname and not isinstance(default_site_hostname, str):
            raise TypeError("Expected argument 'default_site_hostname' to be a str")
        pulumi.set(__self__, "default_site_hostname", default_site_hostname)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if https_only and not isinstance(https_only, bool):
            raise TypeError("Expected argument 'https_only' to be a bool")
        pulumi.set(__self__, "https_only", https_only)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if outbound_ip_address_lists and not isinstance(outbound_ip_address_lists, list):
            raise TypeError("Expected argument 'outbound_ip_address_lists' to be a list")
        pulumi.set(__self__, "outbound_ip_address_lists", outbound_ip_address_lists)
        if outbound_ip_addresses and not isinstance(outbound_ip_addresses, str):
            raise TypeError("Expected argument 'outbound_ip_addresses' to be a str")
        pulumi.set(__self__, "outbound_ip_addresses", outbound_ip_addresses)
        if possible_outbound_ip_address_lists and not isinstance(possible_outbound_ip_address_lists, list):
            raise TypeError("Expected argument 'possible_outbound_ip_address_lists' to be a list")
        pulumi.set(__self__, "possible_outbound_ip_address_lists", possible_outbound_ip_address_lists)
        if possible_outbound_ip_addresses and not isinstance(possible_outbound_ip_addresses, str):
            raise TypeError("Expected argument 'possible_outbound_ip_addresses' to be a str")
        pulumi.set(__self__, "possible_outbound_ip_addresses", possible_outbound_ip_addresses)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if site_configs and not isinstance(site_configs, list):
            raise TypeError("Expected argument 'site_configs' to be a list")
        pulumi.set(__self__, "site_configs", site_configs)
        if site_credentials and not isinstance(site_credentials, list):
            raise TypeError("Expected argument 'site_credentials' to be a list")
        pulumi.set(__self__, "site_credentials", site_credentials)
        if source_controls and not isinstance(source_controls, list):
            raise TypeError("Expected argument 'source_controls' to be a list")
        pulumi.set(__self__, "source_controls", source_controls)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="appServicePlanId")
    def app_service_plan_id(self) -> str:
        """
        The ID of the App Service Plan within which the App Service exists.
        """
        return pulumi.get(self, "app_service_plan_id")

    @property
    @pulumi.getter(name="appSettings")
    def app_settings(self) -> Mapping[str, str]:
        """
        A key-value pair of App Settings for the App Service.
        """
        return pulumi.get(self, "app_settings")

    @property
    @pulumi.getter(name="clientAffinityEnabled")
    def client_affinity_enabled(self) -> bool:
        """
        Does the App Service send session affinity cookies, which route client requests in the same session to the same instance?
        """
        return pulumi.get(self, "client_affinity_enabled")

    @property
    @pulumi.getter(name="clientCertEnabled")
    def client_cert_enabled(self) -> bool:
        """
        Does the App Service require client certificates for incoming requests?
        """
        return pulumi.get(self, "client_cert_enabled")

    @property
    @pulumi.getter(name="connectionStrings")
    def connection_strings(self) -> Sequence['outputs.GetAppServiceConnectionStringResult']:
        """
        An `connection_string` block as defined below.
        """
        return pulumi.get(self, "connection_strings")

    @property
    @pulumi.getter(name="customDomainVerificationId")
    def custom_domain_verification_id(self) -> str:
        """
        An identifier used by App Service to perform domain ownership verification via DNS TXT record.
        """
        return pulumi.get(self, "custom_domain_verification_id")

    @property
    @pulumi.getter(name="defaultSiteHostname")
    def default_site_hostname(self) -> str:
        """
        The Default Hostname associated with the App Service - such as `mysite.azurewebsites.net`
        """
        return pulumi.get(self, "default_site_hostname")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Is the App Service Enabled?
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="httpsOnly")
    def https_only(self) -> bool:
        """
        Can the App Service only be accessed via HTTPS?
        """
        return pulumi.get(self, "https_only")

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
        The Azure location where the App Service exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name for this IP Restriction.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outboundIpAddressLists")
    def outbound_ip_address_lists(self) -> Sequence[str]:
        """
        A list of outbound IP addresses - such as `["52.23.25.3", "52.143.43.12"]`
        """
        return pulumi.get(self, "outbound_ip_address_lists")

    @property
    @pulumi.getter(name="outboundIpAddresses")
    def outbound_ip_addresses(self) -> str:
        """
        A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`
        """
        return pulumi.get(self, "outbound_ip_addresses")

    @property
    @pulumi.getter(name="possibleOutboundIpAddressLists")
    def possible_outbound_ip_address_lists(self) -> Sequence[str]:
        """
        A list of outbound IP addresses - such as `["52.23.25.3", "52.143.43.12", "52.143.43.17"]` - not all of which are necessarily in use. Superset of `outbound_ip_address_list`.
        """
        return pulumi.get(self, "possible_outbound_ip_address_lists")

    @property
    @pulumi.getter(name="possibleOutboundIpAddresses")
    def possible_outbound_ip_addresses(self) -> str:
        """
        A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12,52.143.43.17` - not all of which are necessarily in use. Superset of `outbound_ip_addresses`.
        """
        return pulumi.get(self, "possible_outbound_ip_addresses")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="siteConfigs")
    def site_configs(self) -> Sequence['outputs.GetAppServiceSiteConfigResult']:
        """
        A `site_config` block as defined below.
        """
        return pulumi.get(self, "site_configs")

    @property
    @pulumi.getter(name="siteCredentials")
    def site_credentials(self) -> Sequence['outputs.GetAppServiceSiteCredentialResult']:
        return pulumi.get(self, "site_credentials")

    @property
    @pulumi.getter(name="sourceControls")
    def source_controls(self) -> Sequence['outputs.GetAppServiceSourceControlResult']:
        """
        A `source_control` block as defined below.
        """
        return pulumi.get(self, "source_controls")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetAppServiceResult(GetAppServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAppServiceResult(
            app_service_plan_id=self.app_service_plan_id,
            app_settings=self.app_settings,
            client_affinity_enabled=self.client_affinity_enabled,
            client_cert_enabled=self.client_cert_enabled,
            connection_strings=self.connection_strings,
            custom_domain_verification_id=self.custom_domain_verification_id,
            default_site_hostname=self.default_site_hostname,
            enabled=self.enabled,
            https_only=self.https_only,
            id=self.id,
            location=self.location,
            name=self.name,
            outbound_ip_address_lists=self.outbound_ip_address_lists,
            outbound_ip_addresses=self.outbound_ip_addresses,
            possible_outbound_ip_address_lists=self.possible_outbound_ip_address_lists,
            possible_outbound_ip_addresses=self.possible_outbound_ip_addresses,
            resource_group_name=self.resource_group_name,
            site_configs=self.site_configs,
            site_credentials=self.site_credentials,
            source_controls=self.source_controls,
            tags=self.tags)


def get_app_service(name: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAppServiceResult:
    """
    Use this data source to access information about an existing App Service.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.appservice.get_app_service(name="search-app-service",
        resource_group_name="search-service")
    pulumi.export("appServiceId", example.id)
    ```


    :param str name: The name of the App Service.
    :param str resource_group_name: The Name of the Resource Group where the App Service exists.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:appservice/getAppService:getAppService', __args__, opts=opts, typ=GetAppServiceResult).value

    return AwaitableGetAppServiceResult(
        app_service_plan_id=__ret__.app_service_plan_id,
        app_settings=__ret__.app_settings,
        client_affinity_enabled=__ret__.client_affinity_enabled,
        client_cert_enabled=__ret__.client_cert_enabled,
        connection_strings=__ret__.connection_strings,
        custom_domain_verification_id=__ret__.custom_domain_verification_id,
        default_site_hostname=__ret__.default_site_hostname,
        enabled=__ret__.enabled,
        https_only=__ret__.https_only,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        outbound_ip_address_lists=__ret__.outbound_ip_address_lists,
        outbound_ip_addresses=__ret__.outbound_ip_addresses,
        possible_outbound_ip_address_lists=__ret__.possible_outbound_ip_address_lists,
        possible_outbound_ip_addresses=__ret__.possible_outbound_ip_addresses,
        resource_group_name=__ret__.resource_group_name,
        site_configs=__ret__.site_configs,
        site_credentials=__ret__.site_credentials,
        source_controls=__ret__.source_controls,
        tags=__ret__.tags)
