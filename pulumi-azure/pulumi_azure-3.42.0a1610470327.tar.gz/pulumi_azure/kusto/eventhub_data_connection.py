# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['EventhubDataConnection']


class EventhubDataConnection(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 compression: Optional[pulumi.Input[str]] = None,
                 consumer_group: Optional[pulumi.Input[str]] = None,
                 data_format: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 eventhub_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mapping_rule_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Kusto (also known as Azure Data Explorer) EventHub Data Connection

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        rg = azure.core.ResourceGroup("rg", location="East US")
        cluster = azure.kusto.Cluster("cluster",
            location=rg.location,
            resource_group_name=rg.name,
            sku=azure.kusto.ClusterSkuArgs(
                name="Standard_D13_v2",
                capacity=2,
            ))
        database = azure.kusto.Database("database",
            resource_group_name=rg.name,
            location=rg.location,
            cluster_name=cluster.name,
            hot_cache_period="P7D",
            soft_delete_period="P31D")
        eventhub_ns = azure.eventhub.EventHubNamespace("eventhubNs",
            location=rg.location,
            resource_group_name=rg.name,
            sku="Standard")
        eventhub = azure.eventhub.EventHub("eventhub",
            namespace_name=eventhub_ns.name,
            resource_group_name=rg.name,
            partition_count=1,
            message_retention=1)
        consumer_group = azure.eventhub.ConsumerGroup("consumerGroup",
            namespace_name=eventhub_ns.name,
            eventhub_name=eventhub.name,
            resource_group_name=rg.name)
        eventhub_connection = azure.kusto.EventhubDataConnection("eventhubConnection",
            resource_group_name=rg.name,
            location=rg.location,
            cluster_name=cluster.name,
            database_name=database.name,
            eventhub_id=azurerm_eventhub["evenhub"]["id"],
            consumer_group=consumer_group.name,
            table_name="my-table",
            mapping_rule_name="my-table-mapping",
            data_format="JSON")
        #(Optional)
        ```

        ## Import

        Kusto EventHub Data Connections can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:kusto/eventhubDataConnection:EventhubDataConnection example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Kusto/Clusters/cluster1/Databases/database1/DataConnections/eventHubConnection1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: Specifies the name of the Kusto Cluster this data connection will be added to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] compression: Specifies compression type for the connection. Allowed values: `GZip` and `None`. Defaults to `None`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] consumer_group: Specifies the EventHub consumer group this data connection will use for ingestion. Changing this forces a new resource to be created.
        :param pulumi.Input[str] data_format: Specifies the data format of the EventHub messages. Allowed values: `AVRO`, `CSV`, `JSON`, `MULTIJSON`, `PSV`, `RAW`, `SCSV`, `SINGLEJSON`, `SOHSV`, `TSV` and `TXT`
        :param pulumi.Input[str] database_name: Specifies the name of the Kusto Database this data connection will be added to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] eventhub_id: Specifies the resource id of the EventHub this data connection will use for ingestion. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: The location where the Kusto Database should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] mapping_rule_name: Specifies the mapping rule used for the message ingestion. Mapping rule must exist before resource is created.
        :param pulumi.Input[str] name: The name of the Kusto EventHub Data Connection to create. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the Resource Group where the Kusto Database should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] table_name: Specifies the target table name used for the message ingestion. Table must exist before resource is created.
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

            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__['cluster_name'] = cluster_name
            __props__['compression'] = compression
            if consumer_group is None and not opts.urn:
                raise TypeError("Missing required property 'consumer_group'")
            __props__['consumer_group'] = consumer_group
            __props__['data_format'] = data_format
            if database_name is None and not opts.urn:
                raise TypeError("Missing required property 'database_name'")
            __props__['database_name'] = database_name
            if eventhub_id is None and not opts.urn:
                raise TypeError("Missing required property 'eventhub_id'")
            __props__['eventhub_id'] = eventhub_id
            __props__['location'] = location
            __props__['mapping_rule_name'] = mapping_rule_name
            __props__['name'] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['table_name'] = table_name
        super(EventhubDataConnection, __self__).__init__(
            'azure:kusto/eventhubDataConnection:EventhubDataConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_name: Optional[pulumi.Input[str]] = None,
            compression: Optional[pulumi.Input[str]] = None,
            consumer_group: Optional[pulumi.Input[str]] = None,
            data_format: Optional[pulumi.Input[str]] = None,
            database_name: Optional[pulumi.Input[str]] = None,
            eventhub_id: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            mapping_rule_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            table_name: Optional[pulumi.Input[str]] = None) -> 'EventhubDataConnection':
        """
        Get an existing EventhubDataConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: Specifies the name of the Kusto Cluster this data connection will be added to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] compression: Specifies compression type for the connection. Allowed values: `GZip` and `None`. Defaults to `None`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] consumer_group: Specifies the EventHub consumer group this data connection will use for ingestion. Changing this forces a new resource to be created.
        :param pulumi.Input[str] data_format: Specifies the data format of the EventHub messages. Allowed values: `AVRO`, `CSV`, `JSON`, `MULTIJSON`, `PSV`, `RAW`, `SCSV`, `SINGLEJSON`, `SOHSV`, `TSV` and `TXT`
        :param pulumi.Input[str] database_name: Specifies the name of the Kusto Database this data connection will be added to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] eventhub_id: Specifies the resource id of the EventHub this data connection will use for ingestion. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: The location where the Kusto Database should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] mapping_rule_name: Specifies the mapping rule used for the message ingestion. Mapping rule must exist before resource is created.
        :param pulumi.Input[str] name: The name of the Kusto EventHub Data Connection to create. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the Resource Group where the Kusto Database should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] table_name: Specifies the target table name used for the message ingestion. Table must exist before resource is created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cluster_name"] = cluster_name
        __props__["compression"] = compression
        __props__["consumer_group"] = consumer_group
        __props__["data_format"] = data_format
        __props__["database_name"] = database_name
        __props__["eventhub_id"] = eventhub_id
        __props__["location"] = location
        __props__["mapping_rule_name"] = mapping_rule_name
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["table_name"] = table_name
        return EventhubDataConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Kusto Cluster this data connection will be added to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter
    def compression(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies compression type for the connection. Allowed values: `GZip` and `None`. Defaults to `None`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "compression")

    @property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> pulumi.Output[str]:
        """
        Specifies the EventHub consumer group this data connection will use for ingestion. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "consumer_group")

    @property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the data format of the EventHub messages. Allowed values: `AVRO`, `CSV`, `JSON`, `MULTIJSON`, `PSV`, `RAW`, `SCSV`, `SINGLEJSON`, `SOHSV`, `TSV` and `TXT`
        """
        return pulumi.get(self, "data_format")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Kusto Database this data connection will be added to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter(name="eventhubId")
    def eventhub_id(self) -> pulumi.Output[str]:
        """
        Specifies the resource id of the EventHub this data connection will use for ingestion. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "eventhub_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location where the Kusto Database should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the mapping rule used for the message ingestion. Mapping rule must exist before resource is created.
        """
        return pulumi.get(self, "mapping_rule_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Kusto EventHub Data Connection to create. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        Specifies the Resource Group where the Kusto Database should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the target table name used for the message ingestion. Table must exist before resource is created.
        """
        return pulumi.get(self, "table_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

