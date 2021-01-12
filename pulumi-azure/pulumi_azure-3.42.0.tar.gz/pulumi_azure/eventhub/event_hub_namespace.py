# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['EventHubNamespace']


class EventHubNamespace(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_inflate_enabled: Optional[pulumi.Input[bool]] = None,
                 capacity: Optional[pulumi.Input[int]] = None,
                 dedicated_cluster_id: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['EventHubNamespaceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maximum_throughput_units: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_rulesets: Optional[pulumi.Input[pulumi.InputType['EventHubNamespaceNetworkRulesetsArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone_redundant: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an EventHub Namespace.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_event_hub_namespace = azure.eventhub.EventHubNamespace("exampleEventHubNamespace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="Standard",
            capacity=2,
            tags={
                "environment": "Production",
            })
        ```

        ## Import

        EventHub Namespaces can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:eventhub/eventHubNamespace:EventHubNamespace namespace1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.EventHub/namespaces/namespace1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_inflate_enabled: Is Auto Inflate enabled for the EventHub Namespace?
        :param pulumi.Input[int] capacity: Specifies the Capacity / Throughput Units for a `Standard` SKU namespace. Valid values range from `1` - `20`.
        :param pulumi.Input[str] dedicated_cluster_id: Specifies the ID of the EventHub Dedicated Cluster where this Namespace should created. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['EventHubNamespaceIdentityArgs']] identity: An `identity` block as defined below.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[int] maximum_throughput_units: Specifies the maximum number of throughput units when Auto Inflate is Enabled. Valid values range from `1` - `20`.
        :param pulumi.Input[str] name: Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['EventHubNamespaceNetworkRulesetsArgs']] network_rulesets: A `network_rulesets` block as defined below.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] sku: Defines which tier to use. Valid options are `Basic` and `Standard`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[bool] zone_redundant: Specifies if the EventHub Namespace should be Zone Redundant (created across Availability Zones). Changing this forces a new resource to be created. Defaults to `false`.
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

            __props__['auto_inflate_enabled'] = auto_inflate_enabled
            __props__['capacity'] = capacity
            __props__['dedicated_cluster_id'] = dedicated_cluster_id
            __props__['identity'] = identity
            __props__['location'] = location
            __props__['maximum_throughput_units'] = maximum_throughput_units
            __props__['name'] = name
            __props__['network_rulesets'] = network_rulesets
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__['sku'] = sku
            __props__['tags'] = tags
            __props__['zone_redundant'] = zone_redundant
            __props__['default_primary_connection_string'] = None
            __props__['default_primary_connection_string_alias'] = None
            __props__['default_primary_key'] = None
            __props__['default_secondary_connection_string'] = None
            __props__['default_secondary_connection_string_alias'] = None
            __props__['default_secondary_key'] = None
        super(EventHubNamespace, __self__).__init__(
            'azure:eventhub/eventHubNamespace:EventHubNamespace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auto_inflate_enabled: Optional[pulumi.Input[bool]] = None,
            capacity: Optional[pulumi.Input[int]] = None,
            dedicated_cluster_id: Optional[pulumi.Input[str]] = None,
            default_primary_connection_string: Optional[pulumi.Input[str]] = None,
            default_primary_connection_string_alias: Optional[pulumi.Input[str]] = None,
            default_primary_key: Optional[pulumi.Input[str]] = None,
            default_secondary_connection_string: Optional[pulumi.Input[str]] = None,
            default_secondary_connection_string_alias: Optional[pulumi.Input[str]] = None,
            default_secondary_key: Optional[pulumi.Input[str]] = None,
            identity: Optional[pulumi.Input[pulumi.InputType['EventHubNamespaceIdentityArgs']]] = None,
            location: Optional[pulumi.Input[str]] = None,
            maximum_throughput_units: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_rulesets: Optional[pulumi.Input[pulumi.InputType['EventHubNamespaceNetworkRulesetsArgs']]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            sku: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            zone_redundant: Optional[pulumi.Input[bool]] = None) -> 'EventHubNamespace':
        """
        Get an existing EventHubNamespace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_inflate_enabled: Is Auto Inflate enabled for the EventHub Namespace?
        :param pulumi.Input[int] capacity: Specifies the Capacity / Throughput Units for a `Standard` SKU namespace. Valid values range from `1` - `20`.
        :param pulumi.Input[str] dedicated_cluster_id: Specifies the ID of the EventHub Dedicated Cluster where this Namespace should created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] default_primary_connection_string: The primary connection string for the authorization
               rule `RootManageSharedAccessKey`.
        :param pulumi.Input[str] default_primary_connection_string_alias: The alias of the primary connection string for the authorization
               rule `RootManageSharedAccessKey`, which is generated when disaster recovery is enabled.
        :param pulumi.Input[str] default_primary_key: The primary access key for the authorization rule `RootManageSharedAccessKey`.
        :param pulumi.Input[str] default_secondary_connection_string: The secondary connection string for the
               authorization rule `RootManageSharedAccessKey`.
        :param pulumi.Input[str] default_secondary_connection_string_alias: The alias of the secondary connection string for the
               authorization rule `RootManageSharedAccessKey`, which is generated when disaster recovery is enabled.
        :param pulumi.Input[str] default_secondary_key: The secondary access key for the authorization rule `RootManageSharedAccessKey`.
        :param pulumi.Input[pulumi.InputType['EventHubNamespaceIdentityArgs']] identity: An `identity` block as defined below.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[int] maximum_throughput_units: Specifies the maximum number of throughput units when Auto Inflate is Enabled. Valid values range from `1` - `20`.
        :param pulumi.Input[str] name: Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['EventHubNamespaceNetworkRulesetsArgs']] network_rulesets: A `network_rulesets` block as defined below.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] sku: Defines which tier to use. Valid options are `Basic` and `Standard`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[bool] zone_redundant: Specifies if the EventHub Namespace should be Zone Redundant (created across Availability Zones). Changing this forces a new resource to be created. Defaults to `false`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["auto_inflate_enabled"] = auto_inflate_enabled
        __props__["capacity"] = capacity
        __props__["dedicated_cluster_id"] = dedicated_cluster_id
        __props__["default_primary_connection_string"] = default_primary_connection_string
        __props__["default_primary_connection_string_alias"] = default_primary_connection_string_alias
        __props__["default_primary_key"] = default_primary_key
        __props__["default_secondary_connection_string"] = default_secondary_connection_string
        __props__["default_secondary_connection_string_alias"] = default_secondary_connection_string_alias
        __props__["default_secondary_key"] = default_secondary_key
        __props__["identity"] = identity
        __props__["location"] = location
        __props__["maximum_throughput_units"] = maximum_throughput_units
        __props__["name"] = name
        __props__["network_rulesets"] = network_rulesets
        __props__["resource_group_name"] = resource_group_name
        __props__["sku"] = sku
        __props__["tags"] = tags
        __props__["zone_redundant"] = zone_redundant
        return EventHubNamespace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoInflateEnabled")
    def auto_inflate_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Is Auto Inflate enabled for the EventHub Namespace?
        """
        return pulumi.get(self, "auto_inflate_enabled")

    @property
    @pulumi.getter
    def capacity(self) -> pulumi.Output[Optional[int]]:
        """
        Specifies the Capacity / Throughput Units for a `Standard` SKU namespace. Valid values range from `1` - `20`.
        """
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter(name="dedicatedClusterId")
    def dedicated_cluster_id(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the ID of the EventHub Dedicated Cluster where this Namespace should created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "dedicated_cluster_id")

    @property
    @pulumi.getter(name="defaultPrimaryConnectionString")
    def default_primary_connection_string(self) -> pulumi.Output[str]:
        """
        The primary connection string for the authorization
        rule `RootManageSharedAccessKey`.
        """
        return pulumi.get(self, "default_primary_connection_string")

    @property
    @pulumi.getter(name="defaultPrimaryConnectionStringAlias")
    def default_primary_connection_string_alias(self) -> pulumi.Output[str]:
        """
        The alias of the primary connection string for the authorization
        rule `RootManageSharedAccessKey`, which is generated when disaster recovery is enabled.
        """
        return pulumi.get(self, "default_primary_connection_string_alias")

    @property
    @pulumi.getter(name="defaultPrimaryKey")
    def default_primary_key(self) -> pulumi.Output[str]:
        """
        The primary access key for the authorization rule `RootManageSharedAccessKey`.
        """
        return pulumi.get(self, "default_primary_key")

    @property
    @pulumi.getter(name="defaultSecondaryConnectionString")
    def default_secondary_connection_string(self) -> pulumi.Output[str]:
        """
        The secondary connection string for the
        authorization rule `RootManageSharedAccessKey`.
        """
        return pulumi.get(self, "default_secondary_connection_string")

    @property
    @pulumi.getter(name="defaultSecondaryConnectionStringAlias")
    def default_secondary_connection_string_alias(self) -> pulumi.Output[str]:
        """
        The alias of the secondary connection string for the
        authorization rule `RootManageSharedAccessKey`, which is generated when disaster recovery is enabled.
        """
        return pulumi.get(self, "default_secondary_connection_string_alias")

    @property
    @pulumi.getter(name="defaultSecondaryKey")
    def default_secondary_key(self) -> pulumi.Output[str]:
        """
        The secondary access key for the authorization rule `RootManageSharedAccessKey`.
        """
        return pulumi.get(self, "default_secondary_key")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.EventHubNamespaceIdentity']]:
        """
        An `identity` block as defined below.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maximumThroughputUnits")
    def maximum_throughput_units(self) -> pulumi.Output[int]:
        """
        Specifies the maximum number of throughput units when Auto Inflate is Enabled. Valid values range from `1` - `20`.
        """
        return pulumi.get(self, "maximum_throughput_units")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkRulesets")
    def network_rulesets(self) -> pulumi.Output['outputs.EventHubNamespaceNetworkRulesets']:
        """
        A `network_rulesets` block as defined below.
        """
        return pulumi.get(self, "network_rulesets")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[str]:
        """
        Defines which tier to use. Valid options are `Basic` and `Standard`.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies if the EventHub Namespace should be Zone Redundant (created across Availability Zones). Changing this forces a new resource to be created. Defaults to `false`.
        """
        return pulumi.get(self, "zone_redundant")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

