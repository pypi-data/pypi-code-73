# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['DdosBgpInstance']


class DdosBgpInstance(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bandwidth: Optional[pulumi.Input[int]] = None,
                 base_bandwidth: Optional[pulumi.Input[int]] = None,
                 ip_count: Optional[pulumi.Input[int]] = None,
                 ip_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 period: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Anti-DDoS Advanced instance resource. "Ddosbgp" is the short term of this product.

        > **NOTE:** The endpoint of bssopenapi used only support "business.aliyuncs.com" at present.

        > **NOTE:** Available in 1.57.0+ .

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        instance = alicloud.ddos.DdosBgpInstance("instance",
            bandwidth=201,
            base_bandwidth=20,
            ip_count=100,
            ip_type="IPv4")
        ```

        ## Import

        Ddosbgp instance can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ddos/ddosBgpInstance:DdosBgpInstance example ddosbgp-abc123456
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] bandwidth: Elastic defend bandwidth of the instance. This value must be larger than the base defend bandwidth. Valid values: 51,91,101,201,301. The unit is Gbps.
        :param pulumi.Input[int] base_bandwidth: Base defend bandwidth of the instance. Valid values: 20. The unit is Gbps. Default to `20`.
        :param pulumi.Input[int] ip_count: IP count of the instance. Valid values: 100.
        :param pulumi.Input[str] ip_type: IP version of the instance. Valid values: IPv4,IPv6.
        :param pulumi.Input[str] name: Name of the instance. This name can have a string of 1 to 63 characters.
        :param pulumi.Input[int] period: The duration that you will buy Ddosbgp instance (in month). Valid values: [1~9], 12, 24, 36. Default to 12. At present, the provider does not support modify "period".
        :param pulumi.Input[str] type: Type of the instance. Valid values: Enterprise,Professional. Default to `Enterprise`
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

            if bandwidth is None:
                raise TypeError("Missing required property 'bandwidth'")
            __props__['bandwidth'] = bandwidth
            __props__['base_bandwidth'] = base_bandwidth
            if ip_count is None:
                raise TypeError("Missing required property 'ip_count'")
            __props__['ip_count'] = ip_count
            if ip_type is None:
                raise TypeError("Missing required property 'ip_type'")
            __props__['ip_type'] = ip_type
            __props__['name'] = name
            __props__['period'] = period
            __props__['type'] = type
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="alicloud:dns/ddosBgpInstance:DdosBgpInstance")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DdosBgpInstance, __self__).__init__(
            'alicloud:ddos/ddosBgpInstance:DdosBgpInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bandwidth: Optional[pulumi.Input[int]] = None,
            base_bandwidth: Optional[pulumi.Input[int]] = None,
            ip_count: Optional[pulumi.Input[int]] = None,
            ip_type: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            period: Optional[pulumi.Input[int]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'DdosBgpInstance':
        """
        Get an existing DdosBgpInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] bandwidth: Elastic defend bandwidth of the instance. This value must be larger than the base defend bandwidth. Valid values: 51,91,101,201,301. The unit is Gbps.
        :param pulumi.Input[int] base_bandwidth: Base defend bandwidth of the instance. Valid values: 20. The unit is Gbps. Default to `20`.
        :param pulumi.Input[int] ip_count: IP count of the instance. Valid values: 100.
        :param pulumi.Input[str] ip_type: IP version of the instance. Valid values: IPv4,IPv6.
        :param pulumi.Input[str] name: Name of the instance. This name can have a string of 1 to 63 characters.
        :param pulumi.Input[int] period: The duration that you will buy Ddosbgp instance (in month). Valid values: [1~9], 12, 24, 36. Default to 12. At present, the provider does not support modify "period".
        :param pulumi.Input[str] type: Type of the instance. Valid values: Enterprise,Professional. Default to `Enterprise`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["bandwidth"] = bandwidth
        __props__["base_bandwidth"] = base_bandwidth
        __props__["ip_count"] = ip_count
        __props__["ip_type"] = ip_type
        __props__["name"] = name
        __props__["period"] = period
        __props__["type"] = type
        return DdosBgpInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bandwidth(self) -> pulumi.Output[int]:
        """
        Elastic defend bandwidth of the instance. This value must be larger than the base defend bandwidth. Valid values: 51,91,101,201,301. The unit is Gbps.
        """
        return pulumi.get(self, "bandwidth")

    @property
    @pulumi.getter(name="baseBandwidth")
    def base_bandwidth(self) -> pulumi.Output[Optional[int]]:
        """
        Base defend bandwidth of the instance. Valid values: 20. The unit is Gbps. Default to `20`.
        """
        return pulumi.get(self, "base_bandwidth")

    @property
    @pulumi.getter(name="ipCount")
    def ip_count(self) -> pulumi.Output[int]:
        """
        IP count of the instance. Valid values: 100.
        """
        return pulumi.get(self, "ip_count")

    @property
    @pulumi.getter(name="ipType")
    def ip_type(self) -> pulumi.Output[str]:
        """
        IP version of the instance. Valid values: IPv4,IPv6.
        """
        return pulumi.get(self, "ip_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the instance. This name can have a string of 1 to 63 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def period(self) -> pulumi.Output[Optional[int]]:
        """
        The duration that you will buy Ddosbgp instance (in month). Valid values: [1~9], 12, 24, 36. Default to 12. At present, the provider does not support modify "period".
        """
        return pulumi.get(self, "period")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        Type of the instance. Valid values: Enterprise,Professional. Default to `Enterprise`
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

