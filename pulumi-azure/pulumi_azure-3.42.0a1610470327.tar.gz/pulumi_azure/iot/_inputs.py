# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'IoTHubEndpointArgs',
    'IoTHubFallbackRouteArgs',
    'IoTHubFileUploadArgs',
    'IoTHubIpFilterRuleArgs',
    'IoTHubRouteArgs',
    'IoTHubSharedAccessPolicyArgs',
    'IoTHubSkuArgs',
    'IotHubDpsLinkedHubArgs',
    'IotHubDpsSkuArgs',
    'TimeSeriesInsightsGen2EnvironmentStorageArgs',
    'TimeSeriesInsightsReferenceDataSetKeyPropertyArgs',
]

@pulumi.input_type
class IoTHubEndpointArgs:
    def __init__(__self__, *,
                 connection_string: pulumi.Input[str],
                 name: pulumi.Input[str],
                 type: pulumi.Input[str],
                 batch_frequency_in_seconds: Optional[pulumi.Input[int]] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 encoding: Optional[pulumi.Input[str]] = None,
                 file_name_format: Optional[pulumi.Input[str]] = None,
                 max_chunk_size_in_bytes: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] connection_string: The connection string for the endpoint.
        :param pulumi.Input[str] name: The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  `events`, `operationsMonitoringEvents`, `fileNotifications` and `$default`.
        :param pulumi.Input[str] type: The type of the endpoint. Possible values are `AzureIotHub.StorageContainer`, `AzureIotHub.ServiceBusQueue`, `AzureIotHub.ServiceBusTopic` or `AzureIotHub.EventHub`.
        :param pulumi.Input[int] batch_frequency_in_seconds: Time interval at which blobs are written to storage. Value should be between 60 and 720 seconds. Default value is 300 seconds. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        :param pulumi.Input[str] container_name: The name of storage container in the storage account. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        :param pulumi.Input[str] encoding: Encoding that is used to serialize messages to blobs. Supported values are 'avro' and 'avrodeflate'. Default value is 'avro'. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        :param pulumi.Input[str] file_name_format: File name format for the blob. Default format is ``{iothub}/{partition}/{YYYY}/{MM}/{DD}/{HH}/{mm}``. All parameters are mandatory but can be reordered. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        :param pulumi.Input[int] max_chunk_size_in_bytes: Maximum number of bytes for each blob written to storage. Value should be between 10485760(10MB) and 524288000(500MB). Default value is 314572800(300MB). This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        :param pulumi.Input[str] resource_group_name: The resource group in which the endpoint will be created.
        """
        pulumi.set(__self__, "connection_string", connection_string)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)
        if batch_frequency_in_seconds is not None:
            pulumi.set(__self__, "batch_frequency_in_seconds", batch_frequency_in_seconds)
        if container_name is not None:
            pulumi.set(__self__, "container_name", container_name)
        if encoding is not None:
            pulumi.set(__self__, "encoding", encoding)
        if file_name_format is not None:
            pulumi.set(__self__, "file_name_format", file_name_format)
        if max_chunk_size_in_bytes is not None:
            pulumi.set(__self__, "max_chunk_size_in_bytes", max_chunk_size_in_bytes)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> pulumi.Input[str]:
        """
        The connection string for the endpoint.
        """
        return pulumi.get(self, "connection_string")

    @connection_string.setter
    def connection_string(self, value: pulumi.Input[str]):
        pulumi.set(self, "connection_string", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  `events`, `operationsMonitoringEvents`, `fileNotifications` and `$default`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of the endpoint. Possible values are `AzureIotHub.StorageContainer`, `AzureIotHub.ServiceBusQueue`, `AzureIotHub.ServiceBusTopic` or `AzureIotHub.EventHub`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="batchFrequencyInSeconds")
    def batch_frequency_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        Time interval at which blobs are written to storage. Value should be between 60 and 720 seconds. Default value is 300 seconds. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        """
        return pulumi.get(self, "batch_frequency_in_seconds")

    @batch_frequency_in_seconds.setter
    def batch_frequency_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "batch_frequency_in_seconds", value)

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of storage container in the storage account. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        """
        return pulumi.get(self, "container_name")

    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "container_name", value)

    @property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[str]]:
        """
        Encoding that is used to serialize messages to blobs. Supported values are 'avro' and 'avrodeflate'. Default value is 'avro'. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        """
        return pulumi.get(self, "encoding")

    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encoding", value)

    @property
    @pulumi.getter(name="fileNameFormat")
    def file_name_format(self) -> Optional[pulumi.Input[str]]:
        """
        File name format for the blob. Default format is ``{iothub}/{partition}/{YYYY}/{MM}/{DD}/{HH}/{mm}``. All parameters are mandatory but can be reordered. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        """
        return pulumi.get(self, "file_name_format")

    @file_name_format.setter
    def file_name_format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_name_format", value)

    @property
    @pulumi.getter(name="maxChunkSizeInBytes")
    def max_chunk_size_in_bytes(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum number of bytes for each blob written to storage. Value should be between 10485760(10MB) and 524288000(500MB). Default value is 314572800(300MB). This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        """
        return pulumi.get(self, "max_chunk_size_in_bytes")

    @max_chunk_size_in_bytes.setter
    def max_chunk_size_in_bytes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_chunk_size_in_bytes", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource group in which the endpoint will be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)


