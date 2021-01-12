# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'VariableGroupKeyVaultArgs',
    'VariableGroupVariableArgs',
]

@pulumi.input_type
class VariableGroupKeyVaultArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 service_endpoint_id: pulumi.Input[str]):
        """
        :param pulumi.Input[str] name: The name of the Variable Group.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "service_endpoint_id", service_endpoint_id)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the Variable Group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="serviceEndpointId")
    def service_endpoint_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "service_endpoint_id")

    @service_endpoint_id.setter
    def service_endpoint_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_endpoint_id", value)


@pulumi.input_type
class VariableGroupVariableArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 content_type: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 expires: Optional[pulumi.Input[str]] = None,
                 is_secret: Optional[pulumi.Input[bool]] = None,
                 secret_value: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] name: The key value used for the variable. Must be unique within the Variable Group.
        :param pulumi.Input[bool] is_secret: A boolean flag describing if the variable value is sensitive. Defaults to `false`.
        :param pulumi.Input[str] secret_value: The secret value of the variable. If omitted, it will default to empty string. Used when `is_secret` set to `true`.
        :param pulumi.Input[str] value: The value of the variable. If omitted, it will default to empty string.
        """
        pulumi.set(__self__, "name", name)
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if expires is not None:
            pulumi.set(__self__, "expires", expires)
        if is_secret is not None:
            pulumi.set(__self__, "is_secret", is_secret)
        if secret_value is not None:
            pulumi.set(__self__, "secret_value", secret_value)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The key value used for the variable. Must be unique within the Variable Group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def expires(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "expires")

    @expires.setter
    def expires(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expires", value)

    @property
    @pulumi.getter(name="isSecret")
    def is_secret(self) -> Optional[pulumi.Input[bool]]:
        """
        A boolean flag describing if the variable value is sensitive. Defaults to `false`.
        """
        return pulumi.get(self, "is_secret")

    @is_secret.setter
    def is_secret(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_secret", value)

    @property
    @pulumi.getter(name="secretValue")
    def secret_value(self) -> Optional[pulumi.Input[str]]:
        """
        The secret value of the variable. If omitted, it will default to empty string. Used when `is_secret` set to `true`.
        """
        return pulumi.get(self, "secret_value")

    @secret_value.setter
    def secret_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The value of the variable. If omitted, it will default to empty string.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


