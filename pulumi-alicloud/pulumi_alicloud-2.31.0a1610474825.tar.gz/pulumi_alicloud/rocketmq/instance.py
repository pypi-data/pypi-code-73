# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Instance']


class Instance(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 remark: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an ONS instance resource.

        For more information about how to use it, see [RocketMQ Instance Management API](https://www.alibabacloud.com/help/doc-detail/106354.html).

        > **NOTE:** The number of instances in the same region cannot exceed 8. At present, the resource does not support region "mq-internet-access" and "ap-southeast-5".

        > **NOTE:** Available in 1.51.0+

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.rocketmq.Instance("example",
            instance_name="tf-example-ons-instance",
            remark="tf-example-ons-instance-remark")
        ```

        ## Import

        ONS INSTANCE can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:rocketmq/instance:Instance instance MQ_INST_1234567890_Baso1234567
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_name: Two instances on a single account in the same region cannot have the same name. The length must be 3 to 64 characters. Chinese characters, English letters digits and hyphen are allowed.
        :param pulumi.Input[str] name: Replaced by `instance_name` after version 1.97.0.
        :param pulumi.Input[str] remark: This attribute is a concise description of instance. The length cannot exceed 128.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
               - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
               - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
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

            __props__['instance_name'] = instance_name
            if name is not None:
                warnings.warn("""Field 'name' has been deprecated from version 1.97.0. Use 'instance_name' instead.""", DeprecationWarning)
                pulumi.log.warn("name is deprecated: Field 'name' has been deprecated from version 1.97.0. Use 'instance_name' instead.")
            __props__['name'] = name
            __props__['remark'] = remark
            __props__['tags'] = tags
            __props__['instance_status'] = None
            __props__['instance_type'] = None
            __props__['release_time'] = None
            __props__['status'] = None
        super(Instance, __self__).__init__(
            'alicloud:rocketmq/instance:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            instance_name: Optional[pulumi.Input[str]] = None,
            instance_status: Optional[pulumi.Input[int]] = None,
            instance_type: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            release_time: Optional[pulumi.Input[str]] = None,
            remark: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'Instance':
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_name: Two instances on a single account in the same region cannot have the same name. The length must be 3 to 64 characters. Chinese characters, English letters digits and hyphen are allowed.
        :param pulumi.Input[int] instance_status: The status of instance. 1 represents the platinum edition instance is in deployment. 2 represents the postpaid edition instance are overdue. 5 represents the postpaid or platinum edition instance is in service. 7 represents the platinum version instance is in upgrade and the service is available.
        :param pulumi.Input[int] instance_type: The edition of instance. 1 represents the postPaid edition, and 2 represents the platinum edition.
        :param pulumi.Input[str] name: Replaced by `instance_name` after version 1.97.0.
        :param pulumi.Input[str] release_time: Platinum edition instance expiration time.
        :param pulumi.Input[str] remark: This attribute is a concise description of instance. The length cannot exceed 128.
        :param pulumi.Input[int] status: The status of instance. 1 represents the platinum edition instance is in deployment. 2 represents the postpaid edition instance are overdue. 5 represents the postpaid or platinum edition instance is in service. 7 represents the platinum version instance is in upgrade and the service is available.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
               - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
               - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["instance_name"] = instance_name
        __props__["instance_status"] = instance_status
        __props__["instance_type"] = instance_type
        __props__["name"] = name
        __props__["release_time"] = release_time
        __props__["remark"] = remark
        __props__["status"] = status
        __props__["tags"] = tags
        return Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Output[str]:
        """
        Two instances on a single account in the same region cannot have the same name. The length must be 3 to 64 characters. Chinese characters, English letters digits and hyphen are allowed.
        """
        return pulumi.get(self, "instance_name")

    @property
    @pulumi.getter(name="instanceStatus")
    def instance_status(self) -> pulumi.Output[int]:
        """
        The status of instance. 1 represents the platinum edition instance is in deployment. 2 represents the postpaid edition instance are overdue. 5 represents the postpaid or platinum edition instance is in service. 7 represents the platinum version instance is in upgrade and the service is available.
        """
        return pulumi.get(self, "instance_status")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[int]:
        """
        The edition of instance. 1 represents the postPaid edition, and 2 represents the platinum edition.
        """
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Replaced by `instance_name` after version 1.97.0.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="releaseTime")
    def release_time(self) -> pulumi.Output[str]:
        """
        Platinum edition instance expiration time.
        """
        return pulumi.get(self, "release_time")

    @property
    @pulumi.getter
    def remark(self) -> pulumi.Output[Optional[str]]:
        """
        This attribute is a concise description of instance. The length cannot exceed 128.
        """
        return pulumi.get(self, "remark")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[int]:
        """
        The status of instance. 1 represents the platinum edition instance is in deployment. 2 represents the postpaid edition instance are overdue. 5 represents the postpaid or platinum edition instance is in service. 7 represents the platinum version instance is in upgrade and the service is available.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
        - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

