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

__all__ = ['GuestPolicies']


class GuestPolicies(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assignment: Optional[pulumi.Input[pulumi.InputType['GuestPoliciesAssignmentArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 guest_policy_id: Optional[pulumi.Input[str]] = None,
                 package_repositories: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GuestPoliciesPackageRepositoryArgs']]]]] = None,
                 packages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GuestPoliciesPackageArgs']]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 recipes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GuestPoliciesRecipeArgs']]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        An OS Config resource representing a guest configuration policy. These policies represent
        the desired state for VM instance guest environments including packages to install or remove,
        package repository configurations, and software to install.

        To get more information about GuestPolicies, see:

        * [API documentation](https://cloud.google.com/compute/docs/osconfig/rest)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/compute/docs/os-config-management)

        ## Example Usage
        ### Os Config Guest Policies Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        my_image = gcp.compute.get_image(family="debian-9",
            project="debian-cloud")
        foobar = gcp.compute.Instance("foobar",
            machine_type="e2-medium",
            zone="us-central1-a",
            can_ip_forward=False,
            tags=[
                "foo",
                "bar",
            ],
            boot_disk=gcp.compute.InstanceBootDiskArgs(
                initialize_params=gcp.compute.InstanceBootDiskInitializeParamsArgs(
                    image=my_image.self_link,
                ),
            ),
            network_interfaces=[gcp.compute.InstanceNetworkInterfaceArgs(
                network="default",
            )],
            metadata={
                "foo": "bar",
            },
            opts=pulumi.ResourceOptions(provider=google_beta))
        guest_policies = gcp.osconfig.GuestPolicies("guestPolicies",
            guest_policy_id="guest-policy",
            assignment=gcp.osconfig.GuestPoliciesAssignmentArgs(
                instances=[foobar.id],
            ),
            packages=[gcp.osconfig.GuestPoliciesPackageArgs(
                name="my-package",
                desired_state="UPDATED",
            )],
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```
        ### Os Config Guest Policies Packages

        ```python
        import pulumi
        import pulumi_gcp as gcp

        guest_policies = gcp.osconfig.GuestPolicies("guestPolicies",
            guest_policy_id="guest-policy",
            assignment=gcp.osconfig.GuestPoliciesAssignmentArgs(
                group_labels=[
                    gcp.osconfig.GuestPoliciesAssignmentGroupLabelArgs(
                        labels={
                            "color": "red",
                            "env": "test",
                        },
                    ),
                    gcp.osconfig.GuestPoliciesAssignmentGroupLabelArgs(
                        labels={
                            "color": "blue",
                            "env": "test",
                        },
                    ),
                ],
            ),
            packages=[
                gcp.osconfig.GuestPoliciesPackageArgs(
                    name="my-package",
                    desired_state="INSTALLED",
                ),
                gcp.osconfig.GuestPoliciesPackageArgs(
                    name="bad-package-1",
                    desired_state="REMOVED",
                ),
                gcp.osconfig.GuestPoliciesPackageArgs(
                    name="bad-package-2",
                    desired_state="REMOVED",
                    manager="APT",
                ),
            ],
            package_repositories=[
                gcp.osconfig.GuestPoliciesPackageRepositoryArgs(
                    apt=gcp.osconfig.GuestPoliciesPackageRepositoryAptArgs(
                        uri="https://packages.cloud.google.com/apt",
                        archive_type="DEB",
                        distribution="cloud-sdk-stretch",
                        components=["main"],
                    ),
                ),
                gcp.osconfig.GuestPoliciesPackageRepositoryArgs(
                    yum=gcp.osconfig.GuestPoliciesPackageRepositoryYumArgs(
                        id="google-cloud-sdk",
                        display_name="Google Cloud SDK",
                        base_url="https://packages.cloud.google.com/yum/repos/cloud-sdk-el7-x86_64",
                        gpg_keys=[
                            "https://packages.cloud.google.com/yum/doc/yum-key.gpg",
                            "https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg",
                        ],
                    ),
                ),
            ],
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```
        ### Os Config Guest Policies Recipes

        ```python
        import pulumi
        import pulumi_gcp as gcp

        guest_policies = gcp.osconfig.GuestPolicies("guestPolicies",
            guest_policy_id="guest-policy",
            assignment=gcp.osconfig.GuestPoliciesAssignmentArgs(
                zones=[
                    "us-east1-b",
                    "us-east1-d",
                ],
            ),
            recipes=[gcp.osconfig.GuestPoliciesRecipeArgs(
                name="guest-policy-recipe",
                desired_state="INSTALLED",
                artifacts=[gcp.osconfig.GuestPoliciesRecipeArtifactArgs(
                    id="guest-policy-artifact-id",
                    gcs=gcp.osconfig.GuestPoliciesRecipeArtifactGcsArgs(
                        bucket="my-bucket",
                        object="executable.msi",
                        generation=1546030865175603,
                    ),
                )],
                install_steps=[gcp.osconfig.GuestPoliciesRecipeInstallStepArgs(
                    msi_installation=gcp.osconfig.GuestPoliciesRecipeInstallStepMsiInstallationArgs(
                        artifact_id="guest-policy-artifact-id",
                    ),
                )],
            )],
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```

        ## Import

        GuestPolicies can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:osconfig/guestPolicies:GuestPolicies default projects/{{project}}/guestPolicies/{{name}}
        ```

        ```sh
         $ pulumi import gcp:osconfig/guestPolicies:GuestPolicies default {{project}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:osconfig/guestPolicies:GuestPolicies default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GuestPoliciesAssignmentArgs']] assignment: Specifies the VM instances that are assigned to this policy. This allows you to target sets
               or groups of VM instances by different parameters such as labels, names, OS, or zones.
               If left empty, all VM instances underneath this policy are targeted.
               At the same level in the resource hierarchy (that is within a project), the service prevents
               the creation of multiple policies that conflict with each other.
               For more information, see how the service
               [handles assignment conflicts](https://cloud.google.com/compute/docs/os-config-management/create-guest-policy#handle-conflicts).
               Structure is documented below.
        :param pulumi.Input[str] description: Description of the guest policy. Length of the description is limited to 1024 characters.
        :param pulumi.Input[str] etag: The etag for this guest policy. If this is provided on update, it must match the server's etag.
        :param pulumi.Input[str] guest_policy_id: The logical name of the guest policy in the project with the following restrictions:
               * Must contain only lowercase letters, numbers, and hyphens.
               * Must start with a letter.
               * Must be between 1-63 characters.
               * Must end with a number or a letter.
               * Must be unique within the project.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GuestPoliciesPackageRepositoryArgs']]]] package_repositories: A list of package repositories to configure on the VM instance.
               This is done before any other configs are applied so they can use these repos.
               Package repositories are only configured if the corresponding package manager(s) are available.
               Structure is documented below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GuestPoliciesPackageArgs']]]] packages: The software packages to be managed by this policy.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GuestPoliciesRecipeArgs']]]] recipes: A list of Recipes to install on the VM instance.
               Structure is documented below.
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

            if assignment is None and not opts.urn:
                raise TypeError("Missing required property 'assignment'")
            __props__['assignment'] = assignment
            __props__['description'] = description
            __props__['etag'] = etag
            if guest_policy_id is None and not opts.urn:
                raise TypeError("Missing required property 'guest_policy_id'")
            __props__['guest_policy_id'] = guest_policy_id
            __props__['package_repositories'] = package_repositories
            __props__['packages'] = packages
            __props__['project'] = project
            __props__['recipes'] = recipes
            __props__['create_time'] = None
            __props__['name'] = None
            __props__['update_time'] = None
        super(GuestPolicies, __self__).__init__(
            'gcp:osconfig/guestPolicies:GuestPolicies',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            assignment: Optional[pulumi.Input[pulumi.InputType['GuestPoliciesAssignmentArgs']]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            guest_policy_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            package_repositories: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GuestPoliciesPackageRepositoryArgs']]]]] = None,
            packages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GuestPoliciesPackageArgs']]]]] = None,
            project: Optional[pulumi.Input[str]] = None,
            recipes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GuestPoliciesRecipeArgs']]]]] = None,
            update_time: Optional[pulumi.Input[str]] = None) -> 'GuestPolicies':
        """
        Get an existing GuestPolicies resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GuestPoliciesAssignmentArgs']] assignment: Specifies the VM instances that are assigned to this policy. This allows you to target sets
               or groups of VM instances by different parameters such as labels, names, OS, or zones.
               If left empty, all VM instances underneath this policy are targeted.
               At the same level in the resource hierarchy (that is within a project), the service prevents
               the creation of multiple policies that conflict with each other.
               For more information, see how the service
               [handles assignment conflicts](https://cloud.google.com/compute/docs/os-config-management/create-guest-policy#handle-conflicts).
               Structure is documented below.
        :param pulumi.Input[str] create_time: Time this guest policy was created. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example:
               "2014-10-02T15:01:23.045123456Z".
        :param pulumi.Input[str] description: Description of the guest policy. Length of the description is limited to 1024 characters.
        :param pulumi.Input[str] etag: The etag for this guest policy. If this is provided on update, it must match the server's etag.
        :param pulumi.Input[str] guest_policy_id: The logical name of the guest policy in the project with the following restrictions:
               * Must contain only lowercase letters, numbers, and hyphens.
               * Must start with a letter.
               * Must be between 1-63 characters.
               * Must end with a number or a letter.
               * Must be unique within the project.
        :param pulumi.Input[str] name: Unique identifier for the recipe. Only one recipe with a given name is installed on an instance.
               Names are also used to identify resources which helps to determine whether guest policies have conflicts.
               This means that requests to create multiple recipes with the same name and version are rejected since they
               could potentially have conflicting assignments.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GuestPoliciesPackageRepositoryArgs']]]] package_repositories: A list of package repositories to configure on the VM instance.
               This is done before any other configs are applied so they can use these repos.
               Package repositories are only configured if the corresponding package manager(s) are available.
               Structure is documented below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GuestPoliciesPackageArgs']]]] packages: The software packages to be managed by this policy.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GuestPoliciesRecipeArgs']]]] recipes: A list of Recipes to install on the VM instance.
               Structure is documented below.
        :param pulumi.Input[str] update_time: Last time this guest policy was updated. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example:
               "2014-10-02T15:01:23.045123456Z".
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["assignment"] = assignment
        __props__["create_time"] = create_time
        __props__["description"] = description
        __props__["etag"] = etag
        __props__["guest_policy_id"] = guest_policy_id
        __props__["name"] = name
        __props__["package_repositories"] = package_repositories
        __props__["packages"] = packages
        __props__["project"] = project
        __props__["recipes"] = recipes
        __props__["update_time"] = update_time
        return GuestPolicies(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def assignment(self) -> pulumi.Output['outputs.GuestPoliciesAssignment']:
        """
        Specifies the VM instances that are assigned to this policy. This allows you to target sets
        or groups of VM instances by different parameters such as labels, names, OS, or zones.
        If left empty, all VM instances underneath this policy are targeted.
        At the same level in the resource hierarchy (that is within a project), the service prevents
        the creation of multiple policies that conflict with each other.
        For more information, see how the service
        [handles assignment conflicts](https://cloud.google.com/compute/docs/os-config-management/create-guest-policy#handle-conflicts).
        Structure is documented below.
        """
        return pulumi.get(self, "assignment")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Time this guest policy was created. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example:
        "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the guest policy. Length of the description is limited to 1024 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        The etag for this guest policy. If this is provided on update, it must match the server's etag.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="guestPolicyId")
    def guest_policy_id(self) -> pulumi.Output[str]:
        """
        The logical name of the guest policy in the project with the following restrictions:
        * Must contain only lowercase letters, numbers, and hyphens.
        * Must start with a letter.
        * Must be between 1-63 characters.
        * Must end with a number or a letter.
        * Must be unique within the project.
        """
        return pulumi.get(self, "guest_policy_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Unique identifier for the recipe. Only one recipe with a given name is installed on an instance.
        Names are also used to identify resources which helps to determine whether guest policies have conflicts.
        This means that requests to create multiple recipes with the same name and version are rejected since they
        could potentially have conflicting assignments.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="packageRepositories")
    def package_repositories(self) -> pulumi.Output[Optional[Sequence['outputs.GuestPoliciesPackageRepository']]]:
        """
        A list of package repositories to configure on the VM instance.
        This is done before any other configs are applied so they can use these repos.
        Package repositories are only configured if the corresponding package manager(s) are available.
        Structure is documented below.
        """
        return pulumi.get(self, "package_repositories")

    @property
    @pulumi.getter
    def packages(self) -> pulumi.Output[Optional[Sequence['outputs.GuestPoliciesPackage']]]:
        """
        The software packages to be managed by this policy.
        Structure is documented below.
        """
        return pulumi.get(self, "packages")

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
    def recipes(self) -> pulumi.Output[Optional[Sequence['outputs.GuestPoliciesRecipe']]]:
        """
        A list of Recipes to install on the VM instance.
        Structure is documented below.
        """
        return pulumi.get(self, "recipes")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Last time this guest policy was updated. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example:
        "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "update_time")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

