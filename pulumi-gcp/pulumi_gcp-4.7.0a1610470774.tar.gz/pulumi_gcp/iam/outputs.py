# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'WorkloadIdentityPoolProviderAws',
    'WorkloadIdentityPoolProviderOidc',
    'GetTestablePermissionsPermissionResult',
    'GetWorkloadIdentityPoolProviderAwResult',
    'GetWorkloadIdentityPoolProviderOidcResult',
]

@pulumi.output_type
class WorkloadIdentityPoolProviderAws(dict):
    def __init__(__self__, *,
                 account_id: str):
        """
        :param str account_id: The AWS account ID.
        """
        pulumi.set(__self__, "account_id", account_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        """
        The AWS account ID.
        """
        return pulumi.get(self, "account_id")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class WorkloadIdentityPoolProviderOidc(dict):
    def __init__(__self__, *,
                 issuer_uri: str,
                 allowed_audiences: Optional[Sequence[str]] = None):
        """
        :param str issuer_uri: The OIDC issuer URL.
        :param Sequence[str] allowed_audiences: Acceptable values for the `aud` field (audience) in the OIDC token. Token exchange
               requests are rejected if the token audience does not match one of the configured
               values. Each audience may be at most 256 characters. A maximum of 10 audiences may
               be configured.
               If this list is empty, the OIDC token audience must be equal to the full canonical
               resource name of the WorkloadIdentityPoolProvider, with or without the HTTPS prefix.
               For example:
               ```python
               import pulumi
               ```
        """
        pulumi.set(__self__, "issuer_uri", issuer_uri)
        if allowed_audiences is not None:
            pulumi.set(__self__, "allowed_audiences", allowed_audiences)

    @property
    @pulumi.getter(name="issuerUri")
    def issuer_uri(self) -> str:
        """
        The OIDC issuer URL.
        """
        return pulumi.get(self, "issuer_uri")

    @property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(self) -> Optional[Sequence[str]]:
        """
        Acceptable values for the `aud` field (audience) in the OIDC token. Token exchange
        requests are rejected if the token audience does not match one of the configured
        values. Each audience may be at most 256 characters. A maximum of 10 audiences may
        be configured.
        If this list is empty, the OIDC token audience must be equal to the full canonical
        resource name of the WorkloadIdentityPoolProvider, with or without the HTTPS prefix.
        For example:
        ```python
        import pulumi
        ```
        """
        return pulumi.get(self, "allowed_audiences")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetTestablePermissionsPermissionResult(dict):
    def __init__(__self__, *,
                 api_disabled: bool,
                 custom_support_level: str,
                 name: str,
                 stage: str,
                 title: str):
        """
        :param bool api_disabled: Whether the corresponding API has been enabled for the resource.
        :param str custom_support_level: The level of support for custom roles. Can be one of `"NOT_SUPPORTED"`, `"SUPPORTED"`, `"TESTING"`. Default is `"SUPPORTED"`
        :param str name: Name of the permission.
        :param str stage: Release stage of the permission.
        :param str title: Human readable title of the permission.
        """
        pulumi.set(__self__, "api_disabled", api_disabled)
        pulumi.set(__self__, "custom_support_level", custom_support_level)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "stage", stage)
        pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter(name="apiDisabled")
    def api_disabled(self) -> bool:
        """
        Whether the corresponding API has been enabled for the resource.
        """
        return pulumi.get(self, "api_disabled")

    @property
    @pulumi.getter(name="customSupportLevel")
    def custom_support_level(self) -> str:
        """
        The level of support for custom roles. Can be one of `"NOT_SUPPORTED"`, `"SUPPORTED"`, `"TESTING"`. Default is `"SUPPORTED"`
        """
        return pulumi.get(self, "custom_support_level")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the permission.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def stage(self) -> str:
        """
        Release stage of the permission.
        """
        return pulumi.get(self, "stage")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        Human readable title of the permission.
        """
        return pulumi.get(self, "title")


@pulumi.output_type
class GetWorkloadIdentityPoolProviderAwResult(dict):
    def __init__(__self__, *,
                 account_id: str):
        pulumi.set(__self__, "account_id", account_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")


@pulumi.output_type
class GetWorkloadIdentityPoolProviderOidcResult(dict):
    def __init__(__self__, *,
                 allowed_audiences: Sequence[str],
                 issuer_uri: str):
        pulumi.set(__self__, "allowed_audiences", allowed_audiences)
        pulumi.set(__self__, "issuer_uri", issuer_uri)

    @property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(self) -> Sequence[str]:
        return pulumi.get(self, "allowed_audiences")

    @property
    @pulumi.getter(name="issuerUri")
    def issuer_uri(self) -> str:
        return pulumi.get(self, "issuer_uri")


