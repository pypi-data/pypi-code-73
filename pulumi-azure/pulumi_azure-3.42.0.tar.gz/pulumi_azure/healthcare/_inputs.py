# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'ServiceAuthenticationConfigurationArgs',
    'ServiceCorsConfigurationArgs',
]

@pulumi.input_type
class ServiceAuthenticationConfigurationArgs:
    def __init__(__self__, *,
                 audience: Optional[pulumi.Input[str]] = None,
                 authority: Optional[pulumi.Input[str]] = None,
                 smart_proxy_enabled: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] audience: The intended audience to receive authentication tokens for the service. The default value is https://azurehealthcareapis.com
        :param pulumi.Input[str] authority: The Azure Active Directory (tenant) that serves as the authentication authority to access the service. The default authority is the Directory defined in the authentication scheme in use when running this provider.
               Authority must be registered to Azure AD and in the following format: https://{Azure-AD-endpoint}/{tenant-id}.
        :param pulumi.Input[bool] smart_proxy_enabled: Enables the 'SMART on FHIR' option for mobile and web implementations.
        """
        if audience is not None:
            pulumi.set(__self__, "audience", audience)
        if authority is not None:
            pulumi.set(__self__, "authority", authority)
        if smart_proxy_enabled is not None:
            pulumi.set(__self__, "smart_proxy_enabled", smart_proxy_enabled)

    @property
    @pulumi.getter
    def audience(self) -> Optional[pulumi.Input[str]]:
        """
        The intended audience to receive authentication tokens for the service. The default value is https://azurehealthcareapis.com
        """
        return pulumi.get(self, "audience")

    @audience.setter
    def audience(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "audience", value)

    @property
    @pulumi.getter
    def authority(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Active Directory (tenant) that serves as the authentication authority to access the service. The default authority is the Directory defined in the authentication scheme in use when running this provider.
        Authority must be registered to Azure AD and in the following format: https://{Azure-AD-endpoint}/{tenant-id}.
        """
        return pulumi.get(self, "authority")

    @authority.setter
    def authority(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authority", value)

    @property
    @pulumi.getter(name="smartProxyEnabled")
    def smart_proxy_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Enables the 'SMART on FHIR' option for mobile and web implementations.
        """
        return pulumi.get(self, "smart_proxy_enabled")

    @smart_proxy_enabled.setter
    def smart_proxy_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "smart_proxy_enabled", value)


@pulumi.input_type
class ServiceCorsConfigurationArgs:
    def __init__(__self__, *,
                 allow_credentials: Optional[pulumi.Input[bool]] = None,
                 allowed_headers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 allowed_methods: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 allowed_origins: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 max_age_in_seconds: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[bool] allow_credentials: If credentials are allowed via CORS.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_headers: A set of headers to be allowed via CORS.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_methods: The methods to be allowed via CORS.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_origins: A set of origins to be allowed via CORS.
        :param pulumi.Input[int] max_age_in_seconds: The max age to be allowed via CORS.
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
    def allow_credentials(self) -> Optional[pulumi.Input[bool]]:
        """
        If credentials are allowed via CORS.
        """
        return pulumi.get(self, "allow_credentials")

    @allow_credentials.setter
    def allow_credentials(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_credentials", value)

    @property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A set of headers to be allowed via CORS.
        """
        return pulumi.get(self, "allowed_headers")

    @allowed_headers.setter
    def allowed_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_headers", value)

    @property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The methods to be allowed via CORS.
        """
        return pulumi.get(self, "allowed_methods")

    @allowed_methods.setter
    def allowed_methods(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_methods", value)

    @property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A set of origins to be allowed via CORS.
        """
        return pulumi.get(self, "allowed_origins")

    @allowed_origins.setter
    def allowed_origins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_origins", value)

    @property
    @pulumi.getter(name="maxAgeInSeconds")
    def max_age_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        The max age to be allowed via CORS.
        """
        return pulumi.get(self, "max_age_in_seconds")

    @max_age_in_seconds.setter
    def max_age_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_age_in_seconds", value)


