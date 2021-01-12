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

__all__ = ['DefaultObjectAccessControl']


class DefaultObjectAccessControl(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 entity: Optional[pulumi.Input[str]] = None,
                 object: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The DefaultObjectAccessControls resources represent the Access Control
        Lists (ACLs) applied to a new object within a Google Cloud Storage bucket
        when no ACL was provided for that object. ACLs let you specify who has
        access to your bucket contents and to what extent.

        There are two roles that can be assigned to an entity:

        READERs can get an object, though the acl property will not be revealed.
        OWNERs are READERs, and they can get the acl property, update an object,
        and call all objectAccessControls methods on the object. The owner of an
        object is always an OWNER.
        For more information, see Access Control, with the caveat that this API
        uses READER and OWNER instead of READ and FULL_CONTROL.

        To get more information about DefaultObjectAccessControl, see:

        * [API documentation](https://cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/storage/docs/access-control/create-manage-lists)

        ## Example Usage
        ### Storage Default Object Access Control Public

        ```python
        import pulumi
        import pulumi_gcp as gcp

        bucket = gcp.storage.Bucket("bucket")
        public_rule = gcp.storage.DefaultObjectAccessControl("publicRule",
            bucket=bucket.name,
            role="READER",
            entity="allUsers")
        ```

        ## Import

        DefaultObjectAccessControl can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:storage/defaultObjectAccessControl:DefaultObjectAccessControl default {{bucket}}/{{entity}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the bucket.
        :param pulumi.Input[str] entity: The entity holding the permission, in one of the following forms:
               * user-{{userId}}
               * user-{{email}} (such as "user-liz@example.com")
               * group-{{groupId}}
               * group-{{email}} (such as "group-example@googlegroups.com")
               * domain-{{domain}} (such as "domain-example.com")
               * project-team-{{projectId}}
               * allUsers
               * allAuthenticatedUsers
        :param pulumi.Input[str] object: The name of the object, if applied to an object.
        :param pulumi.Input[str] role: The access permission for the entity.
               Possible values are `OWNER` and `READER`.
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

            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__['bucket'] = bucket
            if entity is None and not opts.urn:
                raise TypeError("Missing required property 'entity'")
            __props__['entity'] = entity
            __props__['object'] = object
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__['role'] = role
            __props__['domain'] = None
            __props__['email'] = None
            __props__['entity_id'] = None
            __props__['generation'] = None
            __props__['project_teams'] = None
        super(DefaultObjectAccessControl, __self__).__init__(
            'gcp:storage/defaultObjectAccessControl:DefaultObjectAccessControl',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bucket: Optional[pulumi.Input[str]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            email: Optional[pulumi.Input[str]] = None,
            entity: Optional[pulumi.Input[str]] = None,
            entity_id: Optional[pulumi.Input[str]] = None,
            generation: Optional[pulumi.Input[int]] = None,
            object: Optional[pulumi.Input[str]] = None,
            project_teams: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DefaultObjectAccessControlProjectTeamArgs']]]]] = None,
            role: Optional[pulumi.Input[str]] = None) -> 'DefaultObjectAccessControl':
        """
        Get an existing DefaultObjectAccessControl resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the bucket.
        :param pulumi.Input[str] domain: The domain associated with the entity.
        :param pulumi.Input[str] email: The email address associated with the entity.
        :param pulumi.Input[str] entity: The entity holding the permission, in one of the following forms:
               * user-{{userId}}
               * user-{{email}} (such as "user-liz@example.com")
               * group-{{groupId}}
               * group-{{email}} (such as "group-example@googlegroups.com")
               * domain-{{domain}} (such as "domain-example.com")
               * project-team-{{projectId}}
               * allUsers
               * allAuthenticatedUsers
        :param pulumi.Input[str] entity_id: The ID for the entity
        :param pulumi.Input[int] generation: The content generation of the object, if applied to an object.
        :param pulumi.Input[str] object: The name of the object, if applied to an object.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DefaultObjectAccessControlProjectTeamArgs']]]] project_teams: The project team associated with the entity
        :param pulumi.Input[str] role: The access permission for the entity.
               Possible values are `OWNER` and `READER`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["bucket"] = bucket
        __props__["domain"] = domain
        __props__["email"] = email
        __props__["entity"] = entity
        __props__["entity_id"] = entity_id
        __props__["generation"] = generation
        __props__["object"] = object
        __props__["project_teams"] = project_teams
        __props__["role"] = role
        return DefaultObjectAccessControl(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        The name of the bucket.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        """
        The domain associated with the entity.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        The email address associated with the entity.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def entity(self) -> pulumi.Output[str]:
        """
        The entity holding the permission, in one of the following forms:
        * user-{{userId}}
        * user-{{email}} (such as "user-liz@example.com")
        * group-{{groupId}}
        * group-{{email}} (such as "group-example@googlegroups.com")
        * domain-{{domain}} (such as "domain-example.com")
        * project-team-{{projectId}}
        * allUsers
        * allAuthenticatedUsers
        """
        return pulumi.get(self, "entity")

    @property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> pulumi.Output[str]:
        """
        The ID for the entity
        """
        return pulumi.get(self, "entity_id")

    @property
    @pulumi.getter
    def generation(self) -> pulumi.Output[int]:
        """
        The content generation of the object, if applied to an object.
        """
        return pulumi.get(self, "generation")

    @property
    @pulumi.getter
    def object(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the object, if applied to an object.
        """
        return pulumi.get(self, "object")

    @property
    @pulumi.getter(name="projectTeams")
    def project_teams(self) -> pulumi.Output[Sequence['outputs.DefaultObjectAccessControlProjectTeam']]:
        """
        The project team associated with the entity
        """
        return pulumi.get(self, "project_teams")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        The access permission for the entity.
        Possible values are `OWNER` and `READER`.
        """
        return pulumi.get(self, "role")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

