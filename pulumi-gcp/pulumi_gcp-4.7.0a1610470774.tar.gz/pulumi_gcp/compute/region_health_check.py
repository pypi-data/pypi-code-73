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

__all__ = ['RegionHealthCheck']


class RegionHealthCheck(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 check_interval_sec: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 grpc_health_check: Optional[pulumi.Input[pulumi.InputType['RegionHealthCheckGrpcHealthCheckArgs']]] = None,
                 healthy_threshold: Optional[pulumi.Input[int]] = None,
                 http2_health_check: Optional[pulumi.Input[pulumi.InputType['RegionHealthCheckHttp2HealthCheckArgs']]] = None,
                 http_health_check: Optional[pulumi.Input[pulumi.InputType['RegionHealthCheckHttpHealthCheckArgs']]] = None,
                 https_health_check: Optional[pulumi.Input[pulumi.InputType['RegionHealthCheckHttpsHealthCheckArgs']]] = None,
                 log_config: Optional[pulumi.Input[pulumi.InputType['RegionHealthCheckLogConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 ssl_health_check: Optional[pulumi.Input[pulumi.InputType['RegionHealthCheckSslHealthCheckArgs']]] = None,
                 tcp_health_check: Optional[pulumi.Input[pulumi.InputType['RegionHealthCheckTcpHealthCheckArgs']]] = None,
                 timeout_sec: Optional[pulumi.Input[int]] = None,
                 unhealthy_threshold: Optional[pulumi.Input[int]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Health Checks determine whether instances are responsive and able to do work.
        They are an important part of a comprehensive load balancing configuration,
        as they enable monitoring instances behind load balancers.

        Health Checks poll instances at a specified interval. Instances that
        do not respond successfully to some number of probes in a row are marked
        as unhealthy. No new connections are sent to unhealthy instances,
        though existing connections will continue. The health check will
        continue to poll unhealthy instances. If an instance later responds
        successfully to some number of consecutive probes, it is marked
        healthy again and can receive new connections.

        To get more information about RegionHealthCheck, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/load-balancing/docs/health-checks)

        ## Example Usage
        ### Region Health Check Tcp

        ```python
        import pulumi
        import pulumi_gcp as gcp

        tcp_region_health_check = gcp.compute.RegionHealthCheck("tcp-region-health-check",
            check_interval_sec=1,
            tcp_health_check=gcp.compute.RegionHealthCheckTcpHealthCheckArgs(
                port=80,
            ),
            timeout_sec=1)
        ```
        ### Region Health Check Tcp Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        tcp_region_health_check = gcp.compute.RegionHealthCheck("tcp-region-health-check",
            check_interval_sec=1,
            description="Health check via tcp",
            healthy_threshold=4,
            tcp_health_check=gcp.compute.RegionHealthCheckTcpHealthCheckArgs(
                port_name="health-check-port",
                port_specification="USE_NAMED_PORT",
                proxy_header="NONE",
                request="ARE YOU HEALTHY?",
                response="I AM HEALTHY",
            ),
            timeout_sec=1,
            unhealthy_threshold=5)
        ```
        ### Region Health Check Ssl

        ```python
        import pulumi
        import pulumi_gcp as gcp

        ssl_region_health_check = gcp.compute.RegionHealthCheck("ssl-region-health-check",
            check_interval_sec=1,
            ssl_health_check=gcp.compute.RegionHealthCheckSslHealthCheckArgs(
                port=443,
            ),
            timeout_sec=1)
        ```
        ### Region Health Check Ssl Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        ssl_region_health_check = gcp.compute.RegionHealthCheck("ssl-region-health-check",
            check_interval_sec=1,
            description="Health check via ssl",
            healthy_threshold=4,
            ssl_health_check=gcp.compute.RegionHealthCheckSslHealthCheckArgs(
                port_name="health-check-port",
                port_specification="USE_NAMED_PORT",
                proxy_header="NONE",
                request="ARE YOU HEALTHY?",
                response="I AM HEALTHY",
            ),
            timeout_sec=1,
            unhealthy_threshold=5)
        ```
        ### Region Health Check Http

        ```python
        import pulumi
        import pulumi_gcp as gcp

        http_region_health_check = gcp.compute.RegionHealthCheck("http-region-health-check",
            check_interval_sec=1,
            http_health_check=gcp.compute.RegionHealthCheckHttpHealthCheckArgs(
                port=80,
            ),
            timeout_sec=1)
        ```
        ### Region Health Check Http Logs

        ```python
        import pulumi
        import pulumi_gcp as gcp

        http_region_health_check = gcp.compute.RegionHealthCheck("http-region-health-check",
            timeout_sec=1,
            check_interval_sec=1,
            http_health_check=gcp.compute.RegionHealthCheckHttpHealthCheckArgs(
                port=80,
            ),
            log_config=gcp.compute.RegionHealthCheckLogConfigArgs(
                enable=True,
            ),
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```
        ### Region Health Check Http Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        http_region_health_check = gcp.compute.RegionHealthCheck("http-region-health-check",
            check_interval_sec=1,
            description="Health check via http",
            healthy_threshold=4,
            http_health_check=gcp.compute.RegionHealthCheckHttpHealthCheckArgs(
                host="1.2.3.4",
                port_name="health-check-port",
                port_specification="USE_NAMED_PORT",
                proxy_header="NONE",
                request_path="/mypath",
                response="I AM HEALTHY",
            ),
            timeout_sec=1,
            unhealthy_threshold=5)
        ```
        ### Region Health Check Https

        ```python
        import pulumi
        import pulumi_gcp as gcp

        https_region_health_check = gcp.compute.RegionHealthCheck("https-region-health-check",
            check_interval_sec=1,
            https_health_check=gcp.compute.RegionHealthCheckHttpsHealthCheckArgs(
                port=443,
            ),
            timeout_sec=1)
        ```
        ### Region Health Check Https Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        https_region_health_check = gcp.compute.RegionHealthCheck("https-region-health-check",
            check_interval_sec=1,
            description="Health check via https",
            healthy_threshold=4,
            https_health_check=gcp.compute.RegionHealthCheckHttpsHealthCheckArgs(
                host="1.2.3.4",
                port_name="health-check-port",
                port_specification="USE_NAMED_PORT",
                proxy_header="NONE",
                request_path="/mypath",
                response="I AM HEALTHY",
            ),
            timeout_sec=1,
            unhealthy_threshold=5)
        ```
        ### Region Health Check Http2

        ```python
        import pulumi
        import pulumi_gcp as gcp

        http2_region_health_check = gcp.compute.RegionHealthCheck("http2-region-health-check",
            check_interval_sec=1,
            http2_health_check=gcp.compute.RegionHealthCheckHttp2HealthCheckArgs(
                port=443,
            ),
            timeout_sec=1)
        ```
        ### Region Health Check Http2 Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        http2_region_health_check = gcp.compute.RegionHealthCheck("http2-region-health-check",
            check_interval_sec=1,
            description="Health check via http2",
            healthy_threshold=4,
            http2_health_check=gcp.compute.RegionHealthCheckHttp2HealthCheckArgs(
                host="1.2.3.4",
                port_name="health-check-port",
                port_specification="USE_NAMED_PORT",
                proxy_header="NONE",
                request_path="/mypath",
                response="I AM HEALTHY",
            ),
            timeout_sec=1,
            unhealthy_threshold=5)
        ```
        ### Region Health Check Grpc

        ```python
        import pulumi
        import pulumi_gcp as gcp

        grpc_region_health_check = gcp.compute.RegionHealthCheck("grpc-region-health-check",
            check_interval_sec=1,
            grpc_health_check=gcp.compute.RegionHealthCheckGrpcHealthCheckArgs(
                port=443,
            ),
            timeout_sec=1)
        ```
        ### Region Health Check Grpc Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        grpc_region_health_check = gcp.compute.RegionHealthCheck("grpc-region-health-check",
            check_interval_sec=1,
            grpc_health_check=gcp.compute.RegionHealthCheckGrpcHealthCheckArgs(
                grpc_service_name="testservice",
                port_name="health-check-port",
                port_specification="USE_NAMED_PORT",
            ),
            timeout_sec=1)
        ```

        ## Import

        RegionHealthCheck can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:compute/regionHealthCheck:RegionHealthCheck default projects/{{project}}/regions/{{region}}/healthChecks/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/regionHealthCheck:RegionHealthCheck default {{project}}/{{region}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/regionHealthCheck:RegionHealthCheck default {{region}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/regionHealthCheck:RegionHealthCheck default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] check_interval_sec: How often (in seconds) to send a health check. The default value is 5
               seconds.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when
               you create the resource.
        :param pulumi.Input[pulumi.InputType['RegionHealthCheckGrpcHealthCheckArgs']] grpc_health_check: A nested object resource
               Structure is documented below.
        :param pulumi.Input[int] healthy_threshold: A so-far unhealthy instance will be marked healthy after this many
               consecutive successes. The default value is 2.
        :param pulumi.Input[pulumi.InputType['RegionHealthCheckHttp2HealthCheckArgs']] http2_health_check: A nested object resource
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['RegionHealthCheckHttpHealthCheckArgs']] http_health_check: A nested object resource
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['RegionHealthCheckHttpsHealthCheckArgs']] https_health_check: A nested object resource
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['RegionHealthCheckLogConfigArgs']] log_config: Configure logging on this health check.  Structure is documented below.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035.  Specifically, the name must be 1-63 characters long and
               match the regular expression `a-z?` which means
               the first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the
               last character, which cannot be a dash.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: The Region in which the created health check should reside.
               If it is not provided, the provider region is used.
        :param pulumi.Input[pulumi.InputType['RegionHealthCheckSslHealthCheckArgs']] ssl_health_check: A nested object resource
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['RegionHealthCheckTcpHealthCheckArgs']] tcp_health_check: A nested object resource
               Structure is documented below.
        :param pulumi.Input[int] timeout_sec: How long (in seconds) to wait before claiming failure.
               The default value is 5 seconds.  It is invalid for timeoutSec to have
               greater value than checkIntervalSec.
        :param pulumi.Input[int] unhealthy_threshold: A so-far healthy instance will be marked unhealthy after this many
               consecutive failures. The default value is 2.
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

            __props__['check_interval_sec'] = check_interval_sec
            __props__['description'] = description
            __props__['grpc_health_check'] = grpc_health_check
            __props__['healthy_threshold'] = healthy_threshold
            __props__['http2_health_check'] = http2_health_check
            __props__['http_health_check'] = http_health_check
            __props__['https_health_check'] = https_health_check
            __props__['log_config'] = log_config
            __props__['name'] = name
            __props__['project'] = project
            __props__['region'] = region
            __props__['ssl_health_check'] = ssl_health_check
            __props__['tcp_health_check'] = tcp_health_check
            __props__['timeout_sec'] = timeout_sec
            __props__['unhealthy_threshold'] = unhealthy_threshold
            __props__['creation_timestamp'] = None
            __props__['self_link'] = None
            __props__['type'] = None
        super(RegionHealthCheck, __self__).__init__(
            'gcp:compute/regionHealthCheck:RegionHealthCheck',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            check_interval_sec: Optional[pulumi.Input[int]] = None,
            creation_timestamp: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            grpc_health_check: Optional[pulumi.Input[pulumi.InputType['RegionHealthCheckGrpcHealthCheckArgs']]] = None,
            healthy_threshold: Optional[pulumi.Input[int]] = None,
            http2_health_check: Optional[pulumi.Input[pulumi.InputType['RegionHealthCheckHttp2HealthCheckArgs']]] = None,
            http_health_check: Optional[pulumi.Input[pulumi.InputType['RegionHealthCheckHttpHealthCheckArgs']]] = None,
            https_health_check: Optional[pulumi.Input[pulumi.InputType['RegionHealthCheckHttpsHealthCheckArgs']]] = None,
            log_config: Optional[pulumi.Input[pulumi.InputType['RegionHealthCheckLogConfigArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None,
            ssl_health_check: Optional[pulumi.Input[pulumi.InputType['RegionHealthCheckSslHealthCheckArgs']]] = None,
            tcp_health_check: Optional[pulumi.Input[pulumi.InputType['RegionHealthCheckTcpHealthCheckArgs']]] = None,
            timeout_sec: Optional[pulumi.Input[int]] = None,
            type: Optional[pulumi.Input[str]] = None,
            unhealthy_threshold: Optional[pulumi.Input[int]] = None) -> 'RegionHealthCheck':
        """
        Get an existing RegionHealthCheck resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] check_interval_sec: How often (in seconds) to send a health check. The default value is 5
               seconds.
        :param pulumi.Input[str] creation_timestamp: Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when
               you create the resource.
        :param pulumi.Input[pulumi.InputType['RegionHealthCheckGrpcHealthCheckArgs']] grpc_health_check: A nested object resource
               Structure is documented below.
        :param pulumi.Input[int] healthy_threshold: A so-far unhealthy instance will be marked healthy after this many
               consecutive successes. The default value is 2.
        :param pulumi.Input[pulumi.InputType['RegionHealthCheckHttp2HealthCheckArgs']] http2_health_check: A nested object resource
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['RegionHealthCheckHttpHealthCheckArgs']] http_health_check: A nested object resource
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['RegionHealthCheckHttpsHealthCheckArgs']] https_health_check: A nested object resource
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['RegionHealthCheckLogConfigArgs']] log_config: Configure logging on this health check.  Structure is documented below.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035.  Specifically, the name must be 1-63 characters long and
               match the regular expression `a-z?` which means
               the first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the
               last character, which cannot be a dash.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: The Region in which the created health check should reside.
               If it is not provided, the provider region is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        :param pulumi.Input[pulumi.InputType['RegionHealthCheckSslHealthCheckArgs']] ssl_health_check: A nested object resource
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['RegionHealthCheckTcpHealthCheckArgs']] tcp_health_check: A nested object resource
               Structure is documented below.
        :param pulumi.Input[int] timeout_sec: How long (in seconds) to wait before claiming failure.
               The default value is 5 seconds.  It is invalid for timeoutSec to have
               greater value than checkIntervalSec.
        :param pulumi.Input[str] type: The type of the health check. One of HTTP, HTTP2, HTTPS, TCP, or SSL.
        :param pulumi.Input[int] unhealthy_threshold: A so-far healthy instance will be marked unhealthy after this many
               consecutive failures. The default value is 2.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["check_interval_sec"] = check_interval_sec
        __props__["creation_timestamp"] = creation_timestamp
        __props__["description"] = description
        __props__["grpc_health_check"] = grpc_health_check
        __props__["healthy_threshold"] = healthy_threshold
        __props__["http2_health_check"] = http2_health_check
        __props__["http_health_check"] = http_health_check
        __props__["https_health_check"] = https_health_check
        __props__["log_config"] = log_config
        __props__["name"] = name
        __props__["project"] = project
        __props__["region"] = region
        __props__["self_link"] = self_link
        __props__["ssl_health_check"] = ssl_health_check
        __props__["tcp_health_check"] = tcp_health_check
        __props__["timeout_sec"] = timeout_sec
        __props__["type"] = type
        __props__["unhealthy_threshold"] = unhealthy_threshold
        return RegionHealthCheck(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="checkIntervalSec")
    def check_interval_sec(self) -> pulumi.Output[Optional[int]]:
        """
        How often (in seconds) to send a health check. The default value is 5
        seconds.
        """
        return pulumi.get(self, "check_interval_sec")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional description of this resource. Provide this property when
        you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="grpcHealthCheck")
    def grpc_health_check(self) -> pulumi.Output[Optional['outputs.RegionHealthCheckGrpcHealthCheck']]:
        """
        A nested object resource
        Structure is documented below.
        """
        return pulumi.get(self, "grpc_health_check")

    @property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> pulumi.Output[Optional[int]]:
        """
        A so-far unhealthy instance will be marked healthy after this many
        consecutive successes. The default value is 2.
        """
        return pulumi.get(self, "healthy_threshold")

    @property
    @pulumi.getter(name="http2HealthCheck")
    def http2_health_check(self) -> pulumi.Output[Optional['outputs.RegionHealthCheckHttp2HealthCheck']]:
        """
        A nested object resource
        Structure is documented below.
        """
        return pulumi.get(self, "http2_health_check")

    @property
    @pulumi.getter(name="httpHealthCheck")
    def http_health_check(self) -> pulumi.Output[Optional['outputs.RegionHealthCheckHttpHealthCheck']]:
        """
        A nested object resource
        Structure is documented below.
        """
        return pulumi.get(self, "http_health_check")

    @property
    @pulumi.getter(name="httpsHealthCheck")
    def https_health_check(self) -> pulumi.Output[Optional['outputs.RegionHealthCheckHttpsHealthCheck']]:
        """
        A nested object resource
        Structure is documented below.
        """
        return pulumi.get(self, "https_health_check")

    @property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> pulumi.Output[Optional['outputs.RegionHealthCheckLogConfig']]:
        """
        Configure logging on this health check.  Structure is documented below.
        """
        return pulumi.get(self, "log_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource. Provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035.  Specifically, the name must be 1-63 characters long and
        match the regular expression `a-z?` which means
        the first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the
        last character, which cannot be a dash.
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
        The Region in which the created health check should reside.
        If it is not provided, the provider region is used.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="sslHealthCheck")
    def ssl_health_check(self) -> pulumi.Output[Optional['outputs.RegionHealthCheckSslHealthCheck']]:
        """
        A nested object resource
        Structure is documented below.
        """
        return pulumi.get(self, "ssl_health_check")

    @property
    @pulumi.getter(name="tcpHealthCheck")
    def tcp_health_check(self) -> pulumi.Output[Optional['outputs.RegionHealthCheckTcpHealthCheck']]:
        """
        A nested object resource
        Structure is documented below.
        """
        return pulumi.get(self, "tcp_health_check")

    @property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> pulumi.Output[Optional[int]]:
        """
        How long (in seconds) to wait before claiming failure.
        The default value is 5 seconds.  It is invalid for timeoutSec to have
        greater value than checkIntervalSec.
        """
        return pulumi.get(self, "timeout_sec")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the health check. One of HTTP, HTTP2, HTTPS, TCP, or SSL.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> pulumi.Output[Optional[int]]:
        """
        A so-far healthy instance will be marked unhealthy after this many
        consecutive failures. The default value is 2.
        """
        return pulumi.get(self, "unhealthy_threshold")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

