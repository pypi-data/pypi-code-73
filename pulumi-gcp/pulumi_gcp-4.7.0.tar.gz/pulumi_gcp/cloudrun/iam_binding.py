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

__all__ = ['IamBinding']


class IamBinding(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 condition: Optional[pulumi.Input[pulumi.InputType['IamBindingConditionArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Three different resources help you manage your IAM policy for Cloud Run Service. Each of these resources serves a different use case:

        * `cloudrun.IamPolicy`: Authoritative. Sets the IAM policy for the service and replaces any existing policy already attached.
        * `cloudrun.IamBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the service are preserved.
        * `cloudrun.IamMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the service are preserved.

        > **Note:** `cloudrun.IamPolicy` **cannot** be used in conjunction with `cloudrun.IamBinding` and `cloudrun.IamMember` or they will fight over what your policy should be.

        > **Note:** `cloudrun.IamBinding` resources **can be** used in conjunction with `cloudrun.IamMember` resources **only if** they do not grant privilege to the same role.

        ## google\_cloud\_run\_service\_iam\_policy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[gcp.organizations.GetIAMPolicyBindingArgs(
            role="roles/viewer",
            members=["user:jane@example.com"],
        )])
        policy = gcp.cloudrun.IamPolicy("policy",
            location=google_cloud_run_service["default"]["location"],
            project=google_cloud_run_service["default"]["project"],
            service=google_cloud_run_service["default"]["name"],
            policy_data=admin.policy_data)
        ```

        ## google\_cloud\_run\_service\_iam\_binding

        ```python
        import pulumi
        import pulumi_gcp as gcp

        binding = gcp.cloudrun.IamBinding("binding",
            location=google_cloud_run_service["default"]["location"],
            project=google_cloud_run_service["default"]["project"],
            service=google_cloud_run_service["default"]["name"],
            role="roles/viewer",
            members=["user:jane@example.com"])
        ```

        ## google\_cloud\_run\_service\_iam\_member

        ```python
        import pulumi
        import pulumi_gcp as gcp

        member = gcp.cloudrun.IamMember("member",
            location=google_cloud_run_service["default"]["location"],
            project=google_cloud_run_service["default"]["project"],
            service=google_cloud_run_service["default"]["name"],
            role="roles/viewer",
            member="user:jane@example.com")
        ```

        ## Import

        For all import syntaxes, the "resource in question" can take any of the following forms* projects/{{project}}/locations/{{location}}/services/{{service}} * {{project}}/{{location}}/{{service}} * {{location}}/{{service}} * {{service}} Any variables not passed in the import command will be taken from the provider configuration. Cloud Run service IAM resources can be imported using the resource identifiers, role, and member. IAM member imports use space-delimited identifiersthe resource in question, the role, and the member identity, e.g.

        ```sh
         $ pulumi import gcp:cloudrun/iamBinding:IamBinding editor "projects/{{project}}/locations/{{location}}/services/{{service}} roles/viewer user:jane@example.com"
        ```

         IAM binding imports use space-delimited identifiersthe resource in question and the role, e.g.

        ```sh
         $ pulumi import gcp:cloudrun/iamBinding:IamBinding editor "projects/{{project}}/locations/{{location}}/services/{{service}} roles/viewer"
        ```

         IAM policy imports use the identifier of the resource in question, e.g.

        ```sh
         $ pulumi import gcp:cloudrun/iamBinding:IamBinding editor projects/{{project}}/locations/{{location}}/services/{{service}}
        ```

         -> **Custom Roles**If you're importing a IAM resource with a custom role, make sure to use the

        full name of the custom role, e.g. `[projects/my-project|organizations/my-org]/roles/my-custom-role`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The location of the cloud run instance. eg us-central1 Used to find the parent resource to bind the IAM policy to
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `cloudrun.IamBinding` can be used per role. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
        :param pulumi.Input[str] service: Used to find the parent resource to bind the IAM policy to
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

            __props__['condition'] = condition
            __props__['location'] = location
            if members is None and not opts.urn:
                raise TypeError("Missing required property 'members'")
            __props__['members'] = members
            __props__['project'] = project
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__['role'] = role
            if service is None and not opts.urn:
                raise TypeError("Missing required property 'service'")
            __props__['service'] = service
            __props__['etag'] = None
        super(IamBinding, __self__).__init__(
            'gcp:cloudrun/iamBinding:IamBinding',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            condition: Optional[pulumi.Input[pulumi.InputType['IamBindingConditionArgs']]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            project: Optional[pulumi.Input[str]] = None,
            role: Optional[pulumi.Input[str]] = None,
            service: Optional[pulumi.Input[str]] = None) -> 'IamBinding':
        """
        Get an existing IamBinding resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] etag: (Computed) The etag of the IAM policy.
        :param pulumi.Input[str] location: The location of the cloud run instance. eg us-central1 Used to find the parent resource to bind the IAM policy to
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `cloudrun.IamBinding` can be used per role. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
        :param pulumi.Input[str] service: Used to find the parent resource to bind the IAM policy to
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["condition"] = condition
        __props__["etag"] = etag
        __props__["location"] = location
        __props__["members"] = members
        __props__["project"] = project
        __props__["role"] = role
        __props__["service"] = service
        return IamBinding(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def condition(self) -> pulumi.Output[Optional['outputs.IamBindingCondition']]:
        return pulumi.get(self, "condition")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        (Computed) The etag of the IAM policy.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location of the cloud run instance. eg us-central1 Used to find the parent resource to bind the IAM policy to
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def members(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "members")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        The role that should be applied. Only one
        `cloudrun.IamBinding` can be used per role. Note that custom roles must be of the format
        `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter
    def service(self) -> pulumi.Output[str]:
        """
        Used to find the parent resource to bind the IAM policy to
        """
        return pulumi.get(self, "service")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

