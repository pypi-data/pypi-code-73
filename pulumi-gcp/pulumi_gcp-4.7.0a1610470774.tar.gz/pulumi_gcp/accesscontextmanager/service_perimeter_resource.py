# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['ServicePerimeterResource']


class ServicePerimeterResource(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 perimeter_name: Optional[pulumi.Input[str]] = None,
                 resource: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Allows configuring a single GCP resource that should be inside of a service perimeter.
        This resource is intended to be used in cases where it is not possible to compile a full list
        of projects to include in a `accesscontextmanager.ServicePerimeter` resource,
        to enable them to be added separately.

        > **Note:** If this resource is used alongside a `accesscontextmanager.ServicePerimeter` resource,
        the service perimeter resource must have a `lifecycle` block with `ignore_changes = [status[0].resources]` so
        they don't fight over which resources should be in the policy.

        To get more information about ServicePerimeterResource, see:

        * [API documentation](https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters)
        * How-to Guides
            * [Service Perimeter Quickstart](https://cloud.google.com/vpc-service-controls/docs/quickstart)

        > **Warning:** If you are using User ADCs (Application Default Credentials) with this resource,
        you must specify a `billing_project` and set `user_project_override` to true
        in the provider configuration. Otherwise the ACM API will return a 403 error.
        Your account must have the `serviceusage.services.use` permission on the
        `billing_project` you defined.

        ## Example Usage
        ### Access Context Manager Service Perimeter Resource Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        access_policy = gcp.accesscontextmanager.AccessPolicy("access-policy",
            parent="organizations/123456789",
            title="my policy")
        service_perimeter_resource_service_perimeter = gcp.accesscontextmanager.ServicePerimeter("service-perimeter-resourceServicePerimeter",
            parent=access_policy.name.apply(lambda name: f"accessPolicies/{name}"),
            title="restrict_all",
            status=gcp.accesscontextmanager.ServicePerimeterStatusArgs(
                restricted_services=["storage.googleapis.com"],
            ))
        service_perimeter_resource_service_perimeter_resource = gcp.accesscontextmanager.ServicePerimeterResource("service-perimeter-resourceServicePerimeterResource",
            perimeter_name=service_perimeter_resource_service_perimeter.name,
            resource="projects/987654321")
        ```

        ## Import

        ServicePerimeterResource can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:accesscontextmanager/servicePerimeterResource:ServicePerimeterResource default {{perimeter_name}}/{{resource}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] perimeter_name: The name of the Service Perimeter to add this resource to.
        :param pulumi.Input[str] resource: A GCP resource that is inside of the service perimeter.
               Currently only projects are allowed.
               Format: projects/{project_number}
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

            if perimeter_name is None and not opts.urn:
                raise TypeError("Missing required property 'perimeter_name'")
            __props__['perimeter_name'] = perimeter_name
            if resource is None and not opts.urn:
                raise TypeError("Missing required property 'resource'")
            __props__['resource'] = resource
        super(ServicePerimeterResource, __self__).__init__(
            'gcp:accesscontextmanager/servicePerimeterResource:ServicePerimeterResource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            perimeter_name: Optional[pulumi.Input[str]] = None,
            resource: Optional[pulumi.Input[str]] = None) -> 'ServicePerimeterResource':
        """
        Get an existing ServicePerimeterResource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] perimeter_name: The name of the Service Perimeter to add this resource to.
        :param pulumi.Input[str] resource: A GCP resource that is inside of the service perimeter.
               Currently only projects are allowed.
               Format: projects/{project_number}
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["perimeter_name"] = perimeter_name
        __props__["resource"] = resource
        return ServicePerimeterResource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="perimeterName")
    def perimeter_name(self) -> pulumi.Output[str]:
        """
        The name of the Service Perimeter to add this resource to.
        """
        return pulumi.get(self, "perimeter_name")

    @property
    @pulumi.getter
    def resource(self) -> pulumi.Output[str]:
        """
        A GCP resource that is inside of the service perimeter.
        Currently only projects are allowed.
        Format: projects/{project_number}
        """
        return pulumi.get(self, "resource")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