@pulumi.input_type
class IoTHubFallbackRouteArgs:
    def __init__(__self__, *,
                 condition: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 endpoint_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 source: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] condition: The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to true by default. For grammar, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language.
        :param pulumi.Input[bool] enabled: Used to specify whether the fallback route is enabled.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] endpoint_names: The endpoints to which messages that satisfy the condition are routed. Currently only 1 endpoint is allowed.
        :param pulumi.Input[str] source: The source that the routing rule is to be applied to, such as `DeviceMessages`. Possible values include: `RoutingSourceInvalid`, `RoutingSourceDeviceMessages`, `RoutingSourceTwinChangeEvents`, `RoutingSourceDeviceLifecycleEvents`, `RoutingSourceDeviceJobLifecycleEvents`.
        """
        if condition is not None:
            pulumi.set(__self__, "condition", condition)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if endpoint_names is not None:
            pulumi.set(__self__, "endpoint_names", endpoint_names)
        if source is not None:
            pulumi.set(__self__, "source", source)

    @property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[str]]:
        """
        The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to true by default. For grammar, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language.
        """
        return pulumi.get(self, "condition")

    @condition.setter
    def condition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "condition", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Used to specify whether the fallback route is enabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="endpointNames")
    def endpoint_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The endpoints to which messages that satisfy the condition are routed. Currently only 1 endpoint is allowed.
        """
        return pulumi.get(self, "endpoint_names")

    @endpoint_names.setter
    def endpoint_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "endpoint_names", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        """
        The source that the routing rule is to be applied to, such as `DeviceMessages`. Possible values include: `RoutingSourceInvalid`, `RoutingSourceDeviceMessages`, `RoutingSourceTwinChangeEvents`, `RoutingSourceDeviceLifecycleEvents`, `RoutingSourceDeviceJobLifecycleEvents`.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)


@pulumi.input_type
class IoTHubFileUploadArgs:
    def __init__(__self__, *,
                 connection_string: pulumi.Input[str],
                 container_name: pulumi.Input[str],
                 default_ttl: Optional[pulumi.Input[str]] = None,
                 lock_duration: Optional[pulumi.Input[str]] = None,
                 max_delivery_count: Optional[pulumi.Input[int]] = None,
                 notifications: Optional[pulumi.Input[bool]] = None,
                 sas_ttl: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] connection_string: The connection string for the Azure Storage account to which files are uploaded.
        :param pulumi.Input[str] container_name: The name of the root container where you upload files. The container need not exist but should be creatable using the connection_string specified.
        :param pulumi.Input[str] default_ttl: The period of time for which a file upload notification message is available to consume before it is expired by the IoT hub, specified as an [ISO 8601 timespan duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). This value must be between 1 minute and 48 hours, and evaluates to 'PT1H' by default.
        :param pulumi.Input[str] lock_duration: The lock duration for the file upload notifications queue, specified as an [ISO 8601 timespan duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). This value must be between 5 and 300 seconds, and evaluates to 'PT1M' by default.
        :param pulumi.Input[int] max_delivery_count: The number of times the IoT hub attempts to deliver a file upload notification message. It evaluates to 10 by default.
        :param pulumi.Input[bool] notifications: Used to specify whether file notifications are sent to IoT Hub on upload. It evaluates to false by default.
        :param pulumi.Input[str] sas_ttl: The period of time for which the SAS URI generated by IoT Hub for file upload is valid, specified as an [ISO 8601 timespan duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). This value must be between 1 minute and 24 hours, and evaluates to 'PT1H' by default.
        """
        pulumi.set(__self__, "connection_string", connection_string)
        pulumi.set(__self__, "container_name", container_name)
        if default_ttl is not None:
            pulumi.set(__self__, "default_ttl", default_ttl)
        if lock_duration is not None:
            pulumi.set(__self__, "lock_duration", lock_duration)
        if max_delivery_count is not None:
            pulumi.set(__self__, "max_delivery_count", max_delivery_count)
        if notifications is not None:
            pulumi.set(__self__, "notifications", notifications)
        if sas_ttl is not None:
            pulumi.set(__self__, "sas_ttl", sas_ttl)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> pulumi.Input[str]:
        """
        The connection string for the Azure Storage account to which files are uploaded.
        """
        return pulumi.get(self, "connection_string")

    @connection_string.setter
    def connection_string(self, value: pulumi.Input[str]):
        pulumi.set(self, "connection_string", value)

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Input[str]:
        """
        The name of the root container where you upload files. The container need not exist but should be creatable using the connection_string specified.
        """
        return pulumi.get(self, "container_name")

    @container_name.setter
    def container_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "container_name", value)

    @property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[pulumi.Input[str]]:
        """
        The period of time for which a file upload notification message is available to consume before it is expired by the IoT hub, specified as an [ISO 8601 timespan duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). This value must be between 1 minute and 48 hours, and evaluates to 'PT1H' by default.
        """
        return pulumi.get(self, "default_ttl")

    @default_ttl.setter
    def default_ttl(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_ttl", value)

    @property
    @pulumi.getter(name="lockDuration")
    def lock_duration(self) -> Optional[pulumi.Input[str]]:
        """
        The lock duration for the file upload notifications queue, specified as an [ISO 8601 timespan duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). This value must be between 5 and 300 seconds, and evaluates to 'PT1M' by default.
        """
        return pulumi.get(self, "lock_duration")

    @lock_duration.setter
    def lock_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lock_duration", value)

    @property
    @pulumi.getter(name="maxDeliveryCount")
    def max_delivery_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of times the IoT hub attempts to deliver a file upload notification message. It evaluates to 10 by default.
        """
        return pulumi.get(self, "max_delivery_count")

    @max_delivery_count.setter
    def max_delivery_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_delivery_count", value)

    @property
    @pulumi.getter
    def notifications(self) -> Optional[pulumi.Input[bool]]:
        """
        Used to specify whether file notifications are sent to IoT Hub on upload. It evaluates to false by default.
        """
        return pulumi.get(self, "notifications")

    @notifications.setter
    def notifications(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "notifications", value)

    @property
    @pulumi.getter(name="sasTtl")
    def sas_ttl(self) -> Optional[pulumi.Input[str]]:
        """
        The period of time for which the SAS URI generated by IoT Hub for file upload is valid, specified as an [ISO 8601 timespan duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). This value must be between 1 minute and 24 hours, and evaluates to 'PT1H' by default.
        """
        return pulumi.get(self, "sas_ttl")

    @sas_ttl.setter
    def sas_ttl(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sas_ttl", value)


@pulumi.input_type
class IoTHubIpFilterRuleArgs:
    def __init__(__self__, *,
                 action: pulumi.Input[str],
                 ip_mask: pulumi.Input[str],
                 name: pulumi.Input[str]):
        """
        :param pulumi.Input[str] action: The desired action for requests captured by this rule. Possible values are  `Accept`, `Reject`
        :param pulumi.Input[str] ip_mask: The IP address range in CIDR notation for the rule.
        :param pulumi.Input[str] name: The name of the filter.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "ip_mask", ip_mask)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input[str]:
        """
        The desired action for requests captured by this rule. Possible values are  `Accept`, `Reject`
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input[str]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter(name="ipMask")
    def ip_mask(self) -> pulumi.Input[str]:
        """
        The IP address range in CIDR notation for the rule.
        """
        return pulumi.get(self, "ip_mask")

    @ip_mask.setter
    def ip_mask(self, value: pulumi.Input[str]):
        pulumi.set(self, "ip_mask", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the filter.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class IoTHubRouteArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 endpoint_names: pulumi.Input[Sequence[pulumi.Input[str]]],
                 name: pulumi.Input[str],
                 source: pulumi.Input[str],
                 condition: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] enabled: Used to specify whether a route is enabled.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] endpoint_names: The list of endpoints to which messages that satisfy the condition are routed.
        :param pulumi.Input[str] name: The name of the route.
        :param pulumi.Input[str] source: The source that the routing rule is to be applied to, such as `DeviceMessages`. Possible values include: `RoutingSourceInvalid`, `RoutingSourceDeviceMessages`, `RoutingSourceTwinChangeEvents`, `RoutingSourceDeviceLifecycleEvents`, `RoutingSourceDeviceJobLifecycleEvents`.
        :param pulumi.Input[str] condition: The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to true by default. For grammar, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language.
        """
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "endpoint_names", endpoint_names)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "source", source)
        if condition is not None:
            pulumi.set(__self__, "condition", condition)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Used to specify whether a route is enabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="endpointNames")
    def endpoint_names(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The list of endpoints to which messages that satisfy the condition are routed.
        """
        return pulumi.get(self, "endpoint_names")

    @endpoint_names.setter
    def endpoint_names(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "endpoint_names", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the route.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input[str]:
        """
        The source that the routing rule is to be applied to, such as `DeviceMessages`. Possible values include: `RoutingSourceInvalid`, `RoutingSourceDeviceMessages`, `RoutingSourceTwinChangeEvents`, `RoutingSourceDeviceLifecycleEvents`, `RoutingSourceDeviceJobLifecycleEvents`.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input[str]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[str]]:
        """
        The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to true by default. For grammar, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language.
        """
        return pulumi.get(self, "condition")

    @condition.setter
    def condition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "condition", value)


