# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'IoTHubEndpoint',
    'IoTHubFallbackRoute',
    'IoTHubFileUpload',
    'IoTHubIpFilterRule',
    'IoTHubRoute',
    'IoTHubSharedAccessPolicy',
    'IoTHubSku',
    'IotHubDpsLinkedHub',
    'IotHubDpsSku',
    'TimeSeriesInsightsGen2EnvironmentStorage',
    'TimeSeriesInsightsReferenceDataSetKeyProperty',
]

@pulumi.output_type
class IoTHubEndpoint(dict):
    def __init__(__self__, *,
                 connection_string: str,
                 name: str,
                 type: str,
                 batch_frequency_in_seconds: Optional[int] = None,
                 container_name: Optional[str] = None,
                 encoding: Optional[str] = None,
                 file_name_format: Optional[str] = None,
                 max_chunk_size_in_bytes: Optional[int] = None,
                 resource_group_name: Optional[str] = None):
        """
        :param str connection_string: The connection string for the endpoint.
        :param str name: The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  `events`, `operationsMonitoringEvents`, `fileNotifications` and `$default`.
        :param str type: The type of the endpoint. Possible values are `AzureIotHub.StorageContainer`, `AzureIotHub.ServiceBusQueue`, `AzureIotHub.ServiceBusTopic` or `AzureIotHub.EventHub`.
        :param int batch_frequency_in_seconds: Time interval at which blobs are written to storage. Value should be between 60 and 720 seconds. Default value is 300 seconds. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        :param str container_name: The name of storage container in the storage account. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        :param str encoding: Encoding that is used to serialize messages to blobs. Supported values are 'avro' and 'avrodeflate'. Default value is 'avro'. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        :param str file_name_format: File name format for the blob. Default format is ``{iothub}/{partition}/{YYYY}/{MM}/{DD}/{HH}/{mm}``. All parameters are mandatory but can be reordered. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        :param int max_chunk_size_in_bytes: Maximum number of bytes for each blob written to storage. Value should be between 10485760(10MB) and 524288000(500MB). Default value is 314572800(300MB). This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        :param str resource_group_name: The resource group in which the endpoint will be created.
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
    def connection_string(self) -> str:
        """
        The connection string for the endpoint.
        """
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  `events`, `operationsMonitoringEvents`, `fileNotifications` and `$default`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the endpoint. Possible values are `AzureIotHub.StorageContainer`, `AzureIotHub.ServiceBusQueue`, `AzureIotHub.ServiceBusTopic` or `AzureIotHub.EventHub`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="batchFrequencyInSeconds")
    def batch_frequency_in_seconds(self) -> Optional[int]:
        """
        Time interval at which blobs are written to storage. Value should be between 60 and 720 seconds. Default value is 300 seconds. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        """
        return pulumi.get(self, "batch_frequency_in_seconds")

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[str]:
        """
        The name of storage container in the storage account. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        """
        return pulumi.get(self, "container_name")

    @property
    @pulumi.getter
    def encoding(self) -> Optional[str]:
        """
        Encoding that is used to serialize messages to blobs. Supported values are 'avro' and 'avrodeflate'. Default value is 'avro'. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        """
        return pulumi.get(self, "encoding")

    @property
    @pulumi.getter(name="fileNameFormat")
    def file_name_format(self) -> Optional[str]:
        """
        File name format for the blob. Default format is ``{iothub}/{partition}/{YYYY}/{MM}/{DD}/{HH}/{mm}``. All parameters are mandatory but can be reordered. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        """
        return pulumi.get(self, "file_name_format")

    @property
    @pulumi.getter(name="maxChunkSizeInBytes")
    def max_chunk_size_in_bytes(self) -> Optional[int]:
        """
        Maximum number of bytes for each blob written to storage. Value should be between 10485760(10MB) and 524288000(500MB). Default value is 314572800(300MB). This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.
        """
        return pulumi.get(self, "max_chunk_size_in_bytes")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[str]:
        """
        The resource group in which the endpoint will be created.
        """
        return pulumi.get(self, "resource_group_name")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class IoTHubFallbackRoute(dict):
    def __init__(__self__, *,
                 condition: Optional[str] = None,
                 enabled: Optional[bool] = None,
                 endpoint_names: Optional[Sequence[str]] = None,
                 source: Optional[str] = None):
        """
        :param str condition: The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to true by default. For grammar, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language.
        :param bool enabled: Used to specify whether the fallback route is enabled.
        :param Sequence[str] endpoint_names: The endpoints to which messages that satisfy the condition are routed. Currently only 1 endpoint is allowed.
        :param str source: The source that the routing rule is to be applied to, such as `DeviceMessages`. Possible values include: `RoutingSourceInvalid`, `RoutingSourceDeviceMessages`, `RoutingSourceTwinChangeEvents`, `RoutingSourceDeviceLifecycleEvents`, `RoutingSourceDeviceJobLifecycleEvents`.
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
    def condition(self) -> Optional[str]:
        """
        The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to true by default. For grammar, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language.
        """
        return pulumi.get(self, "condition")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        Used to specify whether the fallback route is enabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="endpointNames")
    def endpoint_names(self) -> Optional[Sequence[str]]:
        """
        The endpoints to which messages that satisfy the condition are routed. Currently only 1 endpoint is allowed.
        """
        return pulumi.get(self, "endpoint_names")

    @property
    @pulumi.getter
    def source(self) -> Optional[str]:
        """
        The source that the routing rule is to be applied to, such as `DeviceMessages`. Possible values include: `RoutingSourceInvalid`, `RoutingSourceDeviceMessages`, `RoutingSourceTwinChangeEvents`, `RoutingSourceDeviceLifecycleEvents`, `RoutingSourceDeviceJobLifecycleEvents`.
        """
        return pulumi.get(self, "source")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class IoTHubFileUpload(dict):
    def __init__(__self__, *,
                 connection_string: str,
                 container_name: str,
                 default_ttl: Optional[str] = None,
                 lock_duration: Optional[str] = None,
                 max_delivery_count: Optional[int] = None,
                 notifications: Optional[bool] = None,
                 sas_ttl: Optional[str] = None):
        """
        :param str connection_string: The connection string for the Azure Storage account to which files are uploaded.
        :param str container_name: The name of the root container where you upload files. The container need not exist but should be creatable using the connection_string specified.
        :param str default_ttl: The period of time for which a file upload notification message is available to consume before it is expired by the IoT hub, specified as an [ISO 8601 timespan duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). This value must be between 1 minute and 48 hours, and evaluates to 'PT1H' by default.
        :param str lock_duration: The lock duration for the file upload notifications queue, specified as an [ISO 8601 timespan duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). This value must be between 5 and 300 seconds, and evaluates to 'PT1M' by default.
        :param int max_delivery_count: The number of times the IoT hub attempts to deliver a file upload notification message. It evaluates to 10 by default.
        :param bool notifications: Used to specify whether file notifications are sent to IoT Hub on upload. It evaluates to false by default.
        :param str sas_ttl: The period of time for which the SAS URI generated by IoT Hub for file upload is valid, specified as an [ISO 8601 timespan duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). This value must be between 1 minute and 24 hours, and evaluates to 'PT1H' by default.
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
    def connection_string(self) -> str:
        """
        The connection string for the Azure Storage account to which files are uploaded.
        """
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> str:
        """
        The name of the root container where you upload files. The container need not exist but should be creatable using the connection_string specified.
        """
        return pulumi.get(self, "container_name")

    @property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[str]:
        """
        The period of time for which a file upload notification message is available to consume before it is expired by the IoT hub, specified as an [ISO 8601 timespan duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). This value must be between 1 minute and 48 hours, and evaluates to 'PT1H' by default.
        """
        return pulumi.get(self, "default_ttl")

    @property
    @pulumi.getter(name="lockDuration")
    def lock_duration(self) -> Optional[str]:
        """
        The lock duration for the file upload notifications queue, specified as an [ISO 8601 timespan duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). This value must be between 5 and 300 seconds, and evaluates to 'PT1M' by default.
        """
        return pulumi.get(self, "lock_duration")

    @property
    @pulumi.getter(name="maxDeliveryCount")
    def max_delivery_count(self) -> Optional[int]:
        """
        The number of times the IoT hub attempts to deliver a file upload notification message. It evaluates to 10 by default.
        """
        return pulumi.get(self, "max_delivery_count")

    @property
    @pulumi.getter
    def notifications(self) -> Optional[bool]:
        """
        Used to specify whether file notifications are sent to IoT Hub on upload. It evaluates to false by default.
        """
        return pulumi.get(self, "notifications")

    @property
    @pulumi.getter(name="sasTtl")
    def sas_ttl(self) -> Optional[str]:
        """
        The period of time for which the SAS URI generated by IoT Hub for file upload is valid, specified as an [ISO 8601 timespan duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). This value must be between 1 minute and 24 hours, and evaluates to 'PT1H' by default.
        """
        return pulumi.get(self, "sas_ttl")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class IoTHubIpFilterRule(dict):
    def __init__(__self__, *,
                 action: str,
                 ip_mask: str,
                 name: str):
        """
        :param str action: The desired action for requests captured by this rule. Possible values are  `Accept`, `Reject`
        :param str ip_mask: The IP address range in CIDR notation for the rule.
        :param str name: The name of the filter.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "ip_mask", ip_mask)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def action(self) -> str:
        """
        The desired action for requests captured by this rule. Possible values are  `Accept`, `Reject`
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="ipMask")
    def ip_mask(self) -> str:
        """
        The IP address range in CIDR notation for the rule.
        """
        return pulumi.get(self, "ip_mask")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the filter.
        """
        return pulumi.get(self, "name")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class IoTHubRoute(dict):
    def __init__(__self__, *,
                 enabled: bool,
                 endpoint_names: Sequence[str],
                 name: str,
                 source: str,
                 condition: Optional[str] = None):
        """
        :param bool enabled: Used to specify whether a route is enabled.
        :param Sequence[str] endpoint_names: The list of endpoints to which messages that satisfy the condition are routed.
        :param str name: The name of the route.
        :param str source: The source that the routing rule is to be applied to, such as `DeviceMessages`. Possible values include: `RoutingSourceInvalid`, `RoutingSourceDeviceMessages`, `RoutingSourceTwinChangeEvents`, `RoutingSourceDeviceLifecycleEvents`, `RoutingSourceDeviceJobLifecycleEvents`.
        :param str condition: The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to true by default. For grammar, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language.
        """
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "endpoint_names", endpoint_names)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "source", source)
        if condition is not None:
            pulumi.set(__self__, "condition", condition)

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Used to specify whether a route is enabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="endpointNames")
    def endpoint_names(self) -> Sequence[str]:
        """
        The list of endpoints to which messages that satisfy the condition are routed.
        """
        return pulumi.get(self, "endpoint_names")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the route.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def source(self) -> str:
        """
        The source that the routing rule is to be applied to, such as `DeviceMessages`. Possible values include: `RoutingSourceInvalid`, `RoutingSourceDeviceMessages`, `RoutingSourceTwinChangeEvents`, `RoutingSourceDeviceLifecycleEvents`, `RoutingSourceDeviceJobLifecycleEvents`.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def condition(self) -> Optional[str]:
        """
        The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to true by default. For grammar, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language.
        """
        return pulumi.get(self, "condition")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class IoTHubSharedAccessPolicy(dict):
    def __init__(__self__, *,
                 key_name: Optional[str] = None,
                 permissions: Optional[str] = None,
                 primary_key: Optional[str] = None,
                 secondary_key: Optional[str] = None):
        """
        :param str key_name: The name of the shared access policy.
        :param str permissions: The permissions assigned to the shared access policy.
        :param str primary_key: The primary key.
        :param str secondary_key: The secondary key.
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
    def key_name(self) -> Optional[str]:
        """
        The name of the shared access policy.
        """
        return pulumi.get(self, "key_name")

    @property
    @pulumi.getter
    def permissions(self) -> Optional[str]:
        """
        The permissions assigned to the shared access policy.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[str]:
        """
        The primary key.
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[str]:
        """
        The secondary key.
        """
        return pulumi.get(self, "secondary_key")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class IoTHubSku(dict):
    def __init__(__self__, *,
                 capacity: int,
                 name: str):
        """
        :param int capacity: The number of provisioned IoT Hub units.
        :param str name: The name of the sku. Possible values are `B1`, `B2`, `B3`, `F1`, `S1`, `S2`, and `S3`.
        """
        pulumi.set(__self__, "capacity", capacity)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def capacity(self) -> int:
        """
        The number of provisioned IoT Hub units.
        """
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the sku. Possible values are `B1`, `B2`, `B3`, `F1`, `S1`, `S2`, and `S3`.
        """
        return pulumi.get(self, "name")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class IotHubDpsLinkedHub(dict):
    def __init__(__self__, *,
                 connection_string: str,
                 location: str,
                 allocation_weight: Optional[int] = None,
                 apply_allocation_policy: Optional[bool] = None,
                 hostname: Optional[str] = None):
        """
        :param str connection_string: The connection string to connect to the IoT Hub. Changing this forces a new resource.
        :param str location: The location of the IoT hub. Changing this forces a new resource.
        :param int allocation_weight: The weight applied to the IoT Hub. Defaults to 0.
        :param bool apply_allocation_policy: Determines whether to apply allocation policies to the IoT Hub. Defaults to false.
        :param str hostname: The IoT Hub hostname.
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
    def connection_string(self) -> str:
        """
        The connection string to connect to the IoT Hub. Changing this forces a new resource.
        """
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location of the IoT hub. Changing this forces a new resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="allocationWeight")
    def allocation_weight(self) -> Optional[int]:
        """
        The weight applied to the IoT Hub. Defaults to 0.
        """
        return pulumi.get(self, "allocation_weight")

    @property
    @pulumi.getter(name="applyAllocationPolicy")
    def apply_allocation_policy(self) -> Optional[bool]:
        """
        Determines whether to apply allocation policies to the IoT Hub. Defaults to false.
        """
        return pulumi.get(self, "apply_allocation_policy")

    @property
    @pulumi.getter
    def hostname(self) -> Optional[str]:
        """
        The IoT Hub hostname.
        """
        return pulumi.get(self, "hostname")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class IotHubDpsSku(dict):
    def __init__(__self__, *,
                 capacity: int,
                 name: str):
        """
        :param int capacity: The number of provisioned IoT Device Provisioning Service units.
        :param str name: The name of the sku. Currently can only be set to `S1`.
        """
        pulumi.set(__self__, "capacity", capacity)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def capacity(self) -> int:
        """
        The number of provisioned IoT Device Provisioning Service units.
        """
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the sku. Currently can only be set to `S1`.
        """
        return pulumi.get(self, "name")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TimeSeriesInsightsGen2EnvironmentStorage(dict):
    def __init__(__self__, *,
                 key: str,
                 name: str):
        """
        :param str key: Access key of storage account for Azure IoT Time Series Insights Gen2 Environment
        :param str name: Name of storage account for Azure IoT Time Series Insights Gen2 Environment
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Access key of storage account for Azure IoT Time Series Insights Gen2 Environment
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of storage account for Azure IoT Time Series Insights Gen2 Environment
        """
        return pulumi.get(self, "name")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TimeSeriesInsightsReferenceDataSetKeyProperty(dict):
    def __init__(__self__, *,
                 name: str,
                 type: str):
        """
        :param str name: The name of the key property.
        :param str type: The data type of the key property. Valid values include `Bool`, `DateTime`, `Double`, `String`.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the key property.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The data type of the key property. Valid values include `Bool`, `DateTime`, `Double`, `String`.
        """
        return pulumi.get(self, "type")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


