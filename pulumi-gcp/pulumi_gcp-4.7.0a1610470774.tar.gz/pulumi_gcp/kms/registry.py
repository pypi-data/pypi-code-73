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

__all__ = ['Registry']

warnings.warn("""gcp.kms.Registry has been deprecated in favor of gcp.iot.Registry""", DeprecationWarning)


class Registry(pulumi.CustomResource):
    warnings.warn("""gcp.kms.Registry has been deprecated in favor of gcp.iot.Registry""", DeprecationWarning)

    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credentials: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RegistryCredentialArgs']]]]] = None,
                 event_notification_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RegistryEventNotificationConfigItemArgs']]]]] = None,
                 http_config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 log_level: Optional[pulumi.Input[str]] = None,
                 mqtt_config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 state_notification_config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        A Google Cloud IoT Core device registry.

        To get more information about DeviceRegistry, see:

        * [API documentation](https://cloud.google.com/iot/docs/reference/cloudiot/rest/)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/iot/docs/)

        ## Example Usage
        ### Cloudiot Device Registry Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        test_registry = gcp.iot.Registry("test-registry")
        ```
        ### Cloudiot Device Registry Single Event Notification Configs

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default_telemetry = gcp.pubsub.Topic("default-telemetry")
        test_registry = gcp.iot.Registry("test-registry", event_notification_configs=[gcp.iot.RegistryEventNotificationConfigItemArgs(
            pubsub_topic_name=default_telemetry.id,
            subfolder_matches="",
        )])
        ```
        ### Cloudiot Device Registry Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default_devicestatus = gcp.pubsub.Topic("default-devicestatus")
        default_telemetry = gcp.pubsub.Topic("default-telemetry")
        additional_telemetry = gcp.pubsub.Topic("additional-telemetry")
        test_registry = gcp.iot.Registry("test-registry",
            event_notification_configs=[
                gcp.iot.RegistryEventNotificationConfigItemArgs(
                    pubsub_topic_name=additional_telemetry.id,
                    subfolder_matches="test/path",
                ),
                gcp.iot.RegistryEventNotificationConfigItemArgs(
                    pubsub_topic_name=default_telemetry.id,
                    subfolder_matches="",
                ),
            ],
            state_notification_config={
                "pubsub_topic_name": default_devicestatus.id,
            },
            mqtt_config={
                "mqtt_enabled_state": "MQTT_ENABLED",
            },
            http_config={
                "http_enabled_state": "HTTP_ENABLED",
            },
            log_level="INFO",
            credentials=[gcp.iot.RegistryCredentialArgs(
                public_key_certificate={
                    "format": "X509_CERTIFICATE_PEM",
                    "certificate": (lambda path: open(path).read())("test-fixtures/rsa_cert.pem"),
                },
            )])
        ```

        ## Import

        DeviceRegistry can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:kms/registry:Registry default {{project}}/locations/{{region}}/registries/{{name}}
        ```

        ```sh
         $ pulumi import gcp:kms/registry:Registry default {{project}}/{{region}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:kms/registry:Registry default {{region}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:kms/registry:Registry default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RegistryCredentialArgs']]]] credentials: List of public key certificates to authenticate devices.
               The structure is documented below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RegistryEventNotificationConfigItemArgs']]]] event_notification_configs: List of configurations for event notifications, such as PubSub topics
               to publish device events to.
               Structure is documented below.
        :param pulumi.Input[Mapping[str, Any]] http_config: Activate or deactivate HTTP.
               The structure is documented below.
        :param pulumi.Input[str] log_level: The default logging verbosity for activity from devices in this
               registry. Specifies which events should be written to logs. For
               example, if the LogLevel is ERROR, only events that terminate in
               errors will be logged. LogLevel is inclusive; enabling INFO logging
               will also enable ERROR logging.
               Default value is `NONE`.
               Possible values are `NONE`, `ERROR`, `INFO`, and `DEBUG`.
        :param pulumi.Input[Mapping[str, Any]] mqtt_config: Activate or deactivate MQTT.
               The structure is documented below.
        :param pulumi.Input[str] name: A unique name for the resource, required by device registry.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: The region in which the created registry should reside.
               If it is not provided, the provider region is used.
        :param pulumi.Input[Mapping[str, Any]] state_notification_config: A PubSub topic to publish device state updates.
               The structure is documented below.
        """
        pulumi.log.warn("Registry is deprecated: gcp.kms.Registry has been deprecated in favor of gcp.iot.Registry")
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

            __props__['credentials'] = credentials
            __props__['event_notification_configs'] = event_notification_configs
            __props__['http_config'] = http_config
            __props__['log_level'] = log_level
            __props__['mqtt_config'] = mqtt_config
            __props__['name'] = name
            __props__['project'] = project
            __props__['region'] = region
            __props__['state_notification_config'] = state_notification_config
        super(Registry, __self__).__init__(
            'gcp:kms/registry:Registry',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            credentials: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RegistryCredentialArgs']]]]] = None,
            event_notification_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RegistryEventNotificationConfigItemArgs']]]]] = None,
            http_config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            log_level: Optional[pulumi.Input[str]] = None,
            mqtt_config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            state_notification_config: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'Registry':
        """
        Get an existing Registry resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RegistryCredentialArgs']]]] credentials: List of public key certificates to authenticate devices.
               The structure is documented below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RegistryEventNotificationConfigItemArgs']]]] event_notification_configs: List of configurations for event notifications, such as PubSub topics
               to publish device events to.
               Structure is documented below.
        :param pulumi.Input[Mapping[str, Any]] http_config: Activate or deactivate HTTP.
               The structure is documented below.
        :param pulumi.Input[str] log_level: The default logging verbosity for activity from devices in this
               registry. Specifies which events should be written to logs. For
               example, if the LogLevel is ERROR, only events that terminate in
               errors will be logged. LogLevel is inclusive; enabling INFO logging
               will also enable ERROR logging.
               Default value is `NONE`.
               Possible values are `NONE`, `ERROR`, `INFO`, and `DEBUG`.
        :param pulumi.Input[Mapping[str, Any]] mqtt_config: Activate or deactivate MQTT.
               The structure is documented below.
        :param pulumi.Input[str] name: A unique name for the resource, required by device registry.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: The region in which the created registry should reside.
               If it is not provided, the provider region is used.
        :param pulumi.Input[Mapping[str, Any]] state_notification_config: A PubSub topic to publish device state updates.
               The structure is documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["credentials"] = credentials
        __props__["event_notification_configs"] = event_notification_configs
        __props__["http_config"] = http_config
        __props__["log_level"] = log_level
        __props__["mqtt_config"] = mqtt_config
        __props__["name"] = name
        __props__["project"] = project
        __props__["region"] = region
        __props__["state_notification_config"] = state_notification_config
        return Registry(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Optional[Sequence['outputs.RegistryCredential']]]:
        """
        List of public key certificates to authenticate devices.
        The structure is documented below.
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter(name="eventNotificationConfigs")
    def event_notification_configs(self) -> pulumi.Output[Sequence['outputs.RegistryEventNotificationConfigItem']]:
        """
        List of configurations for event notifications, such as PubSub topics
        to publish device events to.
        Structure is documented below.
        """
        return pulumi.get(self, "event_notification_configs")

    @property
    @pulumi.getter(name="httpConfig")
    def http_config(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Activate or deactivate HTTP.
        The structure is documented below.
        """
        return pulumi.get(self, "http_config")

    @property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> pulumi.Output[Optional[str]]:
        """
        The default logging verbosity for activity from devices in this
        registry. Specifies which events should be written to logs. For
        example, if the LogLevel is ERROR, only events that terminate in
        errors will be logged. LogLevel is inclusive; enabling INFO logging
        will also enable ERROR logging.
        Default value is `NONE`.
        Possible values are `NONE`, `ERROR`, `INFO`, and `DEBUG`.
        """
        return pulumi.get(self, "log_level")

    @property
    @pulumi.getter(name="mqttConfig")
    def mqtt_config(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Activate or deactivate MQTT.
        The structure is documented below.
        """
        return pulumi.get(self, "mqtt_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique name for the resource, required by device registry.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which the created registry should reside.
        If it is not provided, the provider region is used.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="stateNotificationConfig")
    def state_notification_config(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        A PubSub topic to publish device state updates.
        The structure is documented below.
        """
        return pulumi.get(self, "state_notification_config")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