@pulumi.input_type
class IoTHubSharedAccessPolicyArgs:
    def __init__(__self__, *,
                 key_name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[str]] = None,
                 primary_key: Optional[pulumi.Input[str]] = None,
                 secondary_key: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] key_name: The name of the shared access policy.
        :param pulumi.Input[str] permissions: The permissions assigned to the shared access policy.
        :param pulumi.Input[str] primary_key: The primary key.
        :param pulumi.Input[str] secondary_key: The secondary key.
        """
        if key_name is not None:
            pulumi.set(__self__, "key_name", key_name)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)
        if primary_key is not None:
            pulumi.set(__self__, "primary_key", primary_key)
        if secondary_key is not None:
            pulumi.set(__self__, "secondary_key", secondary_key)

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the shared access policy.
        """
        return pulumi.get(self, "key_name")

    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_name", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[str]]:
        """
        The permissions assigned to the shared access policy.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[pulumi.Input[str]]:
        """
        The primary key.
        """
        return pulumi.get(self, "primary_key")

    @primary_key.setter
    def primary_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "primary_key", value)

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[pulumi.Input[str]]:
        """
        The secondary key.
        """
        return pulumi.get(self, "secondary_key")

    @secondary_key.setter
    def secondary_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secondary_key", value)


@pulumi.input_type
class IoTHubSkuArgs:
    def __init__(__self__, *,
                 capacity: pulumi.Input[int],
                 name: pulumi.Input[str]):
        """
        :param pulumi.Input[int] capacity: The number of provisioned IoT Hub units.
        :param pulumi.Input[str] name: The name of the sku. Possible values are `B1`, `B2`, `B3`, `F1`, `S1`, `S2`, and `S3`.
        """
        pulumi.set(__self__, "capacity", capacity)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def capacity(self) -> pulumi.Input[int]:
        """
        The number of provisioned IoT Hub units.
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: pulumi.Input[int]):
        pulumi.set(self, "capacity", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the sku. Possible values are `B1`, `B2`, `B3`, `F1`, `S1`, `S2`, and `S3`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class IotHubDpsLinkedHubArgs:
    def __init__(__self__, *,
                 connection_string: pulumi.Input[str],
                 location: pulumi.Input[str],
                 allocation_weight: Optional[pulumi.Input[int]] = None,
                 apply_allocation_policy: Optional[pulumi.Input[bool]] = None,
                 hostname: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] connection_string: The connection string to connect to the IoT Hub. Changing this forces a new resource.
        :param pulumi.Input[str] location: The location of the IoT hub. Changing this forces a new resource.
        :param pulumi.Input[int] allocation_weight: The weight applied to the IoT Hub. Defaults to 0.
        :param pulumi.Input[bool] apply_allocation_policy: Determines whether to apply allocation policies to the IoT Hub. Defaults to false.
        :param pulumi.Input[str] hostname: The IoT Hub hostname.
        """
        pulumi.set(__self__, "connection_string", connection_string)
        pulumi.set(__self__, "location", location)
        if allocation_weight is not None:
            pulumi.set(__self__, "allocation_weight", allocation_weight)
        if apply_allocation_policy is not None:
            pulumi.set(__self__, "apply_allocation_policy", apply_allocation_policy)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> pulumi.Input[str]:
        """
        The connection string to connect to the IoT Hub. Changing this forces a new resource.
        """
        return pulumi.get(self, "connection_string")

    @connection_string.setter
    def connection_string(self, value: pulumi.Input[str]):
        pulumi.set(self, "connection_string", value)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The location of the IoT hub. Changing this forces a new resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="allocationWeight")
    def allocation_weight(self) -> Optional[pulumi.Input[int]]:
        """
        The weight applied to the IoT Hub. Defaults to 0.
        """
        return pulumi.get(self, "allocation_weight")

    @allocation_weight.setter
    def allocation_weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "allocation_weight", value)

    @property
    @pulumi.getter(name="applyAllocationPolicy")
    def apply_allocation_policy(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines whether to apply allocation policies to the IoT Hub. Defaults to false.
        """
        return pulumi.get(self, "apply_allocation_policy")

    @apply_allocation_policy.setter
    def apply_allocation_policy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "apply_allocation_policy", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        """
        The IoT Hub hostname.
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)


@pulumi.input_type
class IotHubDpsSkuArgs:
    def __init__(__self__, *,
                 capacity: pulumi.Input[int],
                 name: pulumi.Input[str]):
        """
        :param pulumi.Input[int] capacity: The number of provisioned IoT Device Provisioning Service units.
        :param pulumi.Input[str] name: The name of the sku. Currently can only be set to `S1`.
        """
        pulumi.set(__self__, "capacity", capacity)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def capacity(self) -> pulumi.Input[int]:
        """
        The number of provisioned IoT Device Provisioning Service units.
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: pulumi.Input[int]):
        pulumi.set(self, "capacity", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the sku. Currently can only be set to `S1`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class TimeSeriesInsightsGen2EnvironmentStorageArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 name: pulumi.Input[str]):
        """
        :param pulumi.Input[str] key: Access key of storage account for Azure IoT Time Series Insights Gen2 Environment
        :param pulumi.Input[str] name: Name of storage account for Azure IoT Time Series Insights Gen2 Environment
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        Access key of storage account for Azure IoT Time Series Insights Gen2 Environment
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of storage account for Azure IoT Time Series Insights Gen2 Environment
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class TimeSeriesInsightsReferenceDataSetKeyPropertyArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 type: pulumi.Input[str]):
        """
        :param pulumi.Input[str] name: The name of the key property.
        :param pulumi.Input[str] type: The data type of the key property. Valid values include `Bool`, `DateTime`, `Double`, `String`.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the key property.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The data type of the key property. Valid values include `Bool`, `DateTime`, `Double`, `String`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


