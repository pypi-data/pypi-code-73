"""
# AWS::Signer Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_signer as signer
```
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.core


@jsii.implements(aws_cdk.core.IInspectable)
class CfnProfilePermission(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-signer.CfnProfilePermission",
):
    """A CloudFormation ``AWS::Signer::ProfilePermission``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html
    :cloudformationResource: AWS::Signer::ProfilePermission
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        action: builtins.str,
        principal: builtins.str,
        profile_name: builtins.str,
        statement_id: builtins.str,
        profile_version: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::Signer::ProfilePermission``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param action: ``AWS::Signer::ProfilePermission.Action``.
        :param principal: ``AWS::Signer::ProfilePermission.Principal``.
        :param profile_name: ``AWS::Signer::ProfilePermission.ProfileName``.
        :param statement_id: ``AWS::Signer::ProfilePermission.StatementId``.
        :param profile_version: ``AWS::Signer::ProfilePermission.ProfileVersion``.
        """
        props = CfnProfilePermissionProps(
            action=action,
            principal=principal,
            profile_name=profile_name,
            statement_id=statement_id,
            profile_version=profile_version,
        )

        jsii.create(CfnProfilePermission, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        """``AWS::Signer::ProfilePermission.Action``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-action
        """
        return jsii.get(self, "action")

    @action.setter # type: ignore
    def action(self, value: builtins.str) -> None:
        jsii.set(self, "action", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="principal")
    def principal(self) -> builtins.str:
        """``AWS::Signer::ProfilePermission.Principal``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-principal
        """
        return jsii.get(self, "principal")

    @principal.setter # type: ignore
    def principal(self, value: builtins.str) -> None:
        jsii.set(self, "principal", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="profileName")
    def profile_name(self) -> builtins.str:
        """``AWS::Signer::ProfilePermission.ProfileName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-profilename
        """
        return jsii.get(self, "profileName")

    @profile_name.setter # type: ignore
    def profile_name(self, value: builtins.str) -> None:
        jsii.set(self, "profileName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="statementId")
    def statement_id(self) -> builtins.str:
        """``AWS::Signer::ProfilePermission.StatementId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-statementid
        """
        return jsii.get(self, "statementId")

    @statement_id.setter # type: ignore
    def statement_id(self, value: builtins.str) -> None:
        jsii.set(self, "statementId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="profileVersion")
    def profile_version(self) -> typing.Optional[builtins.str]:
        """``AWS::Signer::ProfilePermission.ProfileVersion``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-profileversion
        """
        return jsii.get(self, "profileVersion")

    @profile_version.setter # type: ignore
    def profile_version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "profileVersion", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-signer.CfnProfilePermissionProps",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "principal": "principal",
        "profile_name": "profileName",
        "statement_id": "statementId",
        "profile_version": "profileVersion",
    },
)
class CfnProfilePermissionProps:
    def __init__(
        self,
        *,
        action: builtins.str,
        principal: builtins.str,
        profile_name: builtins.str,
        statement_id: builtins.str,
        profile_version: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::Signer::ProfilePermission``.

        :param action: ``AWS::Signer::ProfilePermission.Action``.
        :param principal: ``AWS::Signer::ProfilePermission.Principal``.
        :param profile_name: ``AWS::Signer::ProfilePermission.ProfileName``.
        :param statement_id: ``AWS::Signer::ProfilePermission.StatementId``.
        :param profile_version: ``AWS::Signer::ProfilePermission.ProfileVersion``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "principal": principal,
            "profile_name": profile_name,
            "statement_id": statement_id,
        }
        if profile_version is not None:
            self._values["profile_version"] = profile_version

    @builtins.property
    def action(self) -> builtins.str:
        """``AWS::Signer::ProfilePermission.Action``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-action
        """
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return result

    @builtins.property
    def principal(self) -> builtins.str:
        """``AWS::Signer::ProfilePermission.Principal``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-principal
        """
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return result

    @builtins.property
    def profile_name(self) -> builtins.str:
        """``AWS::Signer::ProfilePermission.ProfileName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-profilename
        """
        result = self._values.get("profile_name")
        assert result is not None, "Required property 'profile_name' is missing"
        return result

    @builtins.property
    def statement_id(self) -> builtins.str:
        """``AWS::Signer::ProfilePermission.StatementId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-statementid
        """
        result = self._values.get("statement_id")
        assert result is not None, "Required property 'statement_id' is missing"
        return result

    @builtins.property
    def profile_version(self) -> typing.Optional[builtins.str]:
        """``AWS::Signer::ProfilePermission.ProfileVersion``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-profileversion
        """
        result = self._values.get("profile_version")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProfilePermissionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnSigningProfile(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-signer.CfnSigningProfile",
):
    """A CloudFormation ``AWS::Signer::SigningProfile``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-signingprofile.html
    :cloudformationResource: AWS::Signer::SigningProfile
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        platform_id: builtins.str,
        signature_validity_period: typing.Optional[typing.Union["CfnSigningProfile.SignatureValidityPeriodProperty", aws_cdk.core.IResolvable]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::Signer::SigningProfile``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param platform_id: ``AWS::Signer::SigningProfile.PlatformId``.
        :param signature_validity_period: ``AWS::Signer::SigningProfile.SignatureValidityPeriod``.
        :param tags: ``AWS::Signer::SigningProfile.Tags``.
        """
        props = CfnSigningProfileProps(
            platform_id=platform_id,
            signature_validity_period=signature_validity_period,
            tags=tags,
        )

        jsii.create(CfnSigningProfile, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: Arn
        """
        return jsii.get(self, "attrArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrProfileName")
    def attr_profile_name(self) -> builtins.str:
        """
        :cloudformationAttribute: ProfileName
        """
        return jsii.get(self, "attrProfileName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrProfileVersion")
    def attr_profile_version(self) -> builtins.str:
        """
        :cloudformationAttribute: ProfileVersion
        """
        return jsii.get(self, "attrProfileVersion")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrProfileVersionArn")
    def attr_profile_version_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: ProfileVersionArn
        """
        return jsii.get(self, "attrProfileVersionArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::Signer::SigningProfile.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-signingprofile.html#cfn-signer-signingprofile-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="platformId")
    def platform_id(self) -> builtins.str:
        """``AWS::Signer::SigningProfile.PlatformId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-signingprofile.html#cfn-signer-signingprofile-platformid
        """
        return jsii.get(self, "platformId")

    @platform_id.setter # type: ignore
    def platform_id(self, value: builtins.str) -> None:
        jsii.set(self, "platformId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="signatureValidityPeriod")
    def signature_validity_period(
        self,
    ) -> typing.Optional[typing.Union["CfnSigningProfile.SignatureValidityPeriodProperty", aws_cdk.core.IResolvable]]:
        """``AWS::Signer::SigningProfile.SignatureValidityPeriod``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-signingprofile.html#cfn-signer-signingprofile-signaturevalidityperiod
        """
        return jsii.get(self, "signatureValidityPeriod")

    @signature_validity_period.setter # type: ignore
    def signature_validity_period(
        self,
        value: typing.Optional[typing.Union["CfnSigningProfile.SignatureValidityPeriodProperty", aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "signatureValidityPeriod", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-signer.CfnSigningProfile.SignatureValidityPeriodProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class SignatureValidityPeriodProperty:
        def __init__(
            self,
            *,
            type: typing.Optional[builtins.str] = None,
            value: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param type: ``CfnSigningProfile.SignatureValidityPeriodProperty.Type``.
            :param value: ``CfnSigningProfile.SignatureValidityPeriodProperty.Value``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-signer-signingprofile-signaturevalidityperiod.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if type is not None:
                self._values["type"] = type
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            """``CfnSigningProfile.SignatureValidityPeriodProperty.Type``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-signer-signingprofile-signaturevalidityperiod.html#cfn-signer-signingprofile-signaturevalidityperiod-type
            """
            result = self._values.get("type")
            return result

        @builtins.property
        def value(self) -> typing.Optional[jsii.Number]:
            """``CfnSigningProfile.SignatureValidityPeriodProperty.Value``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-signer-signingprofile-signaturevalidityperiod.html#cfn-signer-signingprofile-signaturevalidityperiod-value
            """
            result = self._values.get("value")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SignatureValidityPeriodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-signer.CfnSigningProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "platform_id": "platformId",
        "signature_validity_period": "signatureValidityPeriod",
        "tags": "tags",
    },
)
class CfnSigningProfileProps:
    def __init__(
        self,
        *,
        platform_id: builtins.str,
        signature_validity_period: typing.Optional[typing.Union[CfnSigningProfile.SignatureValidityPeriodProperty, aws_cdk.core.IResolvable]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::Signer::SigningProfile``.

        :param platform_id: ``AWS::Signer::SigningProfile.PlatformId``.
        :param signature_validity_period: ``AWS::Signer::SigningProfile.SignatureValidityPeriod``.
        :param tags: ``AWS::Signer::SigningProfile.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-signingprofile.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "platform_id": platform_id,
        }
        if signature_validity_period is not None:
            self._values["signature_validity_period"] = signature_validity_period
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def platform_id(self) -> builtins.str:
        """``AWS::Signer::SigningProfile.PlatformId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-signingprofile.html#cfn-signer-signingprofile-platformid
        """
        result = self._values.get("platform_id")
        assert result is not None, "Required property 'platform_id' is missing"
        return result

    @builtins.property
    def signature_validity_period(
        self,
    ) -> typing.Optional[typing.Union[CfnSigningProfile.SignatureValidityPeriodProperty, aws_cdk.core.IResolvable]]:
        """``AWS::Signer::SigningProfile.SignatureValidityPeriod``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-signingprofile.html#cfn-signer-signingprofile-signaturevalidityperiod
        """
        result = self._values.get("signature_validity_period")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::Signer::SigningProfile.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-signingprofile.html#cfn-signer-signingprofile-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSigningProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnProfilePermission",
    "CfnProfilePermissionProps",
    "CfnSigningProfile",
    "CfnSigningProfileProps",
]

publication.publish()
