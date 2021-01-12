# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .active_directory_administrator import *
from .database import *
from .elastic_pool import *
from .failover_group import *
from .firewall_rule import *
from .get_database import *
from .get_server import *
from .sql_server import *
from .virtual_network_rule import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "azure:sql/activeDirectoryAdministrator:ActiveDirectoryAdministrator":
                return ActiveDirectoryAdministrator(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:sql/database:Database":
                return Database(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:sql/elasticPool:ElasticPool":
                return ElasticPool(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:sql/failoverGroup:FailoverGroup":
                return FailoverGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:sql/firewallRule:FirewallRule":
                return FirewallRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:sql/sqlServer:SqlServer":
                return SqlServer(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:sql/virtualNetworkRule:VirtualNetworkRule":
                return VirtualNetworkRule(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure", "sql/activeDirectoryAdministrator", _module_instance)
    pulumi.runtime.register_resource_module("azure", "sql/database", _module_instance)
    pulumi.runtime.register_resource_module("azure", "sql/elasticPool", _module_instance)
    pulumi.runtime.register_resource_module("azure", "sql/failoverGroup", _module_instance)
    pulumi.runtime.register_resource_module("azure", "sql/firewallRule", _module_instance)
    pulumi.runtime.register_resource_module("azure", "sql/sqlServer", _module_instance)
    pulumi.runtime.register_resource_module("azure", "sql/virtualNetworkRule", _module_instance)

_register_module()
