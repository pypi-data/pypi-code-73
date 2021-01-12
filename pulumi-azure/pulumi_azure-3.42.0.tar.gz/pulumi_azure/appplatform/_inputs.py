# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'SpringCloudAppIdentityArgs',
    'SpringCloudAppPersistentDiskArgs',
    'SpringCloudServiceConfigServerGitSettingArgs',
    'SpringCloudServiceConfigServerGitSettingHttpBasicAuthArgs',
    'SpringCloudServiceConfigServerGitSettingRepositoryArgs',
    'SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuthArgs',
    'SpringCloudServiceConfigServerGitSettingRepositorySshAuthArgs',
    'SpringCloudServiceConfigServerGitSettingSshAuthArgs',
    'SpringCloudServiceNetworkArgs',
    'SpringCloudServiceTraceArgs',
]

@pulumi.input_type
class SpringCloudAppIdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 principal_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: Specifies the identity type of the Spring Cloud Application. Possible value is `SystemAssigned`.
        :param pulumi.Input[str] principal_id: The Principal ID for the Service Principal associated with the Managed Service Identity of this Spring Cloud Application.
        :param pulumi.Input[str] tenant_id: The Tenant ID for the Service Principal associated with the Managed Service Identity of this Spring Cloud Application.
        """
        pulumi.set(__self__, "type", type)
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Specifies the identity type of the Spring Cloud Application. Possible value is `SystemAssigned`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Principal ID for the Service Principal associated with the Managed Service Identity of this Spring Cloud Application.
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Tenant ID for the Service Principal associated with the Managed Service Identity of this Spring Cloud Application.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


@pulumi.input_type
class SpringCloudAppPersistentDiskArgs:
    def __init__(__self__, *,
                 size_in_gb: pulumi.Input[int],
                 mount_path: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[int] size_in_gb: Specifies the size of the persistent disk in GB. Possible values are between `0` and `50`.
        :param pulumi.Input[str] mount_path: Specifies the mount path of the persistent disk. Defaults to `/persistent`.
        """
        pulumi.set(__self__, "size_in_gb", size_in_gb)
        if mount_path is not None:
            pulumi.set(__self__, "mount_path", mount_path)

    @property
    @pulumi.getter(name="sizeInGb")
    def size_in_gb(self) -> pulumi.Input[int]:
        """
        Specifies the size of the persistent disk in GB. Possible values are between `0` and `50`.
        """
        return pulumi.get(self, "size_in_gb")

    @size_in_gb.setter
    def size_in_gb(self, value: pulumi.Input[int]):
        pulumi.set(self, "size_in_gb", value)

    @property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the mount path of the persistent disk. Defaults to `/persistent`.
        """
        return pulumi.get(self, "mount_path")

    @mount_path.setter
    def mount_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mount_path", value)


@pulumi.input_type
class SpringCloudServiceConfigServerGitSettingArgs:
    def __init__(__self__, *,
                 uri: pulumi.Input[str],
                 http_basic_auth: Optional[pulumi.Input['SpringCloudServiceConfigServerGitSettingHttpBasicAuthArgs']] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 repositories: Optional[pulumi.Input[Sequence[pulumi.Input['SpringCloudServiceConfigServerGitSettingRepositoryArgs']]]] = None,
                 search_paths: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ssh_auth: Optional[pulumi.Input['SpringCloudServiceConfigServerGitSettingSshAuthArgs']] = None):
        """
        :param pulumi.Input[str] uri: The URI of the default Git repository used as the Config Server back end, should be started with `http://`, `https://`, `git@`, or `ssh://`.
        :param pulumi.Input['SpringCloudServiceConfigServerGitSettingHttpBasicAuthArgs'] http_basic_auth: A `http_basic_auth` block as defined below.
        :param pulumi.Input[str] label: The default label of the Git repository, should be the branch name, tag name, or commit-id of the repository.
        :param pulumi.Input[Sequence[pulumi.Input['SpringCloudServiceConfigServerGitSettingRepositoryArgs']]] repositories: One or more `repository` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] search_paths: An array of strings used to search subdirectories of the Git repository.
        :param pulumi.Input['SpringCloudServiceConfigServerGitSettingSshAuthArgs'] ssh_auth: A `ssh_auth` block as defined below.
        """
        pulumi.set(__self__, "uri", uri)
        if http_basic_auth is not None:
            pulumi.set(__self__, "http_basic_auth", http_basic_auth)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if repositories is not None:
            pulumi.set(__self__, "repositories", repositories)
        if search_paths is not None:
            pulumi.set(__self__, "search_paths", search_paths)
        if ssh_auth is not None:
            pulumi.set(__self__, "ssh_auth", ssh_auth)

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Input[str]:
        """
        The URI of the default Git repository used as the Config Server back end, should be started with `http://`, `https://`, `git@`, or `ssh://`.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "uri", value)

    @property
    @pulumi.getter(name="httpBasicAuth")
    def http_basic_auth(self) -> Optional[pulumi.Input['SpringCloudServiceConfigServerGitSettingHttpBasicAuthArgs']]:
        """
        A `http_basic_auth` block as defined below.
        """
        return pulumi.get(self, "http_basic_auth")

    @http_basic_auth.setter
    def http_basic_auth(self, value: Optional[pulumi.Input['SpringCloudServiceConfigServerGitSettingHttpBasicAuthArgs']]):
        pulumi.set(self, "http_basic_auth", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        The default label of the Git repository, should be the branch name, tag name, or commit-id of the repository.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter
    def repositories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SpringCloudServiceConfigServerGitSettingRepositoryArgs']]]]:
        """
        One or more `repository` blocks as defined below.
        """
        return pulumi.get(self, "repositories")

    @repositories.setter
    def repositories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SpringCloudServiceConfigServerGitSettingRepositoryArgs']]]]):
        pulumi.set(self, "repositories", value)

    @property
    @pulumi.getter(name="searchPaths")
    def search_paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array of strings used to search subdirectories of the Git repository.
        """
        return pulumi.get(self, "search_paths")

    @search_paths.setter
    def search_paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "search_paths", value)

    @property
    @pulumi.getter(name="sshAuth")
    def ssh_auth(self) -> Optional[pulumi.Input['SpringCloudServiceConfigServerGitSettingSshAuthArgs']]:
        """
        A `ssh_auth` block as defined below.
        """
        return pulumi.get(self, "ssh_auth")

    @ssh_auth.setter
    def ssh_auth(self, value: Optional[pulumi.Input['SpringCloudServiceConfigServerGitSettingSshAuthArgs']]):
        pulumi.set(self, "ssh_auth", value)


@pulumi.input_type
class SpringCloudServiceConfigServerGitSettingHttpBasicAuthArgs:
    def __init__(__self__, *,
                 password: pulumi.Input[str],
                 username: pulumi.Input[str]):
        """
        :param pulumi.Input[str] password: The password used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.
        :param pulumi.Input[str] username: The username that's used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.
        """
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        The password used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        The username that's used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)


@pulumi.input_type
class SpringCloudServiceConfigServerGitSettingRepositoryArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 uri: pulumi.Input[str],
                 http_basic_auth: Optional[pulumi.Input['SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuthArgs']] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 patterns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 search_paths: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ssh_auth: Optional[pulumi.Input['SpringCloudServiceConfigServerGitSettingRepositorySshAuthArgs']] = None):
        """
        :param pulumi.Input[str] name: A name to identify on the Git repository, required only if repos exists.
        :param pulumi.Input[str] uri: The URI of the Git repository that's used as the Config Server back end should be started with `http://`, `https://`, `git@`, or `ssh://`.
        :param pulumi.Input['SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuthArgs'] http_basic_auth: A `http_basic_auth` block as defined below.
        :param pulumi.Input[str] label: The default label of the Git repository, should be the branch name, tag name, or commit-id of the repository.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] patterns: An array of strings used to match an application name. For each pattern, use the `{application}/{profile}` format with wildcards.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] search_paths: An array of strings used to search subdirectories of the Git repository.
        :param pulumi.Input['SpringCloudServiceConfigServerGitSettingRepositorySshAuthArgs'] ssh_auth: A `ssh_auth` block as defined below.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "uri", uri)
        if http_basic_auth is not None:
            pulumi.set(__self__, "http_basic_auth", http_basic_auth)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if patterns is not None:
            pulumi.set(__self__, "patterns", patterns)
        if search_paths is not None:
            pulumi.set(__self__, "search_paths", search_paths)
        if ssh_auth is not None:
            pulumi.set(__self__, "ssh_auth", ssh_auth)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        A name to identify on the Git repository, required only if repos exists.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Input[str]:
        """
        The URI of the Git repository that's used as the Config Server back end should be started with `http://`, `https://`, `git@`, or `ssh://`.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "uri", value)

    @property
    @pulumi.getter(name="httpBasicAuth")
    def http_basic_auth(self) -> Optional[pulumi.Input['SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuthArgs']]:
        """
        A `http_basic_auth` block as defined below.
        """
        return pulumi.get(self, "http_basic_auth")

    @http_basic_auth.setter
    def http_basic_auth(self, value: Optional[pulumi.Input['SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuthArgs']]):
        pulumi.set(self, "http_basic_auth", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        The default label of the Git repository, should be the branch name, tag name, or commit-id of the repository.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter
    def patterns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array of strings used to match an application name. For each pattern, use the `{application}/{profile}` format with wildcards.
        """
        return pulumi.get(self, "patterns")

    @patterns.setter
    def patterns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "patterns", value)

    @property
    @pulumi.getter(name="searchPaths")
    def search_paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array of strings used to search subdirectories of the Git repository.
        """
        return pulumi.get(self, "search_paths")

    @search_paths.setter
    def search_paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "search_paths", value)

    @property
    @pulumi.getter(name="sshAuth")
    def ssh_auth(self) -> Optional[pulumi.Input['SpringCloudServiceConfigServerGitSettingRepositorySshAuthArgs']]:
        """
        A `ssh_auth` block as defined below.
        """
        return pulumi.get(self, "ssh_auth")

    @ssh_auth.setter
    def ssh_auth(self, value: Optional[pulumi.Input['SpringCloudServiceConfigServerGitSettingRepositorySshAuthArgs']]):
        pulumi.set(self, "ssh_auth", value)


@pulumi.input_type
class SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuthArgs:
    def __init__(__self__, *,
                 password: pulumi.Input[str],
                 username: pulumi.Input[str]):
        """
        :param pulumi.Input[str] password: The password used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.
        :param pulumi.Input[str] username: The username that's used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.
        """
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        The password used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        The username that's used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)


@pulumi.input_type
class SpringCloudServiceConfigServerGitSettingRepositorySshAuthArgs:
    def __init__(__self__, *,
                 private_key: pulumi.Input[str],
                 host_key: Optional[pulumi.Input[str]] = None,
                 host_key_algorithm: Optional[pulumi.Input[str]] = None,
                 strict_host_key_checking_enabled: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] private_key: The SSH private key to access the Git repository, required when the URI starts with `git@` or `ssh://`.
        :param pulumi.Input[str] host_key: The host key of the Git repository server, should not include the algorithm prefix as covered by `host-key-algorithm`.
        :param pulumi.Input[str] host_key_algorithm: The host key algorithm, should be `ssh-dss`, `ssh-rsa`, `ecdsa-sha2-nistp256`, `ecdsa-sha2-nistp384`, or `ecdsa-sha2-nistp521`. Required only if `host-key` exists.
        :param pulumi.Input[bool] strict_host_key_checking_enabled: Indicates whether the Config Server instance will fail to start if the host_key does not match.
        """
        pulumi.set(__self__, "private_key", private_key)
        if host_key is not None:
            pulumi.set(__self__, "host_key", host_key)
        if host_key_algorithm is not None:
            pulumi.set(__self__, "host_key_algorithm", host_key_algorithm)
        if strict_host_key_checking_enabled is not None:
            pulumi.set(__self__, "strict_host_key_checking_enabled", strict_host_key_checking_enabled)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Input[str]:
        """
        The SSH private key to access the Git repository, required when the URI starts with `git@` or `ssh://`.
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter(name="hostKey")
    def host_key(self) -> Optional[pulumi.Input[str]]:
        """
        The host key of the Git repository server, should not include the algorithm prefix as covered by `host-key-algorithm`.
        """
        return pulumi.get(self, "host_key")

    @host_key.setter
    def host_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_key", value)

    @property
    @pulumi.getter(name="hostKeyAlgorithm")
    def host_key_algorithm(self) -> Optional[pulumi.Input[str]]:
        """
        The host key algorithm, should be `ssh-dss`, `ssh-rsa`, `ecdsa-sha2-nistp256`, `ecdsa-sha2-nistp384`, or `ecdsa-sha2-nistp521`. Required only if `host-key` exists.
        """
        return pulumi.get(self, "host_key_algorithm")

    @host_key_algorithm.setter
    def host_key_algorithm(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_key_algorithm", value)

    @property
    @pulumi.getter(name="strictHostKeyCheckingEnabled")
    def strict_host_key_checking_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the Config Server instance will fail to start if the host_key does not match.
        """
        return pulumi.get(self, "strict_host_key_checking_enabled")

    @strict_host_key_checking_enabled.setter
    def strict_host_key_checking_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "strict_host_key_checking_enabled", value)


