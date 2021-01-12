# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['ImageSharePermission']


class ImageSharePermission(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 image_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manage image sharing permissions. You can share your custom image to other Alibaba Cloud users. The user can use the shared custom image to create ECS instances or replace the system disk of the instance.

        > **NOTE:** You can only share your own custom images to other Alibaba Cloud users.

        > **NOTE:** Each custom image can be shared with up to 50 Alibaba Cloud accounts. You can submit a ticket to share with more users.

        > **NOTE:** After creating an ECS instance using a shared image, once the custom image owner releases the image sharing relationship or deletes the custom image, the instance cannot initialize the system disk.

        > **NOTE:** Available in 1.68.0+.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.ecs.ImageSharePermission("default",
            account_id="1234567890",
            image_id="m-bp1gxyh***")
        ```
        ## Attributes Reference0

         The following attributes are exported:

        * `id` - ID of the image. It formats as `<image_id>:<account_id>`

        ## Import

        image can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ecs/imageSharePermission:ImageSharePermission default m-uf66yg1q:123456789
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Alibaba Cloud Account ID. It is used to share images.
        :param pulumi.Input[str] image_id: The source image ID.
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

            if account_id is None:
                raise TypeError("Missing required property 'account_id'")
            __props__['account_id'] = account_id
            if image_id is None:
                raise TypeError("Missing required property 'image_id'")
            __props__['image_id'] = image_id
        super(ImageSharePermission, __self__).__init__(
            'alicloud:ecs/imageSharePermission:ImageSharePermission',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            image_id: Optional[pulumi.Input[str]] = None) -> 'ImageSharePermission':
        """
        Get an existing ImageSharePermission resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Alibaba Cloud Account ID. It is used to share images.
        :param pulumi.Input[str] image_id: The source image ID.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["account_id"] = account_id
        __props__["image_id"] = image_id
        return ImageSharePermission(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        Alibaba Cloud Account ID. It is used to share images.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> pulumi.Output[str]:
        """
        The source image ID.
        """
        return pulumi.get(self, "image_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

