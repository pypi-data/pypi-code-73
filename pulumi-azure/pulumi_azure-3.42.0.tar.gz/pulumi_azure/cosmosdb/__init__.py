# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .account import *
from .cassandra_keyspace import *
from .get_account import *
from .gremlin_database import *
from .gremlin_graph import *
from .mongo_collection import *
from .mongo_database import *
from .sql_container import *
from .sql_database import *
from .sql_stored_procedure import *
from .table import *
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
            if typ == "azure:cosmosdb/account:Account":
                return Account(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:cosmosdb/cassandraKeyspace:CassandraKeyspace":
                return CassandraKeyspace(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:cosmosdb/gremlinDatabase:GremlinDatabase":
                return GremlinDatabase(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:cosmosdb/gremlinGraph:GremlinGraph":
                return GremlinGraph(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:cosmosdb/mongoCollection:MongoCollection":
                return MongoCollection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:cosmosdb/mongoDatabase:MongoDatabase":
                return MongoDatabase(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:cosmosdb/sqlContainer:SqlContainer":
                return SqlContainer(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:cosmosdb/sqlDatabase:SqlDatabase":
                return SqlDatabase(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:cosmosdb/sqlStoredProcedure:SqlStoredProcedure":
                return SqlStoredProcedure(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:cosmosdb/table:Table":
                return Table(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure", "cosmosdb/account", _module_instance)
    pulumi.runtime.register_resource_module("azure", "cosmosdb/cassandraKeyspace", _module_instance)
    pulumi.runtime.register_resource_module("azure", "cosmosdb/gremlinDatabase", _module_instance)
    pulumi.runtime.register_resource_module("azure", "cosmosdb/gremlinGraph", _module_instance)
    pulumi.runtime.register_resource_module("azure", "cosmosdb/mongoCollection", _module_instance)
    pulumi.runtime.register_resource_module("azure", "cosmosdb/mongoDatabase", _module_instance)
    pulumi.runtime.register_resource_module("azure", "cosmosdb/sqlContainer", _module_instance)
    pulumi.runtime.register_resource_module("azure", "cosmosdb/sqlDatabase", _module_instance)
    pulumi.runtime.register_resource_module("azure", "cosmosdb/sqlStoredProcedure", _module_instance)
    pulumi.runtime.register_resource_module("azure", "cosmosdb/table", _module_instance)

_register_module()
