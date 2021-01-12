# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['ApplicationDeployment']


class ApplicationDeployment(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 package_version: Optional[pulumi.Input[str]] = None,
                 war_url: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Deploys applications on EDAS.

        > **NOTE:** Available in 1.82.0+

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.edas.ApplicationDeployment("default",
            app_id=var["app_id"],
            group_id=var["group_id"],
            package_version=var["package_version"],
            war_url=var["war_url"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_id: The ID of the application that you want to deploy.
        :param pulumi.Input[str] group_id: The ID of the instance group where the application is going to be deployed. Set this parameter to all if you want to deploy the application to all groups.
        :param pulumi.Input[str] package_version: The version of the application that you want to deploy. It must be unique for every application. The length cannot exceed 64 characters. We recommended you to use a timestamp.
        :param pulumi.Input[str] war_url: The address to store the uploaded web application (WAR) package for application deployment. This parameter is required when the deployType parameter is set as url.
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

            if app_id is None:
                raise TypeError("Missing required property 'app_id'")
            __props__['app_id'] = app_id
            if group_id is None:
                raise TypeError("Missing required property 'group_id'")
            __props__['group_id'] = group_id
            __props__['package_version'] = package_version
            if war_url is None:
                raise TypeError("Missing required property 'war_url'")
            __props__['war_url'] = war_url
            __props__['last_package_version'] = None
        super(ApplicationDeployment, __self__).__init__(
            'alicloud:edas/applicationDeployment:ApplicationDeployment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_id: Optional[pulumi.Input[str]] = None,
            group_id: Optional[pulumi.Input[str]] = None,
            last_package_version: Optional[pulumi.Input[str]] = None,
            package_version: Optional[pulumi.Input[str]] = None,
            war_url: Optional[pulumi.Input[str]] = None) -> 'ApplicationDeployment':
        """
        Get an existing ApplicationDeployment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_id: The ID of the application that you want to deploy.
        :param pulumi.Input[str] group_id: The ID of the instance group where the application is going to be deployed. Set this parameter to all if you want to deploy the application to all groups.
        :param pulumi.Input[str] last_package_version: Last package version deployed.
        :param pulumi.Input[str] package_version: The version of the application that you want to deploy. It must be unique for every application. The length cannot exceed 64 characters. We recommended you to use a timestamp.
        :param pulumi.Input[str] war_url: The address to store the uploaded web application (WAR) package for application deployment. This parameter is required when the deployType parameter is set as url.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["app_id"] = app_id
        __props__["group_id"] = group_id
        __props__["last_package_version"] = last_package_version
        __props__["package_version"] = package_version
        __props__["war_url"] = war_url
        return ApplicationDeployment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[str]:
        """
        The ID of the application that you want to deploy.
        """
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[str]:
        """
        The ID of the instance group where the application is going to be deployed. Set this parameter to all if you want to deploy the application to all groups.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="lastPackageVersion")
    def last_package_version(self) -> pulumi.Output[str]:
        """
        Last package version deployed.
        """
        return pulumi.get(self, "last_package_version")

    @property
    @pulumi.getter(name="packageVersion")
    def package_version(self) -> pulumi.Output[Optional[str]]:
        """
        The version of the application that you want to deploy. It must be unique for every application. The length cannot exceed 64 characters. We recommended you to use a timestamp.
        """
        return pulumi.get(self, "package_version")

    @property
    @pulumi.getter(name="warUrl")
    def war_url(self) -> pulumi.Output[str]:
        """
        The address to store the uploaded web application (WAR) package for application deployment. This parameter is required when the deployType parameter is set as url.
        """
        return pulumi.get(self, "war_url")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

