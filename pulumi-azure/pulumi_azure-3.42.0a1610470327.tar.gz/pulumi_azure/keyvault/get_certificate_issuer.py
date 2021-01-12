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
    'GetCertificateIssuerResult',
    'AwaitableGetCertificateIssuerResult',
    'get_certificate_issuer',
]

@pulumi.output_type
class GetCertificateIssuerResult:
    """
    A collection of values returned by getCertificateIssuer.
    """
    def __init__(__self__, account_id=None, admins=None, id=None, key_vault_id=None, name=None, org_id=None, provider_name=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if admins and not isinstance(admins, list):
            raise TypeError("Expected argument 'admins' to be a list")
        pulumi.set(__self__, "admins", admins)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_vault_id and not isinstance(key_vault_id, str):
            raise TypeError("Expected argument 'key_vault_id' to be a str")
        pulumi.set(__self__, "key_vault_id", key_vault_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if org_id and not isinstance(org_id, str):
            raise TypeError("Expected argument 'org_id' to be a str")
        pulumi.set(__self__, "org_id", org_id)
        if provider_name and not isinstance(provider_name, str):
            raise TypeError("Expected argument 'provider_name' to be a str")
        pulumi.set(__self__, "provider_name", provider_name)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        """
        The account number with the third-party Certificate Issuer.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def admins(self) -> Sequence['outputs.GetCertificateIssuerAdminResult']:
        """
        A list of `admin` blocks as defined below.
        """
        return pulumi.get(self, "admins")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> str:
        return pulumi.get(self, "key_vault_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> str:
        """
        The organization ID with the third-party Certificate Issuer.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> str:
        """
        The name of the third-party Certificate Issuer.
        """
        return pulumi.get(self, "provider_name")


class AwaitableGetCertificateIssuerResult(GetCertificateIssuerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCertificateIssuerResult(
            account_id=self.account_id,
            admins=self.admins,
            id=self.id,
            key_vault_id=self.key_vault_id,
            name=self.name,
            org_id=self.org_id,
            provider_name=self.provider_name)


def get_certificate_issuer(key_vault_id: Optional[str] = None,
                           name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCertificateIssuerResult:
    """
    Use this data source to access information about an existing Key Vault Certificate Issuer.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example_key_vault = azure.keyvault.get_key_vault(name="mykeyvault",
        resource_group_name="some-resource-group")
    example_certificate_issuer = azure.keyvault.get_certificate_issuer(name="existing",
        key_vault_id=example_key_vault.id)
    pulumi.export("id", example_certificate_issuer.id)
    ```


    :param str key_vault_id: The ID of the Key Vault in which to locate the Certificate Issuer.
    :param str name: The name of the Key Vault Certificate Issuer.
    """
    __args__ = dict()
    __args__['keyVaultId'] = key_vault_id
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:keyvault/getCertificateIssuer:getCertificateIssuer', __args__, opts=opts, typ=GetCertificateIssuerResult).value

    return AwaitableGetCertificateIssuerResult(
        account_id=__ret__.account_id,
        admins=__ret__.admins,
        id=__ret__.id,
        key_vault_id=__ret__.key_vault_id,
        name=__ret__.name,
        org_id=__ret__.org_id,
        provider_name=__ret__.provider_name)
