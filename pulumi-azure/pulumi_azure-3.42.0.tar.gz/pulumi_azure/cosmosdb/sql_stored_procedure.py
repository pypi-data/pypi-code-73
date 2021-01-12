# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['SqlStoredProcedure']


class SqlStoredProcedure(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a SQL Stored Procedure within a Cosmos DB Account SQL Database.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_account = azure.cosmosdb.get_account(name="tfex-cosmosdb-account",
            resource_group_name="tfex-cosmosdb-account-rg")
        example_sql_database = azure.cosmosdb.SqlDatabase("exampleSqlDatabase",
            resource_group_name=example_account.resource_group_name,
            account_name=example_account.name,
            throughput=400)
        example_sql_container = azure.cosmosdb.SqlContainer("exampleSqlContainer",
            resource_group_name=azurerm_cosmosdb_account["example"]["resource_group_name"],
            account_name=azurerm_cosmosdb_account["example"]["name"],
            database_name=example_sql_database.name,
            partition_key_path="/id")
        example_sql_stored_procedure = azure.cosmosdb.SqlStoredProcedure("exampleSqlStoredProcedure",
            resource_group_name=azurerm_cosmosdb_account["example"]["resource_group_name"],
            account_name=azurerm_cosmosdb_account["example"]["name"],
            database_name=example_sql_database.name,
            container_name=example_sql_container.name,
            body="  	function () { var context = getContext(); var response = context.getResponse(); response.setBody('Hello, World'); }\n")
        ```

        ## Import

        CosmosDB SQL Stored Procedures can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:cosmosdb/sqlStoredProcedure:SqlStoredProcedure db1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.DocumentDB/databaseAccounts/account1/sqlDatabases/db1/containers/c1/storedProcedures/sp1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the Cosmos DB Account to create the stored procedure within. Changing this forces a new resource to be created.
        :param pulumi.Input[str] body: The body of the stored procedure.
        :param pulumi.Input[str] container_name: The name of the Cosmos DB SQL Container to create the stored procedure within. Changing this forces a new resource to be created.
        :param pulumi.Input[str] database_name: The name of the Cosmos DB SQL Database to create the stored procedure within. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Cosmos DB SQL Stored Procedure. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Cosmos DB SQL Database is created. Changing this forces a new resource to be created.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__['account_name'] = account_name
            if body is None and not opts.urn:
                raise TypeError("Missing required property 'body'")
            __props__['body'] = body
            if container_name is None and not opts.urn:
                raise TypeError("Missing required property 'container_name'")
            __props__['container_name'] = container_name
            if database_name is None and not opts.urn:
                raise TypeError("Missing required property 'database_name'")
            __props__['database_name'] = database_name
            __props__['name'] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
        super(SqlStoredProcedure, __self__).__init__(
            'azure:cosmosdb/sqlStoredProcedure:SqlStoredProcedure',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_name: Optional[pulumi.Input[str]] = None,
            body: Optional[pulumi.Input[str]] = None,
            container_name: Optional[pulumi.Input[str]] = None,
            database_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None) -> 'SqlStoredProcedure':
        """
        Get an existing SqlStoredProcedure resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the Cosmos DB Account to create the stored procedure within. Changing this forces a new resource to be created.
        :param pulumi.Input[str] body: The body of the stored procedure.
        :param pulumi.Input[str] container_name: The name of the Cosmos DB SQL Container to create the stored procedure within. Changing this forces a new resource to be created.
        :param pulumi.Input[str] database_name: The name of the Cosmos DB SQL Database to create the stored procedure within. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Cosmos DB SQL Stored Procedure. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Cosmos DB SQL Database is created. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["account_name"] = account_name
        __props__["body"] = body
        __props__["container_name"] = container_name
        __props__["database_name"] = database_name
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        return SqlStoredProcedure(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Output[str]:
        """
        The name of the Cosmos DB Account to create the stored procedure within. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter
    def body(self) -> pulumi.Output[str]:
        """
        The body of the stored procedure.
        """
        return pulumi.get(self, "body")

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Output[str]:
        """
        The name of the Cosmos DB SQL Container to create the stored procedure within. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "container_name")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[str]:
        """
        The name of the Cosmos DB SQL Database to create the stored procedure within. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Cosmos DB SQL Stored Procedure. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which the Cosmos DB SQL Database is created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

