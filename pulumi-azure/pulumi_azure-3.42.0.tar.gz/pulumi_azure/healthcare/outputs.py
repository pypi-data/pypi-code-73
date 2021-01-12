# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'ServiceAuthenticationConfiguration',
    'ServiceCorsConfiguration',
    'GetServiceAuthenticationConfigurationResult',
    'GetServiceCorsConfigurationResult',
]

@pulumi.output_type
class ServiceAuthenticationConfiguration(dict):
    def __init__(__self__, *,
                 audience: Optional[str] = None,
                 authority: Optional[str] = None,
                 smart_proxy_enabled: Optional[bool] = None):
        """
        :param str audience: The intended audience to receive authentication tokens for the service. The default value is https://azurehealthcareapis.com
        :param str authority: The Azure Active Directory (tenant) that serves as the authentication authority to access the service. The default authority is the Directory defined in the authentication scheme in use when running this provider.
               Authority must be registered to Azure AD and in the following format: https://{Azure-AD-endpoint}/{tenant-id}.
        :param bool smart_proxy_enabled: Enables the 'SMART on FHIR' option for mobile and web implementations.
        """
        if audience is not None:
            pulumi.set(__self__, "audience", audience)
        if authority is not None:
            pulumi.set(__self__, "authority", authority)
        if smart_proxy_enabled is not None:
            pulumi.set(__self__, "smart_proxy_enabled", smart_proxy_enabled)

    @property
    @pulumi.getter
    def audience(self) -> Optional[str]:
        """
        The intended audience to receive authentication tokens for the service. The default value is https://azurehealthcareapis.com
        """
        return pulumi.get(self, "audience")

    @property
    @pulumi.getter
    def authority(self) -> Optional[str]:
        """
        The Azure Active Directory (tenant) that serves as the authentication authority to access the service. The default authority is the Directory defined in the authentication scheme in use when running this provider.
        Authority must be registered to Azure AD and in the following format: https://{Azure-AD-endpoint}/{tenant-id}.
        """
        return pulumi.get(self, "authority")

    @property
    @pulumi.getter(name="smartProxyEnabled")
    def smart_proxy_enabled(self) -> Optional[bool]:
        """
        Enables the 'SMART on FHIR' option for mobile and web implementations.
        """
        return pulumi.get(self, "smart_proxy_enabled")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ServiceCorsConfiguration(dict):
    def __init__(__self__, *,
                 allow_credentials: Optional[bool] = None,
                 allowed_headers: Optional[Sequence[str]] = None,
                 allowed_methods: Optional[Sequence[str]] = None,
                 allowed_origins: Optional[Sequence[str]] = None,
                 max_age_in_seconds: Optional[int] = None):
        """
        :param bool allow_credentials: If credentials are allowed via CORS.
        :param Sequence[str] allowed_headers: A set of headers to be allowed via CORS.
        :param Sequence[str] allowed_methods: The methods to be allowed via CORS.
        :param Sequence[str] allowed_origins: A set of origins to be allowed via CORS.
        :param int max_age_in_seconds: The max age to be allowed via CORS.
        """
        if allow_credentials is not None:
            pulumi.set(__self__, "allow_credentials", allow_credentials)
        if allowed_headers is not None:
            pulumi.set(__self__, "allowed_headers", allowed_headers)
        if allowed_methods is not None:
            pulumi.set(__self__, "allowed_methods", allowed_methods)
        if allowed_origins is not None:
            pulumi.set(__self__, "allowed_origins", allowed_origins)
        if max_age_in_seconds is not None:
            pulumi.set(__self__, "max_age_in_seconds", max_age_in_seconds)

    @property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[bool]:
        """
        If credentials are allowed via CORS.
        """
        return pulumi.get(self, "allow_credentials")

    @property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[Sequence[str]]:
        """
        A set of headers to be allowed via CORS.
        """
        return pulumi.get(self, "allowed_headers")

    @property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Optional[Sequence[str]]:
        """
        The methods to be allowed via CORS.
        """
        return pulumi.get(self, "allowed_methods")

    @property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> Optional[Sequence[str]]:
        """
        A set of origins to be allowed via CORS.
        """
        return pulumi.get(self, "allowed_origins")

    @property
    @pulumi.getter(name="maxAgeInSeconds")
    def max_age_in_seconds(self) -> Optional[int]:
        """
        The max age to be allowed via CORS.
        """
        return pulumi.get(self, "max_age_in_seconds")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetServiceAuthenticationConfigurationResult(dict):
    def __init__(__self__, *,
                 audience: str,
                 authority: str,
                 smart_proxy_enabled: bool):
        """
        :param str audience: The intended audience to receive authentication tokens for the service.
        :param str authority: The Azure Active Directory (tenant) that serves as the authentication authority to access the service.
        :param bool smart_proxy_enabled: Is the 'SMART on FHIR' option for mobile and web implementations enabled?
        """
        pulumi.set(__self__, "audience", audience)
        pulumi.set(__self__, "authority", authority)
        pulumi.set(__self__, "smart_proxy_enabled", smart_proxy_enabled)

    @property
    @pulumi.getter
    def audience(self) -> str:
        """
        The intended audience to receive authentication tokens for the service.
        """
        return pulumi.get(self, "audience")

    @property
    @pulumi.getter
    def authority(self) -> str:
        """
        The Azure Active Directory (tenant) that serves as the authentication authority to access the service.
        """
        return pulumi.get(self, "authority")

    @property
    @pulumi.getter(name="smartProxyEnabled")
    def smart_proxy_enabled(self) -> bool:
        """
        Is the 'SMART on FHIR' option for mobile and web implementations enabled?
        """
        return pulumi.get(self, "smart_proxy_enabled")


@pulumi.output_type
class GetServiceCorsConfigurationResult(dict):
    def __init__(__self__, *,
                 allow_credentials: bool,
                 allowed_headers: Sequence[str],
                 allowed_methods: Sequence[str],
                 allowed_origins: Sequence[str],
                 max_age_in_seconds: int):
        """
        :param bool allow_credentials: Are credentials are allowed via CORS?
        :param Sequence[str] allowed_headers: The set of headers to be allowed via CORS.
        :param Sequence[str] allowed_methods: The methods to be allowed via CORS.
        :param Sequence[str] allowed_origins: The set of origins to be allowed via CORS.
        :param int max_age_in_seconds: The max age to be allowed via CORS.
        """
        pulumi.set(__self__, "allow_credentials", allow_credentials)
        pulumi.set(__self__, "allowed_headers", allowed_headers)
        pulumi.set(__self__, "allowed_methods", allowed_methods)
        pulumi.set(__self__, "allowed_origins", allowed_origins)
        pulumi.set(__self__, "max_age_in_seconds", max_age_in_seconds)

    @property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> bool:
        """
        Are credentials are allowed via CORS?
        """
        return pulumi.get(self, "allow_credentials")

    @property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Sequence[str]:
        """
        The set of headers to be allowed via CORS.
        """
        return pulumi.get(self, "allowed_headers")

    @property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Sequence[str]:
        """
        The methods to be allowed via CORS.
        """
        return pulumi.get(self, "allowed_methods")

    @property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> Sequence[str]:
        """
        The set of origins to be allowed via CORS.
        """
        return pulumi.get(self, "allowed_origins")

    @property
    @pulumi.getter(name="maxAgeInSeconds")
    def max_age_in_seconds(self) -> int:
        """
        The max age to be allowed via CORS.
        """
        return pulumi.get(self, "max_age_in_seconds")


