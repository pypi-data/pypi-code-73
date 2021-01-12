# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['SSLCertificate']


class SSLCertificate(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        An SslCertificate resource, used for HTTPS load balancing. This resource
        provides a mechanism to upload an SSL key and certificate to
        the load balancer to serve secure connections from the user.

        To get more information about SslCertificate, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/sslCertificates)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/load-balancing/docs/ssl-certificates)

        > **Warning:** All arguments including `certificate` and `private_key` will be stored in the raw
        state as plain-text. [Read more about secrets in state](https://www.pulumi.com/docs/intro/concepts/programming-model/#secrets).

        ## Example Usage
        ### Ssl Certificate Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.compute.SSLCertificate("default",
            name_prefix="my-certificate-",
            description="a description",
            private_key=(lambda path: open(path).read())("path/to/private.key"),
            certificate=(lambda path: open(path).read())("path/to/certificate.crt"))
        ```
        ### Ssl Certificate Target Https Proxies

        ```python
        import pulumi
        import pulumi_gcp as gcp

        # Using with Target HTTPS Proxies
        #
        # SSL certificates cannot be updated after creation. In order to apply
        # the specified configuration, the provider will destroy the existing
        # resource and create a replacement. Example:
        default_ssl_certificate = gcp.compute.SSLCertificate("defaultSSLCertificate",
            name_prefix="my-certificate-",
            private_key=(lambda path: open(path).read())("path/to/private.key"),
            certificate=(lambda path: open(path).read())("path/to/certificate.crt"))
        default_http_health_check = gcp.compute.HttpHealthCheck("defaultHttpHealthCheck",
            request_path="/",
            check_interval_sec=1,
            timeout_sec=1)
        default_backend_service = gcp.compute.BackendService("defaultBackendService",
            port_name="http",
            protocol="HTTP",
            timeout_sec=10,
            health_checks=[default_http_health_check.id])
        default_url_map = gcp.compute.URLMap("defaultURLMap",
            description="a description",
            default_service=default_backend_service.id,
            host_rules=[gcp.compute.URLMapHostRuleArgs(
                hosts=["mysite.com"],
                path_matcher="allpaths",
            )],
            path_matchers=[gcp.compute.URLMapPathMatcherArgs(
                name="allpaths",
                default_service=default_backend_service.id,
                path_rules=[gcp.compute.URLMapPathMatcherPathRuleArgs(
                    paths=["/*"],
                    service=default_backend_service.id,
                )],
            )])
        default_target_https_proxy = gcp.compute.TargetHttpsProxy("defaultTargetHttpsProxy",
            url_map=default_url_map.id,
            ssl_certificates=[default_ssl_certificate.id])
        ```

        ## Import

        SslCertificate can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:compute/sSLCertificate:SSLCertificate default projects/{{project}}/global/sslCertificates/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/sSLCertificate:SSLCertificate default {{project}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/sSLCertificate:SSLCertificate default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate: The certificate in PEM format.
               The certificate chain must be no greater than 5 certs long.
               The chain must include at least one intermediate cert.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the
               specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] private_key: The write-only private key in PEM format.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
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

            if certificate is None and not opts.urn:
                raise TypeError("Missing required property 'certificate'")
            __props__['certificate'] = certificate
            __props__['description'] = description
            __props__['name'] = name
            __props__['name_prefix'] = name_prefix
            if private_key is None and not opts.urn:
                raise TypeError("Missing required property 'private_key'")
            __props__['private_key'] = private_key
            __props__['project'] = project
            __props__['certificate_id'] = None
            __props__['creation_timestamp'] = None
            __props__['self_link'] = None
        super(SSLCertificate, __self__).__init__(
            'gcp:compute/sSLCertificate:SSLCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            certificate: Optional[pulumi.Input[str]] = None,
            certificate_id: Optional[pulumi.Input[int]] = None,
            creation_timestamp: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            name_prefix: Optional[pulumi.Input[str]] = None,
            private_key: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None) -> 'SSLCertificate':
        """
        Get an existing SSLCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate: The certificate in PEM format.
               The certificate chain must be no greater than 5 certs long.
               The chain must include at least one intermediate cert.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[int] certificate_id: The unique identifier for the resource.
        :param pulumi.Input[str] creation_timestamp: Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the
               specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] private_key: The write-only private key in PEM format.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["certificate"] = certificate
        __props__["certificate_id"] = certificate_id
        __props__["creation_timestamp"] = creation_timestamp
        __props__["description"] = description
        __props__["name"] = name
        __props__["name_prefix"] = name_prefix
        __props__["private_key"] = private_key
        __props__["project"] = project
        __props__["self_link"] = self_link
        return SSLCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def certificate(self) -> pulumi.Output[str]:
        """
        The certificate in PEM format.
        The certificate chain must be no greater than 5 certs long.
        The chain must include at least one intermediate cert.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "certificate")

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> pulumi.Output[int]:
        """
        The unique identifier for the resource.
        """
        return pulumi.get(self, "certificate_id")

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
        An optional description of this resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource. Provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and match
        the regular expression `a-z?` which means the
        first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last
        character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[str]:
        """
        Creates a unique name beginning with the
        specified prefix. Conflicts with `name`.
        """
        return pulumi.get(self, "name_prefix")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[str]:
        """
        The write-only private key in PEM format.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "private_key")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