@pulumi.input_type
class SpringCloudServiceConfigServerGitSettingSshAuthArgs:
    def __init__(__self__, *,
                 private_key: pulumi.Input[str],
                 host_key: Optional[pulumi.Input[str]] = None,
                 host_key_algorithm: Optional[pulumi.Input[str]] = None,
                 strict_host_key_checking_enabled: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] private_key: The SSH private key to access the Git repository, required when the URI starts with `git@` or `ssh://`.
        :param pulumi.Input[str] host_key: The host key of the Git repository server, should not include the algorithm prefix as covered by `host-key-algorithm`.
        :param pulumi.Input[str] host_key_algorithm: The host key algorithm, should be `ssh-dss`, `ssh-rsa`, `ecdsa-sha2-nistp256`, `ecdsa-sha2-nistp384`, or `ecdsa-sha2-nistp521`. Required only if `host-key` exists.
        :param pulumi.Input[bool] strict_host_key_checking_enabled: Indicates whether the Config Server instance will fail to start if the host_key does not match.
        """
        pulumi.set(__self__, "private_key", private_key)
        if host_key is not None:
            pulumi.set(__self__, "host_key", host_key)
        if host_key_algorithm is not None:
            pulumi.set(__self__, "host_key_algorithm", host_key_algorithm)
        if strict_host_key_checking_enabled is not None:
            pulumi.set(__self__, "strict_host_key_checking_enabled", strict_host_key_checking_enabled)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Input[str]:
        """
        The SSH private key to access the Git repository, required when the URI starts with `git@` or `ssh://`.
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter(name="hostKey")
    def host_key(self) -> Optional[pulumi.Input[str]]:
        """
        The host key of the Git repository server, should not include the algorithm prefix as covered by `host-key-algorithm`.
        """
        return pulumi.get(self, "host_key")

    @host_key.setter
    def host_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_key", value)

    @property
    @pulumi.getter(name="hostKeyAlgorithm")
    def host_key_algorithm(self) -> Optional[pulumi.Input[str]]:
        """
        The host key algorithm, should be `ssh-dss`, `ssh-rsa`, `ecdsa-sha2-nistp256`, `ecdsa-sha2-nistp384`, or `ecdsa-sha2-nistp521`. Required only if `host-key` exists.
        """
        return pulumi.get(self, "host_key_algorithm")

    @host_key_algorithm.setter
    def host_key_algorithm(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_key_algorithm", value)

    @property
    @pulumi.getter(name="strictHostKeyCheckingEnabled")
    def strict_host_key_checking_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the Config Server instance will fail to start if the host_key does not match.
        """
        return pulumi.get(self, "strict_host_key_checking_enabled")

    @strict_host_key_checking_enabled.setter
    def strict_host_key_checking_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "strict_host_key_checking_enabled", value)


@pulumi.input_type
class SpringCloudServiceNetworkArgs:
    def __init__(__self__, *,
                 app_subnet_id: pulumi.Input[str],
                 cidr_ranges: pulumi.Input[Sequence[pulumi.Input[str]]],
                 service_runtime_subnet_id: pulumi.Input[str],
                 app_network_resource_group: Optional[pulumi.Input[str]] = None,
                 service_runtime_network_resource_group: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] app_subnet_id: Specifies the ID of the Subnet which should host the Spring Boot Applications deployed in this Spring Cloud Service. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cidr_ranges: A list of (at least 3) CIDR ranges (at least /16) which are used to host the Spring Cloud infrastructure, which must not overlap with any existing CIDR ranges in the Subnet. Changing this forces a new resource to be created.
        :param pulumi.Input[str] service_runtime_subnet_id: Specifies the ID of the Subnet where the Service Runtime components of the Spring Cloud Service will exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] app_network_resource_group: Specifies the Name of the resource group containing network resources of Azure Spring Cloud Apps. Changing this forces a new resource to be created.
        :param pulumi.Input[str] service_runtime_network_resource_group: Specifies the Name of the resource group containing network resources of Azure Spring Cloud Service Runtime. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "app_subnet_id", app_subnet_id)
        pulumi.set(__self__, "cidr_ranges", cidr_ranges)
        pulumi.set(__self__, "service_runtime_subnet_id", service_runtime_subnet_id)
        if app_network_resource_group is not None:
            pulumi.set(__self__, "app_network_resource_group", app_network_resource_group)
        if service_runtime_network_resource_group is not None:
            pulumi.set(__self__, "service_runtime_network_resource_group", service_runtime_network_resource_group)

    @property
    @pulumi.getter(name="appSubnetId")
    def app_subnet_id(self) -> pulumi.Input[str]:
        """
        Specifies the ID of the Subnet which should host the Spring Boot Applications deployed in this Spring Cloud Service. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "app_subnet_id")

    @app_subnet_id.setter
    def app_subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_subnet_id", value)

    @property
    @pulumi.getter(name="cidrRanges")
    def cidr_ranges(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of (at least 3) CIDR ranges (at least /16) which are used to host the Spring Cloud infrastructure, which must not overlap with any existing CIDR ranges in the Subnet. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "cidr_ranges")

    @cidr_ranges.setter
    def cidr_ranges(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "cidr_ranges", value)

    @property
    @pulumi.getter(name="serviceRuntimeSubnetId")
    def service_runtime_subnet_id(self) -> pulumi.Input[str]:
        """
        Specifies the ID of the Subnet where the Service Runtime components of the Spring Cloud Service will exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "service_runtime_subnet_id")

    @service_runtime_subnet_id.setter
    def service_runtime_subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_runtime_subnet_id", value)

    @property
    @pulumi.getter(name="appNetworkResourceGroup")
    def app_network_resource_group(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Name of the resource group containing network resources of Azure Spring Cloud Apps. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "app_network_resource_group")

    @app_network_resource_group.setter
    def app_network_resource_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_network_resource_group", value)

    @property
    @pulumi.getter(name="serviceRuntimeNetworkResourceGroup")
    def service_runtime_network_resource_group(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Name of the resource group containing network resources of Azure Spring Cloud Service Runtime. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "service_runtime_network_resource_group")

    @service_runtime_network_resource_group.setter
    def service_runtime_network_resource_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_runtime_network_resource_group", value)


@pulumi.input_type
class SpringCloudServiceTraceArgs:
    def __init__(__self__, *,
                 instrumentation_key: pulumi.Input[str]):
        """
        :param pulumi.Input[str] instrumentation_key: The Instrumentation Key used for Application Insights.
        """
        pulumi.set(__self__, "instrumentation_key", instrumentation_key)

    @property
    @pulumi.getter(name="instrumentationKey")
    def instrumentation_key(self) -> pulumi.Input[str]:
        """
        The Instrumentation Key used for Application Insights.
        """
        return pulumi.get(self, "instrumentation_key")

    @instrumentation_key.setter
    def instrumentation_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "instrumentation_key", value)


