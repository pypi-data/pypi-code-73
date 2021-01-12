import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

from .. import (
    CfnResource as _CfnResource_e0a482dc,
    CfnTag as _CfnTag_95fbdc29,
    Construct as _Construct_e78e779f,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    TagManager as _TagManager_0b7ab120,
    TreeInspector as _TreeInspector_1cd1894e,
)


@jsii.implements(_IInspectable_82c04a63)
class CfnDestination(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iotwireless.CfnDestination",
):
    """A CloudFormation ``AWS::IoTWireless::Destination``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html
    :cloudformationResource: AWS::IoTWireless::Destination
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        expression: builtins.str,
        expression_type: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        next_token: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
    ) -> None:
        """Create a new ``AWS::IoTWireless::Destination``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param expression: ``AWS::IoTWireless::Destination.Expression``.
        :param expression_type: ``AWS::IoTWireless::Destination.ExpressionType``.
        :param name: ``AWS::IoTWireless::Destination.Name``.
        :param role_arn: ``AWS::IoTWireless::Destination.RoleArn``.
        :param description: ``AWS::IoTWireless::Destination.Description``.
        :param next_token: ``AWS::IoTWireless::Destination.NextToken``.
        :param tags: ``AWS::IoTWireless::Destination.Tags``.
        """
        props = CfnDestinationProps(
            expression=expression,
            expression_type=expression_type,
            name=name,
            role_arn=role_arn,
            description=description,
            next_token=next_token,
            tags=tags,
        )

        jsii.create(CfnDestination, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::IoTWireless::Destination.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        """``AWS::IoTWireless::Destination.Expression``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expression
        """
        return jsii.get(self, "expression")

    @expression.setter # type: ignore
    def expression(self, value: builtins.str) -> None:
        jsii.set(self, "expression", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="expressionType")
    def expression_type(self) -> builtins.str:
        """``AWS::IoTWireless::Destination.ExpressionType``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expressiontype
        """
        return jsii.get(self, "expressionType")

    @expression_type.setter # type: ignore
    def expression_type(self, value: builtins.str) -> None:
        jsii.set(self, "expressionType", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """``AWS::IoTWireless::Destination.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        """``AWS::IoTWireless::Destination.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-rolearn
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter # type: ignore
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::Destination.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="nextToken")
    def next_token(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::Destination.NextToken``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-nexttoken
        """
        return jsii.get(self, "nextToken")

    @next_token.setter # type: ignore
    def next_token(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "nextToken", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iotwireless.CfnDestinationProps",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "expression_type": "expressionType",
        "name": "name",
        "role_arn": "roleArn",
        "description": "description",
        "next_token": "nextToken",
        "tags": "tags",
    },
)
class CfnDestinationProps:
    def __init__(
        self,
        *,
        expression: builtins.str,
        expression_type: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        next_token: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
    ) -> None:
        """Properties for defining a ``AWS::IoTWireless::Destination``.

        :param expression: ``AWS::IoTWireless::Destination.Expression``.
        :param expression_type: ``AWS::IoTWireless::Destination.ExpressionType``.
        :param name: ``AWS::IoTWireless::Destination.Name``.
        :param role_arn: ``AWS::IoTWireless::Destination.RoleArn``.
        :param description: ``AWS::IoTWireless::Destination.Description``.
        :param next_token: ``AWS::IoTWireless::Destination.NextToken``.
        :param tags: ``AWS::IoTWireless::Destination.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "expression": expression,
            "expression_type": expression_type,
            "name": name,
            "role_arn": role_arn,
        }
        if description is not None:
            self._values["description"] = description
        if next_token is not None:
            self._values["next_token"] = next_token
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def expression(self) -> builtins.str:
        """``AWS::IoTWireless::Destination.Expression``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expression
        """
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return result

    @builtins.property
    def expression_type(self) -> builtins.str:
        """``AWS::IoTWireless::Destination.ExpressionType``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expressiontype
        """
        result = self._values.get("expression_type")
        assert result is not None, "Required property 'expression_type' is missing"
        return result

    @builtins.property
    def name(self) -> builtins.str:
        """``AWS::IoTWireless::Destination.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-name
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return result

    @builtins.property
    def role_arn(self) -> builtins.str:
        """``AWS::IoTWireless::Destination.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-rolearn
        """
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::Destination.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::Destination.NextToken``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-nexttoken
        """
        result = self._values.get("next_token")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        """``AWS::IoTWireless::Destination.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnDeviceProfile(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iotwireless.CfnDeviceProfile",
):
    """A CloudFormation ``AWS::IoTWireless::DeviceProfile``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html
    :cloudformationResource: AWS::IoTWireless::DeviceProfile
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        lo_ra_wan_device_profile: typing.Optional[typing.Union["CfnDeviceProfile.LoRaWANDeviceProfileProperty", _IResolvable_a771d0ef]] = None,
        name: typing.Optional[builtins.str] = None,
        next_token: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
    ) -> None:
        """Create a new ``AWS::IoTWireless::DeviceProfile``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param lo_ra_wan_device_profile: ``AWS::IoTWireless::DeviceProfile.LoRaWANDeviceProfile``.
        :param name: ``AWS::IoTWireless::DeviceProfile.Name``.
        :param next_token: ``AWS::IoTWireless::DeviceProfile.NextToken``.
        :param tags: ``AWS::IoTWireless::DeviceProfile.Tags``.
        """
        props = CfnDeviceProfileProps(
            lo_ra_wan_device_profile=lo_ra_wan_device_profile,
            name=name,
            next_token=next_token,
            tags=tags,
        )

        jsii.create(CfnDeviceProfile, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        """
        :cloudformationAttribute: Id
        """
        return jsii.get(self, "attrId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::IoTWireless::DeviceProfile.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="loRaWanDeviceProfile")
    def lo_ra_wan_device_profile(
        self,
    ) -> typing.Optional[typing.Union["CfnDeviceProfile.LoRaWANDeviceProfileProperty", _IResolvable_a771d0ef]]:
        """``AWS::IoTWireless::DeviceProfile.LoRaWANDeviceProfile``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile
        """
        return jsii.get(self, "loRaWanDeviceProfile")

    @lo_ra_wan_device_profile.setter # type: ignore
    def lo_ra_wan_device_profile(
        self,
        value: typing.Optional[typing.Union["CfnDeviceProfile.LoRaWANDeviceProfileProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "loRaWanDeviceProfile", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::DeviceProfile.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="nextToken")
    def next_token(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::DeviceProfile.NextToken``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-nexttoken
        """
        return jsii.get(self, "nextToken")

    @next_token.setter # type: ignore
    def next_token(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "nextToken", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_iotwireless.CfnDeviceProfile.LoRaWANDeviceProfileProperty",
        jsii_struct_bases=[],
        name_mapping={
            "class_b_timeout": "classBTimeout",
            "class_c_timeout": "classCTimeout",
            "mac_version": "macVersion",
            "max_duty_cycle": "maxDutyCycle",
            "max_eirp": "maxEirp",
            "ping_slot_dr": "pingSlotDr",
            "ping_slot_freq": "pingSlotFreq",
            "ping_slot_period": "pingSlotPeriod",
            "reg_params_revision": "regParamsRevision",
            "rf_region": "rfRegion",
            "supports32_bit_f_cnt": "supports32BitFCnt",
            "supports_class_b": "supportsClassB",
            "supports_class_c": "supportsClassC",
            "supports_join": "supportsJoin",
        },
    )
    class LoRaWANDeviceProfileProperty:
        def __init__(
            self,
            *,
            class_b_timeout: typing.Optional[jsii.Number] = None,
            class_c_timeout: typing.Optional[jsii.Number] = None,
            mac_version: typing.Optional[builtins.str] = None,
            max_duty_cycle: typing.Optional[jsii.Number] = None,
            max_eirp: typing.Optional[jsii.Number] = None,
            ping_slot_dr: typing.Optional[jsii.Number] = None,
            ping_slot_freq: typing.Optional[jsii.Number] = None,
            ping_slot_period: typing.Optional[jsii.Number] = None,
            reg_params_revision: typing.Optional[builtins.str] = None,
            rf_region: typing.Optional[builtins.str] = None,
            supports32_bit_f_cnt: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            supports_class_b: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            supports_class_c: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            supports_join: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param class_b_timeout: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.ClassBTimeout``.
            :param class_c_timeout: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.ClassCTimeout``.
            :param mac_version: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.MacVersion``.
            :param max_duty_cycle: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.MaxDutyCycle``.
            :param max_eirp: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.MaxEirp``.
            :param ping_slot_dr: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.PingSlotDr``.
            :param ping_slot_freq: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.PingSlotFreq``.
            :param ping_slot_period: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.PingSlotPeriod``.
            :param reg_params_revision: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.RegParamsRevision``.
            :param rf_region: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.RfRegion``.
            :param supports32_bit_f_cnt: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.Supports32BitFCnt``.
            :param supports_class_b: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.SupportsClassB``.
            :param supports_class_c: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.SupportsClassC``.
            :param supports_join: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.SupportsJoin``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if class_b_timeout is not None:
                self._values["class_b_timeout"] = class_b_timeout
            if class_c_timeout is not None:
                self._values["class_c_timeout"] = class_c_timeout
            if mac_version is not None:
                self._values["mac_version"] = mac_version
            if max_duty_cycle is not None:
                self._values["max_duty_cycle"] = max_duty_cycle
            if max_eirp is not None:
                self._values["max_eirp"] = max_eirp
            if ping_slot_dr is not None:
                self._values["ping_slot_dr"] = ping_slot_dr
            if ping_slot_freq is not None:
                self._values["ping_slot_freq"] = ping_slot_freq
            if ping_slot_period is not None:
                self._values["ping_slot_period"] = ping_slot_period
            if reg_params_revision is not None:
                self._values["reg_params_revision"] = reg_params_revision
            if rf_region is not None:
                self._values["rf_region"] = rf_region
            if supports32_bit_f_cnt is not None:
                self._values["supports32_bit_f_cnt"] = supports32_bit_f_cnt
            if supports_class_b is not None:
                self._values["supports_class_b"] = supports_class_b
            if supports_class_c is not None:
                self._values["supports_class_c"] = supports_class_c
            if supports_join is not None:
                self._values["supports_join"] = supports_join

        @builtins.property
        def class_b_timeout(self) -> typing.Optional[jsii.Number]:
            """``CfnDeviceProfile.LoRaWANDeviceProfileProperty.ClassBTimeout``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-classbtimeout
            """
            result = self._values.get("class_b_timeout")
            return result

        @builtins.property
        def class_c_timeout(self) -> typing.Optional[jsii.Number]:
            """``CfnDeviceProfile.LoRaWANDeviceProfileProperty.ClassCTimeout``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-classctimeout
            """
            result = self._values.get("class_c_timeout")
            return result

        @builtins.property
        def mac_version(self) -> typing.Optional[builtins.str]:
            """``CfnDeviceProfile.LoRaWANDeviceProfileProperty.MacVersion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-macversion
            """
            result = self._values.get("mac_version")
            return result

        @builtins.property
        def max_duty_cycle(self) -> typing.Optional[jsii.Number]:
            """``CfnDeviceProfile.LoRaWANDeviceProfileProperty.MaxDutyCycle``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxdutycycle
            """
            result = self._values.get("max_duty_cycle")
            return result

        @builtins.property
        def max_eirp(self) -> typing.Optional[jsii.Number]:
            """``CfnDeviceProfile.LoRaWANDeviceProfileProperty.MaxEirp``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxeirp
            """
            result = self._values.get("max_eirp")
            return result

        @builtins.property
        def ping_slot_dr(self) -> typing.Optional[jsii.Number]:
            """``CfnDeviceProfile.LoRaWANDeviceProfileProperty.PingSlotDr``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotdr
            """
            result = self._values.get("ping_slot_dr")
            return result

        @builtins.property
        def ping_slot_freq(self) -> typing.Optional[jsii.Number]:
            """``CfnDeviceProfile.LoRaWANDeviceProfileProperty.PingSlotFreq``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotfreq
            """
            result = self._values.get("ping_slot_freq")
            return result

        @builtins.property
        def ping_slot_period(self) -> typing.Optional[jsii.Number]:
            """``CfnDeviceProfile.LoRaWANDeviceProfileProperty.PingSlotPeriod``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotperiod
            """
            result = self._values.get("ping_slot_period")
            return result

        @builtins.property
        def reg_params_revision(self) -> typing.Optional[builtins.str]:
            """``CfnDeviceProfile.LoRaWANDeviceProfileProperty.RegParamsRevision``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-regparamsrevision
            """
            result = self._values.get("reg_params_revision")
            return result

        @builtins.property
        def rf_region(self) -> typing.Optional[builtins.str]:
            """``CfnDeviceProfile.LoRaWANDeviceProfileProperty.RfRegion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rfregion
            """
            result = self._values.get("rf_region")
            return result

        @builtins.property
        def supports32_bit_f_cnt(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnDeviceProfile.LoRaWANDeviceProfileProperty.Supports32BitFCnt``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supports32bitfcnt
            """
            result = self._values.get("supports32_bit_f_cnt")
            return result

        @builtins.property
        def supports_class_b(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnDeviceProfile.LoRaWANDeviceProfileProperty.SupportsClassB``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassb
            """
            result = self._values.get("supports_class_b")
            return result

        @builtins.property
        def supports_class_c(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnDeviceProfile.LoRaWANDeviceProfileProperty.SupportsClassC``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassc
            """
            result = self._values.get("supports_class_c")
            return result

        @builtins.property
        def supports_join(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnDeviceProfile.LoRaWANDeviceProfileProperty.SupportsJoin``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsjoin
            """
            result = self._values.get("supports_join")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANDeviceProfileProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_iotwireless.CfnDeviceProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "lo_ra_wan_device_profile": "loRaWanDeviceProfile",
        "name": "name",
        "next_token": "nextToken",
        "tags": "tags",
    },
)
class CfnDeviceProfileProps:
    def __init__(
        self,
        *,
        lo_ra_wan_device_profile: typing.Optional[typing.Union[CfnDeviceProfile.LoRaWANDeviceProfileProperty, _IResolvable_a771d0ef]] = None,
        name: typing.Optional[builtins.str] = None,
        next_token: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
    ) -> None:
        """Properties for defining a ``AWS::IoTWireless::DeviceProfile``.

        :param lo_ra_wan_device_profile: ``AWS::IoTWireless::DeviceProfile.LoRaWANDeviceProfile``.
        :param name: ``AWS::IoTWireless::DeviceProfile.Name``.
        :param next_token: ``AWS::IoTWireless::DeviceProfile.NextToken``.
        :param tags: ``AWS::IoTWireless::DeviceProfile.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if lo_ra_wan_device_profile is not None:
            self._values["lo_ra_wan_device_profile"] = lo_ra_wan_device_profile
        if name is not None:
            self._values["name"] = name
        if next_token is not None:
            self._values["next_token"] = next_token
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def lo_ra_wan_device_profile(
        self,
    ) -> typing.Optional[typing.Union[CfnDeviceProfile.LoRaWANDeviceProfileProperty, _IResolvable_a771d0ef]]:
        """``AWS::IoTWireless::DeviceProfile.LoRaWANDeviceProfile``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile
        """
        result = self._values.get("lo_ra_wan_device_profile")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::DeviceProfile.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::DeviceProfile.NextToken``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-nexttoken
        """
        result = self._values.get("next_token")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        """``AWS::IoTWireless::DeviceProfile.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeviceProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnServiceProfile(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iotwireless.CfnServiceProfile",
):
    """A CloudFormation ``AWS::IoTWireless::ServiceProfile``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html
    :cloudformationResource: AWS::IoTWireless::ServiceProfile
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        lo_ra_wan_get_service_profile_info: typing.Optional[typing.Union["CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty", _IResolvable_a771d0ef]] = None,
        lo_ra_wan_service_profile: typing.Optional[typing.Union["CfnServiceProfile.LoRaWANServiceProfileProperty", _IResolvable_a771d0ef]] = None,
        name: typing.Optional[builtins.str] = None,
        next_token: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
    ) -> None:
        """Create a new ``AWS::IoTWireless::ServiceProfile``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param lo_ra_wan_get_service_profile_info: ``AWS::IoTWireless::ServiceProfile.LoRaWANGetServiceProfileInfo``.
        :param lo_ra_wan_service_profile: ``AWS::IoTWireless::ServiceProfile.LoRaWANServiceProfile``.
        :param name: ``AWS::IoTWireless::ServiceProfile.Name``.
        :param next_token: ``AWS::IoTWireless::ServiceProfile.NextToken``.
        :param tags: ``AWS::IoTWireless::ServiceProfile.Tags``.
        """
        props = CfnServiceProfileProps(
            lo_ra_wan_get_service_profile_info=lo_ra_wan_get_service_profile_info,
            lo_ra_wan_service_profile=lo_ra_wan_service_profile,
            name=name,
            next_token=next_token,
            tags=tags,
        )

        jsii.create(CfnServiceProfile, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        """
        :cloudformationAttribute: Id
        """
        return jsii.get(self, "attrId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::IoTWireless::ServiceProfile.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="loRaWanGetServiceProfileInfo")
    def lo_ra_wan_get_service_profile_info(
        self,
    ) -> typing.Optional[typing.Union["CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty", _IResolvable_a771d0ef]]:
        """``AWS::IoTWireless::ServiceProfile.LoRaWANGetServiceProfileInfo``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo
        """
        return jsii.get(self, "loRaWanGetServiceProfileInfo")

    @lo_ra_wan_get_service_profile_info.setter # type: ignore
    def lo_ra_wan_get_service_profile_info(
        self,
        value: typing.Optional[typing.Union["CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "loRaWanGetServiceProfileInfo", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="loRaWanServiceProfile")
    def lo_ra_wan_service_profile(
        self,
    ) -> typing.Optional[typing.Union["CfnServiceProfile.LoRaWANServiceProfileProperty", _IResolvable_a771d0ef]]:
        """``AWS::IoTWireless::ServiceProfile.LoRaWANServiceProfile``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile
        """
        return jsii.get(self, "loRaWanServiceProfile")

    @lo_ra_wan_service_profile.setter # type: ignore
    def lo_ra_wan_service_profile(
        self,
        value: typing.Optional[typing.Union["CfnServiceProfile.LoRaWANServiceProfileProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "loRaWanServiceProfile", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::ServiceProfile.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="nextToken")
    def next_token(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::ServiceProfile.NextToken``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-nexttoken
        """
        return jsii.get(self, "nextToken")

    @next_token.setter # type: ignore
    def next_token(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "nextToken", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_iotwireless.CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_gw_metadata": "addGwMetadata",
            "channel_mask": "channelMask",
            "dev_status_req_freq": "devStatusReqFreq",
            "dl_bucket_size": "dlBucketSize",
            "dl_rate": "dlRate",
            "dl_rate_policy": "dlRatePolicy",
            "dr_max": "drMax",
            "dr_min": "drMin",
            "hr_allowed": "hrAllowed",
            "min_gw_diversity": "minGwDiversity",
            "nwk_geo_loc": "nwkGeoLoc",
            "pr_allowed": "prAllowed",
            "ra_allowed": "raAllowed",
            "report_dev_status_battery": "reportDevStatusBattery",
            "report_dev_status_margin": "reportDevStatusMargin",
            "target_per": "targetPer",
            "ul_bucket_size": "ulBucketSize",
            "ul_rate": "ulRate",
            "ul_rate_policy": "ulRatePolicy",
        },
    )
    class LoRaWANGetServiceProfileInfoProperty:
        def __init__(
            self,
            *,
            add_gw_metadata: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            channel_mask: typing.Optional[builtins.str] = None,
            dev_status_req_freq: typing.Optional[jsii.Number] = None,
            dl_bucket_size: typing.Optional[jsii.Number] = None,
            dl_rate: typing.Optional[jsii.Number] = None,
            dl_rate_policy: typing.Optional[builtins.str] = None,
            dr_max: typing.Optional[jsii.Number] = None,
            dr_min: typing.Optional[jsii.Number] = None,
            hr_allowed: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            min_gw_diversity: typing.Optional[jsii.Number] = None,
            nwk_geo_loc: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            pr_allowed: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            ra_allowed: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            report_dev_status_battery: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            report_dev_status_margin: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            target_per: typing.Optional[jsii.Number] = None,
            ul_bucket_size: typing.Optional[jsii.Number] = None,
            ul_rate: typing.Optional[jsii.Number] = None,
            ul_rate_policy: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param add_gw_metadata: ``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.AddGwMetadata``.
            :param channel_mask: ``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.ChannelMask``.
            :param dev_status_req_freq: ``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.DevStatusReqFreq``.
            :param dl_bucket_size: ``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.DlBucketSize``.
            :param dl_rate: ``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.DlRate``.
            :param dl_rate_policy: ``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.DlRatePolicy``.
            :param dr_max: ``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.DrMax``.
            :param dr_min: ``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.DrMin``.
            :param hr_allowed: ``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.HrAllowed``.
            :param min_gw_diversity: ``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.MinGwDiversity``.
            :param nwk_geo_loc: ``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.NwkGeoLoc``.
            :param pr_allowed: ``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.PrAllowed``.
            :param ra_allowed: ``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.RaAllowed``.
            :param report_dev_status_battery: ``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.ReportDevStatusBattery``.
            :param report_dev_status_margin: ``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.ReportDevStatusMargin``.
            :param target_per: ``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.TargetPer``.
            :param ul_bucket_size: ``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.UlBucketSize``.
            :param ul_rate: ``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.UlRate``.
            :param ul_rate_policy: ``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.UlRatePolicy``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if add_gw_metadata is not None:
                self._values["add_gw_metadata"] = add_gw_metadata
            if channel_mask is not None:
                self._values["channel_mask"] = channel_mask
            if dev_status_req_freq is not None:
                self._values["dev_status_req_freq"] = dev_status_req_freq
            if dl_bucket_size is not None:
                self._values["dl_bucket_size"] = dl_bucket_size
            if dl_rate is not None:
                self._values["dl_rate"] = dl_rate
            if dl_rate_policy is not None:
                self._values["dl_rate_policy"] = dl_rate_policy
            if dr_max is not None:
                self._values["dr_max"] = dr_max
            if dr_min is not None:
                self._values["dr_min"] = dr_min
            if hr_allowed is not None:
                self._values["hr_allowed"] = hr_allowed
            if min_gw_diversity is not None:
                self._values["min_gw_diversity"] = min_gw_diversity
            if nwk_geo_loc is not None:
                self._values["nwk_geo_loc"] = nwk_geo_loc
            if pr_allowed is not None:
                self._values["pr_allowed"] = pr_allowed
            if ra_allowed is not None:
                self._values["ra_allowed"] = ra_allowed
            if report_dev_status_battery is not None:
                self._values["report_dev_status_battery"] = report_dev_status_battery
            if report_dev_status_margin is not None:
                self._values["report_dev_status_margin"] = report_dev_status_margin
            if target_per is not None:
                self._values["target_per"] = target_per
            if ul_bucket_size is not None:
                self._values["ul_bucket_size"] = ul_bucket_size
            if ul_rate is not None:
                self._values["ul_rate"] = ul_rate
            if ul_rate_policy is not None:
                self._values["ul_rate_policy"] = ul_rate_policy

        @builtins.property
        def add_gw_metadata(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.AddGwMetadata``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo-addgwmetadata
            """
            result = self._values.get("add_gw_metadata")
            return result

        @builtins.property
        def channel_mask(self) -> typing.Optional[builtins.str]:
            """``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.ChannelMask``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo-channelmask
            """
            result = self._values.get("channel_mask")
            return result

        @builtins.property
        def dev_status_req_freq(self) -> typing.Optional[jsii.Number]:
            """``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.DevStatusReqFreq``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo-devstatusreqfreq
            """
            result = self._values.get("dev_status_req_freq")
            return result

        @builtins.property
        def dl_bucket_size(self) -> typing.Optional[jsii.Number]:
            """``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.DlBucketSize``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo-dlbucketsize
            """
            result = self._values.get("dl_bucket_size")
            return result

        @builtins.property
        def dl_rate(self) -> typing.Optional[jsii.Number]:
            """``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.DlRate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo-dlrate
            """
            result = self._values.get("dl_rate")
            return result

        @builtins.property
        def dl_rate_policy(self) -> typing.Optional[builtins.str]:
            """``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.DlRatePolicy``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo-dlratepolicy
            """
            result = self._values.get("dl_rate_policy")
            return result

        @builtins.property
        def dr_max(self) -> typing.Optional[jsii.Number]:
            """``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.DrMax``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo-drmax
            """
            result = self._values.get("dr_max")
            return result

        @builtins.property
        def dr_min(self) -> typing.Optional[jsii.Number]:
            """``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.DrMin``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo-drmin
            """
            result = self._values.get("dr_min")
            return result

        @builtins.property
        def hr_allowed(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.HrAllowed``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo-hrallowed
            """
            result = self._values.get("hr_allowed")
            return result

        @builtins.property
        def min_gw_diversity(self) -> typing.Optional[jsii.Number]:
            """``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.MinGwDiversity``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo-mingwdiversity
            """
            result = self._values.get("min_gw_diversity")
            return result

        @builtins.property
        def nwk_geo_loc(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.NwkGeoLoc``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo-nwkgeoloc
            """
            result = self._values.get("nwk_geo_loc")
            return result

        @builtins.property
        def pr_allowed(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.PrAllowed``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo-prallowed
            """
            result = self._values.get("pr_allowed")
            return result

        @builtins.property
        def ra_allowed(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.RaAllowed``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo-raallowed
            """
            result = self._values.get("ra_allowed")
            return result

        @builtins.property
        def report_dev_status_battery(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.ReportDevStatusBattery``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo-reportdevstatusbattery
            """
            result = self._values.get("report_dev_status_battery")
            return result

        @builtins.property
        def report_dev_status_margin(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.ReportDevStatusMargin``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo-reportdevstatusmargin
            """
            result = self._values.get("report_dev_status_margin")
            return result

        @builtins.property
        def target_per(self) -> typing.Optional[jsii.Number]:
            """``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.TargetPer``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo-targetper
            """
            result = self._values.get("target_per")
            return result

        @builtins.property
        def ul_bucket_size(self) -> typing.Optional[jsii.Number]:
            """``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.UlBucketSize``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo-ulbucketsize
            """
            result = self._values.get("ul_bucket_size")
            return result

        @builtins.property
        def ul_rate(self) -> typing.Optional[jsii.Number]:
            """``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.UlRate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo-ulrate
            """
            result = self._values.get("ul_rate")
            return result

        @builtins.property
        def ul_rate_policy(self) -> typing.Optional[builtins.str]:
            """``CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty.UlRatePolicy``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawangetserviceprofileinfo.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo-ulratepolicy
            """
            result = self._values.get("ul_rate_policy")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANGetServiceProfileInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iotwireless.CfnServiceProfile.LoRaWANServiceProfileProperty",
        jsii_struct_bases=[],
        name_mapping={"add_gw_metadata": "addGwMetadata"},
    )
    class LoRaWANServiceProfileProperty:
        def __init__(
            self,
            *,
            add_gw_metadata: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param add_gw_metadata: ``CfnServiceProfile.LoRaWANServiceProfileProperty.AddGwMetadata``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if add_gw_metadata is not None:
                self._values["add_gw_metadata"] = add_gw_metadata

        @builtins.property
        def add_gw_metadata(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnServiceProfile.LoRaWANServiceProfileProperty.AddGwMetadata``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-addgwmetadata
            """
            result = self._values.get("add_gw_metadata")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANServiceProfileProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_iotwireless.CfnServiceProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "lo_ra_wan_get_service_profile_info": "loRaWanGetServiceProfileInfo",
        "lo_ra_wan_service_profile": "loRaWanServiceProfile",
        "name": "name",
        "next_token": "nextToken",
        "tags": "tags",
    },
)
class CfnServiceProfileProps:
    def __init__(
        self,
        *,
        lo_ra_wan_get_service_profile_info: typing.Optional[typing.Union[CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty, _IResolvable_a771d0ef]] = None,
        lo_ra_wan_service_profile: typing.Optional[typing.Union[CfnServiceProfile.LoRaWANServiceProfileProperty, _IResolvable_a771d0ef]] = None,
        name: typing.Optional[builtins.str] = None,
        next_token: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
    ) -> None:
        """Properties for defining a ``AWS::IoTWireless::ServiceProfile``.

        :param lo_ra_wan_get_service_profile_info: ``AWS::IoTWireless::ServiceProfile.LoRaWANGetServiceProfileInfo``.
        :param lo_ra_wan_service_profile: ``AWS::IoTWireless::ServiceProfile.LoRaWANServiceProfile``.
        :param name: ``AWS::IoTWireless::ServiceProfile.Name``.
        :param next_token: ``AWS::IoTWireless::ServiceProfile.NextToken``.
        :param tags: ``AWS::IoTWireless::ServiceProfile.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if lo_ra_wan_get_service_profile_info is not None:
            self._values["lo_ra_wan_get_service_profile_info"] = lo_ra_wan_get_service_profile_info
        if lo_ra_wan_service_profile is not None:
            self._values["lo_ra_wan_service_profile"] = lo_ra_wan_service_profile
        if name is not None:
            self._values["name"] = name
        if next_token is not None:
            self._values["next_token"] = next_token
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def lo_ra_wan_get_service_profile_info(
        self,
    ) -> typing.Optional[typing.Union[CfnServiceProfile.LoRaWANGetServiceProfileInfoProperty, _IResolvable_a771d0ef]]:
        """``AWS::IoTWireless::ServiceProfile.LoRaWANGetServiceProfileInfo``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-lorawangetserviceprofileinfo
        """
        result = self._values.get("lo_ra_wan_get_service_profile_info")
        return result

    @builtins.property
    def lo_ra_wan_service_profile(
        self,
    ) -> typing.Optional[typing.Union[CfnServiceProfile.LoRaWANServiceProfileProperty, _IResolvable_a771d0ef]]:
        """``AWS::IoTWireless::ServiceProfile.LoRaWANServiceProfile``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile
        """
        result = self._values.get("lo_ra_wan_service_profile")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::ServiceProfile.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::ServiceProfile.NextToken``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-nexttoken
        """
        result = self._values.get("next_token")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        """``AWS::IoTWireless::ServiceProfile.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnWirelessDevice(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iotwireless.CfnWirelessDevice",
):
    """A CloudFormation ``AWS::IoTWireless::WirelessDevice``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html
    :cloudformationResource: AWS::IoTWireless::WirelessDevice
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        destination_name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        lo_ra_wan_device: typing.Optional[typing.Union["CfnWirelessDevice.LoRaWANDeviceProperty", _IResolvable_a771d0ef]] = None,
        name: typing.Optional[builtins.str] = None,
        next_token: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
    ) -> None:
        """Create a new ``AWS::IoTWireless::WirelessDevice``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param destination_name: ``AWS::IoTWireless::WirelessDevice.DestinationName``.
        :param type: ``AWS::IoTWireless::WirelessDevice.Type``.
        :param description: ``AWS::IoTWireless::WirelessDevice.Description``.
        :param lo_ra_wan_device: ``AWS::IoTWireless::WirelessDevice.LoRaWANDevice``.
        :param name: ``AWS::IoTWireless::WirelessDevice.Name``.
        :param next_token: ``AWS::IoTWireless::WirelessDevice.NextToken``.
        :param tags: ``AWS::IoTWireless::WirelessDevice.Tags``.
        """
        props = CfnWirelessDeviceProps(
            destination_name=destination_name,
            type=type,
            description=description,
            lo_ra_wan_device=lo_ra_wan_device,
            name=name,
            next_token=next_token,
            tags=tags,
        )

        jsii.create(CfnWirelessDevice, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        """
        :cloudformationAttribute: Id
        """
        return jsii.get(self, "attrId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrThingArn")
    def attr_thing_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: ThingArn
        """
        return jsii.get(self, "attrThingArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrThingName")
    def attr_thing_name(self) -> builtins.str:
        """
        :cloudformationAttribute: ThingName
        """
        return jsii.get(self, "attrThingName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::IoTWireless::WirelessDevice.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="destinationName")
    def destination_name(self) -> builtins.str:
        """``AWS::IoTWireless::WirelessDevice.DestinationName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-destinationname
        """
        return jsii.get(self, "destinationName")

    @destination_name.setter # type: ignore
    def destination_name(self, value: builtins.str) -> None:
        jsii.set(self, "destinationName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        """``AWS::IoTWireless::WirelessDevice.Type``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-type
        """
        return jsii.get(self, "type")

    @type.setter # type: ignore
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::WirelessDevice.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="loRaWanDevice")
    def lo_ra_wan_device(
        self,
    ) -> typing.Optional[typing.Union["CfnWirelessDevice.LoRaWANDeviceProperty", _IResolvable_a771d0ef]]:
        """``AWS::IoTWireless::WirelessDevice.LoRaWANDevice``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-lorawandevice
        """
        return jsii.get(self, "loRaWanDevice")

    @lo_ra_wan_device.setter # type: ignore
    def lo_ra_wan_device(
        self,
        value: typing.Optional[typing.Union["CfnWirelessDevice.LoRaWANDeviceProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "loRaWanDevice", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::WirelessDevice.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="nextToken")
    def next_token(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::WirelessDevice.NextToken``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-nexttoken
        """
        return jsii.get(self, "nextToken")

    @next_token.setter # type: ignore
    def next_token(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "nextToken", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_iotwireless.CfnWirelessDevice.AbpV10XProperty",
        jsii_struct_bases=[],
        name_mapping={"dev_addr": "devAddr", "session_keys": "sessionKeys"},
    )
    class AbpV10XProperty:
        def __init__(
            self,
            *,
            dev_addr: typing.Optional[builtins.str] = None,
            session_keys: typing.Optional[typing.Union["CfnWirelessDevice.SessionKeysAbpV10XProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param dev_addr: ``CfnWirelessDevice.AbpV10XProperty.DevAddr``.
            :param session_keys: ``CfnWirelessDevice.AbpV10XProperty.SessionKeys``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if dev_addr is not None:
                self._values["dev_addr"] = dev_addr
            if session_keys is not None:
                self._values["session_keys"] = session_keys

        @builtins.property
        def dev_addr(self) -> typing.Optional[builtins.str]:
            """``CfnWirelessDevice.AbpV10XProperty.DevAddr``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html#cfn-iotwireless-wirelessdevice-abpv10x-devaddr
            """
            result = self._values.get("dev_addr")
            return result

        @builtins.property
        def session_keys(
            self,
        ) -> typing.Optional[typing.Union["CfnWirelessDevice.SessionKeysAbpV10XProperty", _IResolvable_a771d0ef]]:
            """``CfnWirelessDevice.AbpV10XProperty.SessionKeys``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html#cfn-iotwireless-wirelessdevice-abpv10x-sessionkeys
            """
            result = self._values.get("session_keys")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AbpV10XProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iotwireless.CfnWirelessDevice.AbpV11Property",
        jsii_struct_bases=[],
        name_mapping={"dev_addr": "devAddr", "session_keys": "sessionKeys"},
    )
    class AbpV11Property:
        def __init__(
            self,
            *,
            dev_addr: typing.Optional[builtins.str] = None,
            session_keys: typing.Optional[typing.Union["CfnWirelessDevice.SessionKeysAbpV11Property", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param dev_addr: ``CfnWirelessDevice.AbpV11Property.DevAddr``.
            :param session_keys: ``CfnWirelessDevice.AbpV11Property.SessionKeys``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if dev_addr is not None:
                self._values["dev_addr"] = dev_addr
            if session_keys is not None:
                self._values["session_keys"] = session_keys

        @builtins.property
        def dev_addr(self) -> typing.Optional[builtins.str]:
            """``CfnWirelessDevice.AbpV11Property.DevAddr``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html#cfn-iotwireless-wirelessdevice-abpv11-devaddr
            """
            result = self._values.get("dev_addr")
            return result

        @builtins.property
        def session_keys(
            self,
        ) -> typing.Optional[typing.Union["CfnWirelessDevice.SessionKeysAbpV11Property", _IResolvable_a771d0ef]]:
            """``CfnWirelessDevice.AbpV11Property.SessionKeys``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html#cfn-iotwireless-wirelessdevice-abpv11-sessionkeys
            """
            result = self._values.get("session_keys")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AbpV11Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iotwireless.CfnWirelessDevice.LoRaWANDeviceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "abp_v10_x": "abpV10X",
            "abp_v11": "abpV11",
            "dev_eui": "devEui",
            "device_profile_id": "deviceProfileId",
            "otaa_v10_x": "otaaV10X",
            "otaa_v11": "otaaV11",
            "service_profile_id": "serviceProfileId",
        },
    )
    class LoRaWANDeviceProperty:
        def __init__(
            self,
            *,
            abp_v10_x: typing.Optional[typing.Union["CfnWirelessDevice.AbpV10XProperty", _IResolvable_a771d0ef]] = None,
            abp_v11: typing.Optional[typing.Union["CfnWirelessDevice.AbpV11Property", _IResolvable_a771d0ef]] = None,
            dev_eui: typing.Optional[builtins.str] = None,
            device_profile_id: typing.Optional[builtins.str] = None,
            otaa_v10_x: typing.Optional[typing.Union["CfnWirelessDevice.OtaaV10XProperty", _IResolvable_a771d0ef]] = None,
            otaa_v11: typing.Optional[typing.Union["CfnWirelessDevice.OtaaV11Property", _IResolvable_a771d0ef]] = None,
            service_profile_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param abp_v10_x: ``CfnWirelessDevice.LoRaWANDeviceProperty.AbpV10X``.
            :param abp_v11: ``CfnWirelessDevice.LoRaWANDeviceProperty.AbpV11``.
            :param dev_eui: ``CfnWirelessDevice.LoRaWANDeviceProperty.DevEui``.
            :param device_profile_id: ``CfnWirelessDevice.LoRaWANDeviceProperty.DeviceProfileId``.
            :param otaa_v10_x: ``CfnWirelessDevice.LoRaWANDeviceProperty.OtaaV10X``.
            :param otaa_v11: ``CfnWirelessDevice.LoRaWANDeviceProperty.OtaaV11``.
            :param service_profile_id: ``CfnWirelessDevice.LoRaWANDeviceProperty.ServiceProfileId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if abp_v10_x is not None:
                self._values["abp_v10_x"] = abp_v10_x
            if abp_v11 is not None:
                self._values["abp_v11"] = abp_v11
            if dev_eui is not None:
                self._values["dev_eui"] = dev_eui
            if device_profile_id is not None:
                self._values["device_profile_id"] = device_profile_id
            if otaa_v10_x is not None:
                self._values["otaa_v10_x"] = otaa_v10_x
            if otaa_v11 is not None:
                self._values["otaa_v11"] = otaa_v11
            if service_profile_id is not None:
                self._values["service_profile_id"] = service_profile_id

        @builtins.property
        def abp_v10_x(
            self,
        ) -> typing.Optional[typing.Union["CfnWirelessDevice.AbpV10XProperty", _IResolvable_a771d0ef]]:
            """``CfnWirelessDevice.LoRaWANDeviceProperty.AbpV10X``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-abpv10x
            """
            result = self._values.get("abp_v10_x")
            return result

        @builtins.property
        def abp_v11(
            self,
        ) -> typing.Optional[typing.Union["CfnWirelessDevice.AbpV11Property", _IResolvable_a771d0ef]]:
            """``CfnWirelessDevice.LoRaWANDeviceProperty.AbpV11``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-abpv11
            """
            result = self._values.get("abp_v11")
            return result

        @builtins.property
        def dev_eui(self) -> typing.Optional[builtins.str]:
            """``CfnWirelessDevice.LoRaWANDeviceProperty.DevEui``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-deveui
            """
            result = self._values.get("dev_eui")
            return result

        @builtins.property
        def device_profile_id(self) -> typing.Optional[builtins.str]:
            """``CfnWirelessDevice.LoRaWANDeviceProperty.DeviceProfileId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-deviceprofileid
            """
            result = self._values.get("device_profile_id")
            return result

        @builtins.property
        def otaa_v10_x(
            self,
        ) -> typing.Optional[typing.Union["CfnWirelessDevice.OtaaV10XProperty", _IResolvable_a771d0ef]]:
            """``CfnWirelessDevice.LoRaWANDeviceProperty.OtaaV10X``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-otaav10x
            """
            result = self._values.get("otaa_v10_x")
            return result

        @builtins.property
        def otaa_v11(
            self,
        ) -> typing.Optional[typing.Union["CfnWirelessDevice.OtaaV11Property", _IResolvable_a771d0ef]]:
            """``CfnWirelessDevice.LoRaWANDeviceProperty.OtaaV11``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-otaav11
            """
            result = self._values.get("otaa_v11")
            return result

        @builtins.property
        def service_profile_id(self) -> typing.Optional[builtins.str]:
            """``CfnWirelessDevice.LoRaWANDeviceProperty.ServiceProfileId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-serviceprofileid
            """
            result = self._values.get("service_profile_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANDeviceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iotwireless.CfnWirelessDevice.OtaaV10XProperty",
        jsii_struct_bases=[],
        name_mapping={"app_eui": "appEui", "app_key": "appKey"},
    )
    class OtaaV10XProperty:
        def __init__(
            self,
            *,
            app_eui: typing.Optional[builtins.str] = None,
            app_key: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param app_eui: ``CfnWirelessDevice.OtaaV10XProperty.AppEui``.
            :param app_key: ``CfnWirelessDevice.OtaaV10XProperty.AppKey``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if app_eui is not None:
                self._values["app_eui"] = app_eui
            if app_key is not None:
                self._values["app_key"] = app_key

        @builtins.property
        def app_eui(self) -> typing.Optional[builtins.str]:
            """``CfnWirelessDevice.OtaaV10XProperty.AppEui``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html#cfn-iotwireless-wirelessdevice-otaav10x-appeui
            """
            result = self._values.get("app_eui")
            return result

        @builtins.property
        def app_key(self) -> typing.Optional[builtins.str]:
            """``CfnWirelessDevice.OtaaV10XProperty.AppKey``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html#cfn-iotwireless-wirelessdevice-otaav10x-appkey
            """
            result = self._values.get("app_key")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OtaaV10XProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iotwireless.CfnWirelessDevice.OtaaV11Property",
        jsii_struct_bases=[],
        name_mapping={"app_key": "appKey", "join_eui": "joinEui", "nwk_key": "nwkKey"},
    )
    class OtaaV11Property:
        def __init__(
            self,
            *,
            app_key: typing.Optional[builtins.str] = None,
            join_eui: typing.Optional[builtins.str] = None,
            nwk_key: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param app_key: ``CfnWirelessDevice.OtaaV11Property.AppKey``.
            :param join_eui: ``CfnWirelessDevice.OtaaV11Property.JoinEui``.
            :param nwk_key: ``CfnWirelessDevice.OtaaV11Property.NwkKey``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if app_key is not None:
                self._values["app_key"] = app_key
            if join_eui is not None:
                self._values["join_eui"] = join_eui
            if nwk_key is not None:
                self._values["nwk_key"] = nwk_key

        @builtins.property
        def app_key(self) -> typing.Optional[builtins.str]:
            """``CfnWirelessDevice.OtaaV11Property.AppKey``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-appkey
            """
            result = self._values.get("app_key")
            return result

        @builtins.property
        def join_eui(self) -> typing.Optional[builtins.str]:
            """``CfnWirelessDevice.OtaaV11Property.JoinEui``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-joineui
            """
            result = self._values.get("join_eui")
            return result

        @builtins.property
        def nwk_key(self) -> typing.Optional[builtins.str]:
            """``CfnWirelessDevice.OtaaV11Property.NwkKey``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-nwkkey
            """
            result = self._values.get("nwk_key")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OtaaV11Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iotwireless.CfnWirelessDevice.SessionKeysAbpV10XProperty",
        jsii_struct_bases=[],
        name_mapping={"app_s_key": "appSKey", "nwk_s_key": "nwkSKey"},
    )
    class SessionKeysAbpV10XProperty:
        def __init__(
            self,
            *,
            app_s_key: typing.Optional[builtins.str] = None,
            nwk_s_key: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param app_s_key: ``CfnWirelessDevice.SessionKeysAbpV10XProperty.AppSKey``.
            :param nwk_s_key: ``CfnWirelessDevice.SessionKeysAbpV10XProperty.NwkSKey``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if app_s_key is not None:
                self._values["app_s_key"] = app_s_key
            if nwk_s_key is not None:
                self._values["nwk_s_key"] = nwk_s_key

        @builtins.property
        def app_s_key(self) -> typing.Optional[builtins.str]:
            """``CfnWirelessDevice.SessionKeysAbpV10XProperty.AppSKey``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-appskey
            """
            result = self._values.get("app_s_key")
            return result

        @builtins.property
        def nwk_s_key(self) -> typing.Optional[builtins.str]:
            """``CfnWirelessDevice.SessionKeysAbpV10XProperty.NwkSKey``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-nwkskey
            """
            result = self._values.get("nwk_s_key")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SessionKeysAbpV10XProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iotwireless.CfnWirelessDevice.SessionKeysAbpV11Property",
        jsii_struct_bases=[],
        name_mapping={
            "app_s_key": "appSKey",
            "f_nwk_s_int_key": "fNwkSIntKey",
            "nwk_s_enc_key": "nwkSEncKey",
            "s_nwk_s_int_key": "sNwkSIntKey",
        },
    )
    class SessionKeysAbpV11Property:
        def __init__(
            self,
            *,
            app_s_key: typing.Optional[builtins.str] = None,
            f_nwk_s_int_key: typing.Optional[builtins.str] = None,
            nwk_s_enc_key: typing.Optional[builtins.str] = None,
            s_nwk_s_int_key: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param app_s_key: ``CfnWirelessDevice.SessionKeysAbpV11Property.AppSKey``.
            :param f_nwk_s_int_key: ``CfnWirelessDevice.SessionKeysAbpV11Property.FNwkSIntKey``.
            :param nwk_s_enc_key: ``CfnWirelessDevice.SessionKeysAbpV11Property.NwkSEncKey``.
            :param s_nwk_s_int_key: ``CfnWirelessDevice.SessionKeysAbpV11Property.SNwkSIntKey``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if app_s_key is not None:
                self._values["app_s_key"] = app_s_key
            if f_nwk_s_int_key is not None:
                self._values["f_nwk_s_int_key"] = f_nwk_s_int_key
            if nwk_s_enc_key is not None:
                self._values["nwk_s_enc_key"] = nwk_s_enc_key
            if s_nwk_s_int_key is not None:
                self._values["s_nwk_s_int_key"] = s_nwk_s_int_key

        @builtins.property
        def app_s_key(self) -> typing.Optional[builtins.str]:
            """``CfnWirelessDevice.SessionKeysAbpV11Property.AppSKey``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-appskey
            """
            result = self._values.get("app_s_key")
            return result

        @builtins.property
        def f_nwk_s_int_key(self) -> typing.Optional[builtins.str]:
            """``CfnWirelessDevice.SessionKeysAbpV11Property.FNwkSIntKey``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-fnwksintkey
            """
            result = self._values.get("f_nwk_s_int_key")
            return result

        @builtins.property
        def nwk_s_enc_key(self) -> typing.Optional[builtins.str]:
            """``CfnWirelessDevice.SessionKeysAbpV11Property.NwkSEncKey``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-nwksenckey
            """
            result = self._values.get("nwk_s_enc_key")
            return result

        @builtins.property
        def s_nwk_s_int_key(self) -> typing.Optional[builtins.str]:
            """``CfnWirelessDevice.SessionKeysAbpV11Property.SNwkSIntKey``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-snwksintkey
            """
            result = self._values.get("s_nwk_s_int_key")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SessionKeysAbpV11Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_iotwireless.CfnWirelessDeviceProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_name": "destinationName",
        "type": "type",
        "description": "description",
        "lo_ra_wan_device": "loRaWanDevice",
        "name": "name",
        "next_token": "nextToken",
        "tags": "tags",
    },
)
class CfnWirelessDeviceProps:
    def __init__(
        self,
        *,
        destination_name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        lo_ra_wan_device: typing.Optional[typing.Union[CfnWirelessDevice.LoRaWANDeviceProperty, _IResolvable_a771d0ef]] = None,
        name: typing.Optional[builtins.str] = None,
        next_token: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
    ) -> None:
        """Properties for defining a ``AWS::IoTWireless::WirelessDevice``.

        :param destination_name: ``AWS::IoTWireless::WirelessDevice.DestinationName``.
        :param type: ``AWS::IoTWireless::WirelessDevice.Type``.
        :param description: ``AWS::IoTWireless::WirelessDevice.Description``.
        :param lo_ra_wan_device: ``AWS::IoTWireless::WirelessDevice.LoRaWANDevice``.
        :param name: ``AWS::IoTWireless::WirelessDevice.Name``.
        :param next_token: ``AWS::IoTWireless::WirelessDevice.NextToken``.
        :param tags: ``AWS::IoTWireless::WirelessDevice.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "destination_name": destination_name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if lo_ra_wan_device is not None:
            self._values["lo_ra_wan_device"] = lo_ra_wan_device
        if name is not None:
            self._values["name"] = name
        if next_token is not None:
            self._values["next_token"] = next_token
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def destination_name(self) -> builtins.str:
        """``AWS::IoTWireless::WirelessDevice.DestinationName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-destinationname
        """
        result = self._values.get("destination_name")
        assert result is not None, "Required property 'destination_name' is missing"
        return result

    @builtins.property
    def type(self) -> builtins.str:
        """``AWS::IoTWireless::WirelessDevice.Type``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-type
        """
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::WirelessDevice.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def lo_ra_wan_device(
        self,
    ) -> typing.Optional[typing.Union[CfnWirelessDevice.LoRaWANDeviceProperty, _IResolvable_a771d0ef]]:
        """``AWS::IoTWireless::WirelessDevice.LoRaWANDevice``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-lorawandevice
        """
        result = self._values.get("lo_ra_wan_device")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::WirelessDevice.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::WirelessDevice.NextToken``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-nexttoken
        """
        result = self._values.get("next_token")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        """``AWS::IoTWireless::WirelessDevice.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWirelessDeviceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnWirelessGateway(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iotwireless.CfnWirelessGateway",
):
    """A CloudFormation ``AWS::IoTWireless::WirelessGateway``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html
    :cloudformationResource: AWS::IoTWireless::WirelessGateway
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        lo_ra_wan_gateway: typing.Union["CfnWirelessGateway.LoRaWANGatewayProperty", _IResolvable_a771d0ef],
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        next_token: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
        thing_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::IoTWireless::WirelessGateway``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param lo_ra_wan_gateway: ``AWS::IoTWireless::WirelessGateway.LoRaWANGateway``.
        :param description: ``AWS::IoTWireless::WirelessGateway.Description``.
        :param name: ``AWS::IoTWireless::WirelessGateway.Name``.
        :param next_token: ``AWS::IoTWireless::WirelessGateway.NextToken``.
        :param tags: ``AWS::IoTWireless::WirelessGateway.Tags``.
        :param thing_name: ``AWS::IoTWireless::WirelessGateway.ThingName``.
        """
        props = CfnWirelessGatewayProps(
            lo_ra_wan_gateway=lo_ra_wan_gateway,
            description=description,
            name=name,
            next_token=next_token,
            tags=tags,
            thing_name=thing_name,
        )

        jsii.create(CfnWirelessGateway, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        """
        :cloudformationAttribute: Id
        """
        return jsii.get(self, "attrId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrThingArn")
    def attr_thing_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: ThingArn
        """
        return jsii.get(self, "attrThingArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::IoTWireless::WirelessGateway.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="loRaWanGateway")
    def lo_ra_wan_gateway(
        self,
    ) -> typing.Union["CfnWirelessGateway.LoRaWANGatewayProperty", _IResolvable_a771d0ef]:
        """``AWS::IoTWireless::WirelessGateway.LoRaWANGateway``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-lorawangateway
        """
        return jsii.get(self, "loRaWanGateway")

    @lo_ra_wan_gateway.setter # type: ignore
    def lo_ra_wan_gateway(
        self,
        value: typing.Union["CfnWirelessGateway.LoRaWANGatewayProperty", _IResolvable_a771d0ef],
    ) -> None:
        jsii.set(self, "loRaWanGateway", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::WirelessGateway.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::WirelessGateway.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="nextToken")
    def next_token(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::WirelessGateway.NextToken``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-nexttoken
        """
        return jsii.get(self, "nextToken")

    @next_token.setter # type: ignore
    def next_token(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "nextToken", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="thingName")
    def thing_name(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::WirelessGateway.ThingName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-thingname
        """
        return jsii.get(self, "thingName")

    @thing_name.setter # type: ignore
    def thing_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "thingName", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_iotwireless.CfnWirelessGateway.LoRaWANGatewayProperty",
        jsii_struct_bases=[],
        name_mapping={"gateway_eui": "gatewayEui", "rf_region": "rfRegion"},
    )
    class LoRaWANGatewayProperty:
        def __init__(
            self,
            *,
            gateway_eui: typing.Optional[builtins.str] = None,
            rf_region: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param gateway_eui: ``CfnWirelessGateway.LoRaWANGatewayProperty.GatewayEui``.
            :param rf_region: ``CfnWirelessGateway.LoRaWANGatewayProperty.RfRegion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if gateway_eui is not None:
                self._values["gateway_eui"] = gateway_eui
            if rf_region is not None:
                self._values["rf_region"] = rf_region

        @builtins.property
        def gateway_eui(self) -> typing.Optional[builtins.str]:
            """``CfnWirelessGateway.LoRaWANGatewayProperty.GatewayEui``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html#cfn-iotwireless-wirelessgateway-lorawangateway-gatewayeui
            """
            result = self._values.get("gateway_eui")
            return result

        @builtins.property
        def rf_region(self) -> typing.Optional[builtins.str]:
            """``CfnWirelessGateway.LoRaWANGatewayProperty.RfRegion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html#cfn-iotwireless-wirelessgateway-lorawangateway-rfregion
            """
            result = self._values.get("rf_region")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANGatewayProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_iotwireless.CfnWirelessGatewayProps",
    jsii_struct_bases=[],
    name_mapping={
        "lo_ra_wan_gateway": "loRaWanGateway",
        "description": "description",
        "name": "name",
        "next_token": "nextToken",
        "tags": "tags",
        "thing_name": "thingName",
    },
)
class CfnWirelessGatewayProps:
    def __init__(
        self,
        *,
        lo_ra_wan_gateway: typing.Union[CfnWirelessGateway.LoRaWANGatewayProperty, _IResolvable_a771d0ef],
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        next_token: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
        thing_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::IoTWireless::WirelessGateway``.

        :param lo_ra_wan_gateway: ``AWS::IoTWireless::WirelessGateway.LoRaWANGateway``.
        :param description: ``AWS::IoTWireless::WirelessGateway.Description``.
        :param name: ``AWS::IoTWireless::WirelessGateway.Name``.
        :param next_token: ``AWS::IoTWireless::WirelessGateway.NextToken``.
        :param tags: ``AWS::IoTWireless::WirelessGateway.Tags``.
        :param thing_name: ``AWS::IoTWireless::WirelessGateway.ThingName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "lo_ra_wan_gateway": lo_ra_wan_gateway,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if next_token is not None:
            self._values["next_token"] = next_token
        if tags is not None:
            self._values["tags"] = tags
        if thing_name is not None:
            self._values["thing_name"] = thing_name

    @builtins.property
    def lo_ra_wan_gateway(
        self,
    ) -> typing.Union[CfnWirelessGateway.LoRaWANGatewayProperty, _IResolvable_a771d0ef]:
        """``AWS::IoTWireless::WirelessGateway.LoRaWANGateway``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-lorawangateway
        """
        result = self._values.get("lo_ra_wan_gateway")
        assert result is not None, "Required property 'lo_ra_wan_gateway' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::WirelessGateway.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::WirelessGateway.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::WirelessGateway.NextToken``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-nexttoken
        """
        result = self._values.get("next_token")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        """``AWS::IoTWireless::WirelessGateway.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-tags
        """
        result = self._values.get("tags")
        return result

    @builtins.property
    def thing_name(self) -> typing.Optional[builtins.str]:
        """``AWS::IoTWireless::WirelessGateway.ThingName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-thingname
        """
        result = self._values.get("thing_name")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWirelessGatewayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDestination",
    "CfnDestinationProps",
    "CfnDeviceProfile",
    "CfnDeviceProfileProps",
    "CfnServiceProfile",
    "CfnServiceProfileProps",
    "CfnWirelessDevice",
    "CfnWirelessDeviceProps",
    "CfnWirelessGateway",
    "CfnWirelessGatewayProps",
]

publication.publish()
