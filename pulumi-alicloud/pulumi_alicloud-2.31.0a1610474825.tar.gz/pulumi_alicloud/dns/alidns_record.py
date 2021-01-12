# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['AlidnsRecord']


class AlidnsRecord(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 lang: Optional[pulumi.Input[str]] = None,
                 line: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 remark: Optional[pulumi.Input[str]] = None,
                 rr: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 user_client_ip: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Alidns Record resource. For information about Alidns Domain Record and how to use it, see [What is Resource Alidns Record](https://www.alibabacloud.com/help/en/doc-detail/29772.htm).

        > **NOTE:** Available in v1.85.0+.

        > **NOTE:** When the site is an international site, the `type` neither supports `REDIRECT_URL` nor `REDIRECT_URL`

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        # Create a new Domain Record
        record = alicloud.dns.AlidnsRecord("record",
            domain_name="domainname",
            remark="Test new alidns record.",
            rr="@",
            status="ENABLE",
            type="A",
            value="192.168.99.99")
        ```

        ## Import

        Alidns Domain Record can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:dns/alidnsRecord:AlidnsRecord example abc123456
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: Name of the domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
        :param pulumi.Input[str] lang: User language.
        :param pulumi.Input[str] line: The resolution line of domain record. When the `type` is `FORWORD_URL`, this parameter must be `default`. Default value is `default`. For checking all resolution lines enumeration please visit [Alibaba Cloud DNS doc](https://www.alibabacloud.com/help/doc-detail/34339.htm) or using dns.getResolutionLines in data source to get the value.
        :param pulumi.Input[int] priority: The priority of domain record. Valid values: `[1-10]`. When the `type` is `MX`, this parameter is required.
        :param pulumi.Input[str] remark: The remark of the domain record.
        :param pulumi.Input[str] rr: Host record for the domain record. This host_record can have at most 253 characters, and each part split with `.` can have at most 63 characters, and must contain only alphanumeric characters or hyphens, such as `-`, `.`, `*`, `@`, and must not begin or end with `-`.
        :param pulumi.Input[str] status: The status of the domain record. Valid values: `ENABLE`,`DISABLE`.
        :param pulumi.Input[int] ttl: The effective time of domain record. Its scope depends on the edition of the cloud resolution. Free is `[600, 86400]`, Basic is `[120, 86400]`, Standard is `[60, 86400]`, Ultimate is `[10, 86400]`, Exclusive is `[1, 86400]`. Default value is `600`.
        :param pulumi.Input[str] type: The type of domain record. Valid values: `A`,`NS`,`MX`,`TXT`,`CNAME`,`SRV`,`AAAA`,`CAA`, `REDIRECT_URL` and `FORWORD_URL`.
        :param pulumi.Input[str] user_client_ip: The IP address of the client.
        :param pulumi.Input[str] value: The value of domain record, When the `type` is `MX`,`NS`,`CNAME`,`SRV`, the server will treat the `value` as a fully qualified domain name, so it's no need to add a `.` at the end.
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

            if domain_name is None:
                raise TypeError("Missing required property 'domain_name'")
            __props__['domain_name'] = domain_name
            __props__['lang'] = lang
            __props__['line'] = line
            __props__['priority'] = priority
            __props__['remark'] = remark
            if rr is None:
                raise TypeError("Missing required property 'rr'")
            __props__['rr'] = rr
            __props__['status'] = status
            __props__['ttl'] = ttl
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['user_client_ip'] = user_client_ip
            if value is None:
                raise TypeError("Missing required property 'value'")
            __props__['value'] = value
        super(AlidnsRecord, __self__).__init__(
            'alicloud:dns/alidnsRecord:AlidnsRecord',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            domain_name: Optional[pulumi.Input[str]] = None,
            lang: Optional[pulumi.Input[str]] = None,
            line: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            remark: Optional[pulumi.Input[str]] = None,
            rr: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            ttl: Optional[pulumi.Input[int]] = None,
            type: Optional[pulumi.Input[str]] = None,
            user_client_ip: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'AlidnsRecord':
        """
        Get an existing AlidnsRecord resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: Name of the domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
        :param pulumi.Input[str] lang: User language.
        :param pulumi.Input[str] line: The resolution line of domain record. When the `type` is `FORWORD_URL`, this parameter must be `default`. Default value is `default`. For checking all resolution lines enumeration please visit [Alibaba Cloud DNS doc](https://www.alibabacloud.com/help/doc-detail/34339.htm) or using dns.getResolutionLines in data source to get the value.
        :param pulumi.Input[int] priority: The priority of domain record. Valid values: `[1-10]`. When the `type` is `MX`, this parameter is required.
        :param pulumi.Input[str] remark: The remark of the domain record.
        :param pulumi.Input[str] rr: Host record for the domain record. This host_record can have at most 253 characters, and each part split with `.` can have at most 63 characters, and must contain only alphanumeric characters or hyphens, such as `-`, `.`, `*`, `@`, and must not begin or end with `-`.
        :param pulumi.Input[str] status: The status of the domain record. Valid values: `ENABLE`,`DISABLE`.
        :param pulumi.Input[int] ttl: The effective time of domain record. Its scope depends on the edition of the cloud resolution. Free is `[600, 86400]`, Basic is `[120, 86400]`, Standard is `[60, 86400]`, Ultimate is `[10, 86400]`, Exclusive is `[1, 86400]`. Default value is `600`.
        :param pulumi.Input[str] type: The type of domain record. Valid values: `A`,`NS`,`MX`,`TXT`,`CNAME`,`SRV`,`AAAA`,`CAA`, `REDIRECT_URL` and `FORWORD_URL`.
        :param pulumi.Input[str] user_client_ip: The IP address of the client.
        :param pulumi.Input[str] value: The value of domain record, When the `type` is `MX`,`NS`,`CNAME`,`SRV`, the server will treat the `value` as a fully qualified domain name, so it's no need to add a `.` at the end.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["domain_name"] = domain_name
        __props__["lang"] = lang
        __props__["line"] = line
        __props__["priority"] = priority
        __props__["remark"] = remark
        __props__["rr"] = rr
        __props__["status"] = status
        __props__["ttl"] = ttl
        __props__["type"] = type
        __props__["user_client_ip"] = user_client_ip
        __props__["value"] = value
        return AlidnsRecord(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        Name of the domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter
    def lang(self) -> pulumi.Output[Optional[str]]:
        """
        User language.
        """
        return pulumi.get(self, "lang")

    @property
    @pulumi.getter
    def line(self) -> pulumi.Output[Optional[str]]:
        """
        The resolution line of domain record. When the `type` is `FORWORD_URL`, this parameter must be `default`. Default value is `default`. For checking all resolution lines enumeration please visit [Alibaba Cloud DNS doc](https://www.alibabacloud.com/help/doc-detail/34339.htm) or using dns.getResolutionLines in data source to get the value.
        """
        return pulumi.get(self, "line")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        The priority of domain record. Valid values: `[1-10]`. When the `type` is `MX`, this parameter is required.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def remark(self) -> pulumi.Output[Optional[str]]:
        """
        The remark of the domain record.
        """
        return pulumi.get(self, "remark")

    @property
    @pulumi.getter
    def rr(self) -> pulumi.Output[str]:
        """
        Host record for the domain record. This host_record can have at most 253 characters, and each part split with `.` can have at most 63 characters, and must contain only alphanumeric characters or hyphens, such as `-`, `.`, `*`, `@`, and must not begin or end with `-`.
        """
        return pulumi.get(self, "rr")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the domain record. Valid values: `ENABLE`,`DISABLE`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[Optional[int]]:
        """
        The effective time of domain record. Its scope depends on the edition of the cloud resolution. Free is `[600, 86400]`, Basic is `[120, 86400]`, Standard is `[60, 86400]`, Ultimate is `[10, 86400]`, Exclusive is `[1, 86400]`. Default value is `600`.
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of domain record. Valid values: `A`,`NS`,`MX`,`TXT`,`CNAME`,`SRV`,`AAAA`,`CAA`, `REDIRECT_URL` and `FORWORD_URL`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userClientIp")
    def user_client_ip(self) -> pulumi.Output[Optional[str]]:
        """
        The IP address of the client.
        """
        return pulumi.get(self, "user_client_ip")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The value of domain record, When the `type` is `MX`,`NS`,`CNAME`,`SRV`, the server will treat the `value` as a fully qualified domain name, so it's no need to add a `.` at the end.
        """
        return pulumi.get(self, "value")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

