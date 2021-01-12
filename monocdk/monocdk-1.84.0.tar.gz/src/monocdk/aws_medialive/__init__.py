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
    Construct as _Construct_e78e779f,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    TagManager as _TagManager_0b7ab120,
    TreeInspector as _TreeInspector_1cd1894e,
)


@jsii.implements(_IInspectable_82c04a63)
class CfnChannel(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_medialive.CfnChannel",
):
    """A CloudFormation ``AWS::MediaLive::Channel``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html
    :cloudformationResource: AWS::MediaLive::Channel
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        channel_class: typing.Optional[builtins.str] = None,
        destinations: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.OutputDestinationProperty", _IResolvable_a771d0ef]]]] = None,
        encoder_settings: typing.Optional[typing.Union["CfnChannel.EncoderSettingsProperty", _IResolvable_a771d0ef]] = None,
        input_attachments: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.InputAttachmentProperty", _IResolvable_a771d0ef]]]] = None,
        input_specification: typing.Optional[typing.Union["CfnChannel.InputSpecificationProperty", _IResolvable_a771d0ef]] = None,
        log_level: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        """Create a new ``AWS::MediaLive::Channel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param channel_class: ``AWS::MediaLive::Channel.ChannelClass``.
        :param destinations: ``AWS::MediaLive::Channel.Destinations``.
        :param encoder_settings: ``AWS::MediaLive::Channel.EncoderSettings``.
        :param input_attachments: ``AWS::MediaLive::Channel.InputAttachments``.
        :param input_specification: ``AWS::MediaLive::Channel.InputSpecification``.
        :param log_level: ``AWS::MediaLive::Channel.LogLevel``.
        :param name: ``AWS::MediaLive::Channel.Name``.
        :param role_arn: ``AWS::MediaLive::Channel.RoleArn``.
        :param tags: ``AWS::MediaLive::Channel.Tags``.
        """
        props = CfnChannelProps(
            channel_class=channel_class,
            destinations=destinations,
            encoder_settings=encoder_settings,
            input_attachments=input_attachments,
            input_specification=input_specification,
            log_level=log_level,
            name=name,
            role_arn=role_arn,
            tags=tags,
        )

        jsii.create(CfnChannel, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrInputs")
    def attr_inputs(self) -> typing.List[builtins.str]:
        """
        :cloudformationAttribute: Inputs
        """
        return jsii.get(self, "attrInputs")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::MediaLive::Channel.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="channelClass")
    def channel_class(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaLive::Channel.ChannelClass``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-channelclass
        """
        return jsii.get(self, "channelClass")

    @channel_class.setter # type: ignore
    def channel_class(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "channelClass", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="destinations")
    def destinations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.OutputDestinationProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::MediaLive::Channel.Destinations``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-destinations
        """
        return jsii.get(self, "destinations")

    @destinations.setter # type: ignore
    def destinations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.OutputDestinationProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "destinations", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="encoderSettings")
    def encoder_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnChannel.EncoderSettingsProperty", _IResolvable_a771d0ef]]:
        """``AWS::MediaLive::Channel.EncoderSettings``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-encodersettings
        """
        return jsii.get(self, "encoderSettings")

    @encoder_settings.setter # type: ignore
    def encoder_settings(
        self,
        value: typing.Optional[typing.Union["CfnChannel.EncoderSettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "encoderSettings", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="inputAttachments")
    def input_attachments(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.InputAttachmentProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::MediaLive::Channel.InputAttachments``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-inputattachments
        """
        return jsii.get(self, "inputAttachments")

    @input_attachments.setter # type: ignore
    def input_attachments(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.InputAttachmentProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "inputAttachments", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="inputSpecification")
    def input_specification(
        self,
    ) -> typing.Optional[typing.Union["CfnChannel.InputSpecificationProperty", _IResolvable_a771d0ef]]:
        """``AWS::MediaLive::Channel.InputSpecification``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-inputspecification
        """
        return jsii.get(self, "inputSpecification")

    @input_specification.setter # type: ignore
    def input_specification(
        self,
        value: typing.Optional[typing.Union["CfnChannel.InputSpecificationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "inputSpecification", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="logLevel")
    def log_level(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaLive::Channel.LogLevel``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-loglevel
        """
        return jsii.get(self, "logLevel")

    @log_level.setter # type: ignore
    def log_level(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "logLevel", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaLive::Channel.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaLive::Channel.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-rolearn
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter # type: ignore
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "roleArn", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.AacSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bitrate": "bitrate",
            "coding_mode": "codingMode",
            "input_type": "inputType",
            "profile": "profile",
            "rate_control_mode": "rateControlMode",
            "raw_format": "rawFormat",
            "sample_rate": "sampleRate",
            "spec": "spec",
            "vbr_quality": "vbrQuality",
        },
    )
    class AacSettingsProperty:
        def __init__(
            self,
            *,
            bitrate: typing.Optional[jsii.Number] = None,
            coding_mode: typing.Optional[builtins.str] = None,
            input_type: typing.Optional[builtins.str] = None,
            profile: typing.Optional[builtins.str] = None,
            rate_control_mode: typing.Optional[builtins.str] = None,
            raw_format: typing.Optional[builtins.str] = None,
            sample_rate: typing.Optional[jsii.Number] = None,
            spec: typing.Optional[builtins.str] = None,
            vbr_quality: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param bitrate: ``CfnChannel.AacSettingsProperty.Bitrate``.
            :param coding_mode: ``CfnChannel.AacSettingsProperty.CodingMode``.
            :param input_type: ``CfnChannel.AacSettingsProperty.InputType``.
            :param profile: ``CfnChannel.AacSettingsProperty.Profile``.
            :param rate_control_mode: ``CfnChannel.AacSettingsProperty.RateControlMode``.
            :param raw_format: ``CfnChannel.AacSettingsProperty.RawFormat``.
            :param sample_rate: ``CfnChannel.AacSettingsProperty.SampleRate``.
            :param spec: ``CfnChannel.AacSettingsProperty.Spec``.
            :param vbr_quality: ``CfnChannel.AacSettingsProperty.VbrQuality``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if bitrate is not None:
                self._values["bitrate"] = bitrate
            if coding_mode is not None:
                self._values["coding_mode"] = coding_mode
            if input_type is not None:
                self._values["input_type"] = input_type
            if profile is not None:
                self._values["profile"] = profile
            if rate_control_mode is not None:
                self._values["rate_control_mode"] = rate_control_mode
            if raw_format is not None:
                self._values["raw_format"] = raw_format
            if sample_rate is not None:
                self._values["sample_rate"] = sample_rate
            if spec is not None:
                self._values["spec"] = spec
            if vbr_quality is not None:
                self._values["vbr_quality"] = vbr_quality

        @builtins.property
        def bitrate(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.AacSettingsProperty.Bitrate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-bitrate
            """
            result = self._values.get("bitrate")
            return result

        @builtins.property
        def coding_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AacSettingsProperty.CodingMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-codingmode
            """
            result = self._values.get("coding_mode")
            return result

        @builtins.property
        def input_type(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AacSettingsProperty.InputType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-inputtype
            """
            result = self._values.get("input_type")
            return result

        @builtins.property
        def profile(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AacSettingsProperty.Profile``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-profile
            """
            result = self._values.get("profile")
            return result

        @builtins.property
        def rate_control_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AacSettingsProperty.RateControlMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-ratecontrolmode
            """
            result = self._values.get("rate_control_mode")
            return result

        @builtins.property
        def raw_format(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AacSettingsProperty.RawFormat``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-rawformat
            """
            result = self._values.get("raw_format")
            return result

        @builtins.property
        def sample_rate(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.AacSettingsProperty.SampleRate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-samplerate
            """
            result = self._values.get("sample_rate")
            return result

        @builtins.property
        def spec(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AacSettingsProperty.Spec``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-spec
            """
            result = self._values.get("spec")
            return result

        @builtins.property
        def vbr_quality(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AacSettingsProperty.VbrQuality``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-vbrquality
            """
            result = self._values.get("vbr_quality")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AacSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.Ac3SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bitrate": "bitrate",
            "bitstream_mode": "bitstreamMode",
            "coding_mode": "codingMode",
            "dialnorm": "dialnorm",
            "drc_profile": "drcProfile",
            "lfe_filter": "lfeFilter",
            "metadata_control": "metadataControl",
        },
    )
    class Ac3SettingsProperty:
        def __init__(
            self,
            *,
            bitrate: typing.Optional[jsii.Number] = None,
            bitstream_mode: typing.Optional[builtins.str] = None,
            coding_mode: typing.Optional[builtins.str] = None,
            dialnorm: typing.Optional[jsii.Number] = None,
            drc_profile: typing.Optional[builtins.str] = None,
            lfe_filter: typing.Optional[builtins.str] = None,
            metadata_control: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param bitrate: ``CfnChannel.Ac3SettingsProperty.Bitrate``.
            :param bitstream_mode: ``CfnChannel.Ac3SettingsProperty.BitstreamMode``.
            :param coding_mode: ``CfnChannel.Ac3SettingsProperty.CodingMode``.
            :param dialnorm: ``CfnChannel.Ac3SettingsProperty.Dialnorm``.
            :param drc_profile: ``CfnChannel.Ac3SettingsProperty.DrcProfile``.
            :param lfe_filter: ``CfnChannel.Ac3SettingsProperty.LfeFilter``.
            :param metadata_control: ``CfnChannel.Ac3SettingsProperty.MetadataControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if bitrate is not None:
                self._values["bitrate"] = bitrate
            if bitstream_mode is not None:
                self._values["bitstream_mode"] = bitstream_mode
            if coding_mode is not None:
                self._values["coding_mode"] = coding_mode
            if dialnorm is not None:
                self._values["dialnorm"] = dialnorm
            if drc_profile is not None:
                self._values["drc_profile"] = drc_profile
            if lfe_filter is not None:
                self._values["lfe_filter"] = lfe_filter
            if metadata_control is not None:
                self._values["metadata_control"] = metadata_control

        @builtins.property
        def bitrate(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.Ac3SettingsProperty.Bitrate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-bitrate
            """
            result = self._values.get("bitrate")
            return result

        @builtins.property
        def bitstream_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Ac3SettingsProperty.BitstreamMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-bitstreammode
            """
            result = self._values.get("bitstream_mode")
            return result

        @builtins.property
        def coding_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Ac3SettingsProperty.CodingMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-codingmode
            """
            result = self._values.get("coding_mode")
            return result

        @builtins.property
        def dialnorm(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.Ac3SettingsProperty.Dialnorm``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-dialnorm
            """
            result = self._values.get("dialnorm")
            return result

        @builtins.property
        def drc_profile(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Ac3SettingsProperty.DrcProfile``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-drcprofile
            """
            result = self._values.get("drc_profile")
            return result

        @builtins.property
        def lfe_filter(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Ac3SettingsProperty.LfeFilter``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-lfefilter
            """
            result = self._values.get("lfe_filter")
            return result

        @builtins.property
        def metadata_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Ac3SettingsProperty.MetadataControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-metadatacontrol
            """
            result = self._values.get("metadata_control")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Ac3SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.ArchiveContainerSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"m2_ts_settings": "m2TsSettings"},
    )
    class ArchiveContainerSettingsProperty:
        def __init__(
            self,
            *,
            m2_ts_settings: typing.Optional[typing.Union["CfnChannel.M2tsSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param m2_ts_settings: ``CfnChannel.ArchiveContainerSettingsProperty.M2tsSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecontainersettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if m2_ts_settings is not None:
                self._values["m2_ts_settings"] = m2_ts_settings

        @builtins.property
        def m2_ts_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.M2tsSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.ArchiveContainerSettingsProperty.M2tsSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecontainersettings.html#cfn-medialive-channel-archivecontainersettings-m2tssettings
            """
            result = self._values.get("m2_ts_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ArchiveContainerSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.ArchiveGroupSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination": "destination",
            "rollover_interval": "rolloverInterval",
        },
    )
    class ArchiveGroupSettingsProperty:
        def __init__(
            self,
            *,
            destination: typing.Optional[typing.Union["CfnChannel.OutputLocationRefProperty", _IResolvable_a771d0ef]] = None,
            rollover_interval: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param destination: ``CfnChannel.ArchiveGroupSettingsProperty.Destination``.
            :param rollover_interval: ``CfnChannel.ArchiveGroupSettingsProperty.RolloverInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivegroupsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if destination is not None:
                self._values["destination"] = destination
            if rollover_interval is not None:
                self._values["rollover_interval"] = rollover_interval

        @builtins.property
        def destination(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.OutputLocationRefProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.ArchiveGroupSettingsProperty.Destination``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivegroupsettings.html#cfn-medialive-channel-archivegroupsettings-destination
            """
            result = self._values.get("destination")
            return result

        @builtins.property
        def rollover_interval(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.ArchiveGroupSettingsProperty.RolloverInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivegroupsettings.html#cfn-medialive-channel-archivegroupsettings-rolloverinterval
            """
            result = self._values.get("rollover_interval")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ArchiveGroupSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.ArchiveOutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_settings": "containerSettings",
            "extension": "extension",
            "name_modifier": "nameModifier",
        },
    )
    class ArchiveOutputSettingsProperty:
        def __init__(
            self,
            *,
            container_settings: typing.Optional[typing.Union["CfnChannel.ArchiveContainerSettingsProperty", _IResolvable_a771d0ef]] = None,
            extension: typing.Optional[builtins.str] = None,
            name_modifier: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param container_settings: ``CfnChannel.ArchiveOutputSettingsProperty.ContainerSettings``.
            :param extension: ``CfnChannel.ArchiveOutputSettingsProperty.Extension``.
            :param name_modifier: ``CfnChannel.ArchiveOutputSettingsProperty.NameModifier``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archiveoutputsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if container_settings is not None:
                self._values["container_settings"] = container_settings
            if extension is not None:
                self._values["extension"] = extension
            if name_modifier is not None:
                self._values["name_modifier"] = name_modifier

        @builtins.property
        def container_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.ArchiveContainerSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.ArchiveOutputSettingsProperty.ContainerSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archiveoutputsettings.html#cfn-medialive-channel-archiveoutputsettings-containersettings
            """
            result = self._values.get("container_settings")
            return result

        @builtins.property
        def extension(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.ArchiveOutputSettingsProperty.Extension``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archiveoutputsettings.html#cfn-medialive-channel-archiveoutputsettings-extension
            """
            result = self._values.get("extension")
            return result

        @builtins.property
        def name_modifier(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.ArchiveOutputSettingsProperty.NameModifier``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archiveoutputsettings.html#cfn-medialive-channel-archiveoutputsettings-namemodifier
            """
            result = self._values.get("name_modifier")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ArchiveOutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.AribDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class AribDestinationSettingsProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aribdestinationsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AribDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.AribSourceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class AribSourceSettingsProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aribsourcesettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AribSourceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.AudioChannelMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "input_channel_levels": "inputChannelLevels",
            "output_channel": "outputChannel",
        },
    )
    class AudioChannelMappingProperty:
        def __init__(
            self,
            *,
            input_channel_levels: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.InputChannelLevelProperty", _IResolvable_a771d0ef]]]] = None,
            output_channel: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param input_channel_levels: ``CfnChannel.AudioChannelMappingProperty.InputChannelLevels``.
            :param output_channel: ``CfnChannel.AudioChannelMappingProperty.OutputChannel``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiochannelmapping.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if input_channel_levels is not None:
                self._values["input_channel_levels"] = input_channel_levels
            if output_channel is not None:
                self._values["output_channel"] = output_channel

        @builtins.property
        def input_channel_levels(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.InputChannelLevelProperty", _IResolvable_a771d0ef]]]]:
            """``CfnChannel.AudioChannelMappingProperty.InputChannelLevels``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiochannelmapping.html#cfn-medialive-channel-audiochannelmapping-inputchannellevels
            """
            result = self._values.get("input_channel_levels")
            return result

        @builtins.property
        def output_channel(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.AudioChannelMappingProperty.OutputChannel``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiochannelmapping.html#cfn-medialive-channel-audiochannelmapping-outputchannel
            """
            result = self._values.get("output_channel")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioChannelMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.AudioCodecSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aac_settings": "aacSettings",
            "ac3_settings": "ac3Settings",
            "eac3_settings": "eac3Settings",
            "mp2_settings": "mp2Settings",
            "pass_through_settings": "passThroughSettings",
        },
    )
    class AudioCodecSettingsProperty:
        def __init__(
            self,
            *,
            aac_settings: typing.Optional[typing.Union["CfnChannel.AacSettingsProperty", _IResolvable_a771d0ef]] = None,
            ac3_settings: typing.Optional[typing.Union["CfnChannel.Ac3SettingsProperty", _IResolvable_a771d0ef]] = None,
            eac3_settings: typing.Optional[typing.Union["CfnChannel.Eac3SettingsProperty", _IResolvable_a771d0ef]] = None,
            mp2_settings: typing.Optional[typing.Union["CfnChannel.Mp2SettingsProperty", _IResolvable_a771d0ef]] = None,
            pass_through_settings: typing.Optional[typing.Union["CfnChannel.PassThroughSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param aac_settings: ``CfnChannel.AudioCodecSettingsProperty.AacSettings``.
            :param ac3_settings: ``CfnChannel.AudioCodecSettingsProperty.Ac3Settings``.
            :param eac3_settings: ``CfnChannel.AudioCodecSettingsProperty.Eac3Settings``.
            :param mp2_settings: ``CfnChannel.AudioCodecSettingsProperty.Mp2Settings``.
            :param pass_through_settings: ``CfnChannel.AudioCodecSettingsProperty.PassThroughSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if aac_settings is not None:
                self._values["aac_settings"] = aac_settings
            if ac3_settings is not None:
                self._values["ac3_settings"] = ac3_settings
            if eac3_settings is not None:
                self._values["eac3_settings"] = eac3_settings
            if mp2_settings is not None:
                self._values["mp2_settings"] = mp2_settings
            if pass_through_settings is not None:
                self._values["pass_through_settings"] = pass_through_settings

        @builtins.property
        def aac_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.AacSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.AudioCodecSettingsProperty.AacSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html#cfn-medialive-channel-audiocodecsettings-aacsettings
            """
            result = self._values.get("aac_settings")
            return result

        @builtins.property
        def ac3_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.Ac3SettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.AudioCodecSettingsProperty.Ac3Settings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html#cfn-medialive-channel-audiocodecsettings-ac3settings
            """
            result = self._values.get("ac3_settings")
            return result

        @builtins.property
        def eac3_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.Eac3SettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.AudioCodecSettingsProperty.Eac3Settings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html#cfn-medialive-channel-audiocodecsettings-eac3settings
            """
            result = self._values.get("eac3_settings")
            return result

        @builtins.property
        def mp2_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.Mp2SettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.AudioCodecSettingsProperty.Mp2Settings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html#cfn-medialive-channel-audiocodecsettings-mp2settings
            """
            result = self._values.get("mp2_settings")
            return result

        @builtins.property
        def pass_through_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.PassThroughSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.AudioCodecSettingsProperty.PassThroughSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html#cfn-medialive-channel-audiocodecsettings-passthroughsettings
            """
            result = self._values.get("pass_through_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioCodecSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.AudioDescriptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_normalization_settings": "audioNormalizationSettings",
            "audio_selector_name": "audioSelectorName",
            "audio_type": "audioType",
            "audio_type_control": "audioTypeControl",
            "codec_settings": "codecSettings",
            "language_code": "languageCode",
            "language_code_control": "languageCodeControl",
            "name": "name",
            "remix_settings": "remixSettings",
            "stream_name": "streamName",
        },
    )
    class AudioDescriptionProperty:
        def __init__(
            self,
            *,
            audio_normalization_settings: typing.Optional[typing.Union["CfnChannel.AudioNormalizationSettingsProperty", _IResolvable_a771d0ef]] = None,
            audio_selector_name: typing.Optional[builtins.str] = None,
            audio_type: typing.Optional[builtins.str] = None,
            audio_type_control: typing.Optional[builtins.str] = None,
            codec_settings: typing.Optional[typing.Union["CfnChannel.AudioCodecSettingsProperty", _IResolvable_a771d0ef]] = None,
            language_code: typing.Optional[builtins.str] = None,
            language_code_control: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            remix_settings: typing.Optional[typing.Union["CfnChannel.RemixSettingsProperty", _IResolvable_a771d0ef]] = None,
            stream_name: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param audio_normalization_settings: ``CfnChannel.AudioDescriptionProperty.AudioNormalizationSettings``.
            :param audio_selector_name: ``CfnChannel.AudioDescriptionProperty.AudioSelectorName``.
            :param audio_type: ``CfnChannel.AudioDescriptionProperty.AudioType``.
            :param audio_type_control: ``CfnChannel.AudioDescriptionProperty.AudioTypeControl``.
            :param codec_settings: ``CfnChannel.AudioDescriptionProperty.CodecSettings``.
            :param language_code: ``CfnChannel.AudioDescriptionProperty.LanguageCode``.
            :param language_code_control: ``CfnChannel.AudioDescriptionProperty.LanguageCodeControl``.
            :param name: ``CfnChannel.AudioDescriptionProperty.Name``.
            :param remix_settings: ``CfnChannel.AudioDescriptionProperty.RemixSettings``.
            :param stream_name: ``CfnChannel.AudioDescriptionProperty.StreamName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_normalization_settings is not None:
                self._values["audio_normalization_settings"] = audio_normalization_settings
            if audio_selector_name is not None:
                self._values["audio_selector_name"] = audio_selector_name
            if audio_type is not None:
                self._values["audio_type"] = audio_type
            if audio_type_control is not None:
                self._values["audio_type_control"] = audio_type_control
            if codec_settings is not None:
                self._values["codec_settings"] = codec_settings
            if language_code is not None:
                self._values["language_code"] = language_code
            if language_code_control is not None:
                self._values["language_code_control"] = language_code_control
            if name is not None:
                self._values["name"] = name
            if remix_settings is not None:
                self._values["remix_settings"] = remix_settings
            if stream_name is not None:
                self._values["stream_name"] = stream_name

        @builtins.property
        def audio_normalization_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.AudioNormalizationSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.AudioDescriptionProperty.AudioNormalizationSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-audionormalizationsettings
            """
            result = self._values.get("audio_normalization_settings")
            return result

        @builtins.property
        def audio_selector_name(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AudioDescriptionProperty.AudioSelectorName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-audioselectorname
            """
            result = self._values.get("audio_selector_name")
            return result

        @builtins.property
        def audio_type(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AudioDescriptionProperty.AudioType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-audiotype
            """
            result = self._values.get("audio_type")
            return result

        @builtins.property
        def audio_type_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AudioDescriptionProperty.AudioTypeControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-audiotypecontrol
            """
            result = self._values.get("audio_type_control")
            return result

        @builtins.property
        def codec_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.AudioCodecSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.AudioDescriptionProperty.CodecSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-codecsettings
            """
            result = self._values.get("codec_settings")
            return result

        @builtins.property
        def language_code(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AudioDescriptionProperty.LanguageCode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-languagecode
            """
            result = self._values.get("language_code")
            return result

        @builtins.property
        def language_code_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AudioDescriptionProperty.LanguageCodeControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-languagecodecontrol
            """
            result = self._values.get("language_code_control")
            return result

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AudioDescriptionProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-name
            """
            result = self._values.get("name")
            return result

        @builtins.property
        def remix_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.RemixSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.AudioDescriptionProperty.RemixSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-remixsettings
            """
            result = self._values.get("remix_settings")
            return result

        @builtins.property
        def stream_name(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AudioDescriptionProperty.StreamName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-streamname
            """
            result = self._values.get("stream_name")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioDescriptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.AudioLanguageSelectionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "language_code": "languageCode",
            "language_selection_policy": "languageSelectionPolicy",
        },
    )
    class AudioLanguageSelectionProperty:
        def __init__(
            self,
            *,
            language_code: typing.Optional[builtins.str] = None,
            language_selection_policy: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param language_code: ``CfnChannel.AudioLanguageSelectionProperty.LanguageCode``.
            :param language_selection_policy: ``CfnChannel.AudioLanguageSelectionProperty.LanguageSelectionPolicy``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiolanguageselection.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if language_code is not None:
                self._values["language_code"] = language_code
            if language_selection_policy is not None:
                self._values["language_selection_policy"] = language_selection_policy

        @builtins.property
        def language_code(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AudioLanguageSelectionProperty.LanguageCode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiolanguageselection.html#cfn-medialive-channel-audiolanguageselection-languagecode
            """
            result = self._values.get("language_code")
            return result

        @builtins.property
        def language_selection_policy(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AudioLanguageSelectionProperty.LanguageSelectionPolicy``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiolanguageselection.html#cfn-medialive-channel-audiolanguageselection-languageselectionpolicy
            """
            result = self._values.get("language_selection_policy")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioLanguageSelectionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.AudioNormalizationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "algorithm": "algorithm",
            "algorithm_control": "algorithmControl",
            "target_lkfs": "targetLkfs",
        },
    )
    class AudioNormalizationSettingsProperty:
        def __init__(
            self,
            *,
            algorithm: typing.Optional[builtins.str] = None,
            algorithm_control: typing.Optional[builtins.str] = None,
            target_lkfs: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param algorithm: ``CfnChannel.AudioNormalizationSettingsProperty.Algorithm``.
            :param algorithm_control: ``CfnChannel.AudioNormalizationSettingsProperty.AlgorithmControl``.
            :param target_lkfs: ``CfnChannel.AudioNormalizationSettingsProperty.TargetLkfs``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audionormalizationsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if algorithm is not None:
                self._values["algorithm"] = algorithm
            if algorithm_control is not None:
                self._values["algorithm_control"] = algorithm_control
            if target_lkfs is not None:
                self._values["target_lkfs"] = target_lkfs

        @builtins.property
        def algorithm(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AudioNormalizationSettingsProperty.Algorithm``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audionormalizationsettings.html#cfn-medialive-channel-audionormalizationsettings-algorithm
            """
            result = self._values.get("algorithm")
            return result

        @builtins.property
        def algorithm_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AudioNormalizationSettingsProperty.AlgorithmControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audionormalizationsettings.html#cfn-medialive-channel-audionormalizationsettings-algorithmcontrol
            """
            result = self._values.get("algorithm_control")
            return result

        @builtins.property
        def target_lkfs(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.AudioNormalizationSettingsProperty.TargetLkfs``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audionormalizationsettings.html#cfn-medialive-channel-audionormalizationsettings-targetlkfs
            """
            result = self._values.get("target_lkfs")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioNormalizationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.AudioOnlyHlsSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_group_id": "audioGroupId",
            "audio_only_image": "audioOnlyImage",
            "audio_track_type": "audioTrackType",
            "segment_type": "segmentType",
        },
    )
    class AudioOnlyHlsSettingsProperty:
        def __init__(
            self,
            *,
            audio_group_id: typing.Optional[builtins.str] = None,
            audio_only_image: typing.Optional[typing.Union["CfnChannel.InputLocationProperty", _IResolvable_a771d0ef]] = None,
            audio_track_type: typing.Optional[builtins.str] = None,
            segment_type: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param audio_group_id: ``CfnChannel.AudioOnlyHlsSettingsProperty.AudioGroupId``.
            :param audio_only_image: ``CfnChannel.AudioOnlyHlsSettingsProperty.AudioOnlyImage``.
            :param audio_track_type: ``CfnChannel.AudioOnlyHlsSettingsProperty.AudioTrackType``.
            :param segment_type: ``CfnChannel.AudioOnlyHlsSettingsProperty.SegmentType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_group_id is not None:
                self._values["audio_group_id"] = audio_group_id
            if audio_only_image is not None:
                self._values["audio_only_image"] = audio_only_image
            if audio_track_type is not None:
                self._values["audio_track_type"] = audio_track_type
            if segment_type is not None:
                self._values["segment_type"] = segment_type

        @builtins.property
        def audio_group_id(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AudioOnlyHlsSettingsProperty.AudioGroupId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html#cfn-medialive-channel-audioonlyhlssettings-audiogroupid
            """
            result = self._values.get("audio_group_id")
            return result

        @builtins.property
        def audio_only_image(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.InputLocationProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.AudioOnlyHlsSettingsProperty.AudioOnlyImage``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html#cfn-medialive-channel-audioonlyhlssettings-audioonlyimage
            """
            result = self._values.get("audio_only_image")
            return result

        @builtins.property
        def audio_track_type(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AudioOnlyHlsSettingsProperty.AudioTrackType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html#cfn-medialive-channel-audioonlyhlssettings-audiotracktype
            """
            result = self._values.get("audio_track_type")
            return result

        @builtins.property
        def segment_type(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AudioOnlyHlsSettingsProperty.SegmentType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html#cfn-medialive-channel-audioonlyhlssettings-segmenttype
            """
            result = self._values.get("segment_type")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioOnlyHlsSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.AudioPidSelectionProperty",
        jsii_struct_bases=[],
        name_mapping={"pid": "pid"},
    )
    class AudioPidSelectionProperty:
        def __init__(self, *, pid: typing.Optional[jsii.Number] = None) -> None:
            """
            :param pid: ``CfnChannel.AudioPidSelectionProperty.Pid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiopidselection.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if pid is not None:
                self._values["pid"] = pid

        @builtins.property
        def pid(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.AudioPidSelectionProperty.Pid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiopidselection.html#cfn-medialive-channel-audiopidselection-pid
            """
            result = self._values.get("pid")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioPidSelectionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.AudioSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "selector_settings": "selectorSettings"},
    )
    class AudioSelectorProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            selector_settings: typing.Optional[typing.Union["CfnChannel.AudioSelectorSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param name: ``CfnChannel.AudioSelectorProperty.Name``.
            :param selector_settings: ``CfnChannel.AudioSelectorProperty.SelectorSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselector.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if selector_settings is not None:
                self._values["selector_settings"] = selector_settings

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AudioSelectorProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselector.html#cfn-medialive-channel-audioselector-name
            """
            result = self._values.get("name")
            return result

        @builtins.property
        def selector_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.AudioSelectorSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.AudioSelectorProperty.SelectorSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselector.html#cfn-medialive-channel-audioselector-selectorsettings
            """
            result = self._values.get("selector_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.AudioSelectorSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_language_selection": "audioLanguageSelection",
            "audio_pid_selection": "audioPidSelection",
            "audio_track_selection": "audioTrackSelection",
        },
    )
    class AudioSelectorSettingsProperty:
        def __init__(
            self,
            *,
            audio_language_selection: typing.Optional[typing.Union["CfnChannel.AudioLanguageSelectionProperty", _IResolvable_a771d0ef]] = None,
            audio_pid_selection: typing.Optional[typing.Union["CfnChannel.AudioPidSelectionProperty", _IResolvable_a771d0ef]] = None,
            audio_track_selection: typing.Optional[typing.Union["CfnChannel.AudioTrackSelectionProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param audio_language_selection: ``CfnChannel.AudioSelectorSettingsProperty.AudioLanguageSelection``.
            :param audio_pid_selection: ``CfnChannel.AudioSelectorSettingsProperty.AudioPidSelection``.
            :param audio_track_selection: ``CfnChannel.AudioSelectorSettingsProperty.AudioTrackSelection``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselectorsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_language_selection is not None:
                self._values["audio_language_selection"] = audio_language_selection
            if audio_pid_selection is not None:
                self._values["audio_pid_selection"] = audio_pid_selection
            if audio_track_selection is not None:
                self._values["audio_track_selection"] = audio_track_selection

        @builtins.property
        def audio_language_selection(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.AudioLanguageSelectionProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.AudioSelectorSettingsProperty.AudioLanguageSelection``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselectorsettings.html#cfn-medialive-channel-audioselectorsettings-audiolanguageselection
            """
            result = self._values.get("audio_language_selection")
            return result

        @builtins.property
        def audio_pid_selection(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.AudioPidSelectionProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.AudioSelectorSettingsProperty.AudioPidSelection``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselectorsettings.html#cfn-medialive-channel-audioselectorsettings-audiopidselection
            """
            result = self._values.get("audio_pid_selection")
            return result

        @builtins.property
        def audio_track_selection(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.AudioTrackSelectionProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.AudioSelectorSettingsProperty.AudioTrackSelection``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselectorsettings.html#cfn-medialive-channel-audioselectorsettings-audiotrackselection
            """
            result = self._values.get("audio_track_selection")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioSelectorSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.AudioTrackProperty",
        jsii_struct_bases=[],
        name_mapping={"track": "track"},
    )
    class AudioTrackProperty:
        def __init__(self, *, track: typing.Optional[jsii.Number] = None) -> None:
            """
            :param track: ``CfnChannel.AudioTrackProperty.Track``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrack.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if track is not None:
                self._values["track"] = track

        @builtins.property
        def track(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.AudioTrackProperty.Track``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrack.html#cfn-medialive-channel-audiotrack-track
            """
            result = self._values.get("track")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioTrackProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.AudioTrackSelectionProperty",
        jsii_struct_bases=[],
        name_mapping={"tracks": "tracks"},
    )
    class AudioTrackSelectionProperty:
        def __init__(
            self,
            *,
            tracks: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.AudioTrackProperty", _IResolvable_a771d0ef]]]] = None,
        ) -> None:
            """
            :param tracks: ``CfnChannel.AudioTrackSelectionProperty.Tracks``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrackselection.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if tracks is not None:
                self._values["tracks"] = tracks

        @builtins.property
        def tracks(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.AudioTrackProperty", _IResolvable_a771d0ef]]]]:
            """``CfnChannel.AudioTrackSelectionProperty.Tracks``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrackselection.html#cfn-medialive-channel-audiotrackselection-tracks
            """
            result = self._values.get("tracks")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioTrackSelectionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.AutomaticInputFailoverSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "input_preference": "inputPreference",
            "secondary_input_id": "secondaryInputId",
        },
    )
    class AutomaticInputFailoverSettingsProperty:
        def __init__(
            self,
            *,
            input_preference: typing.Optional[builtins.str] = None,
            secondary_input_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param input_preference: ``CfnChannel.AutomaticInputFailoverSettingsProperty.InputPreference``.
            :param secondary_input_id: ``CfnChannel.AutomaticInputFailoverSettingsProperty.SecondaryInputId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-automaticinputfailoversettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if input_preference is not None:
                self._values["input_preference"] = input_preference
            if secondary_input_id is not None:
                self._values["secondary_input_id"] = secondary_input_id

        @builtins.property
        def input_preference(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AutomaticInputFailoverSettingsProperty.InputPreference``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-automaticinputfailoversettings.html#cfn-medialive-channel-automaticinputfailoversettings-inputpreference
            """
            result = self._values.get("input_preference")
            return result

        @builtins.property
        def secondary_input_id(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AutomaticInputFailoverSettingsProperty.SecondaryInputId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-automaticinputfailoversettings.html#cfn-medialive-channel-automaticinputfailoversettings-secondaryinputid
            """
            result = self._values.get("secondary_input_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutomaticInputFailoverSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.AvailBlankingProperty",
        jsii_struct_bases=[],
        name_mapping={"avail_blanking_image": "availBlankingImage", "state": "state"},
    )
    class AvailBlankingProperty:
        def __init__(
            self,
            *,
            avail_blanking_image: typing.Optional[typing.Union["CfnChannel.InputLocationProperty", _IResolvable_a771d0ef]] = None,
            state: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param avail_blanking_image: ``CfnChannel.AvailBlankingProperty.AvailBlankingImage``.
            :param state: ``CfnChannel.AvailBlankingProperty.State``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availblanking.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if avail_blanking_image is not None:
                self._values["avail_blanking_image"] = avail_blanking_image
            if state is not None:
                self._values["state"] = state

        @builtins.property
        def avail_blanking_image(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.InputLocationProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.AvailBlankingProperty.AvailBlankingImage``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availblanking.html#cfn-medialive-channel-availblanking-availblankingimage
            """
            result = self._values.get("avail_blanking_image")
            return result

        @builtins.property
        def state(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.AvailBlankingProperty.State``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availblanking.html#cfn-medialive-channel-availblanking-state
            """
            result = self._values.get("state")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AvailBlankingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.AvailConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"avail_settings": "availSettings"},
    )
    class AvailConfigurationProperty:
        def __init__(
            self,
            *,
            avail_settings: typing.Optional[typing.Union["CfnChannel.AvailSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param avail_settings: ``CfnChannel.AvailConfigurationProperty.AvailSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if avail_settings is not None:
                self._values["avail_settings"] = avail_settings

        @builtins.property
        def avail_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.AvailSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.AvailConfigurationProperty.AvailSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availconfiguration.html#cfn-medialive-channel-availconfiguration-availsettings
            """
            result = self._values.get("avail_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AvailConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.AvailSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "scte35_splice_insert": "scte35SpliceInsert",
            "scte35_time_signal_apos": "scte35TimeSignalApos",
        },
    )
    class AvailSettingsProperty:
        def __init__(
            self,
            *,
            scte35_splice_insert: typing.Optional[typing.Union["CfnChannel.Scte35SpliceInsertProperty", _IResolvable_a771d0ef]] = None,
            scte35_time_signal_apos: typing.Optional[typing.Union["CfnChannel.Scte35TimeSignalAposProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param scte35_splice_insert: ``CfnChannel.AvailSettingsProperty.Scte35SpliceInsert``.
            :param scte35_time_signal_apos: ``CfnChannel.AvailSettingsProperty.Scte35TimeSignalApos``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if scte35_splice_insert is not None:
                self._values["scte35_splice_insert"] = scte35_splice_insert
            if scte35_time_signal_apos is not None:
                self._values["scte35_time_signal_apos"] = scte35_time_signal_apos

        @builtins.property
        def scte35_splice_insert(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.Scte35SpliceInsertProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.AvailSettingsProperty.Scte35SpliceInsert``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availsettings.html#cfn-medialive-channel-availsettings-scte35spliceinsert
            """
            result = self._values.get("scte35_splice_insert")
            return result

        @builtins.property
        def scte35_time_signal_apos(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.Scte35TimeSignalAposProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.AvailSettingsProperty.Scte35TimeSignalApos``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availsettings.html#cfn-medialive-channel-availsettings-scte35timesignalapos
            """
            result = self._values.get("scte35_time_signal_apos")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AvailSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.BlackoutSlateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "blackout_slate_image": "blackoutSlateImage",
            "network_end_blackout": "networkEndBlackout",
            "network_end_blackout_image": "networkEndBlackoutImage",
            "network_id": "networkId",
            "state": "state",
        },
    )
    class BlackoutSlateProperty:
        def __init__(
            self,
            *,
            blackout_slate_image: typing.Optional[typing.Union["CfnChannel.InputLocationProperty", _IResolvable_a771d0ef]] = None,
            network_end_blackout: typing.Optional[builtins.str] = None,
            network_end_blackout_image: typing.Optional[typing.Union["CfnChannel.InputLocationProperty", _IResolvable_a771d0ef]] = None,
            network_id: typing.Optional[builtins.str] = None,
            state: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param blackout_slate_image: ``CfnChannel.BlackoutSlateProperty.BlackoutSlateImage``.
            :param network_end_blackout: ``CfnChannel.BlackoutSlateProperty.NetworkEndBlackout``.
            :param network_end_blackout_image: ``CfnChannel.BlackoutSlateProperty.NetworkEndBlackoutImage``.
            :param network_id: ``CfnChannel.BlackoutSlateProperty.NetworkId``.
            :param state: ``CfnChannel.BlackoutSlateProperty.State``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if blackout_slate_image is not None:
                self._values["blackout_slate_image"] = blackout_slate_image
            if network_end_blackout is not None:
                self._values["network_end_blackout"] = network_end_blackout
            if network_end_blackout_image is not None:
                self._values["network_end_blackout_image"] = network_end_blackout_image
            if network_id is not None:
                self._values["network_id"] = network_id
            if state is not None:
                self._values["state"] = state

        @builtins.property
        def blackout_slate_image(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.InputLocationProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.BlackoutSlateProperty.BlackoutSlateImage``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html#cfn-medialive-channel-blackoutslate-blackoutslateimage
            """
            result = self._values.get("blackout_slate_image")
            return result

        @builtins.property
        def network_end_blackout(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.BlackoutSlateProperty.NetworkEndBlackout``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html#cfn-medialive-channel-blackoutslate-networkendblackout
            """
            result = self._values.get("network_end_blackout")
            return result

        @builtins.property
        def network_end_blackout_image(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.InputLocationProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.BlackoutSlateProperty.NetworkEndBlackoutImage``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html#cfn-medialive-channel-blackoutslate-networkendblackoutimage
            """
            result = self._values.get("network_end_blackout_image")
            return result

        @builtins.property
        def network_id(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.BlackoutSlateProperty.NetworkId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html#cfn-medialive-channel-blackoutslate-networkid
            """
            result = self._values.get("network_id")
            return result

        @builtins.property
        def state(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.BlackoutSlateProperty.State``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html#cfn-medialive-channel-blackoutslate-state
            """
            result = self._values.get("state")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BlackoutSlateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.BurnInDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alignment": "alignment",
            "background_color": "backgroundColor",
            "background_opacity": "backgroundOpacity",
            "font": "font",
            "font_color": "fontColor",
            "font_opacity": "fontOpacity",
            "font_resolution": "fontResolution",
            "font_size": "fontSize",
            "outline_color": "outlineColor",
            "outline_size": "outlineSize",
            "shadow_color": "shadowColor",
            "shadow_opacity": "shadowOpacity",
            "shadow_x_offset": "shadowXOffset",
            "shadow_y_offset": "shadowYOffset",
            "teletext_grid_control": "teletextGridControl",
            "x_position": "xPosition",
            "y_position": "yPosition",
        },
    )
    class BurnInDestinationSettingsProperty:
        def __init__(
            self,
            *,
            alignment: typing.Optional[builtins.str] = None,
            background_color: typing.Optional[builtins.str] = None,
            background_opacity: typing.Optional[jsii.Number] = None,
            font: typing.Optional[typing.Union["CfnChannel.InputLocationProperty", _IResolvable_a771d0ef]] = None,
            font_color: typing.Optional[builtins.str] = None,
            font_opacity: typing.Optional[jsii.Number] = None,
            font_resolution: typing.Optional[jsii.Number] = None,
            font_size: typing.Optional[builtins.str] = None,
            outline_color: typing.Optional[builtins.str] = None,
            outline_size: typing.Optional[jsii.Number] = None,
            shadow_color: typing.Optional[builtins.str] = None,
            shadow_opacity: typing.Optional[jsii.Number] = None,
            shadow_x_offset: typing.Optional[jsii.Number] = None,
            shadow_y_offset: typing.Optional[jsii.Number] = None,
            teletext_grid_control: typing.Optional[builtins.str] = None,
            x_position: typing.Optional[jsii.Number] = None,
            y_position: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param alignment: ``CfnChannel.BurnInDestinationSettingsProperty.Alignment``.
            :param background_color: ``CfnChannel.BurnInDestinationSettingsProperty.BackgroundColor``.
            :param background_opacity: ``CfnChannel.BurnInDestinationSettingsProperty.BackgroundOpacity``.
            :param font: ``CfnChannel.BurnInDestinationSettingsProperty.Font``.
            :param font_color: ``CfnChannel.BurnInDestinationSettingsProperty.FontColor``.
            :param font_opacity: ``CfnChannel.BurnInDestinationSettingsProperty.FontOpacity``.
            :param font_resolution: ``CfnChannel.BurnInDestinationSettingsProperty.FontResolution``.
            :param font_size: ``CfnChannel.BurnInDestinationSettingsProperty.FontSize``.
            :param outline_color: ``CfnChannel.BurnInDestinationSettingsProperty.OutlineColor``.
            :param outline_size: ``CfnChannel.BurnInDestinationSettingsProperty.OutlineSize``.
            :param shadow_color: ``CfnChannel.BurnInDestinationSettingsProperty.ShadowColor``.
            :param shadow_opacity: ``CfnChannel.BurnInDestinationSettingsProperty.ShadowOpacity``.
            :param shadow_x_offset: ``CfnChannel.BurnInDestinationSettingsProperty.ShadowXOffset``.
            :param shadow_y_offset: ``CfnChannel.BurnInDestinationSettingsProperty.ShadowYOffset``.
            :param teletext_grid_control: ``CfnChannel.BurnInDestinationSettingsProperty.TeletextGridControl``.
            :param x_position: ``CfnChannel.BurnInDestinationSettingsProperty.XPosition``.
            :param y_position: ``CfnChannel.BurnInDestinationSettingsProperty.YPosition``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if alignment is not None:
                self._values["alignment"] = alignment
            if background_color is not None:
                self._values["background_color"] = background_color
            if background_opacity is not None:
                self._values["background_opacity"] = background_opacity
            if font is not None:
                self._values["font"] = font
            if font_color is not None:
                self._values["font_color"] = font_color
            if font_opacity is not None:
                self._values["font_opacity"] = font_opacity
            if font_resolution is not None:
                self._values["font_resolution"] = font_resolution
            if font_size is not None:
                self._values["font_size"] = font_size
            if outline_color is not None:
                self._values["outline_color"] = outline_color
            if outline_size is not None:
                self._values["outline_size"] = outline_size
            if shadow_color is not None:
                self._values["shadow_color"] = shadow_color
            if shadow_opacity is not None:
                self._values["shadow_opacity"] = shadow_opacity
            if shadow_x_offset is not None:
                self._values["shadow_x_offset"] = shadow_x_offset
            if shadow_y_offset is not None:
                self._values["shadow_y_offset"] = shadow_y_offset
            if teletext_grid_control is not None:
                self._values["teletext_grid_control"] = teletext_grid_control
            if x_position is not None:
                self._values["x_position"] = x_position
            if y_position is not None:
                self._values["y_position"] = y_position

        @builtins.property
        def alignment(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.BurnInDestinationSettingsProperty.Alignment``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-alignment
            """
            result = self._values.get("alignment")
            return result

        @builtins.property
        def background_color(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.BurnInDestinationSettingsProperty.BackgroundColor``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-backgroundcolor
            """
            result = self._values.get("background_color")
            return result

        @builtins.property
        def background_opacity(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.BurnInDestinationSettingsProperty.BackgroundOpacity``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-backgroundopacity
            """
            result = self._values.get("background_opacity")
            return result

        @builtins.property
        def font(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.InputLocationProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.BurnInDestinationSettingsProperty.Font``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-font
            """
            result = self._values.get("font")
            return result

        @builtins.property
        def font_color(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.BurnInDestinationSettingsProperty.FontColor``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-fontcolor
            """
            result = self._values.get("font_color")
            return result

        @builtins.property
        def font_opacity(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.BurnInDestinationSettingsProperty.FontOpacity``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-fontopacity
            """
            result = self._values.get("font_opacity")
            return result

        @builtins.property
        def font_resolution(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.BurnInDestinationSettingsProperty.FontResolution``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-fontresolution
            """
            result = self._values.get("font_resolution")
            return result

        @builtins.property
        def font_size(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.BurnInDestinationSettingsProperty.FontSize``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-fontsize
            """
            result = self._values.get("font_size")
            return result

        @builtins.property
        def outline_color(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.BurnInDestinationSettingsProperty.OutlineColor``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-outlinecolor
            """
            result = self._values.get("outline_color")
            return result

        @builtins.property
        def outline_size(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.BurnInDestinationSettingsProperty.OutlineSize``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-outlinesize
            """
            result = self._values.get("outline_size")
            return result

        @builtins.property
        def shadow_color(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.BurnInDestinationSettingsProperty.ShadowColor``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-shadowcolor
            """
            result = self._values.get("shadow_color")
            return result

        @builtins.property
        def shadow_opacity(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.BurnInDestinationSettingsProperty.ShadowOpacity``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-shadowopacity
            """
            result = self._values.get("shadow_opacity")
            return result

        @builtins.property
        def shadow_x_offset(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.BurnInDestinationSettingsProperty.ShadowXOffset``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-shadowxoffset
            """
            result = self._values.get("shadow_x_offset")
            return result

        @builtins.property
        def shadow_y_offset(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.BurnInDestinationSettingsProperty.ShadowYOffset``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-shadowyoffset
            """
            result = self._values.get("shadow_y_offset")
            return result

        @builtins.property
        def teletext_grid_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.BurnInDestinationSettingsProperty.TeletextGridControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-teletextgridcontrol
            """
            result = self._values.get("teletext_grid_control")
            return result

        @builtins.property
        def x_position(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.BurnInDestinationSettingsProperty.XPosition``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-xposition
            """
            result = self._values.get("x_position")
            return result

        @builtins.property
        def y_position(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.BurnInDestinationSettingsProperty.YPosition``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-yposition
            """
            result = self._values.get("y_position")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BurnInDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.CaptionDescriptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "caption_selector_name": "captionSelectorName",
            "destination_settings": "destinationSettings",
            "language_code": "languageCode",
            "language_description": "languageDescription",
            "name": "name",
        },
    )
    class CaptionDescriptionProperty:
        def __init__(
            self,
            *,
            caption_selector_name: typing.Optional[builtins.str] = None,
            destination_settings: typing.Optional[typing.Union["CfnChannel.CaptionDestinationSettingsProperty", _IResolvable_a771d0ef]] = None,
            language_code: typing.Optional[builtins.str] = None,
            language_description: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param caption_selector_name: ``CfnChannel.CaptionDescriptionProperty.CaptionSelectorName``.
            :param destination_settings: ``CfnChannel.CaptionDescriptionProperty.DestinationSettings``.
            :param language_code: ``CfnChannel.CaptionDescriptionProperty.LanguageCode``.
            :param language_description: ``CfnChannel.CaptionDescriptionProperty.LanguageDescription``.
            :param name: ``CfnChannel.CaptionDescriptionProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if caption_selector_name is not None:
                self._values["caption_selector_name"] = caption_selector_name
            if destination_settings is not None:
                self._values["destination_settings"] = destination_settings
            if language_code is not None:
                self._values["language_code"] = language_code
            if language_description is not None:
                self._values["language_description"] = language_description
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def caption_selector_name(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.CaptionDescriptionProperty.CaptionSelectorName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-captionselectorname
            """
            result = self._values.get("caption_selector_name")
            return result

        @builtins.property
        def destination_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.CaptionDestinationSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionDescriptionProperty.DestinationSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-destinationsettings
            """
            result = self._values.get("destination_settings")
            return result

        @builtins.property
        def language_code(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.CaptionDescriptionProperty.LanguageCode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-languagecode
            """
            result = self._values.get("language_code")
            return result

        @builtins.property
        def language_description(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.CaptionDescriptionProperty.LanguageDescription``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-languagedescription
            """
            result = self._values.get("language_description")
            return result

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.CaptionDescriptionProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-name
            """
            result = self._values.get("name")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CaptionDescriptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.CaptionDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arib_destination_settings": "aribDestinationSettings",
            "burn_in_destination_settings": "burnInDestinationSettings",
            "dvb_sub_destination_settings": "dvbSubDestinationSettings",
            "ebu_tt_d_destination_settings": "ebuTtDDestinationSettings",
            "embedded_destination_settings": "embeddedDestinationSettings",
            "embedded_plus_scte20_destination_settings": "embeddedPlusScte20DestinationSettings",
            "rtmp_caption_info_destination_settings": "rtmpCaptionInfoDestinationSettings",
            "scte20_plus_embedded_destination_settings": "scte20PlusEmbeddedDestinationSettings",
            "scte27_destination_settings": "scte27DestinationSettings",
            "smpte_tt_destination_settings": "smpteTtDestinationSettings",
            "teletext_destination_settings": "teletextDestinationSettings",
            "ttml_destination_settings": "ttmlDestinationSettings",
            "webvtt_destination_settings": "webvttDestinationSettings",
        },
    )
    class CaptionDestinationSettingsProperty:
        def __init__(
            self,
            *,
            arib_destination_settings: typing.Optional[typing.Union["CfnChannel.AribDestinationSettingsProperty", _IResolvable_a771d0ef]] = None,
            burn_in_destination_settings: typing.Optional[typing.Union["CfnChannel.BurnInDestinationSettingsProperty", _IResolvable_a771d0ef]] = None,
            dvb_sub_destination_settings: typing.Optional[typing.Union["CfnChannel.DvbSubDestinationSettingsProperty", _IResolvable_a771d0ef]] = None,
            ebu_tt_d_destination_settings: typing.Optional[typing.Union["CfnChannel.EbuTtDDestinationSettingsProperty", _IResolvable_a771d0ef]] = None,
            embedded_destination_settings: typing.Optional[typing.Union["CfnChannel.EmbeddedDestinationSettingsProperty", _IResolvable_a771d0ef]] = None,
            embedded_plus_scte20_destination_settings: typing.Optional[typing.Union["CfnChannel.EmbeddedPlusScte20DestinationSettingsProperty", _IResolvable_a771d0ef]] = None,
            rtmp_caption_info_destination_settings: typing.Optional[typing.Union["CfnChannel.RtmpCaptionInfoDestinationSettingsProperty", _IResolvable_a771d0ef]] = None,
            scte20_plus_embedded_destination_settings: typing.Optional[typing.Union["CfnChannel.Scte20PlusEmbeddedDestinationSettingsProperty", _IResolvable_a771d0ef]] = None,
            scte27_destination_settings: typing.Optional[typing.Union["CfnChannel.Scte27DestinationSettingsProperty", _IResolvable_a771d0ef]] = None,
            smpte_tt_destination_settings: typing.Optional[typing.Union["CfnChannel.SmpteTtDestinationSettingsProperty", _IResolvable_a771d0ef]] = None,
            teletext_destination_settings: typing.Optional[typing.Union["CfnChannel.TeletextDestinationSettingsProperty", _IResolvable_a771d0ef]] = None,
            ttml_destination_settings: typing.Optional[typing.Union["CfnChannel.TtmlDestinationSettingsProperty", _IResolvable_a771d0ef]] = None,
            webvtt_destination_settings: typing.Optional[typing.Union["CfnChannel.WebvttDestinationSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param arib_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.AribDestinationSettings``.
            :param burn_in_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.BurnInDestinationSettings``.
            :param dvb_sub_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.DvbSubDestinationSettings``.
            :param ebu_tt_d_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.EbuTtDDestinationSettings``.
            :param embedded_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.EmbeddedDestinationSettings``.
            :param embedded_plus_scte20_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.EmbeddedPlusScte20DestinationSettings``.
            :param rtmp_caption_info_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.RtmpCaptionInfoDestinationSettings``.
            :param scte20_plus_embedded_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.Scte20PlusEmbeddedDestinationSettings``.
            :param scte27_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.Scte27DestinationSettings``.
            :param smpte_tt_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.SmpteTtDestinationSettings``.
            :param teletext_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.TeletextDestinationSettings``.
            :param ttml_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.TtmlDestinationSettings``.
            :param webvtt_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.WebvttDestinationSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if arib_destination_settings is not None:
                self._values["arib_destination_settings"] = arib_destination_settings
            if burn_in_destination_settings is not None:
                self._values["burn_in_destination_settings"] = burn_in_destination_settings
            if dvb_sub_destination_settings is not None:
                self._values["dvb_sub_destination_settings"] = dvb_sub_destination_settings
            if ebu_tt_d_destination_settings is not None:
                self._values["ebu_tt_d_destination_settings"] = ebu_tt_d_destination_settings
            if embedded_destination_settings is not None:
                self._values["embedded_destination_settings"] = embedded_destination_settings
            if embedded_plus_scte20_destination_settings is not None:
                self._values["embedded_plus_scte20_destination_settings"] = embedded_plus_scte20_destination_settings
            if rtmp_caption_info_destination_settings is not None:
                self._values["rtmp_caption_info_destination_settings"] = rtmp_caption_info_destination_settings
            if scte20_plus_embedded_destination_settings is not None:
                self._values["scte20_plus_embedded_destination_settings"] = scte20_plus_embedded_destination_settings
            if scte27_destination_settings is not None:
                self._values["scte27_destination_settings"] = scte27_destination_settings
            if smpte_tt_destination_settings is not None:
                self._values["smpte_tt_destination_settings"] = smpte_tt_destination_settings
            if teletext_destination_settings is not None:
                self._values["teletext_destination_settings"] = teletext_destination_settings
            if ttml_destination_settings is not None:
                self._values["ttml_destination_settings"] = ttml_destination_settings
            if webvtt_destination_settings is not None:
                self._values["webvtt_destination_settings"] = webvtt_destination_settings

        @builtins.property
        def arib_destination_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.AribDestinationSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionDestinationSettingsProperty.AribDestinationSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-aribdestinationsettings
            """
            result = self._values.get("arib_destination_settings")
            return result

        @builtins.property
        def burn_in_destination_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.BurnInDestinationSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionDestinationSettingsProperty.BurnInDestinationSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-burnindestinationsettings
            """
            result = self._values.get("burn_in_destination_settings")
            return result

        @builtins.property
        def dvb_sub_destination_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.DvbSubDestinationSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionDestinationSettingsProperty.DvbSubDestinationSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-dvbsubdestinationsettings
            """
            result = self._values.get("dvb_sub_destination_settings")
            return result

        @builtins.property
        def ebu_tt_d_destination_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.EbuTtDDestinationSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionDestinationSettingsProperty.EbuTtDDestinationSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-ebuttddestinationsettings
            """
            result = self._values.get("ebu_tt_d_destination_settings")
            return result

        @builtins.property
        def embedded_destination_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.EmbeddedDestinationSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionDestinationSettingsProperty.EmbeddedDestinationSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-embeddeddestinationsettings
            """
            result = self._values.get("embedded_destination_settings")
            return result

        @builtins.property
        def embedded_plus_scte20_destination_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.EmbeddedPlusScte20DestinationSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionDestinationSettingsProperty.EmbeddedPlusScte20DestinationSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-embeddedplusscte20destinationsettings
            """
            result = self._values.get("embedded_plus_scte20_destination_settings")
            return result

        @builtins.property
        def rtmp_caption_info_destination_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.RtmpCaptionInfoDestinationSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionDestinationSettingsProperty.RtmpCaptionInfoDestinationSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-rtmpcaptioninfodestinationsettings
            """
            result = self._values.get("rtmp_caption_info_destination_settings")
            return result

        @builtins.property
        def scte20_plus_embedded_destination_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.Scte20PlusEmbeddedDestinationSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionDestinationSettingsProperty.Scte20PlusEmbeddedDestinationSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-scte20plusembeddeddestinationsettings
            """
            result = self._values.get("scte20_plus_embedded_destination_settings")
            return result

        @builtins.property
        def scte27_destination_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.Scte27DestinationSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionDestinationSettingsProperty.Scte27DestinationSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-scte27destinationsettings
            """
            result = self._values.get("scte27_destination_settings")
            return result

        @builtins.property
        def smpte_tt_destination_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.SmpteTtDestinationSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionDestinationSettingsProperty.SmpteTtDestinationSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-smptettdestinationsettings
            """
            result = self._values.get("smpte_tt_destination_settings")
            return result

        @builtins.property
        def teletext_destination_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.TeletextDestinationSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionDestinationSettingsProperty.TeletextDestinationSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-teletextdestinationsettings
            """
            result = self._values.get("teletext_destination_settings")
            return result

        @builtins.property
        def ttml_destination_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.TtmlDestinationSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionDestinationSettingsProperty.TtmlDestinationSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-ttmldestinationsettings
            """
            result = self._values.get("ttml_destination_settings")
            return result

        @builtins.property
        def webvtt_destination_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.WebvttDestinationSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionDestinationSettingsProperty.WebvttDestinationSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-webvttdestinationsettings
            """
            result = self._values.get("webvtt_destination_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CaptionDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.CaptionLanguageMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "caption_channel": "captionChannel",
            "language_code": "languageCode",
            "language_description": "languageDescription",
        },
    )
    class CaptionLanguageMappingProperty:
        def __init__(
            self,
            *,
            caption_channel: typing.Optional[jsii.Number] = None,
            language_code: typing.Optional[builtins.str] = None,
            language_description: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param caption_channel: ``CfnChannel.CaptionLanguageMappingProperty.CaptionChannel``.
            :param language_code: ``CfnChannel.CaptionLanguageMappingProperty.LanguageCode``.
            :param language_description: ``CfnChannel.CaptionLanguageMappingProperty.LanguageDescription``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionlanguagemapping.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if caption_channel is not None:
                self._values["caption_channel"] = caption_channel
            if language_code is not None:
                self._values["language_code"] = language_code
            if language_description is not None:
                self._values["language_description"] = language_description

        @builtins.property
        def caption_channel(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.CaptionLanguageMappingProperty.CaptionChannel``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionlanguagemapping.html#cfn-medialive-channel-captionlanguagemapping-captionchannel
            """
            result = self._values.get("caption_channel")
            return result

        @builtins.property
        def language_code(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.CaptionLanguageMappingProperty.LanguageCode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionlanguagemapping.html#cfn-medialive-channel-captionlanguagemapping-languagecode
            """
            result = self._values.get("language_code")
            return result

        @builtins.property
        def language_description(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.CaptionLanguageMappingProperty.LanguageDescription``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionlanguagemapping.html#cfn-medialive-channel-captionlanguagemapping-languagedescription
            """
            result = self._values.get("language_description")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CaptionLanguageMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.CaptionSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "language_code": "languageCode",
            "name": "name",
            "selector_settings": "selectorSettings",
        },
    )
    class CaptionSelectorProperty:
        def __init__(
            self,
            *,
            language_code: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            selector_settings: typing.Optional[typing.Union["CfnChannel.CaptionSelectorSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param language_code: ``CfnChannel.CaptionSelectorProperty.LanguageCode``.
            :param name: ``CfnChannel.CaptionSelectorProperty.Name``.
            :param selector_settings: ``CfnChannel.CaptionSelectorProperty.SelectorSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselector.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if language_code is not None:
                self._values["language_code"] = language_code
            if name is not None:
                self._values["name"] = name
            if selector_settings is not None:
                self._values["selector_settings"] = selector_settings

        @builtins.property
        def language_code(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.CaptionSelectorProperty.LanguageCode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselector.html#cfn-medialive-channel-captionselector-languagecode
            """
            result = self._values.get("language_code")
            return result

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.CaptionSelectorProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselector.html#cfn-medialive-channel-captionselector-name
            """
            result = self._values.get("name")
            return result

        @builtins.property
        def selector_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.CaptionSelectorSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionSelectorProperty.SelectorSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselector.html#cfn-medialive-channel-captionselector-selectorsettings
            """
            result = self._values.get("selector_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CaptionSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.CaptionSelectorSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arib_source_settings": "aribSourceSettings",
            "dvb_sub_source_settings": "dvbSubSourceSettings",
            "embedded_source_settings": "embeddedSourceSettings",
            "scte20_source_settings": "scte20SourceSettings",
            "scte27_source_settings": "scte27SourceSettings",
            "teletext_source_settings": "teletextSourceSettings",
        },
    )
    class CaptionSelectorSettingsProperty:
        def __init__(
            self,
            *,
            arib_source_settings: typing.Optional[typing.Union["CfnChannel.AribSourceSettingsProperty", _IResolvable_a771d0ef]] = None,
            dvb_sub_source_settings: typing.Optional[typing.Union["CfnChannel.DvbSubSourceSettingsProperty", _IResolvable_a771d0ef]] = None,
            embedded_source_settings: typing.Optional[typing.Union["CfnChannel.EmbeddedSourceSettingsProperty", _IResolvable_a771d0ef]] = None,
            scte20_source_settings: typing.Optional[typing.Union["CfnChannel.Scte20SourceSettingsProperty", _IResolvable_a771d0ef]] = None,
            scte27_source_settings: typing.Optional[typing.Union["CfnChannel.Scte27SourceSettingsProperty", _IResolvable_a771d0ef]] = None,
            teletext_source_settings: typing.Optional[typing.Union["CfnChannel.TeletextSourceSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param arib_source_settings: ``CfnChannel.CaptionSelectorSettingsProperty.AribSourceSettings``.
            :param dvb_sub_source_settings: ``CfnChannel.CaptionSelectorSettingsProperty.DvbSubSourceSettings``.
            :param embedded_source_settings: ``CfnChannel.CaptionSelectorSettingsProperty.EmbeddedSourceSettings``.
            :param scte20_source_settings: ``CfnChannel.CaptionSelectorSettingsProperty.Scte20SourceSettings``.
            :param scte27_source_settings: ``CfnChannel.CaptionSelectorSettingsProperty.Scte27SourceSettings``.
            :param teletext_source_settings: ``CfnChannel.CaptionSelectorSettingsProperty.TeletextSourceSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if arib_source_settings is not None:
                self._values["arib_source_settings"] = arib_source_settings
            if dvb_sub_source_settings is not None:
                self._values["dvb_sub_source_settings"] = dvb_sub_source_settings
            if embedded_source_settings is not None:
                self._values["embedded_source_settings"] = embedded_source_settings
            if scte20_source_settings is not None:
                self._values["scte20_source_settings"] = scte20_source_settings
            if scte27_source_settings is not None:
                self._values["scte27_source_settings"] = scte27_source_settings
            if teletext_source_settings is not None:
                self._values["teletext_source_settings"] = teletext_source_settings

        @builtins.property
        def arib_source_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.AribSourceSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionSelectorSettingsProperty.AribSourceSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-aribsourcesettings
            """
            result = self._values.get("arib_source_settings")
            return result

        @builtins.property
        def dvb_sub_source_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.DvbSubSourceSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionSelectorSettingsProperty.DvbSubSourceSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-dvbsubsourcesettings
            """
            result = self._values.get("dvb_sub_source_settings")
            return result

        @builtins.property
        def embedded_source_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.EmbeddedSourceSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionSelectorSettingsProperty.EmbeddedSourceSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-embeddedsourcesettings
            """
            result = self._values.get("embedded_source_settings")
            return result

        @builtins.property
        def scte20_source_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.Scte20SourceSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionSelectorSettingsProperty.Scte20SourceSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-scte20sourcesettings
            """
            result = self._values.get("scte20_source_settings")
            return result

        @builtins.property
        def scte27_source_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.Scte27SourceSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionSelectorSettingsProperty.Scte27SourceSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-scte27sourcesettings
            """
            result = self._values.get("scte27_source_settings")
            return result

        @builtins.property
        def teletext_source_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.TeletextSourceSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.CaptionSelectorSettingsProperty.TeletextSourceSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-teletextsourcesettings
            """
            result = self._values.get("teletext_source_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CaptionSelectorSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.ColorSpacePassthroughSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class ColorSpacePassthroughSettingsProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-colorspacepassthroughsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColorSpacePassthroughSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.DvbNitSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "network_id": "networkId",
            "network_name": "networkName",
            "rep_interval": "repInterval",
        },
    )
    class DvbNitSettingsProperty:
        def __init__(
            self,
            *,
            network_id: typing.Optional[jsii.Number] = None,
            network_name: typing.Optional[builtins.str] = None,
            rep_interval: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param network_id: ``CfnChannel.DvbNitSettingsProperty.NetworkId``.
            :param network_name: ``CfnChannel.DvbNitSettingsProperty.NetworkName``.
            :param rep_interval: ``CfnChannel.DvbNitSettingsProperty.RepInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbnitsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if network_id is not None:
                self._values["network_id"] = network_id
            if network_name is not None:
                self._values["network_name"] = network_name
            if rep_interval is not None:
                self._values["rep_interval"] = rep_interval

        @builtins.property
        def network_id(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.DvbNitSettingsProperty.NetworkId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbnitsettings.html#cfn-medialive-channel-dvbnitsettings-networkid
            """
            result = self._values.get("network_id")
            return result

        @builtins.property
        def network_name(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.DvbNitSettingsProperty.NetworkName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbnitsettings.html#cfn-medialive-channel-dvbnitsettings-networkname
            """
            result = self._values.get("network_name")
            return result

        @builtins.property
        def rep_interval(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.DvbNitSettingsProperty.RepInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbnitsettings.html#cfn-medialive-channel-dvbnitsettings-repinterval
            """
            result = self._values.get("rep_interval")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DvbNitSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.DvbSdtSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "output_sdt": "outputSdt",
            "rep_interval": "repInterval",
            "service_name": "serviceName",
            "service_provider_name": "serviceProviderName",
        },
    )
    class DvbSdtSettingsProperty:
        def __init__(
            self,
            *,
            output_sdt: typing.Optional[builtins.str] = None,
            rep_interval: typing.Optional[jsii.Number] = None,
            service_name: typing.Optional[builtins.str] = None,
            service_provider_name: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param output_sdt: ``CfnChannel.DvbSdtSettingsProperty.OutputSdt``.
            :param rep_interval: ``CfnChannel.DvbSdtSettingsProperty.RepInterval``.
            :param service_name: ``CfnChannel.DvbSdtSettingsProperty.ServiceName``.
            :param service_provider_name: ``CfnChannel.DvbSdtSettingsProperty.ServiceProviderName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if output_sdt is not None:
                self._values["output_sdt"] = output_sdt
            if rep_interval is not None:
                self._values["rep_interval"] = rep_interval
            if service_name is not None:
                self._values["service_name"] = service_name
            if service_provider_name is not None:
                self._values["service_provider_name"] = service_provider_name

        @builtins.property
        def output_sdt(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.DvbSdtSettingsProperty.OutputSdt``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html#cfn-medialive-channel-dvbsdtsettings-outputsdt
            """
            result = self._values.get("output_sdt")
            return result

        @builtins.property
        def rep_interval(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.DvbSdtSettingsProperty.RepInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html#cfn-medialive-channel-dvbsdtsettings-repinterval
            """
            result = self._values.get("rep_interval")
            return result

        @builtins.property
        def service_name(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.DvbSdtSettingsProperty.ServiceName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html#cfn-medialive-channel-dvbsdtsettings-servicename
            """
            result = self._values.get("service_name")
            return result

        @builtins.property
        def service_provider_name(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.DvbSdtSettingsProperty.ServiceProviderName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html#cfn-medialive-channel-dvbsdtsettings-serviceprovidername
            """
            result = self._values.get("service_provider_name")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DvbSdtSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.DvbSubDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alignment": "alignment",
            "background_color": "backgroundColor",
            "background_opacity": "backgroundOpacity",
            "font": "font",
            "font_color": "fontColor",
            "font_opacity": "fontOpacity",
            "font_resolution": "fontResolution",
            "font_size": "fontSize",
            "outline_color": "outlineColor",
            "outline_size": "outlineSize",
            "shadow_color": "shadowColor",
            "shadow_opacity": "shadowOpacity",
            "shadow_x_offset": "shadowXOffset",
            "shadow_y_offset": "shadowYOffset",
            "teletext_grid_control": "teletextGridControl",
            "x_position": "xPosition",
            "y_position": "yPosition",
        },
    )
    class DvbSubDestinationSettingsProperty:
        def __init__(
            self,
            *,
            alignment: typing.Optional[builtins.str] = None,
            background_color: typing.Optional[builtins.str] = None,
            background_opacity: typing.Optional[jsii.Number] = None,
            font: typing.Optional[typing.Union["CfnChannel.InputLocationProperty", _IResolvable_a771d0ef]] = None,
            font_color: typing.Optional[builtins.str] = None,
            font_opacity: typing.Optional[jsii.Number] = None,
            font_resolution: typing.Optional[jsii.Number] = None,
            font_size: typing.Optional[builtins.str] = None,
            outline_color: typing.Optional[builtins.str] = None,
            outline_size: typing.Optional[jsii.Number] = None,
            shadow_color: typing.Optional[builtins.str] = None,
            shadow_opacity: typing.Optional[jsii.Number] = None,
            shadow_x_offset: typing.Optional[jsii.Number] = None,
            shadow_y_offset: typing.Optional[jsii.Number] = None,
            teletext_grid_control: typing.Optional[builtins.str] = None,
            x_position: typing.Optional[jsii.Number] = None,
            y_position: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param alignment: ``CfnChannel.DvbSubDestinationSettingsProperty.Alignment``.
            :param background_color: ``CfnChannel.DvbSubDestinationSettingsProperty.BackgroundColor``.
            :param background_opacity: ``CfnChannel.DvbSubDestinationSettingsProperty.BackgroundOpacity``.
            :param font: ``CfnChannel.DvbSubDestinationSettingsProperty.Font``.
            :param font_color: ``CfnChannel.DvbSubDestinationSettingsProperty.FontColor``.
            :param font_opacity: ``CfnChannel.DvbSubDestinationSettingsProperty.FontOpacity``.
            :param font_resolution: ``CfnChannel.DvbSubDestinationSettingsProperty.FontResolution``.
            :param font_size: ``CfnChannel.DvbSubDestinationSettingsProperty.FontSize``.
            :param outline_color: ``CfnChannel.DvbSubDestinationSettingsProperty.OutlineColor``.
            :param outline_size: ``CfnChannel.DvbSubDestinationSettingsProperty.OutlineSize``.
            :param shadow_color: ``CfnChannel.DvbSubDestinationSettingsProperty.ShadowColor``.
            :param shadow_opacity: ``CfnChannel.DvbSubDestinationSettingsProperty.ShadowOpacity``.
            :param shadow_x_offset: ``CfnChannel.DvbSubDestinationSettingsProperty.ShadowXOffset``.
            :param shadow_y_offset: ``CfnChannel.DvbSubDestinationSettingsProperty.ShadowYOffset``.
            :param teletext_grid_control: ``CfnChannel.DvbSubDestinationSettingsProperty.TeletextGridControl``.
            :param x_position: ``CfnChannel.DvbSubDestinationSettingsProperty.XPosition``.
            :param y_position: ``CfnChannel.DvbSubDestinationSettingsProperty.YPosition``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if alignment is not None:
                self._values["alignment"] = alignment
            if background_color is not None:
                self._values["background_color"] = background_color
            if background_opacity is not None:
                self._values["background_opacity"] = background_opacity
            if font is not None:
                self._values["font"] = font
            if font_color is not None:
                self._values["font_color"] = font_color
            if font_opacity is not None:
                self._values["font_opacity"] = font_opacity
            if font_resolution is not None:
                self._values["font_resolution"] = font_resolution
            if font_size is not None:
                self._values["font_size"] = font_size
            if outline_color is not None:
                self._values["outline_color"] = outline_color
            if outline_size is not None:
                self._values["outline_size"] = outline_size
            if shadow_color is not None:
                self._values["shadow_color"] = shadow_color
            if shadow_opacity is not None:
                self._values["shadow_opacity"] = shadow_opacity
            if shadow_x_offset is not None:
                self._values["shadow_x_offset"] = shadow_x_offset
            if shadow_y_offset is not None:
                self._values["shadow_y_offset"] = shadow_y_offset
            if teletext_grid_control is not None:
                self._values["teletext_grid_control"] = teletext_grid_control
            if x_position is not None:
                self._values["x_position"] = x_position
            if y_position is not None:
                self._values["y_position"] = y_position

        @builtins.property
        def alignment(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.DvbSubDestinationSettingsProperty.Alignment``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-alignment
            """
            result = self._values.get("alignment")
            return result

        @builtins.property
        def background_color(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.DvbSubDestinationSettingsProperty.BackgroundColor``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-backgroundcolor
            """
            result = self._values.get("background_color")
            return result

        @builtins.property
        def background_opacity(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.DvbSubDestinationSettingsProperty.BackgroundOpacity``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-backgroundopacity
            """
            result = self._values.get("background_opacity")
            return result

        @builtins.property
        def font(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.InputLocationProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.DvbSubDestinationSettingsProperty.Font``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-font
            """
            result = self._values.get("font")
            return result

        @builtins.property
        def font_color(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.DvbSubDestinationSettingsProperty.FontColor``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-fontcolor
            """
            result = self._values.get("font_color")
            return result

        @builtins.property
        def font_opacity(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.DvbSubDestinationSettingsProperty.FontOpacity``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-fontopacity
            """
            result = self._values.get("font_opacity")
            return result

        @builtins.property
        def font_resolution(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.DvbSubDestinationSettingsProperty.FontResolution``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-fontresolution
            """
            result = self._values.get("font_resolution")
            return result

        @builtins.property
        def font_size(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.DvbSubDestinationSettingsProperty.FontSize``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-fontsize
            """
            result = self._values.get("font_size")
            return result

        @builtins.property
        def outline_color(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.DvbSubDestinationSettingsProperty.OutlineColor``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-outlinecolor
            """
            result = self._values.get("outline_color")
            return result

        @builtins.property
        def outline_size(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.DvbSubDestinationSettingsProperty.OutlineSize``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-outlinesize
            """
            result = self._values.get("outline_size")
            return result

        @builtins.property
        def shadow_color(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.DvbSubDestinationSettingsProperty.ShadowColor``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-shadowcolor
            """
            result = self._values.get("shadow_color")
            return result

        @builtins.property
        def shadow_opacity(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.DvbSubDestinationSettingsProperty.ShadowOpacity``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-shadowopacity
            """
            result = self._values.get("shadow_opacity")
            return result

        @builtins.property
        def shadow_x_offset(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.DvbSubDestinationSettingsProperty.ShadowXOffset``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-shadowxoffset
            """
            result = self._values.get("shadow_x_offset")
            return result

        @builtins.property
        def shadow_y_offset(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.DvbSubDestinationSettingsProperty.ShadowYOffset``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-shadowyoffset
            """
            result = self._values.get("shadow_y_offset")
            return result

        @builtins.property
        def teletext_grid_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.DvbSubDestinationSettingsProperty.TeletextGridControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-teletextgridcontrol
            """
            result = self._values.get("teletext_grid_control")
            return result

        @builtins.property
        def x_position(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.DvbSubDestinationSettingsProperty.XPosition``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-xposition
            """
            result = self._values.get("x_position")
            return result

        @builtins.property
        def y_position(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.DvbSubDestinationSettingsProperty.YPosition``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-yposition
            """
            result = self._values.get("y_position")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DvbSubDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.DvbSubSourceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"pid": "pid"},
    )
    class DvbSubSourceSettingsProperty:
        def __init__(self, *, pid: typing.Optional[jsii.Number] = None) -> None:
            """
            :param pid: ``CfnChannel.DvbSubSourceSettingsProperty.Pid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubsourcesettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if pid is not None:
                self._values["pid"] = pid

        @builtins.property
        def pid(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.DvbSubSourceSettingsProperty.Pid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubsourcesettings.html#cfn-medialive-channel-dvbsubsourcesettings-pid
            """
            result = self._values.get("pid")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DvbSubSourceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.DvbTdtSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"rep_interval": "repInterval"},
    )
    class DvbTdtSettingsProperty:
        def __init__(
            self,
            *,
            rep_interval: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param rep_interval: ``CfnChannel.DvbTdtSettingsProperty.RepInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbtdtsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if rep_interval is not None:
                self._values["rep_interval"] = rep_interval

        @builtins.property
        def rep_interval(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.DvbTdtSettingsProperty.RepInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbtdtsettings.html#cfn-medialive-channel-dvbtdtsettings-repinterval
            """
            result = self._values.get("rep_interval")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DvbTdtSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.Eac3SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attenuation_control": "attenuationControl",
            "bitrate": "bitrate",
            "bitstream_mode": "bitstreamMode",
            "coding_mode": "codingMode",
            "dc_filter": "dcFilter",
            "dialnorm": "dialnorm",
            "drc_line": "drcLine",
            "drc_rf": "drcRf",
            "lfe_control": "lfeControl",
            "lfe_filter": "lfeFilter",
            "lo_ro_center_mix_level": "loRoCenterMixLevel",
            "lo_ro_surround_mix_level": "loRoSurroundMixLevel",
            "lt_rt_center_mix_level": "ltRtCenterMixLevel",
            "lt_rt_surround_mix_level": "ltRtSurroundMixLevel",
            "metadata_control": "metadataControl",
            "passthrough_control": "passthroughControl",
            "phase_control": "phaseControl",
            "stereo_downmix": "stereoDownmix",
            "surround_ex_mode": "surroundExMode",
            "surround_mode": "surroundMode",
        },
    )
    class Eac3SettingsProperty:
        def __init__(
            self,
            *,
            attenuation_control: typing.Optional[builtins.str] = None,
            bitrate: typing.Optional[jsii.Number] = None,
            bitstream_mode: typing.Optional[builtins.str] = None,
            coding_mode: typing.Optional[builtins.str] = None,
            dc_filter: typing.Optional[builtins.str] = None,
            dialnorm: typing.Optional[jsii.Number] = None,
            drc_line: typing.Optional[builtins.str] = None,
            drc_rf: typing.Optional[builtins.str] = None,
            lfe_control: typing.Optional[builtins.str] = None,
            lfe_filter: typing.Optional[builtins.str] = None,
            lo_ro_center_mix_level: typing.Optional[jsii.Number] = None,
            lo_ro_surround_mix_level: typing.Optional[jsii.Number] = None,
            lt_rt_center_mix_level: typing.Optional[jsii.Number] = None,
            lt_rt_surround_mix_level: typing.Optional[jsii.Number] = None,
            metadata_control: typing.Optional[builtins.str] = None,
            passthrough_control: typing.Optional[builtins.str] = None,
            phase_control: typing.Optional[builtins.str] = None,
            stereo_downmix: typing.Optional[builtins.str] = None,
            surround_ex_mode: typing.Optional[builtins.str] = None,
            surround_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param attenuation_control: ``CfnChannel.Eac3SettingsProperty.AttenuationControl``.
            :param bitrate: ``CfnChannel.Eac3SettingsProperty.Bitrate``.
            :param bitstream_mode: ``CfnChannel.Eac3SettingsProperty.BitstreamMode``.
            :param coding_mode: ``CfnChannel.Eac3SettingsProperty.CodingMode``.
            :param dc_filter: ``CfnChannel.Eac3SettingsProperty.DcFilter``.
            :param dialnorm: ``CfnChannel.Eac3SettingsProperty.Dialnorm``.
            :param drc_line: ``CfnChannel.Eac3SettingsProperty.DrcLine``.
            :param drc_rf: ``CfnChannel.Eac3SettingsProperty.DrcRf``.
            :param lfe_control: ``CfnChannel.Eac3SettingsProperty.LfeControl``.
            :param lfe_filter: ``CfnChannel.Eac3SettingsProperty.LfeFilter``.
            :param lo_ro_center_mix_level: ``CfnChannel.Eac3SettingsProperty.LoRoCenterMixLevel``.
            :param lo_ro_surround_mix_level: ``CfnChannel.Eac3SettingsProperty.LoRoSurroundMixLevel``.
            :param lt_rt_center_mix_level: ``CfnChannel.Eac3SettingsProperty.LtRtCenterMixLevel``.
            :param lt_rt_surround_mix_level: ``CfnChannel.Eac3SettingsProperty.LtRtSurroundMixLevel``.
            :param metadata_control: ``CfnChannel.Eac3SettingsProperty.MetadataControl``.
            :param passthrough_control: ``CfnChannel.Eac3SettingsProperty.PassthroughControl``.
            :param phase_control: ``CfnChannel.Eac3SettingsProperty.PhaseControl``.
            :param stereo_downmix: ``CfnChannel.Eac3SettingsProperty.StereoDownmix``.
            :param surround_ex_mode: ``CfnChannel.Eac3SettingsProperty.SurroundExMode``.
            :param surround_mode: ``CfnChannel.Eac3SettingsProperty.SurroundMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if attenuation_control is not None:
                self._values["attenuation_control"] = attenuation_control
            if bitrate is not None:
                self._values["bitrate"] = bitrate
            if bitstream_mode is not None:
                self._values["bitstream_mode"] = bitstream_mode
            if coding_mode is not None:
                self._values["coding_mode"] = coding_mode
            if dc_filter is not None:
                self._values["dc_filter"] = dc_filter
            if dialnorm is not None:
                self._values["dialnorm"] = dialnorm
            if drc_line is not None:
                self._values["drc_line"] = drc_line
            if drc_rf is not None:
                self._values["drc_rf"] = drc_rf
            if lfe_control is not None:
                self._values["lfe_control"] = lfe_control
            if lfe_filter is not None:
                self._values["lfe_filter"] = lfe_filter
            if lo_ro_center_mix_level is not None:
                self._values["lo_ro_center_mix_level"] = lo_ro_center_mix_level
            if lo_ro_surround_mix_level is not None:
                self._values["lo_ro_surround_mix_level"] = lo_ro_surround_mix_level
            if lt_rt_center_mix_level is not None:
                self._values["lt_rt_center_mix_level"] = lt_rt_center_mix_level
            if lt_rt_surround_mix_level is not None:
                self._values["lt_rt_surround_mix_level"] = lt_rt_surround_mix_level
            if metadata_control is not None:
                self._values["metadata_control"] = metadata_control
            if passthrough_control is not None:
                self._values["passthrough_control"] = passthrough_control
            if phase_control is not None:
                self._values["phase_control"] = phase_control
            if stereo_downmix is not None:
                self._values["stereo_downmix"] = stereo_downmix
            if surround_ex_mode is not None:
                self._values["surround_ex_mode"] = surround_ex_mode
            if surround_mode is not None:
                self._values["surround_mode"] = surround_mode

        @builtins.property
        def attenuation_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Eac3SettingsProperty.AttenuationControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-attenuationcontrol
            """
            result = self._values.get("attenuation_control")
            return result

        @builtins.property
        def bitrate(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.Eac3SettingsProperty.Bitrate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-bitrate
            """
            result = self._values.get("bitrate")
            return result

        @builtins.property
        def bitstream_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Eac3SettingsProperty.BitstreamMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-bitstreammode
            """
            result = self._values.get("bitstream_mode")
            return result

        @builtins.property
        def coding_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Eac3SettingsProperty.CodingMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-codingmode
            """
            result = self._values.get("coding_mode")
            return result

        @builtins.property
        def dc_filter(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Eac3SettingsProperty.DcFilter``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-dcfilter
            """
            result = self._values.get("dc_filter")
            return result

        @builtins.property
        def dialnorm(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.Eac3SettingsProperty.Dialnorm``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-dialnorm
            """
            result = self._values.get("dialnorm")
            return result

        @builtins.property
        def drc_line(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Eac3SettingsProperty.DrcLine``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-drcline
            """
            result = self._values.get("drc_line")
            return result

        @builtins.property
        def drc_rf(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Eac3SettingsProperty.DrcRf``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-drcrf
            """
            result = self._values.get("drc_rf")
            return result

        @builtins.property
        def lfe_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Eac3SettingsProperty.LfeControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-lfecontrol
            """
            result = self._values.get("lfe_control")
            return result

        @builtins.property
        def lfe_filter(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Eac3SettingsProperty.LfeFilter``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-lfefilter
            """
            result = self._values.get("lfe_filter")
            return result

        @builtins.property
        def lo_ro_center_mix_level(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.Eac3SettingsProperty.LoRoCenterMixLevel``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-lorocentermixlevel
            """
            result = self._values.get("lo_ro_center_mix_level")
            return result

        @builtins.property
        def lo_ro_surround_mix_level(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.Eac3SettingsProperty.LoRoSurroundMixLevel``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-lorosurroundmixlevel
            """
            result = self._values.get("lo_ro_surround_mix_level")
            return result

        @builtins.property
        def lt_rt_center_mix_level(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.Eac3SettingsProperty.LtRtCenterMixLevel``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-ltrtcentermixlevel
            """
            result = self._values.get("lt_rt_center_mix_level")
            return result

        @builtins.property
        def lt_rt_surround_mix_level(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.Eac3SettingsProperty.LtRtSurroundMixLevel``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-ltrtsurroundmixlevel
            """
            result = self._values.get("lt_rt_surround_mix_level")
            return result

        @builtins.property
        def metadata_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Eac3SettingsProperty.MetadataControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-metadatacontrol
            """
            result = self._values.get("metadata_control")
            return result

        @builtins.property
        def passthrough_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Eac3SettingsProperty.PassthroughControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-passthroughcontrol
            """
            result = self._values.get("passthrough_control")
            return result

        @builtins.property
        def phase_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Eac3SettingsProperty.PhaseControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-phasecontrol
            """
            result = self._values.get("phase_control")
            return result

        @builtins.property
        def stereo_downmix(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Eac3SettingsProperty.StereoDownmix``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-stereodownmix
            """
            result = self._values.get("stereo_downmix")
            return result

        @builtins.property
        def surround_ex_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Eac3SettingsProperty.SurroundExMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-surroundexmode
            """
            result = self._values.get("surround_ex_mode")
            return result

        @builtins.property
        def surround_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Eac3SettingsProperty.SurroundMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-surroundmode
            """
            result = self._values.get("surround_mode")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Eac3SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.EbuTtDDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "fill_line_gap": "fillLineGap",
            "font_family": "fontFamily",
            "style_control": "styleControl",
        },
    )
    class EbuTtDDestinationSettingsProperty:
        def __init__(
            self,
            *,
            fill_line_gap: typing.Optional[builtins.str] = None,
            font_family: typing.Optional[builtins.str] = None,
            style_control: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param fill_line_gap: ``CfnChannel.EbuTtDDestinationSettingsProperty.FillLineGap``.
            :param font_family: ``CfnChannel.EbuTtDDestinationSettingsProperty.FontFamily``.
            :param style_control: ``CfnChannel.EbuTtDDestinationSettingsProperty.StyleControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if fill_line_gap is not None:
                self._values["fill_line_gap"] = fill_line_gap
            if font_family is not None:
                self._values["font_family"] = font_family
            if style_control is not None:
                self._values["style_control"] = style_control

        @builtins.property
        def fill_line_gap(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.EbuTtDDestinationSettingsProperty.FillLineGap``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html#cfn-medialive-channel-ebuttddestinationsettings-filllinegap
            """
            result = self._values.get("fill_line_gap")
            return result

        @builtins.property
        def font_family(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.EbuTtDDestinationSettingsProperty.FontFamily``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html#cfn-medialive-channel-ebuttddestinationsettings-fontfamily
            """
            result = self._values.get("font_family")
            return result

        @builtins.property
        def style_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.EbuTtDDestinationSettingsProperty.StyleControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html#cfn-medialive-channel-ebuttddestinationsettings-stylecontrol
            """
            result = self._values.get("style_control")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbuTtDDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.EmbeddedDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class EmbeddedDestinationSettingsProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddeddestinationsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EmbeddedDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.EmbeddedPlusScte20DestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class EmbeddedPlusScte20DestinationSettingsProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedplusscte20destinationsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EmbeddedPlusScte20DestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.EmbeddedSourceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "convert608_to708": "convert608To708",
            "scte20_detection": "scte20Detection",
            "source608_channel_number": "source608ChannelNumber",
            "source608_track_number": "source608TrackNumber",
        },
    )
    class EmbeddedSourceSettingsProperty:
        def __init__(
            self,
            *,
            convert608_to708: typing.Optional[builtins.str] = None,
            scte20_detection: typing.Optional[builtins.str] = None,
            source608_channel_number: typing.Optional[jsii.Number] = None,
            source608_track_number: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param convert608_to708: ``CfnChannel.EmbeddedSourceSettingsProperty.Convert608To708``.
            :param scte20_detection: ``CfnChannel.EmbeddedSourceSettingsProperty.Scte20Detection``.
            :param source608_channel_number: ``CfnChannel.EmbeddedSourceSettingsProperty.Source608ChannelNumber``.
            :param source608_track_number: ``CfnChannel.EmbeddedSourceSettingsProperty.Source608TrackNumber``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedsourcesettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if convert608_to708 is not None:
                self._values["convert608_to708"] = convert608_to708
            if scte20_detection is not None:
                self._values["scte20_detection"] = scte20_detection
            if source608_channel_number is not None:
                self._values["source608_channel_number"] = source608_channel_number
            if source608_track_number is not None:
                self._values["source608_track_number"] = source608_track_number

        @builtins.property
        def convert608_to708(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.EmbeddedSourceSettingsProperty.Convert608To708``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedsourcesettings.html#cfn-medialive-channel-embeddedsourcesettings-convert608to708
            """
            result = self._values.get("convert608_to708")
            return result

        @builtins.property
        def scte20_detection(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.EmbeddedSourceSettingsProperty.Scte20Detection``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedsourcesettings.html#cfn-medialive-channel-embeddedsourcesettings-scte20detection
            """
            result = self._values.get("scte20_detection")
            return result

        @builtins.property
        def source608_channel_number(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.EmbeddedSourceSettingsProperty.Source608ChannelNumber``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedsourcesettings.html#cfn-medialive-channel-embeddedsourcesettings-source608channelnumber
            """
            result = self._values.get("source608_channel_number")
            return result

        @builtins.property
        def source608_track_number(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.EmbeddedSourceSettingsProperty.Source608TrackNumber``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedsourcesettings.html#cfn-medialive-channel-embeddedsourcesettings-source608tracknumber
            """
            result = self._values.get("source608_track_number")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EmbeddedSourceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.EncoderSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_descriptions": "audioDescriptions",
            "avail_blanking": "availBlanking",
            "avail_configuration": "availConfiguration",
            "blackout_slate": "blackoutSlate",
            "caption_descriptions": "captionDescriptions",
            "feature_activations": "featureActivations",
            "global_configuration": "globalConfiguration",
            "nielsen_configuration": "nielsenConfiguration",
            "output_groups": "outputGroups",
            "timecode_config": "timecodeConfig",
            "video_descriptions": "videoDescriptions",
        },
    )
    class EncoderSettingsProperty:
        def __init__(
            self,
            *,
            audio_descriptions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.AudioDescriptionProperty", _IResolvable_a771d0ef]]]] = None,
            avail_blanking: typing.Optional[typing.Union["CfnChannel.AvailBlankingProperty", _IResolvable_a771d0ef]] = None,
            avail_configuration: typing.Optional[typing.Union["CfnChannel.AvailConfigurationProperty", _IResolvable_a771d0ef]] = None,
            blackout_slate: typing.Optional[typing.Union["CfnChannel.BlackoutSlateProperty", _IResolvable_a771d0ef]] = None,
            caption_descriptions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.CaptionDescriptionProperty", _IResolvable_a771d0ef]]]] = None,
            feature_activations: typing.Optional[typing.Union["CfnChannel.FeatureActivationsProperty", _IResolvable_a771d0ef]] = None,
            global_configuration: typing.Optional[typing.Union["CfnChannel.GlobalConfigurationProperty", _IResolvable_a771d0ef]] = None,
            nielsen_configuration: typing.Optional[typing.Union["CfnChannel.NielsenConfigurationProperty", _IResolvable_a771d0ef]] = None,
            output_groups: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.OutputGroupProperty", _IResolvable_a771d0ef]]]] = None,
            timecode_config: typing.Optional[typing.Union["CfnChannel.TimecodeConfigProperty", _IResolvable_a771d0ef]] = None,
            video_descriptions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.VideoDescriptionProperty", _IResolvable_a771d0ef]]]] = None,
        ) -> None:
            """
            :param audio_descriptions: ``CfnChannel.EncoderSettingsProperty.AudioDescriptions``.
            :param avail_blanking: ``CfnChannel.EncoderSettingsProperty.AvailBlanking``.
            :param avail_configuration: ``CfnChannel.EncoderSettingsProperty.AvailConfiguration``.
            :param blackout_slate: ``CfnChannel.EncoderSettingsProperty.BlackoutSlate``.
            :param caption_descriptions: ``CfnChannel.EncoderSettingsProperty.CaptionDescriptions``.
            :param feature_activations: ``CfnChannel.EncoderSettingsProperty.FeatureActivations``.
            :param global_configuration: ``CfnChannel.EncoderSettingsProperty.GlobalConfiguration``.
            :param nielsen_configuration: ``CfnChannel.EncoderSettingsProperty.NielsenConfiguration``.
            :param output_groups: ``CfnChannel.EncoderSettingsProperty.OutputGroups``.
            :param timecode_config: ``CfnChannel.EncoderSettingsProperty.TimecodeConfig``.
            :param video_descriptions: ``CfnChannel.EncoderSettingsProperty.VideoDescriptions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_descriptions is not None:
                self._values["audio_descriptions"] = audio_descriptions
            if avail_blanking is not None:
                self._values["avail_blanking"] = avail_blanking
            if avail_configuration is not None:
                self._values["avail_configuration"] = avail_configuration
            if blackout_slate is not None:
                self._values["blackout_slate"] = blackout_slate
            if caption_descriptions is not None:
                self._values["caption_descriptions"] = caption_descriptions
            if feature_activations is not None:
                self._values["feature_activations"] = feature_activations
            if global_configuration is not None:
                self._values["global_configuration"] = global_configuration
            if nielsen_configuration is not None:
                self._values["nielsen_configuration"] = nielsen_configuration
            if output_groups is not None:
                self._values["output_groups"] = output_groups
            if timecode_config is not None:
                self._values["timecode_config"] = timecode_config
            if video_descriptions is not None:
                self._values["video_descriptions"] = video_descriptions

        @builtins.property
        def audio_descriptions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.AudioDescriptionProperty", _IResolvable_a771d0ef]]]]:
            """``CfnChannel.EncoderSettingsProperty.AudioDescriptions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-audiodescriptions
            """
            result = self._values.get("audio_descriptions")
            return result

        @builtins.property
        def avail_blanking(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.AvailBlankingProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.EncoderSettingsProperty.AvailBlanking``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-availblanking
            """
            result = self._values.get("avail_blanking")
            return result

        @builtins.property
        def avail_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.AvailConfigurationProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.EncoderSettingsProperty.AvailConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-availconfiguration
            """
            result = self._values.get("avail_configuration")
            return result

        @builtins.property
        def blackout_slate(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.BlackoutSlateProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.EncoderSettingsProperty.BlackoutSlate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-blackoutslate
            """
            result = self._values.get("blackout_slate")
            return result

        @builtins.property
        def caption_descriptions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.CaptionDescriptionProperty", _IResolvable_a771d0ef]]]]:
            """``CfnChannel.EncoderSettingsProperty.CaptionDescriptions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-captiondescriptions
            """
            result = self._values.get("caption_descriptions")
            return result

        @builtins.property
        def feature_activations(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.FeatureActivationsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.EncoderSettingsProperty.FeatureActivations``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-featureactivations
            """
            result = self._values.get("feature_activations")
            return result

        @builtins.property
        def global_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.GlobalConfigurationProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.EncoderSettingsProperty.GlobalConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-globalconfiguration
            """
            result = self._values.get("global_configuration")
            return result

        @builtins.property
        def nielsen_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.NielsenConfigurationProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.EncoderSettingsProperty.NielsenConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-nielsenconfiguration
            """
            result = self._values.get("nielsen_configuration")
            return result

        @builtins.property
        def output_groups(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.OutputGroupProperty", _IResolvable_a771d0ef]]]]:
            """``CfnChannel.EncoderSettingsProperty.OutputGroups``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-outputgroups
            """
            result = self._values.get("output_groups")
            return result

        @builtins.property
        def timecode_config(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.TimecodeConfigProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.EncoderSettingsProperty.TimecodeConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-timecodeconfig
            """
            result = self._values.get("timecode_config")
            return result

        @builtins.property
        def video_descriptions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.VideoDescriptionProperty", _IResolvable_a771d0ef]]]]:
            """``CfnChannel.EncoderSettingsProperty.VideoDescriptions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-videodescriptions
            """
            result = self._values.get("video_descriptions")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncoderSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.FeatureActivationsProperty",
        jsii_struct_bases=[],
        name_mapping={"input_prepare_schedule_actions": "inputPrepareScheduleActions"},
    )
    class FeatureActivationsProperty:
        def __init__(
            self,
            *,
            input_prepare_schedule_actions: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param input_prepare_schedule_actions: ``CfnChannel.FeatureActivationsProperty.InputPrepareScheduleActions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-featureactivations.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if input_prepare_schedule_actions is not None:
                self._values["input_prepare_schedule_actions"] = input_prepare_schedule_actions

        @builtins.property
        def input_prepare_schedule_actions(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.FeatureActivationsProperty.InputPrepareScheduleActions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-featureactivations.html#cfn-medialive-channel-featureactivations-inputpreparescheduleactions
            """
            result = self._values.get("input_prepare_schedule_actions")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FeatureActivationsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.FecOutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "column_depth": "columnDepth",
            "include_fec": "includeFec",
            "row_length": "rowLength",
        },
    )
    class FecOutputSettingsProperty:
        def __init__(
            self,
            *,
            column_depth: typing.Optional[jsii.Number] = None,
            include_fec: typing.Optional[builtins.str] = None,
            row_length: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param column_depth: ``CfnChannel.FecOutputSettingsProperty.ColumnDepth``.
            :param include_fec: ``CfnChannel.FecOutputSettingsProperty.IncludeFec``.
            :param row_length: ``CfnChannel.FecOutputSettingsProperty.RowLength``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fecoutputsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if column_depth is not None:
                self._values["column_depth"] = column_depth
            if include_fec is not None:
                self._values["include_fec"] = include_fec
            if row_length is not None:
                self._values["row_length"] = row_length

        @builtins.property
        def column_depth(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.FecOutputSettingsProperty.ColumnDepth``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fecoutputsettings.html#cfn-medialive-channel-fecoutputsettings-columndepth
            """
            result = self._values.get("column_depth")
            return result

        @builtins.property
        def include_fec(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.FecOutputSettingsProperty.IncludeFec``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fecoutputsettings.html#cfn-medialive-channel-fecoutputsettings-includefec
            """
            result = self._values.get("include_fec")
            return result

        @builtins.property
        def row_length(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.FecOutputSettingsProperty.RowLength``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fecoutputsettings.html#cfn-medialive-channel-fecoutputsettings-rowlength
            """
            result = self._values.get("row_length")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FecOutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.Fmp4HlsSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_rendition_sets": "audioRenditionSets",
            "nielsen_id3_behavior": "nielsenId3Behavior",
            "timed_metadata_behavior": "timedMetadataBehavior",
        },
    )
    class Fmp4HlsSettingsProperty:
        def __init__(
            self,
            *,
            audio_rendition_sets: typing.Optional[builtins.str] = None,
            nielsen_id3_behavior: typing.Optional[builtins.str] = None,
            timed_metadata_behavior: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param audio_rendition_sets: ``CfnChannel.Fmp4HlsSettingsProperty.AudioRenditionSets``.
            :param nielsen_id3_behavior: ``CfnChannel.Fmp4HlsSettingsProperty.NielsenId3Behavior``.
            :param timed_metadata_behavior: ``CfnChannel.Fmp4HlsSettingsProperty.TimedMetadataBehavior``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fmp4hlssettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_rendition_sets is not None:
                self._values["audio_rendition_sets"] = audio_rendition_sets
            if nielsen_id3_behavior is not None:
                self._values["nielsen_id3_behavior"] = nielsen_id3_behavior
            if timed_metadata_behavior is not None:
                self._values["timed_metadata_behavior"] = timed_metadata_behavior

        @builtins.property
        def audio_rendition_sets(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Fmp4HlsSettingsProperty.AudioRenditionSets``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fmp4hlssettings.html#cfn-medialive-channel-fmp4hlssettings-audiorenditionsets
            """
            result = self._values.get("audio_rendition_sets")
            return result

        @builtins.property
        def nielsen_id3_behavior(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Fmp4HlsSettingsProperty.NielsenId3Behavior``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fmp4hlssettings.html#cfn-medialive-channel-fmp4hlssettings-nielsenid3behavior
            """
            result = self._values.get("nielsen_id3_behavior")
            return result

        @builtins.property
        def timed_metadata_behavior(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Fmp4HlsSettingsProperty.TimedMetadataBehavior``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fmp4hlssettings.html#cfn-medialive-channel-fmp4hlssettings-timedmetadatabehavior
            """
            result = self._values.get("timed_metadata_behavior")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Fmp4HlsSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.FrameCaptureGroupSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination"},
    )
    class FrameCaptureGroupSettingsProperty:
        def __init__(
            self,
            *,
            destination: typing.Optional[typing.Union["CfnChannel.OutputLocationRefProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param destination: ``CfnChannel.FrameCaptureGroupSettingsProperty.Destination``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturegroupsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if destination is not None:
                self._values["destination"] = destination

        @builtins.property
        def destination(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.OutputLocationRefProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.FrameCaptureGroupSettingsProperty.Destination``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturegroupsettings.html#cfn-medialive-channel-framecapturegroupsettings-destination
            """
            result = self._values.get("destination")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FrameCaptureGroupSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.FrameCaptureOutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"name_modifier": "nameModifier"},
    )
    class FrameCaptureOutputSettingsProperty:
        def __init__(
            self,
            *,
            name_modifier: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param name_modifier: ``CfnChannel.FrameCaptureOutputSettingsProperty.NameModifier``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptureoutputsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if name_modifier is not None:
                self._values["name_modifier"] = name_modifier

        @builtins.property
        def name_modifier(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.FrameCaptureOutputSettingsProperty.NameModifier``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptureoutputsettings.html#cfn-medialive-channel-framecaptureoutputsettings-namemodifier
            """
            result = self._values.get("name_modifier")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FrameCaptureOutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.FrameCaptureSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "capture_interval": "captureInterval",
            "capture_interval_units": "captureIntervalUnits",
        },
    )
    class FrameCaptureSettingsProperty:
        def __init__(
            self,
            *,
            capture_interval: typing.Optional[jsii.Number] = None,
            capture_interval_units: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param capture_interval: ``CfnChannel.FrameCaptureSettingsProperty.CaptureInterval``.
            :param capture_interval_units: ``CfnChannel.FrameCaptureSettingsProperty.CaptureIntervalUnits``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturesettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if capture_interval is not None:
                self._values["capture_interval"] = capture_interval
            if capture_interval_units is not None:
                self._values["capture_interval_units"] = capture_interval_units

        @builtins.property
        def capture_interval(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.FrameCaptureSettingsProperty.CaptureInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturesettings.html#cfn-medialive-channel-framecapturesettings-captureinterval
            """
            result = self._values.get("capture_interval")
            return result

        @builtins.property
        def capture_interval_units(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.FrameCaptureSettingsProperty.CaptureIntervalUnits``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturesettings.html#cfn-medialive-channel-framecapturesettings-captureintervalunits
            """
            result = self._values.get("capture_interval_units")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FrameCaptureSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.GlobalConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "initial_audio_gain": "initialAudioGain",
            "input_end_action": "inputEndAction",
            "input_loss_behavior": "inputLossBehavior",
            "output_locking_mode": "outputLockingMode",
            "output_timing_source": "outputTimingSource",
            "support_low_framerate_inputs": "supportLowFramerateInputs",
        },
    )
    class GlobalConfigurationProperty:
        def __init__(
            self,
            *,
            initial_audio_gain: typing.Optional[jsii.Number] = None,
            input_end_action: typing.Optional[builtins.str] = None,
            input_loss_behavior: typing.Optional[typing.Union["CfnChannel.InputLossBehaviorProperty", _IResolvable_a771d0ef]] = None,
            output_locking_mode: typing.Optional[builtins.str] = None,
            output_timing_source: typing.Optional[builtins.str] = None,
            support_low_framerate_inputs: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param initial_audio_gain: ``CfnChannel.GlobalConfigurationProperty.InitialAudioGain``.
            :param input_end_action: ``CfnChannel.GlobalConfigurationProperty.InputEndAction``.
            :param input_loss_behavior: ``CfnChannel.GlobalConfigurationProperty.InputLossBehavior``.
            :param output_locking_mode: ``CfnChannel.GlobalConfigurationProperty.OutputLockingMode``.
            :param output_timing_source: ``CfnChannel.GlobalConfigurationProperty.OutputTimingSource``.
            :param support_low_framerate_inputs: ``CfnChannel.GlobalConfigurationProperty.SupportLowFramerateInputs``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if initial_audio_gain is not None:
                self._values["initial_audio_gain"] = initial_audio_gain
            if input_end_action is not None:
                self._values["input_end_action"] = input_end_action
            if input_loss_behavior is not None:
                self._values["input_loss_behavior"] = input_loss_behavior
            if output_locking_mode is not None:
                self._values["output_locking_mode"] = output_locking_mode
            if output_timing_source is not None:
                self._values["output_timing_source"] = output_timing_source
            if support_low_framerate_inputs is not None:
                self._values["support_low_framerate_inputs"] = support_low_framerate_inputs

        @builtins.property
        def initial_audio_gain(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.GlobalConfigurationProperty.InitialAudioGain``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html#cfn-medialive-channel-globalconfiguration-initialaudiogain
            """
            result = self._values.get("initial_audio_gain")
            return result

        @builtins.property
        def input_end_action(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.GlobalConfigurationProperty.InputEndAction``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html#cfn-medialive-channel-globalconfiguration-inputendaction
            """
            result = self._values.get("input_end_action")
            return result

        @builtins.property
        def input_loss_behavior(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.InputLossBehaviorProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.GlobalConfigurationProperty.InputLossBehavior``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html#cfn-medialive-channel-globalconfiguration-inputlossbehavior
            """
            result = self._values.get("input_loss_behavior")
            return result

        @builtins.property
        def output_locking_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.GlobalConfigurationProperty.OutputLockingMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html#cfn-medialive-channel-globalconfiguration-outputlockingmode
            """
            result = self._values.get("output_locking_mode")
            return result

        @builtins.property
        def output_timing_source(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.GlobalConfigurationProperty.OutputTimingSource``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html#cfn-medialive-channel-globalconfiguration-outputtimingsource
            """
            result = self._values.get("output_timing_source")
            return result

        @builtins.property
        def support_low_framerate_inputs(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.GlobalConfigurationProperty.SupportLowFramerateInputs``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html#cfn-medialive-channel-globalconfiguration-supportlowframerateinputs
            """
            result = self._values.get("support_low_framerate_inputs")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlobalConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.H264ColorSpaceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "color_space_passthrough_settings": "colorSpacePassthroughSettings",
            "rec601_settings": "rec601Settings",
            "rec709_settings": "rec709Settings",
        },
    )
    class H264ColorSpaceSettingsProperty:
        def __init__(
            self,
            *,
            color_space_passthrough_settings: typing.Optional[typing.Union["CfnChannel.ColorSpacePassthroughSettingsProperty", _IResolvable_a771d0ef]] = None,
            rec601_settings: typing.Optional[typing.Union["CfnChannel.Rec601SettingsProperty", _IResolvable_a771d0ef]] = None,
            rec709_settings: typing.Optional[typing.Union["CfnChannel.Rec709SettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param color_space_passthrough_settings: ``CfnChannel.H264ColorSpaceSettingsProperty.ColorSpacePassthroughSettings``.
            :param rec601_settings: ``CfnChannel.H264ColorSpaceSettingsProperty.Rec601Settings``.
            :param rec709_settings: ``CfnChannel.H264ColorSpaceSettingsProperty.Rec709Settings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264colorspacesettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if color_space_passthrough_settings is not None:
                self._values["color_space_passthrough_settings"] = color_space_passthrough_settings
            if rec601_settings is not None:
                self._values["rec601_settings"] = rec601_settings
            if rec709_settings is not None:
                self._values["rec709_settings"] = rec709_settings

        @builtins.property
        def color_space_passthrough_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.ColorSpacePassthroughSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.H264ColorSpaceSettingsProperty.ColorSpacePassthroughSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264colorspacesettings.html#cfn-medialive-channel-h264colorspacesettings-colorspacepassthroughsettings
            """
            result = self._values.get("color_space_passthrough_settings")
            return result

        @builtins.property
        def rec601_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.Rec601SettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.H264ColorSpaceSettingsProperty.Rec601Settings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264colorspacesettings.html#cfn-medialive-channel-h264colorspacesettings-rec601settings
            """
            result = self._values.get("rec601_settings")
            return result

        @builtins.property
        def rec709_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.Rec709SettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.H264ColorSpaceSettingsProperty.Rec709Settings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264colorspacesettings.html#cfn-medialive-channel-h264colorspacesettings-rec709settings
            """
            result = self._values.get("rec709_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "H264ColorSpaceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.H264FilterSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"temporal_filter_settings": "temporalFilterSettings"},
    )
    class H264FilterSettingsProperty:
        def __init__(
            self,
            *,
            temporal_filter_settings: typing.Optional[typing.Union["CfnChannel.TemporalFilterSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param temporal_filter_settings: ``CfnChannel.H264FilterSettingsProperty.TemporalFilterSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264filtersettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if temporal_filter_settings is not None:
                self._values["temporal_filter_settings"] = temporal_filter_settings

        @builtins.property
        def temporal_filter_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.TemporalFilterSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.H264FilterSettingsProperty.TemporalFilterSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264filtersettings.html#cfn-medialive-channel-h264filtersettings-temporalfiltersettings
            """
            result = self._values.get("temporal_filter_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "H264FilterSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.H264SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "adaptive_quantization": "adaptiveQuantization",
            "afd_signaling": "afdSignaling",
            "bitrate": "bitrate",
            "buf_fill_pct": "bufFillPct",
            "buf_size": "bufSize",
            "color_metadata": "colorMetadata",
            "color_space_settings": "colorSpaceSettings",
            "entropy_encoding": "entropyEncoding",
            "filter_settings": "filterSettings",
            "fixed_afd": "fixedAfd",
            "flicker_aq": "flickerAq",
            "force_field_pictures": "forceFieldPictures",
            "framerate_control": "framerateControl",
            "framerate_denominator": "framerateDenominator",
            "framerate_numerator": "framerateNumerator",
            "gop_b_reference": "gopBReference",
            "gop_closed_cadence": "gopClosedCadence",
            "gop_num_b_frames": "gopNumBFrames",
            "gop_size": "gopSize",
            "gop_size_units": "gopSizeUnits",
            "level": "level",
            "look_ahead_rate_control": "lookAheadRateControl",
            "max_bitrate": "maxBitrate",
            "min_i_interval": "minIInterval",
            "num_ref_frames": "numRefFrames",
            "par_control": "parControl",
            "par_denominator": "parDenominator",
            "par_numerator": "parNumerator",
            "profile": "profile",
            "quality_level": "qualityLevel",
            "qvbr_quality_level": "qvbrQualityLevel",
            "rate_control_mode": "rateControlMode",
            "scan_type": "scanType",
            "scene_change_detect": "sceneChangeDetect",
            "slices": "slices",
            "softness": "softness",
            "spatial_aq": "spatialAq",
            "subgop_length": "subgopLength",
            "syntax": "syntax",
            "temporal_aq": "temporalAq",
            "timecode_insertion": "timecodeInsertion",
        },
    )
    class H264SettingsProperty:
        def __init__(
            self,
            *,
            adaptive_quantization: typing.Optional[builtins.str] = None,
            afd_signaling: typing.Optional[builtins.str] = None,
            bitrate: typing.Optional[jsii.Number] = None,
            buf_fill_pct: typing.Optional[jsii.Number] = None,
            buf_size: typing.Optional[jsii.Number] = None,
            color_metadata: typing.Optional[builtins.str] = None,
            color_space_settings: typing.Optional[typing.Union["CfnChannel.H264ColorSpaceSettingsProperty", _IResolvable_a771d0ef]] = None,
            entropy_encoding: typing.Optional[builtins.str] = None,
            filter_settings: typing.Optional[typing.Union["CfnChannel.H264FilterSettingsProperty", _IResolvable_a771d0ef]] = None,
            fixed_afd: typing.Optional[builtins.str] = None,
            flicker_aq: typing.Optional[builtins.str] = None,
            force_field_pictures: typing.Optional[builtins.str] = None,
            framerate_control: typing.Optional[builtins.str] = None,
            framerate_denominator: typing.Optional[jsii.Number] = None,
            framerate_numerator: typing.Optional[jsii.Number] = None,
            gop_b_reference: typing.Optional[builtins.str] = None,
            gop_closed_cadence: typing.Optional[jsii.Number] = None,
            gop_num_b_frames: typing.Optional[jsii.Number] = None,
            gop_size: typing.Optional[jsii.Number] = None,
            gop_size_units: typing.Optional[builtins.str] = None,
            level: typing.Optional[builtins.str] = None,
            look_ahead_rate_control: typing.Optional[builtins.str] = None,
            max_bitrate: typing.Optional[jsii.Number] = None,
            min_i_interval: typing.Optional[jsii.Number] = None,
            num_ref_frames: typing.Optional[jsii.Number] = None,
            par_control: typing.Optional[builtins.str] = None,
            par_denominator: typing.Optional[jsii.Number] = None,
            par_numerator: typing.Optional[jsii.Number] = None,
            profile: typing.Optional[builtins.str] = None,
            quality_level: typing.Optional[builtins.str] = None,
            qvbr_quality_level: typing.Optional[jsii.Number] = None,
            rate_control_mode: typing.Optional[builtins.str] = None,
            scan_type: typing.Optional[builtins.str] = None,
            scene_change_detect: typing.Optional[builtins.str] = None,
            slices: typing.Optional[jsii.Number] = None,
            softness: typing.Optional[jsii.Number] = None,
            spatial_aq: typing.Optional[builtins.str] = None,
            subgop_length: typing.Optional[builtins.str] = None,
            syntax: typing.Optional[builtins.str] = None,
            temporal_aq: typing.Optional[builtins.str] = None,
            timecode_insertion: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param adaptive_quantization: ``CfnChannel.H264SettingsProperty.AdaptiveQuantization``.
            :param afd_signaling: ``CfnChannel.H264SettingsProperty.AfdSignaling``.
            :param bitrate: ``CfnChannel.H264SettingsProperty.Bitrate``.
            :param buf_fill_pct: ``CfnChannel.H264SettingsProperty.BufFillPct``.
            :param buf_size: ``CfnChannel.H264SettingsProperty.BufSize``.
            :param color_metadata: ``CfnChannel.H264SettingsProperty.ColorMetadata``.
            :param color_space_settings: ``CfnChannel.H264SettingsProperty.ColorSpaceSettings``.
            :param entropy_encoding: ``CfnChannel.H264SettingsProperty.EntropyEncoding``.
            :param filter_settings: ``CfnChannel.H264SettingsProperty.FilterSettings``.
            :param fixed_afd: ``CfnChannel.H264SettingsProperty.FixedAfd``.
            :param flicker_aq: ``CfnChannel.H264SettingsProperty.FlickerAq``.
            :param force_field_pictures: ``CfnChannel.H264SettingsProperty.ForceFieldPictures``.
            :param framerate_control: ``CfnChannel.H264SettingsProperty.FramerateControl``.
            :param framerate_denominator: ``CfnChannel.H264SettingsProperty.FramerateDenominator``.
            :param framerate_numerator: ``CfnChannel.H264SettingsProperty.FramerateNumerator``.
            :param gop_b_reference: ``CfnChannel.H264SettingsProperty.GopBReference``.
            :param gop_closed_cadence: ``CfnChannel.H264SettingsProperty.GopClosedCadence``.
            :param gop_num_b_frames: ``CfnChannel.H264SettingsProperty.GopNumBFrames``.
            :param gop_size: ``CfnChannel.H264SettingsProperty.GopSize``.
            :param gop_size_units: ``CfnChannel.H264SettingsProperty.GopSizeUnits``.
            :param level: ``CfnChannel.H264SettingsProperty.Level``.
            :param look_ahead_rate_control: ``CfnChannel.H264SettingsProperty.LookAheadRateControl``.
            :param max_bitrate: ``CfnChannel.H264SettingsProperty.MaxBitrate``.
            :param min_i_interval: ``CfnChannel.H264SettingsProperty.MinIInterval``.
            :param num_ref_frames: ``CfnChannel.H264SettingsProperty.NumRefFrames``.
            :param par_control: ``CfnChannel.H264SettingsProperty.ParControl``.
            :param par_denominator: ``CfnChannel.H264SettingsProperty.ParDenominator``.
            :param par_numerator: ``CfnChannel.H264SettingsProperty.ParNumerator``.
            :param profile: ``CfnChannel.H264SettingsProperty.Profile``.
            :param quality_level: ``CfnChannel.H264SettingsProperty.QualityLevel``.
            :param qvbr_quality_level: ``CfnChannel.H264SettingsProperty.QvbrQualityLevel``.
            :param rate_control_mode: ``CfnChannel.H264SettingsProperty.RateControlMode``.
            :param scan_type: ``CfnChannel.H264SettingsProperty.ScanType``.
            :param scene_change_detect: ``CfnChannel.H264SettingsProperty.SceneChangeDetect``.
            :param slices: ``CfnChannel.H264SettingsProperty.Slices``.
            :param softness: ``CfnChannel.H264SettingsProperty.Softness``.
            :param spatial_aq: ``CfnChannel.H264SettingsProperty.SpatialAq``.
            :param subgop_length: ``CfnChannel.H264SettingsProperty.SubgopLength``.
            :param syntax: ``CfnChannel.H264SettingsProperty.Syntax``.
            :param temporal_aq: ``CfnChannel.H264SettingsProperty.TemporalAq``.
            :param timecode_insertion: ``CfnChannel.H264SettingsProperty.TimecodeInsertion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if adaptive_quantization is not None:
                self._values["adaptive_quantization"] = adaptive_quantization
            if afd_signaling is not None:
                self._values["afd_signaling"] = afd_signaling
            if bitrate is not None:
                self._values["bitrate"] = bitrate
            if buf_fill_pct is not None:
                self._values["buf_fill_pct"] = buf_fill_pct
            if buf_size is not None:
                self._values["buf_size"] = buf_size
            if color_metadata is not None:
                self._values["color_metadata"] = color_metadata
            if color_space_settings is not None:
                self._values["color_space_settings"] = color_space_settings
            if entropy_encoding is not None:
                self._values["entropy_encoding"] = entropy_encoding
            if filter_settings is not None:
                self._values["filter_settings"] = filter_settings
            if fixed_afd is not None:
                self._values["fixed_afd"] = fixed_afd
            if flicker_aq is not None:
                self._values["flicker_aq"] = flicker_aq
            if force_field_pictures is not None:
                self._values["force_field_pictures"] = force_field_pictures
            if framerate_control is not None:
                self._values["framerate_control"] = framerate_control
            if framerate_denominator is not None:
                self._values["framerate_denominator"] = framerate_denominator
            if framerate_numerator is not None:
                self._values["framerate_numerator"] = framerate_numerator
            if gop_b_reference is not None:
                self._values["gop_b_reference"] = gop_b_reference
            if gop_closed_cadence is not None:
                self._values["gop_closed_cadence"] = gop_closed_cadence
            if gop_num_b_frames is not None:
                self._values["gop_num_b_frames"] = gop_num_b_frames
            if gop_size is not None:
                self._values["gop_size"] = gop_size
            if gop_size_units is not None:
                self._values["gop_size_units"] = gop_size_units
            if level is not None:
                self._values["level"] = level
            if look_ahead_rate_control is not None:
                self._values["look_ahead_rate_control"] = look_ahead_rate_control
            if max_bitrate is not None:
                self._values["max_bitrate"] = max_bitrate
            if min_i_interval is not None:
                self._values["min_i_interval"] = min_i_interval
            if num_ref_frames is not None:
                self._values["num_ref_frames"] = num_ref_frames
            if par_control is not None:
                self._values["par_control"] = par_control
            if par_denominator is not None:
                self._values["par_denominator"] = par_denominator
            if par_numerator is not None:
                self._values["par_numerator"] = par_numerator
            if profile is not None:
                self._values["profile"] = profile
            if quality_level is not None:
                self._values["quality_level"] = quality_level
            if qvbr_quality_level is not None:
                self._values["qvbr_quality_level"] = qvbr_quality_level
            if rate_control_mode is not None:
                self._values["rate_control_mode"] = rate_control_mode
            if scan_type is not None:
                self._values["scan_type"] = scan_type
            if scene_change_detect is not None:
                self._values["scene_change_detect"] = scene_change_detect
            if slices is not None:
                self._values["slices"] = slices
            if softness is not None:
                self._values["softness"] = softness
            if spatial_aq is not None:
                self._values["spatial_aq"] = spatial_aq
            if subgop_length is not None:
                self._values["subgop_length"] = subgop_length
            if syntax is not None:
                self._values["syntax"] = syntax
            if temporal_aq is not None:
                self._values["temporal_aq"] = temporal_aq
            if timecode_insertion is not None:
                self._values["timecode_insertion"] = timecode_insertion

        @builtins.property
        def adaptive_quantization(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.AdaptiveQuantization``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-adaptivequantization
            """
            result = self._values.get("adaptive_quantization")
            return result

        @builtins.property
        def afd_signaling(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.AfdSignaling``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-afdsignaling
            """
            result = self._values.get("afd_signaling")
            return result

        @builtins.property
        def bitrate(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H264SettingsProperty.Bitrate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-bitrate
            """
            result = self._values.get("bitrate")
            return result

        @builtins.property
        def buf_fill_pct(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H264SettingsProperty.BufFillPct``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-buffillpct
            """
            result = self._values.get("buf_fill_pct")
            return result

        @builtins.property
        def buf_size(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H264SettingsProperty.BufSize``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-bufsize
            """
            result = self._values.get("buf_size")
            return result

        @builtins.property
        def color_metadata(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.ColorMetadata``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-colormetadata
            """
            result = self._values.get("color_metadata")
            return result

        @builtins.property
        def color_space_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.H264ColorSpaceSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.H264SettingsProperty.ColorSpaceSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-colorspacesettings
            """
            result = self._values.get("color_space_settings")
            return result

        @builtins.property
        def entropy_encoding(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.EntropyEncoding``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-entropyencoding
            """
            result = self._values.get("entropy_encoding")
            return result

        @builtins.property
        def filter_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.H264FilterSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.H264SettingsProperty.FilterSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-filtersettings
            """
            result = self._values.get("filter_settings")
            return result

        @builtins.property
        def fixed_afd(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.FixedAfd``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-fixedafd
            """
            result = self._values.get("fixed_afd")
            return result

        @builtins.property
        def flicker_aq(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.FlickerAq``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-flickeraq
            """
            result = self._values.get("flicker_aq")
            return result

        @builtins.property
        def force_field_pictures(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.ForceFieldPictures``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-forcefieldpictures
            """
            result = self._values.get("force_field_pictures")
            return result

        @builtins.property
        def framerate_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.FramerateControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-frameratecontrol
            """
            result = self._values.get("framerate_control")
            return result

        @builtins.property
        def framerate_denominator(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H264SettingsProperty.FramerateDenominator``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-frameratedenominator
            """
            result = self._values.get("framerate_denominator")
            return result

        @builtins.property
        def framerate_numerator(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H264SettingsProperty.FramerateNumerator``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-frameratenumerator
            """
            result = self._values.get("framerate_numerator")
            return result

        @builtins.property
        def gop_b_reference(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.GopBReference``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-gopbreference
            """
            result = self._values.get("gop_b_reference")
            return result

        @builtins.property
        def gop_closed_cadence(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H264SettingsProperty.GopClosedCadence``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-gopclosedcadence
            """
            result = self._values.get("gop_closed_cadence")
            return result

        @builtins.property
        def gop_num_b_frames(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H264SettingsProperty.GopNumBFrames``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-gopnumbframes
            """
            result = self._values.get("gop_num_b_frames")
            return result

        @builtins.property
        def gop_size(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H264SettingsProperty.GopSize``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-gopsize
            """
            result = self._values.get("gop_size")
            return result

        @builtins.property
        def gop_size_units(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.GopSizeUnits``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-gopsizeunits
            """
            result = self._values.get("gop_size_units")
            return result

        @builtins.property
        def level(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.Level``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-level
            """
            result = self._values.get("level")
            return result

        @builtins.property
        def look_ahead_rate_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.LookAheadRateControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-lookaheadratecontrol
            """
            result = self._values.get("look_ahead_rate_control")
            return result

        @builtins.property
        def max_bitrate(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H264SettingsProperty.MaxBitrate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-maxbitrate
            """
            result = self._values.get("max_bitrate")
            return result

        @builtins.property
        def min_i_interval(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H264SettingsProperty.MinIInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-miniinterval
            """
            result = self._values.get("min_i_interval")
            return result

        @builtins.property
        def num_ref_frames(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H264SettingsProperty.NumRefFrames``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-numrefframes
            """
            result = self._values.get("num_ref_frames")
            return result

        @builtins.property
        def par_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.ParControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-parcontrol
            """
            result = self._values.get("par_control")
            return result

        @builtins.property
        def par_denominator(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H264SettingsProperty.ParDenominator``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-pardenominator
            """
            result = self._values.get("par_denominator")
            return result

        @builtins.property
        def par_numerator(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H264SettingsProperty.ParNumerator``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-parnumerator
            """
            result = self._values.get("par_numerator")
            return result

        @builtins.property
        def profile(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.Profile``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-profile
            """
            result = self._values.get("profile")
            return result

        @builtins.property
        def quality_level(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.QualityLevel``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-qualitylevel
            """
            result = self._values.get("quality_level")
            return result

        @builtins.property
        def qvbr_quality_level(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H264SettingsProperty.QvbrQualityLevel``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-qvbrqualitylevel
            """
            result = self._values.get("qvbr_quality_level")
            return result

        @builtins.property
        def rate_control_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.RateControlMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-ratecontrolmode
            """
            result = self._values.get("rate_control_mode")
            return result

        @builtins.property
        def scan_type(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.ScanType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-scantype
            """
            result = self._values.get("scan_type")
            return result

        @builtins.property
        def scene_change_detect(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.SceneChangeDetect``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-scenechangedetect
            """
            result = self._values.get("scene_change_detect")
            return result

        @builtins.property
        def slices(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H264SettingsProperty.Slices``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-slices
            """
            result = self._values.get("slices")
            return result

        @builtins.property
        def softness(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H264SettingsProperty.Softness``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-softness
            """
            result = self._values.get("softness")
            return result

        @builtins.property
        def spatial_aq(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.SpatialAq``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-spatialaq
            """
            result = self._values.get("spatial_aq")
            return result

        @builtins.property
        def subgop_length(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.SubgopLength``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-subgoplength
            """
            result = self._values.get("subgop_length")
            return result

        @builtins.property
        def syntax(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.Syntax``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-syntax
            """
            result = self._values.get("syntax")
            return result

        @builtins.property
        def temporal_aq(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.TemporalAq``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-temporalaq
            """
            result = self._values.get("temporal_aq")
            return result

        @builtins.property
        def timecode_insertion(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H264SettingsProperty.TimecodeInsertion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-timecodeinsertion
            """
            result = self._values.get("timecode_insertion")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "H264SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.H265ColorSpaceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "color_space_passthrough_settings": "colorSpacePassthroughSettings",
            "hdr10_settings": "hdr10Settings",
            "rec601_settings": "rec601Settings",
            "rec709_settings": "rec709Settings",
        },
    )
    class H265ColorSpaceSettingsProperty:
        def __init__(
            self,
            *,
            color_space_passthrough_settings: typing.Optional[typing.Union["CfnChannel.ColorSpacePassthroughSettingsProperty", _IResolvable_a771d0ef]] = None,
            hdr10_settings: typing.Optional[typing.Union["CfnChannel.Hdr10SettingsProperty", _IResolvable_a771d0ef]] = None,
            rec601_settings: typing.Optional[typing.Union["CfnChannel.Rec601SettingsProperty", _IResolvable_a771d0ef]] = None,
            rec709_settings: typing.Optional[typing.Union["CfnChannel.Rec709SettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param color_space_passthrough_settings: ``CfnChannel.H265ColorSpaceSettingsProperty.ColorSpacePassthroughSettings``.
            :param hdr10_settings: ``CfnChannel.H265ColorSpaceSettingsProperty.Hdr10Settings``.
            :param rec601_settings: ``CfnChannel.H265ColorSpaceSettingsProperty.Rec601Settings``.
            :param rec709_settings: ``CfnChannel.H265ColorSpaceSettingsProperty.Rec709Settings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if color_space_passthrough_settings is not None:
                self._values["color_space_passthrough_settings"] = color_space_passthrough_settings
            if hdr10_settings is not None:
                self._values["hdr10_settings"] = hdr10_settings
            if rec601_settings is not None:
                self._values["rec601_settings"] = rec601_settings
            if rec709_settings is not None:
                self._values["rec709_settings"] = rec709_settings

        @builtins.property
        def color_space_passthrough_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.ColorSpacePassthroughSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.H265ColorSpaceSettingsProperty.ColorSpacePassthroughSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html#cfn-medialive-channel-h265colorspacesettings-colorspacepassthroughsettings
            """
            result = self._values.get("color_space_passthrough_settings")
            return result

        @builtins.property
        def hdr10_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.Hdr10SettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.H265ColorSpaceSettingsProperty.Hdr10Settings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html#cfn-medialive-channel-h265colorspacesettings-hdr10settings
            """
            result = self._values.get("hdr10_settings")
            return result

        @builtins.property
        def rec601_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.Rec601SettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.H265ColorSpaceSettingsProperty.Rec601Settings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html#cfn-medialive-channel-h265colorspacesettings-rec601settings
            """
            result = self._values.get("rec601_settings")
            return result

        @builtins.property
        def rec709_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.Rec709SettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.H265ColorSpaceSettingsProperty.Rec709Settings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html#cfn-medialive-channel-h265colorspacesettings-rec709settings
            """
            result = self._values.get("rec709_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "H265ColorSpaceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.H265FilterSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"temporal_filter_settings": "temporalFilterSettings"},
    )
    class H265FilterSettingsProperty:
        def __init__(
            self,
            *,
            temporal_filter_settings: typing.Optional[typing.Union["CfnChannel.TemporalFilterSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param temporal_filter_settings: ``CfnChannel.H265FilterSettingsProperty.TemporalFilterSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265filtersettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if temporal_filter_settings is not None:
                self._values["temporal_filter_settings"] = temporal_filter_settings

        @builtins.property
        def temporal_filter_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.TemporalFilterSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.H265FilterSettingsProperty.TemporalFilterSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265filtersettings.html#cfn-medialive-channel-h265filtersettings-temporalfiltersettings
            """
            result = self._values.get("temporal_filter_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "H265FilterSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.H265SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "adaptive_quantization": "adaptiveQuantization",
            "afd_signaling": "afdSignaling",
            "alternative_transfer_function": "alternativeTransferFunction",
            "bitrate": "bitrate",
            "buf_size": "bufSize",
            "color_metadata": "colorMetadata",
            "color_space_settings": "colorSpaceSettings",
            "filter_settings": "filterSettings",
            "fixed_afd": "fixedAfd",
            "flicker_aq": "flickerAq",
            "framerate_denominator": "framerateDenominator",
            "framerate_numerator": "framerateNumerator",
            "gop_closed_cadence": "gopClosedCadence",
            "gop_size": "gopSize",
            "gop_size_units": "gopSizeUnits",
            "level": "level",
            "look_ahead_rate_control": "lookAheadRateControl",
            "max_bitrate": "maxBitrate",
            "min_i_interval": "minIInterval",
            "par_denominator": "parDenominator",
            "par_numerator": "parNumerator",
            "profile": "profile",
            "qvbr_quality_level": "qvbrQualityLevel",
            "rate_control_mode": "rateControlMode",
            "scan_type": "scanType",
            "scene_change_detect": "sceneChangeDetect",
            "slices": "slices",
            "tier": "tier",
            "timecode_insertion": "timecodeInsertion",
        },
    )
    class H265SettingsProperty:
        def __init__(
            self,
            *,
            adaptive_quantization: typing.Optional[builtins.str] = None,
            afd_signaling: typing.Optional[builtins.str] = None,
            alternative_transfer_function: typing.Optional[builtins.str] = None,
            bitrate: typing.Optional[jsii.Number] = None,
            buf_size: typing.Optional[jsii.Number] = None,
            color_metadata: typing.Optional[builtins.str] = None,
            color_space_settings: typing.Optional[typing.Union["CfnChannel.H265ColorSpaceSettingsProperty", _IResolvable_a771d0ef]] = None,
            filter_settings: typing.Optional[typing.Union["CfnChannel.H265FilterSettingsProperty", _IResolvable_a771d0ef]] = None,
            fixed_afd: typing.Optional[builtins.str] = None,
            flicker_aq: typing.Optional[builtins.str] = None,
            framerate_denominator: typing.Optional[jsii.Number] = None,
            framerate_numerator: typing.Optional[jsii.Number] = None,
            gop_closed_cadence: typing.Optional[jsii.Number] = None,
            gop_size: typing.Optional[jsii.Number] = None,
            gop_size_units: typing.Optional[builtins.str] = None,
            level: typing.Optional[builtins.str] = None,
            look_ahead_rate_control: typing.Optional[builtins.str] = None,
            max_bitrate: typing.Optional[jsii.Number] = None,
            min_i_interval: typing.Optional[jsii.Number] = None,
            par_denominator: typing.Optional[jsii.Number] = None,
            par_numerator: typing.Optional[jsii.Number] = None,
            profile: typing.Optional[builtins.str] = None,
            qvbr_quality_level: typing.Optional[jsii.Number] = None,
            rate_control_mode: typing.Optional[builtins.str] = None,
            scan_type: typing.Optional[builtins.str] = None,
            scene_change_detect: typing.Optional[builtins.str] = None,
            slices: typing.Optional[jsii.Number] = None,
            tier: typing.Optional[builtins.str] = None,
            timecode_insertion: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param adaptive_quantization: ``CfnChannel.H265SettingsProperty.AdaptiveQuantization``.
            :param afd_signaling: ``CfnChannel.H265SettingsProperty.AfdSignaling``.
            :param alternative_transfer_function: ``CfnChannel.H265SettingsProperty.AlternativeTransferFunction``.
            :param bitrate: ``CfnChannel.H265SettingsProperty.Bitrate``.
            :param buf_size: ``CfnChannel.H265SettingsProperty.BufSize``.
            :param color_metadata: ``CfnChannel.H265SettingsProperty.ColorMetadata``.
            :param color_space_settings: ``CfnChannel.H265SettingsProperty.ColorSpaceSettings``.
            :param filter_settings: ``CfnChannel.H265SettingsProperty.FilterSettings``.
            :param fixed_afd: ``CfnChannel.H265SettingsProperty.FixedAfd``.
            :param flicker_aq: ``CfnChannel.H265SettingsProperty.FlickerAq``.
            :param framerate_denominator: ``CfnChannel.H265SettingsProperty.FramerateDenominator``.
            :param framerate_numerator: ``CfnChannel.H265SettingsProperty.FramerateNumerator``.
            :param gop_closed_cadence: ``CfnChannel.H265SettingsProperty.GopClosedCadence``.
            :param gop_size: ``CfnChannel.H265SettingsProperty.GopSize``.
            :param gop_size_units: ``CfnChannel.H265SettingsProperty.GopSizeUnits``.
            :param level: ``CfnChannel.H265SettingsProperty.Level``.
            :param look_ahead_rate_control: ``CfnChannel.H265SettingsProperty.LookAheadRateControl``.
            :param max_bitrate: ``CfnChannel.H265SettingsProperty.MaxBitrate``.
            :param min_i_interval: ``CfnChannel.H265SettingsProperty.MinIInterval``.
            :param par_denominator: ``CfnChannel.H265SettingsProperty.ParDenominator``.
            :param par_numerator: ``CfnChannel.H265SettingsProperty.ParNumerator``.
            :param profile: ``CfnChannel.H265SettingsProperty.Profile``.
            :param qvbr_quality_level: ``CfnChannel.H265SettingsProperty.QvbrQualityLevel``.
            :param rate_control_mode: ``CfnChannel.H265SettingsProperty.RateControlMode``.
            :param scan_type: ``CfnChannel.H265SettingsProperty.ScanType``.
            :param scene_change_detect: ``CfnChannel.H265SettingsProperty.SceneChangeDetect``.
            :param slices: ``CfnChannel.H265SettingsProperty.Slices``.
            :param tier: ``CfnChannel.H265SettingsProperty.Tier``.
            :param timecode_insertion: ``CfnChannel.H265SettingsProperty.TimecodeInsertion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if adaptive_quantization is not None:
                self._values["adaptive_quantization"] = adaptive_quantization
            if afd_signaling is not None:
                self._values["afd_signaling"] = afd_signaling
            if alternative_transfer_function is not None:
                self._values["alternative_transfer_function"] = alternative_transfer_function
            if bitrate is not None:
                self._values["bitrate"] = bitrate
            if buf_size is not None:
                self._values["buf_size"] = buf_size
            if color_metadata is not None:
                self._values["color_metadata"] = color_metadata
            if color_space_settings is not None:
                self._values["color_space_settings"] = color_space_settings
            if filter_settings is not None:
                self._values["filter_settings"] = filter_settings
            if fixed_afd is not None:
                self._values["fixed_afd"] = fixed_afd
            if flicker_aq is not None:
                self._values["flicker_aq"] = flicker_aq
            if framerate_denominator is not None:
                self._values["framerate_denominator"] = framerate_denominator
            if framerate_numerator is not None:
                self._values["framerate_numerator"] = framerate_numerator
            if gop_closed_cadence is not None:
                self._values["gop_closed_cadence"] = gop_closed_cadence
            if gop_size is not None:
                self._values["gop_size"] = gop_size
            if gop_size_units is not None:
                self._values["gop_size_units"] = gop_size_units
            if level is not None:
                self._values["level"] = level
            if look_ahead_rate_control is not None:
                self._values["look_ahead_rate_control"] = look_ahead_rate_control
            if max_bitrate is not None:
                self._values["max_bitrate"] = max_bitrate
            if min_i_interval is not None:
                self._values["min_i_interval"] = min_i_interval
            if par_denominator is not None:
                self._values["par_denominator"] = par_denominator
            if par_numerator is not None:
                self._values["par_numerator"] = par_numerator
            if profile is not None:
                self._values["profile"] = profile
            if qvbr_quality_level is not None:
                self._values["qvbr_quality_level"] = qvbr_quality_level
            if rate_control_mode is not None:
                self._values["rate_control_mode"] = rate_control_mode
            if scan_type is not None:
                self._values["scan_type"] = scan_type
            if scene_change_detect is not None:
                self._values["scene_change_detect"] = scene_change_detect
            if slices is not None:
                self._values["slices"] = slices
            if tier is not None:
                self._values["tier"] = tier
            if timecode_insertion is not None:
                self._values["timecode_insertion"] = timecode_insertion

        @builtins.property
        def adaptive_quantization(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H265SettingsProperty.AdaptiveQuantization``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-adaptivequantization
            """
            result = self._values.get("adaptive_quantization")
            return result

        @builtins.property
        def afd_signaling(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H265SettingsProperty.AfdSignaling``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-afdsignaling
            """
            result = self._values.get("afd_signaling")
            return result

        @builtins.property
        def alternative_transfer_function(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H265SettingsProperty.AlternativeTransferFunction``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-alternativetransferfunction
            """
            result = self._values.get("alternative_transfer_function")
            return result

        @builtins.property
        def bitrate(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H265SettingsProperty.Bitrate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-bitrate
            """
            result = self._values.get("bitrate")
            return result

        @builtins.property
        def buf_size(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H265SettingsProperty.BufSize``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-bufsize
            """
            result = self._values.get("buf_size")
            return result

        @builtins.property
        def color_metadata(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H265SettingsProperty.ColorMetadata``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-colormetadata
            """
            result = self._values.get("color_metadata")
            return result

        @builtins.property
        def color_space_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.H265ColorSpaceSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.H265SettingsProperty.ColorSpaceSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-colorspacesettings
            """
            result = self._values.get("color_space_settings")
            return result

        @builtins.property
        def filter_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.H265FilterSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.H265SettingsProperty.FilterSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-filtersettings
            """
            result = self._values.get("filter_settings")
            return result

        @builtins.property
        def fixed_afd(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H265SettingsProperty.FixedAfd``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-fixedafd
            """
            result = self._values.get("fixed_afd")
            return result

        @builtins.property
        def flicker_aq(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H265SettingsProperty.FlickerAq``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-flickeraq
            """
            result = self._values.get("flicker_aq")
            return result

        @builtins.property
        def framerate_denominator(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H265SettingsProperty.FramerateDenominator``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-frameratedenominator
            """
            result = self._values.get("framerate_denominator")
            return result

        @builtins.property
        def framerate_numerator(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H265SettingsProperty.FramerateNumerator``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-frameratenumerator
            """
            result = self._values.get("framerate_numerator")
            return result

        @builtins.property
        def gop_closed_cadence(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H265SettingsProperty.GopClosedCadence``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-gopclosedcadence
            """
            result = self._values.get("gop_closed_cadence")
            return result

        @builtins.property
        def gop_size(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H265SettingsProperty.GopSize``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-gopsize
            """
            result = self._values.get("gop_size")
            return result

        @builtins.property
        def gop_size_units(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H265SettingsProperty.GopSizeUnits``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-gopsizeunits
            """
            result = self._values.get("gop_size_units")
            return result

        @builtins.property
        def level(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H265SettingsProperty.Level``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-level
            """
            result = self._values.get("level")
            return result

        @builtins.property
        def look_ahead_rate_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H265SettingsProperty.LookAheadRateControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-lookaheadratecontrol
            """
            result = self._values.get("look_ahead_rate_control")
            return result

        @builtins.property
        def max_bitrate(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H265SettingsProperty.MaxBitrate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-maxbitrate
            """
            result = self._values.get("max_bitrate")
            return result

        @builtins.property
        def min_i_interval(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H265SettingsProperty.MinIInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-miniinterval
            """
            result = self._values.get("min_i_interval")
            return result

        @builtins.property
        def par_denominator(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H265SettingsProperty.ParDenominator``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-pardenominator
            """
            result = self._values.get("par_denominator")
            return result

        @builtins.property
        def par_numerator(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H265SettingsProperty.ParNumerator``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-parnumerator
            """
            result = self._values.get("par_numerator")
            return result

        @builtins.property
        def profile(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H265SettingsProperty.Profile``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-profile
            """
            result = self._values.get("profile")
            return result

        @builtins.property
        def qvbr_quality_level(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H265SettingsProperty.QvbrQualityLevel``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-qvbrqualitylevel
            """
            result = self._values.get("qvbr_quality_level")
            return result

        @builtins.property
        def rate_control_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H265SettingsProperty.RateControlMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-ratecontrolmode
            """
            result = self._values.get("rate_control_mode")
            return result

        @builtins.property
        def scan_type(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H265SettingsProperty.ScanType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-scantype
            """
            result = self._values.get("scan_type")
            return result

        @builtins.property
        def scene_change_detect(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H265SettingsProperty.SceneChangeDetect``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-scenechangedetect
            """
            result = self._values.get("scene_change_detect")
            return result

        @builtins.property
        def slices(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.H265SettingsProperty.Slices``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-slices
            """
            result = self._values.get("slices")
            return result

        @builtins.property
        def tier(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H265SettingsProperty.Tier``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-tier
            """
            result = self._values.get("tier")
            return result

        @builtins.property
        def timecode_insertion(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.H265SettingsProperty.TimecodeInsertion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-timecodeinsertion
            """
            result = self._values.get("timecode_insertion")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "H265SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.Hdr10SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"max_cll": "maxCll", "max_fall": "maxFall"},
    )
    class Hdr10SettingsProperty:
        def __init__(
            self,
            *,
            max_cll: typing.Optional[jsii.Number] = None,
            max_fall: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param max_cll: ``CfnChannel.Hdr10SettingsProperty.MaxCll``.
            :param max_fall: ``CfnChannel.Hdr10SettingsProperty.MaxFall``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hdr10settings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if max_cll is not None:
                self._values["max_cll"] = max_cll
            if max_fall is not None:
                self._values["max_fall"] = max_fall

        @builtins.property
        def max_cll(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.Hdr10SettingsProperty.MaxCll``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hdr10settings.html#cfn-medialive-channel-hdr10settings-maxcll
            """
            result = self._values.get("max_cll")
            return result

        @builtins.property
        def max_fall(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.Hdr10SettingsProperty.MaxFall``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hdr10settings.html#cfn-medialive-channel-hdr10settings-maxfall
            """
            result = self._values.get("max_fall")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Hdr10SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.HlsAkamaiSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connection_retry_interval": "connectionRetryInterval",
            "filecache_duration": "filecacheDuration",
            "http_transfer_mode": "httpTransferMode",
            "num_retries": "numRetries",
            "restart_delay": "restartDelay",
            "salt": "salt",
            "token": "token",
        },
    )
    class HlsAkamaiSettingsProperty:
        def __init__(
            self,
            *,
            connection_retry_interval: typing.Optional[jsii.Number] = None,
            filecache_duration: typing.Optional[jsii.Number] = None,
            http_transfer_mode: typing.Optional[builtins.str] = None,
            num_retries: typing.Optional[jsii.Number] = None,
            restart_delay: typing.Optional[jsii.Number] = None,
            salt: typing.Optional[builtins.str] = None,
            token: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param connection_retry_interval: ``CfnChannel.HlsAkamaiSettingsProperty.ConnectionRetryInterval``.
            :param filecache_duration: ``CfnChannel.HlsAkamaiSettingsProperty.FilecacheDuration``.
            :param http_transfer_mode: ``CfnChannel.HlsAkamaiSettingsProperty.HttpTransferMode``.
            :param num_retries: ``CfnChannel.HlsAkamaiSettingsProperty.NumRetries``.
            :param restart_delay: ``CfnChannel.HlsAkamaiSettingsProperty.RestartDelay``.
            :param salt: ``CfnChannel.HlsAkamaiSettingsProperty.Salt``.
            :param token: ``CfnChannel.HlsAkamaiSettingsProperty.Token``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if connection_retry_interval is not None:
                self._values["connection_retry_interval"] = connection_retry_interval
            if filecache_duration is not None:
                self._values["filecache_duration"] = filecache_duration
            if http_transfer_mode is not None:
                self._values["http_transfer_mode"] = http_transfer_mode
            if num_retries is not None:
                self._values["num_retries"] = num_retries
            if restart_delay is not None:
                self._values["restart_delay"] = restart_delay
            if salt is not None:
                self._values["salt"] = salt
            if token is not None:
                self._values["token"] = token

        @builtins.property
        def connection_retry_interval(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsAkamaiSettingsProperty.ConnectionRetryInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-connectionretryinterval
            """
            result = self._values.get("connection_retry_interval")
            return result

        @builtins.property
        def filecache_duration(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsAkamaiSettingsProperty.FilecacheDuration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-filecacheduration
            """
            result = self._values.get("filecache_duration")
            return result

        @builtins.property
        def http_transfer_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsAkamaiSettingsProperty.HttpTransferMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-httptransfermode
            """
            result = self._values.get("http_transfer_mode")
            return result

        @builtins.property
        def num_retries(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsAkamaiSettingsProperty.NumRetries``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-numretries
            """
            result = self._values.get("num_retries")
            return result

        @builtins.property
        def restart_delay(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsAkamaiSettingsProperty.RestartDelay``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-restartdelay
            """
            result = self._values.get("restart_delay")
            return result

        @builtins.property
        def salt(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsAkamaiSettingsProperty.Salt``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-salt
            """
            result = self._values.get("salt")
            return result

        @builtins.property
        def token(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsAkamaiSettingsProperty.Token``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-token
            """
            result = self._values.get("token")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsAkamaiSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.HlsBasicPutSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connection_retry_interval": "connectionRetryInterval",
            "filecache_duration": "filecacheDuration",
            "num_retries": "numRetries",
            "restart_delay": "restartDelay",
        },
    )
    class HlsBasicPutSettingsProperty:
        def __init__(
            self,
            *,
            connection_retry_interval: typing.Optional[jsii.Number] = None,
            filecache_duration: typing.Optional[jsii.Number] = None,
            num_retries: typing.Optional[jsii.Number] = None,
            restart_delay: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param connection_retry_interval: ``CfnChannel.HlsBasicPutSettingsProperty.ConnectionRetryInterval``.
            :param filecache_duration: ``CfnChannel.HlsBasicPutSettingsProperty.FilecacheDuration``.
            :param num_retries: ``CfnChannel.HlsBasicPutSettingsProperty.NumRetries``.
            :param restart_delay: ``CfnChannel.HlsBasicPutSettingsProperty.RestartDelay``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if connection_retry_interval is not None:
                self._values["connection_retry_interval"] = connection_retry_interval
            if filecache_duration is not None:
                self._values["filecache_duration"] = filecache_duration
            if num_retries is not None:
                self._values["num_retries"] = num_retries
            if restart_delay is not None:
                self._values["restart_delay"] = restart_delay

        @builtins.property
        def connection_retry_interval(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsBasicPutSettingsProperty.ConnectionRetryInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html#cfn-medialive-channel-hlsbasicputsettings-connectionretryinterval
            """
            result = self._values.get("connection_retry_interval")
            return result

        @builtins.property
        def filecache_duration(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsBasicPutSettingsProperty.FilecacheDuration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html#cfn-medialive-channel-hlsbasicputsettings-filecacheduration
            """
            result = self._values.get("filecache_duration")
            return result

        @builtins.property
        def num_retries(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsBasicPutSettingsProperty.NumRetries``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html#cfn-medialive-channel-hlsbasicputsettings-numretries
            """
            result = self._values.get("num_retries")
            return result

        @builtins.property
        def restart_delay(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsBasicPutSettingsProperty.RestartDelay``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html#cfn-medialive-channel-hlsbasicputsettings-restartdelay
            """
            result = self._values.get("restart_delay")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsBasicPutSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.HlsCdnSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hls_akamai_settings": "hlsAkamaiSettings",
            "hls_basic_put_settings": "hlsBasicPutSettings",
            "hls_media_store_settings": "hlsMediaStoreSettings",
            "hls_webdav_settings": "hlsWebdavSettings",
        },
    )
    class HlsCdnSettingsProperty:
        def __init__(
            self,
            *,
            hls_akamai_settings: typing.Optional[typing.Union["CfnChannel.HlsAkamaiSettingsProperty", _IResolvable_a771d0ef]] = None,
            hls_basic_put_settings: typing.Optional[typing.Union["CfnChannel.HlsBasicPutSettingsProperty", _IResolvable_a771d0ef]] = None,
            hls_media_store_settings: typing.Optional[typing.Union["CfnChannel.HlsMediaStoreSettingsProperty", _IResolvable_a771d0ef]] = None,
            hls_webdav_settings: typing.Optional[typing.Union["CfnChannel.HlsWebdavSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param hls_akamai_settings: ``CfnChannel.HlsCdnSettingsProperty.HlsAkamaiSettings``.
            :param hls_basic_put_settings: ``CfnChannel.HlsCdnSettingsProperty.HlsBasicPutSettings``.
            :param hls_media_store_settings: ``CfnChannel.HlsCdnSettingsProperty.HlsMediaStoreSettings``.
            :param hls_webdav_settings: ``CfnChannel.HlsCdnSettingsProperty.HlsWebdavSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if hls_akamai_settings is not None:
                self._values["hls_akamai_settings"] = hls_akamai_settings
            if hls_basic_put_settings is not None:
                self._values["hls_basic_put_settings"] = hls_basic_put_settings
            if hls_media_store_settings is not None:
                self._values["hls_media_store_settings"] = hls_media_store_settings
            if hls_webdav_settings is not None:
                self._values["hls_webdav_settings"] = hls_webdav_settings

        @builtins.property
        def hls_akamai_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.HlsAkamaiSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.HlsCdnSettingsProperty.HlsAkamaiSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html#cfn-medialive-channel-hlscdnsettings-hlsakamaisettings
            """
            result = self._values.get("hls_akamai_settings")
            return result

        @builtins.property
        def hls_basic_put_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.HlsBasicPutSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.HlsCdnSettingsProperty.HlsBasicPutSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html#cfn-medialive-channel-hlscdnsettings-hlsbasicputsettings
            """
            result = self._values.get("hls_basic_put_settings")
            return result

        @builtins.property
        def hls_media_store_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.HlsMediaStoreSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.HlsCdnSettingsProperty.HlsMediaStoreSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html#cfn-medialive-channel-hlscdnsettings-hlsmediastoresettings
            """
            result = self._values.get("hls_media_store_settings")
            return result

        @builtins.property
        def hls_webdav_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.HlsWebdavSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.HlsCdnSettingsProperty.HlsWebdavSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html#cfn-medialive-channel-hlscdnsettings-hlswebdavsettings
            """
            result = self._values.get("hls_webdav_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsCdnSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.HlsGroupSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ad_markers": "adMarkers",
            "base_url_content": "baseUrlContent",
            "base_url_content1": "baseUrlContent1",
            "base_url_manifest": "baseUrlManifest",
            "base_url_manifest1": "baseUrlManifest1",
            "caption_language_mappings": "captionLanguageMappings",
            "caption_language_setting": "captionLanguageSetting",
            "client_cache": "clientCache",
            "codec_specification": "codecSpecification",
            "constant_iv": "constantIv",
            "destination": "destination",
            "directory_structure": "directoryStructure",
            "encryption_type": "encryptionType",
            "hls_cdn_settings": "hlsCdnSettings",
            "hls_id3_segment_tagging": "hlsId3SegmentTagging",
            "i_frame_only_playlists": "iFrameOnlyPlaylists",
            "index_n_segments": "indexNSegments",
            "input_loss_action": "inputLossAction",
            "iv_in_manifest": "ivInManifest",
            "iv_source": "ivSource",
            "keep_segments": "keepSegments",
            "key_format": "keyFormat",
            "key_format_versions": "keyFormatVersions",
            "key_provider_settings": "keyProviderSettings",
            "manifest_compression": "manifestCompression",
            "manifest_duration_format": "manifestDurationFormat",
            "min_segment_length": "minSegmentLength",
            "mode": "mode",
            "output_selection": "outputSelection",
            "program_date_time": "programDateTime",
            "program_date_time_period": "programDateTimePeriod",
            "redundant_manifest": "redundantManifest",
            "segmentation_mode": "segmentationMode",
            "segment_length": "segmentLength",
            "segments_per_subdirectory": "segmentsPerSubdirectory",
            "stream_inf_resolution": "streamInfResolution",
            "timed_metadata_id3_frame": "timedMetadataId3Frame",
            "timed_metadata_id3_period": "timedMetadataId3Period",
            "timestamp_delta_milliseconds": "timestampDeltaMilliseconds",
            "ts_file_mode": "tsFileMode",
        },
    )
    class HlsGroupSettingsProperty:
        def __init__(
            self,
            *,
            ad_markers: typing.Optional[typing.List[builtins.str]] = None,
            base_url_content: typing.Optional[builtins.str] = None,
            base_url_content1: typing.Optional[builtins.str] = None,
            base_url_manifest: typing.Optional[builtins.str] = None,
            base_url_manifest1: typing.Optional[builtins.str] = None,
            caption_language_mappings: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.CaptionLanguageMappingProperty", _IResolvable_a771d0ef]]]] = None,
            caption_language_setting: typing.Optional[builtins.str] = None,
            client_cache: typing.Optional[builtins.str] = None,
            codec_specification: typing.Optional[builtins.str] = None,
            constant_iv: typing.Optional[builtins.str] = None,
            destination: typing.Optional[typing.Union["CfnChannel.OutputLocationRefProperty", _IResolvable_a771d0ef]] = None,
            directory_structure: typing.Optional[builtins.str] = None,
            encryption_type: typing.Optional[builtins.str] = None,
            hls_cdn_settings: typing.Optional[typing.Union["CfnChannel.HlsCdnSettingsProperty", _IResolvable_a771d0ef]] = None,
            hls_id3_segment_tagging: typing.Optional[builtins.str] = None,
            i_frame_only_playlists: typing.Optional[builtins.str] = None,
            index_n_segments: typing.Optional[jsii.Number] = None,
            input_loss_action: typing.Optional[builtins.str] = None,
            iv_in_manifest: typing.Optional[builtins.str] = None,
            iv_source: typing.Optional[builtins.str] = None,
            keep_segments: typing.Optional[jsii.Number] = None,
            key_format: typing.Optional[builtins.str] = None,
            key_format_versions: typing.Optional[builtins.str] = None,
            key_provider_settings: typing.Optional[typing.Union["CfnChannel.KeyProviderSettingsProperty", _IResolvable_a771d0ef]] = None,
            manifest_compression: typing.Optional[builtins.str] = None,
            manifest_duration_format: typing.Optional[builtins.str] = None,
            min_segment_length: typing.Optional[jsii.Number] = None,
            mode: typing.Optional[builtins.str] = None,
            output_selection: typing.Optional[builtins.str] = None,
            program_date_time: typing.Optional[builtins.str] = None,
            program_date_time_period: typing.Optional[jsii.Number] = None,
            redundant_manifest: typing.Optional[builtins.str] = None,
            segmentation_mode: typing.Optional[builtins.str] = None,
            segment_length: typing.Optional[jsii.Number] = None,
            segments_per_subdirectory: typing.Optional[jsii.Number] = None,
            stream_inf_resolution: typing.Optional[builtins.str] = None,
            timed_metadata_id3_frame: typing.Optional[builtins.str] = None,
            timed_metadata_id3_period: typing.Optional[jsii.Number] = None,
            timestamp_delta_milliseconds: typing.Optional[jsii.Number] = None,
            ts_file_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param ad_markers: ``CfnChannel.HlsGroupSettingsProperty.AdMarkers``.
            :param base_url_content: ``CfnChannel.HlsGroupSettingsProperty.BaseUrlContent``.
            :param base_url_content1: ``CfnChannel.HlsGroupSettingsProperty.BaseUrlContent1``.
            :param base_url_manifest: ``CfnChannel.HlsGroupSettingsProperty.BaseUrlManifest``.
            :param base_url_manifest1: ``CfnChannel.HlsGroupSettingsProperty.BaseUrlManifest1``.
            :param caption_language_mappings: ``CfnChannel.HlsGroupSettingsProperty.CaptionLanguageMappings``.
            :param caption_language_setting: ``CfnChannel.HlsGroupSettingsProperty.CaptionLanguageSetting``.
            :param client_cache: ``CfnChannel.HlsGroupSettingsProperty.ClientCache``.
            :param codec_specification: ``CfnChannel.HlsGroupSettingsProperty.CodecSpecification``.
            :param constant_iv: ``CfnChannel.HlsGroupSettingsProperty.ConstantIv``.
            :param destination: ``CfnChannel.HlsGroupSettingsProperty.Destination``.
            :param directory_structure: ``CfnChannel.HlsGroupSettingsProperty.DirectoryStructure``.
            :param encryption_type: ``CfnChannel.HlsGroupSettingsProperty.EncryptionType``.
            :param hls_cdn_settings: ``CfnChannel.HlsGroupSettingsProperty.HlsCdnSettings``.
            :param hls_id3_segment_tagging: ``CfnChannel.HlsGroupSettingsProperty.HlsId3SegmentTagging``.
            :param i_frame_only_playlists: ``CfnChannel.HlsGroupSettingsProperty.IFrameOnlyPlaylists``.
            :param index_n_segments: ``CfnChannel.HlsGroupSettingsProperty.IndexNSegments``.
            :param input_loss_action: ``CfnChannel.HlsGroupSettingsProperty.InputLossAction``.
            :param iv_in_manifest: ``CfnChannel.HlsGroupSettingsProperty.IvInManifest``.
            :param iv_source: ``CfnChannel.HlsGroupSettingsProperty.IvSource``.
            :param keep_segments: ``CfnChannel.HlsGroupSettingsProperty.KeepSegments``.
            :param key_format: ``CfnChannel.HlsGroupSettingsProperty.KeyFormat``.
            :param key_format_versions: ``CfnChannel.HlsGroupSettingsProperty.KeyFormatVersions``.
            :param key_provider_settings: ``CfnChannel.HlsGroupSettingsProperty.KeyProviderSettings``.
            :param manifest_compression: ``CfnChannel.HlsGroupSettingsProperty.ManifestCompression``.
            :param manifest_duration_format: ``CfnChannel.HlsGroupSettingsProperty.ManifestDurationFormat``.
            :param min_segment_length: ``CfnChannel.HlsGroupSettingsProperty.MinSegmentLength``.
            :param mode: ``CfnChannel.HlsGroupSettingsProperty.Mode``.
            :param output_selection: ``CfnChannel.HlsGroupSettingsProperty.OutputSelection``.
            :param program_date_time: ``CfnChannel.HlsGroupSettingsProperty.ProgramDateTime``.
            :param program_date_time_period: ``CfnChannel.HlsGroupSettingsProperty.ProgramDateTimePeriod``.
            :param redundant_manifest: ``CfnChannel.HlsGroupSettingsProperty.RedundantManifest``.
            :param segmentation_mode: ``CfnChannel.HlsGroupSettingsProperty.SegmentationMode``.
            :param segment_length: ``CfnChannel.HlsGroupSettingsProperty.SegmentLength``.
            :param segments_per_subdirectory: ``CfnChannel.HlsGroupSettingsProperty.SegmentsPerSubdirectory``.
            :param stream_inf_resolution: ``CfnChannel.HlsGroupSettingsProperty.StreamInfResolution``.
            :param timed_metadata_id3_frame: ``CfnChannel.HlsGroupSettingsProperty.TimedMetadataId3Frame``.
            :param timed_metadata_id3_period: ``CfnChannel.HlsGroupSettingsProperty.TimedMetadataId3Period``.
            :param timestamp_delta_milliseconds: ``CfnChannel.HlsGroupSettingsProperty.TimestampDeltaMilliseconds``.
            :param ts_file_mode: ``CfnChannel.HlsGroupSettingsProperty.TsFileMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if ad_markers is not None:
                self._values["ad_markers"] = ad_markers
            if base_url_content is not None:
                self._values["base_url_content"] = base_url_content
            if base_url_content1 is not None:
                self._values["base_url_content1"] = base_url_content1
            if base_url_manifest is not None:
                self._values["base_url_manifest"] = base_url_manifest
            if base_url_manifest1 is not None:
                self._values["base_url_manifest1"] = base_url_manifest1
            if caption_language_mappings is not None:
                self._values["caption_language_mappings"] = caption_language_mappings
            if caption_language_setting is not None:
                self._values["caption_language_setting"] = caption_language_setting
            if client_cache is not None:
                self._values["client_cache"] = client_cache
            if codec_specification is not None:
                self._values["codec_specification"] = codec_specification
            if constant_iv is not None:
                self._values["constant_iv"] = constant_iv
            if destination is not None:
                self._values["destination"] = destination
            if directory_structure is not None:
                self._values["directory_structure"] = directory_structure
            if encryption_type is not None:
                self._values["encryption_type"] = encryption_type
            if hls_cdn_settings is not None:
                self._values["hls_cdn_settings"] = hls_cdn_settings
            if hls_id3_segment_tagging is not None:
                self._values["hls_id3_segment_tagging"] = hls_id3_segment_tagging
            if i_frame_only_playlists is not None:
                self._values["i_frame_only_playlists"] = i_frame_only_playlists
            if index_n_segments is not None:
                self._values["index_n_segments"] = index_n_segments
            if input_loss_action is not None:
                self._values["input_loss_action"] = input_loss_action
            if iv_in_manifest is not None:
                self._values["iv_in_manifest"] = iv_in_manifest
            if iv_source is not None:
                self._values["iv_source"] = iv_source
            if keep_segments is not None:
                self._values["keep_segments"] = keep_segments
            if key_format is not None:
                self._values["key_format"] = key_format
            if key_format_versions is not None:
                self._values["key_format_versions"] = key_format_versions
            if key_provider_settings is not None:
                self._values["key_provider_settings"] = key_provider_settings
            if manifest_compression is not None:
                self._values["manifest_compression"] = manifest_compression
            if manifest_duration_format is not None:
                self._values["manifest_duration_format"] = manifest_duration_format
            if min_segment_length is not None:
                self._values["min_segment_length"] = min_segment_length
            if mode is not None:
                self._values["mode"] = mode
            if output_selection is not None:
                self._values["output_selection"] = output_selection
            if program_date_time is not None:
                self._values["program_date_time"] = program_date_time
            if program_date_time_period is not None:
                self._values["program_date_time_period"] = program_date_time_period
            if redundant_manifest is not None:
                self._values["redundant_manifest"] = redundant_manifest
            if segmentation_mode is not None:
                self._values["segmentation_mode"] = segmentation_mode
            if segment_length is not None:
                self._values["segment_length"] = segment_length
            if segments_per_subdirectory is not None:
                self._values["segments_per_subdirectory"] = segments_per_subdirectory
            if stream_inf_resolution is not None:
                self._values["stream_inf_resolution"] = stream_inf_resolution
            if timed_metadata_id3_frame is not None:
                self._values["timed_metadata_id3_frame"] = timed_metadata_id3_frame
            if timed_metadata_id3_period is not None:
                self._values["timed_metadata_id3_period"] = timed_metadata_id3_period
            if timestamp_delta_milliseconds is not None:
                self._values["timestamp_delta_milliseconds"] = timestamp_delta_milliseconds
            if ts_file_mode is not None:
                self._values["ts_file_mode"] = ts_file_mode

        @builtins.property
        def ad_markers(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnChannel.HlsGroupSettingsProperty.AdMarkers``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-admarkers
            """
            result = self._values.get("ad_markers")
            return result

        @builtins.property
        def base_url_content(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.BaseUrlContent``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-baseurlcontent
            """
            result = self._values.get("base_url_content")
            return result

        @builtins.property
        def base_url_content1(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.BaseUrlContent1``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-baseurlcontent1
            """
            result = self._values.get("base_url_content1")
            return result

        @builtins.property
        def base_url_manifest(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.BaseUrlManifest``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-baseurlmanifest
            """
            result = self._values.get("base_url_manifest")
            return result

        @builtins.property
        def base_url_manifest1(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.BaseUrlManifest1``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-baseurlmanifest1
            """
            result = self._values.get("base_url_manifest1")
            return result

        @builtins.property
        def caption_language_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.CaptionLanguageMappingProperty", _IResolvable_a771d0ef]]]]:
            """``CfnChannel.HlsGroupSettingsProperty.CaptionLanguageMappings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-captionlanguagemappings
            """
            result = self._values.get("caption_language_mappings")
            return result

        @builtins.property
        def caption_language_setting(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.CaptionLanguageSetting``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-captionlanguagesetting
            """
            result = self._values.get("caption_language_setting")
            return result

        @builtins.property
        def client_cache(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.ClientCache``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-clientcache
            """
            result = self._values.get("client_cache")
            return result

        @builtins.property
        def codec_specification(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.CodecSpecification``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-codecspecification
            """
            result = self._values.get("codec_specification")
            return result

        @builtins.property
        def constant_iv(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.ConstantIv``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-constantiv
            """
            result = self._values.get("constant_iv")
            return result

        @builtins.property
        def destination(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.OutputLocationRefProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.HlsGroupSettingsProperty.Destination``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-destination
            """
            result = self._values.get("destination")
            return result

        @builtins.property
        def directory_structure(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.DirectoryStructure``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-directorystructure
            """
            result = self._values.get("directory_structure")
            return result

        @builtins.property
        def encryption_type(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.EncryptionType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-encryptiontype
            """
            result = self._values.get("encryption_type")
            return result

        @builtins.property
        def hls_cdn_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.HlsCdnSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.HlsGroupSettingsProperty.HlsCdnSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-hlscdnsettings
            """
            result = self._values.get("hls_cdn_settings")
            return result

        @builtins.property
        def hls_id3_segment_tagging(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.HlsId3SegmentTagging``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-hlsid3segmenttagging
            """
            result = self._values.get("hls_id3_segment_tagging")
            return result

        @builtins.property
        def i_frame_only_playlists(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.IFrameOnlyPlaylists``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-iframeonlyplaylists
            """
            result = self._values.get("i_frame_only_playlists")
            return result

        @builtins.property
        def index_n_segments(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsGroupSettingsProperty.IndexNSegments``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-indexnsegments
            """
            result = self._values.get("index_n_segments")
            return result

        @builtins.property
        def input_loss_action(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.InputLossAction``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-inputlossaction
            """
            result = self._values.get("input_loss_action")
            return result

        @builtins.property
        def iv_in_manifest(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.IvInManifest``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-ivinmanifest
            """
            result = self._values.get("iv_in_manifest")
            return result

        @builtins.property
        def iv_source(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.IvSource``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-ivsource
            """
            result = self._values.get("iv_source")
            return result

        @builtins.property
        def keep_segments(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsGroupSettingsProperty.KeepSegments``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-keepsegments
            """
            result = self._values.get("keep_segments")
            return result

        @builtins.property
        def key_format(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.KeyFormat``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-keyformat
            """
            result = self._values.get("key_format")
            return result

        @builtins.property
        def key_format_versions(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.KeyFormatVersions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-keyformatversions
            """
            result = self._values.get("key_format_versions")
            return result

        @builtins.property
        def key_provider_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.KeyProviderSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.HlsGroupSettingsProperty.KeyProviderSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-keyprovidersettings
            """
            result = self._values.get("key_provider_settings")
            return result

        @builtins.property
        def manifest_compression(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.ManifestCompression``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-manifestcompression
            """
            result = self._values.get("manifest_compression")
            return result

        @builtins.property
        def manifest_duration_format(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.ManifestDurationFormat``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-manifestdurationformat
            """
            result = self._values.get("manifest_duration_format")
            return result

        @builtins.property
        def min_segment_length(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsGroupSettingsProperty.MinSegmentLength``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-minsegmentlength
            """
            result = self._values.get("min_segment_length")
            return result

        @builtins.property
        def mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.Mode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-mode
            """
            result = self._values.get("mode")
            return result

        @builtins.property
        def output_selection(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.OutputSelection``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-outputselection
            """
            result = self._values.get("output_selection")
            return result

        @builtins.property
        def program_date_time(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.ProgramDateTime``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-programdatetime
            """
            result = self._values.get("program_date_time")
            return result

        @builtins.property
        def program_date_time_period(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsGroupSettingsProperty.ProgramDateTimePeriod``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-programdatetimeperiod
            """
            result = self._values.get("program_date_time_period")
            return result

        @builtins.property
        def redundant_manifest(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.RedundantManifest``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-redundantmanifest
            """
            result = self._values.get("redundant_manifest")
            return result

        @builtins.property
        def segmentation_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.SegmentationMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-segmentationmode
            """
            result = self._values.get("segmentation_mode")
            return result

        @builtins.property
        def segment_length(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsGroupSettingsProperty.SegmentLength``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-segmentlength
            """
            result = self._values.get("segment_length")
            return result

        @builtins.property
        def segments_per_subdirectory(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsGroupSettingsProperty.SegmentsPerSubdirectory``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-segmentspersubdirectory
            """
            result = self._values.get("segments_per_subdirectory")
            return result

        @builtins.property
        def stream_inf_resolution(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.StreamInfResolution``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-streaminfresolution
            """
            result = self._values.get("stream_inf_resolution")
            return result

        @builtins.property
        def timed_metadata_id3_frame(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.TimedMetadataId3Frame``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-timedmetadataid3frame
            """
            result = self._values.get("timed_metadata_id3_frame")
            return result

        @builtins.property
        def timed_metadata_id3_period(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsGroupSettingsProperty.TimedMetadataId3Period``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-timedmetadataid3period
            """
            result = self._values.get("timed_metadata_id3_period")
            return result

        @builtins.property
        def timestamp_delta_milliseconds(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsGroupSettingsProperty.TimestampDeltaMilliseconds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-timestampdeltamilliseconds
            """
            result = self._values.get("timestamp_delta_milliseconds")
            return result

        @builtins.property
        def ts_file_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsGroupSettingsProperty.TsFileMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-tsfilemode
            """
            result = self._values.get("ts_file_mode")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsGroupSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.HlsInputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bandwidth": "bandwidth",
            "buffer_segments": "bufferSegments",
            "retries": "retries",
            "retry_interval": "retryInterval",
        },
    )
    class HlsInputSettingsProperty:
        def __init__(
            self,
            *,
            bandwidth: typing.Optional[jsii.Number] = None,
            buffer_segments: typing.Optional[jsii.Number] = None,
            retries: typing.Optional[jsii.Number] = None,
            retry_interval: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param bandwidth: ``CfnChannel.HlsInputSettingsProperty.Bandwidth``.
            :param buffer_segments: ``CfnChannel.HlsInputSettingsProperty.BufferSegments``.
            :param retries: ``CfnChannel.HlsInputSettingsProperty.Retries``.
            :param retry_interval: ``CfnChannel.HlsInputSettingsProperty.RetryInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsinputsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if bandwidth is not None:
                self._values["bandwidth"] = bandwidth
            if buffer_segments is not None:
                self._values["buffer_segments"] = buffer_segments
            if retries is not None:
                self._values["retries"] = retries
            if retry_interval is not None:
                self._values["retry_interval"] = retry_interval

        @builtins.property
        def bandwidth(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsInputSettingsProperty.Bandwidth``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsinputsettings.html#cfn-medialive-channel-hlsinputsettings-bandwidth
            """
            result = self._values.get("bandwidth")
            return result

        @builtins.property
        def buffer_segments(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsInputSettingsProperty.BufferSegments``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsinputsettings.html#cfn-medialive-channel-hlsinputsettings-buffersegments
            """
            result = self._values.get("buffer_segments")
            return result

        @builtins.property
        def retries(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsInputSettingsProperty.Retries``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsinputsettings.html#cfn-medialive-channel-hlsinputsettings-retries
            """
            result = self._values.get("retries")
            return result

        @builtins.property
        def retry_interval(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsInputSettingsProperty.RetryInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsinputsettings.html#cfn-medialive-channel-hlsinputsettings-retryinterval
            """
            result = self._values.get("retry_interval")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsInputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.HlsMediaStoreSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connection_retry_interval": "connectionRetryInterval",
            "filecache_duration": "filecacheDuration",
            "media_store_storage_class": "mediaStoreStorageClass",
            "num_retries": "numRetries",
            "restart_delay": "restartDelay",
        },
    )
    class HlsMediaStoreSettingsProperty:
        def __init__(
            self,
            *,
            connection_retry_interval: typing.Optional[jsii.Number] = None,
            filecache_duration: typing.Optional[jsii.Number] = None,
            media_store_storage_class: typing.Optional[builtins.str] = None,
            num_retries: typing.Optional[jsii.Number] = None,
            restart_delay: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param connection_retry_interval: ``CfnChannel.HlsMediaStoreSettingsProperty.ConnectionRetryInterval``.
            :param filecache_duration: ``CfnChannel.HlsMediaStoreSettingsProperty.FilecacheDuration``.
            :param media_store_storage_class: ``CfnChannel.HlsMediaStoreSettingsProperty.MediaStoreStorageClass``.
            :param num_retries: ``CfnChannel.HlsMediaStoreSettingsProperty.NumRetries``.
            :param restart_delay: ``CfnChannel.HlsMediaStoreSettingsProperty.RestartDelay``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if connection_retry_interval is not None:
                self._values["connection_retry_interval"] = connection_retry_interval
            if filecache_duration is not None:
                self._values["filecache_duration"] = filecache_duration
            if media_store_storage_class is not None:
                self._values["media_store_storage_class"] = media_store_storage_class
            if num_retries is not None:
                self._values["num_retries"] = num_retries
            if restart_delay is not None:
                self._values["restart_delay"] = restart_delay

        @builtins.property
        def connection_retry_interval(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsMediaStoreSettingsProperty.ConnectionRetryInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html#cfn-medialive-channel-hlsmediastoresettings-connectionretryinterval
            """
            result = self._values.get("connection_retry_interval")
            return result

        @builtins.property
        def filecache_duration(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsMediaStoreSettingsProperty.FilecacheDuration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html#cfn-medialive-channel-hlsmediastoresettings-filecacheduration
            """
            result = self._values.get("filecache_duration")
            return result

        @builtins.property
        def media_store_storage_class(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsMediaStoreSettingsProperty.MediaStoreStorageClass``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html#cfn-medialive-channel-hlsmediastoresettings-mediastorestorageclass
            """
            result = self._values.get("media_store_storage_class")
            return result

        @builtins.property
        def num_retries(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsMediaStoreSettingsProperty.NumRetries``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html#cfn-medialive-channel-hlsmediastoresettings-numretries
            """
            result = self._values.get("num_retries")
            return result

        @builtins.property
        def restart_delay(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsMediaStoreSettingsProperty.RestartDelay``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html#cfn-medialive-channel-hlsmediastoresettings-restartdelay
            """
            result = self._values.get("restart_delay")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsMediaStoreSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.HlsOutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "h265_packaging_type": "h265PackagingType",
            "hls_settings": "hlsSettings",
            "name_modifier": "nameModifier",
            "segment_modifier": "segmentModifier",
        },
    )
    class HlsOutputSettingsProperty:
        def __init__(
            self,
            *,
            h265_packaging_type: typing.Optional[builtins.str] = None,
            hls_settings: typing.Optional[typing.Union["CfnChannel.HlsSettingsProperty", _IResolvable_a771d0ef]] = None,
            name_modifier: typing.Optional[builtins.str] = None,
            segment_modifier: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param h265_packaging_type: ``CfnChannel.HlsOutputSettingsProperty.H265PackagingType``.
            :param hls_settings: ``CfnChannel.HlsOutputSettingsProperty.HlsSettings``.
            :param name_modifier: ``CfnChannel.HlsOutputSettingsProperty.NameModifier``.
            :param segment_modifier: ``CfnChannel.HlsOutputSettingsProperty.SegmentModifier``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if h265_packaging_type is not None:
                self._values["h265_packaging_type"] = h265_packaging_type
            if hls_settings is not None:
                self._values["hls_settings"] = hls_settings
            if name_modifier is not None:
                self._values["name_modifier"] = name_modifier
            if segment_modifier is not None:
                self._values["segment_modifier"] = segment_modifier

        @builtins.property
        def h265_packaging_type(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsOutputSettingsProperty.H265PackagingType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html#cfn-medialive-channel-hlsoutputsettings-h265packagingtype
            """
            result = self._values.get("h265_packaging_type")
            return result

        @builtins.property
        def hls_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.HlsSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.HlsOutputSettingsProperty.HlsSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html#cfn-medialive-channel-hlsoutputsettings-hlssettings
            """
            result = self._values.get("hls_settings")
            return result

        @builtins.property
        def name_modifier(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsOutputSettingsProperty.NameModifier``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html#cfn-medialive-channel-hlsoutputsettings-namemodifier
            """
            result = self._values.get("name_modifier")
            return result

        @builtins.property
        def segment_modifier(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsOutputSettingsProperty.SegmentModifier``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html#cfn-medialive-channel-hlsoutputsettings-segmentmodifier
            """
            result = self._values.get("segment_modifier")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsOutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.HlsSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_only_hls_settings": "audioOnlyHlsSettings",
            "fmp4_hls_settings": "fmp4HlsSettings",
            "standard_hls_settings": "standardHlsSettings",
        },
    )
    class HlsSettingsProperty:
        def __init__(
            self,
            *,
            audio_only_hls_settings: typing.Optional[typing.Union["CfnChannel.AudioOnlyHlsSettingsProperty", _IResolvable_a771d0ef]] = None,
            fmp4_hls_settings: typing.Optional[typing.Union["CfnChannel.Fmp4HlsSettingsProperty", _IResolvable_a771d0ef]] = None,
            standard_hls_settings: typing.Optional[typing.Union["CfnChannel.StandardHlsSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param audio_only_hls_settings: ``CfnChannel.HlsSettingsProperty.AudioOnlyHlsSettings``.
            :param fmp4_hls_settings: ``CfnChannel.HlsSettingsProperty.Fmp4HlsSettings``.
            :param standard_hls_settings: ``CfnChannel.HlsSettingsProperty.StandardHlsSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_only_hls_settings is not None:
                self._values["audio_only_hls_settings"] = audio_only_hls_settings
            if fmp4_hls_settings is not None:
                self._values["fmp4_hls_settings"] = fmp4_hls_settings
            if standard_hls_settings is not None:
                self._values["standard_hls_settings"] = standard_hls_settings

        @builtins.property
        def audio_only_hls_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.AudioOnlyHlsSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.HlsSettingsProperty.AudioOnlyHlsSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html#cfn-medialive-channel-hlssettings-audioonlyhlssettings
            """
            result = self._values.get("audio_only_hls_settings")
            return result

        @builtins.property
        def fmp4_hls_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.Fmp4HlsSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.HlsSettingsProperty.Fmp4HlsSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html#cfn-medialive-channel-hlssettings-fmp4hlssettings
            """
            result = self._values.get("fmp4_hls_settings")
            return result

        @builtins.property
        def standard_hls_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.StandardHlsSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.HlsSettingsProperty.StandardHlsSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html#cfn-medialive-channel-hlssettings-standardhlssettings
            """
            result = self._values.get("standard_hls_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.HlsWebdavSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connection_retry_interval": "connectionRetryInterval",
            "filecache_duration": "filecacheDuration",
            "http_transfer_mode": "httpTransferMode",
            "num_retries": "numRetries",
            "restart_delay": "restartDelay",
        },
    )
    class HlsWebdavSettingsProperty:
        def __init__(
            self,
            *,
            connection_retry_interval: typing.Optional[jsii.Number] = None,
            filecache_duration: typing.Optional[jsii.Number] = None,
            http_transfer_mode: typing.Optional[builtins.str] = None,
            num_retries: typing.Optional[jsii.Number] = None,
            restart_delay: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param connection_retry_interval: ``CfnChannel.HlsWebdavSettingsProperty.ConnectionRetryInterval``.
            :param filecache_duration: ``CfnChannel.HlsWebdavSettingsProperty.FilecacheDuration``.
            :param http_transfer_mode: ``CfnChannel.HlsWebdavSettingsProperty.HttpTransferMode``.
            :param num_retries: ``CfnChannel.HlsWebdavSettingsProperty.NumRetries``.
            :param restart_delay: ``CfnChannel.HlsWebdavSettingsProperty.RestartDelay``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if connection_retry_interval is not None:
                self._values["connection_retry_interval"] = connection_retry_interval
            if filecache_duration is not None:
                self._values["filecache_duration"] = filecache_duration
            if http_transfer_mode is not None:
                self._values["http_transfer_mode"] = http_transfer_mode
            if num_retries is not None:
                self._values["num_retries"] = num_retries
            if restart_delay is not None:
                self._values["restart_delay"] = restart_delay

        @builtins.property
        def connection_retry_interval(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsWebdavSettingsProperty.ConnectionRetryInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html#cfn-medialive-channel-hlswebdavsettings-connectionretryinterval
            """
            result = self._values.get("connection_retry_interval")
            return result

        @builtins.property
        def filecache_duration(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsWebdavSettingsProperty.FilecacheDuration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html#cfn-medialive-channel-hlswebdavsettings-filecacheduration
            """
            result = self._values.get("filecache_duration")
            return result

        @builtins.property
        def http_transfer_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.HlsWebdavSettingsProperty.HttpTransferMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html#cfn-medialive-channel-hlswebdavsettings-httptransfermode
            """
            result = self._values.get("http_transfer_mode")
            return result

        @builtins.property
        def num_retries(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsWebdavSettingsProperty.NumRetries``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html#cfn-medialive-channel-hlswebdavsettings-numretries
            """
            result = self._values.get("num_retries")
            return result

        @builtins.property
        def restart_delay(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.HlsWebdavSettingsProperty.RestartDelay``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html#cfn-medialive-channel-hlswebdavsettings-restartdelay
            """
            result = self._values.get("restart_delay")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsWebdavSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.InputAttachmentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "automatic_input_failover_settings": "automaticInputFailoverSettings",
            "input_attachment_name": "inputAttachmentName",
            "input_id": "inputId",
            "input_settings": "inputSettings",
        },
    )
    class InputAttachmentProperty:
        def __init__(
            self,
            *,
            automatic_input_failover_settings: typing.Optional[typing.Union["CfnChannel.AutomaticInputFailoverSettingsProperty", _IResolvable_a771d0ef]] = None,
            input_attachment_name: typing.Optional[builtins.str] = None,
            input_id: typing.Optional[builtins.str] = None,
            input_settings: typing.Optional[typing.Union["CfnChannel.InputSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param automatic_input_failover_settings: ``CfnChannel.InputAttachmentProperty.AutomaticInputFailoverSettings``.
            :param input_attachment_name: ``CfnChannel.InputAttachmentProperty.InputAttachmentName``.
            :param input_id: ``CfnChannel.InputAttachmentProperty.InputId``.
            :param input_settings: ``CfnChannel.InputAttachmentProperty.InputSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputattachment.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if automatic_input_failover_settings is not None:
                self._values["automatic_input_failover_settings"] = automatic_input_failover_settings
            if input_attachment_name is not None:
                self._values["input_attachment_name"] = input_attachment_name
            if input_id is not None:
                self._values["input_id"] = input_id
            if input_settings is not None:
                self._values["input_settings"] = input_settings

        @builtins.property
        def automatic_input_failover_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.AutomaticInputFailoverSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.InputAttachmentProperty.AutomaticInputFailoverSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputattachment.html#cfn-medialive-channel-inputattachment-automaticinputfailoversettings
            """
            result = self._values.get("automatic_input_failover_settings")
            return result

        @builtins.property
        def input_attachment_name(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.InputAttachmentProperty.InputAttachmentName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputattachment.html#cfn-medialive-channel-inputattachment-inputattachmentname
            """
            result = self._values.get("input_attachment_name")
            return result

        @builtins.property
        def input_id(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.InputAttachmentProperty.InputId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputattachment.html#cfn-medialive-channel-inputattachment-inputid
            """
            result = self._values.get("input_id")
            return result

        @builtins.property
        def input_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.InputSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.InputAttachmentProperty.InputSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputattachment.html#cfn-medialive-channel-inputattachment-inputsettings
            """
            result = self._values.get("input_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputAttachmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.InputChannelLevelProperty",
        jsii_struct_bases=[],
        name_mapping={"gain": "gain", "input_channel": "inputChannel"},
    )
    class InputChannelLevelProperty:
        def __init__(
            self,
            *,
            gain: typing.Optional[jsii.Number] = None,
            input_channel: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param gain: ``CfnChannel.InputChannelLevelProperty.Gain``.
            :param input_channel: ``CfnChannel.InputChannelLevelProperty.InputChannel``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputchannellevel.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if gain is not None:
                self._values["gain"] = gain
            if input_channel is not None:
                self._values["input_channel"] = input_channel

        @builtins.property
        def gain(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.InputChannelLevelProperty.Gain``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputchannellevel.html#cfn-medialive-channel-inputchannellevel-gain
            """
            result = self._values.get("gain")
            return result

        @builtins.property
        def input_channel(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.InputChannelLevelProperty.InputChannel``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputchannellevel.html#cfn-medialive-channel-inputchannellevel-inputchannel
            """
            result = self._values.get("input_channel")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputChannelLevelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.InputLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "password_param": "passwordParam",
            "uri": "uri",
            "username": "username",
        },
    )
    class InputLocationProperty:
        def __init__(
            self,
            *,
            password_param: typing.Optional[builtins.str] = None,
            uri: typing.Optional[builtins.str] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param password_param: ``CfnChannel.InputLocationProperty.PasswordParam``.
            :param uri: ``CfnChannel.InputLocationProperty.Uri``.
            :param username: ``CfnChannel.InputLocationProperty.Username``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlocation.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if password_param is not None:
                self._values["password_param"] = password_param
            if uri is not None:
                self._values["uri"] = uri
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def password_param(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.InputLocationProperty.PasswordParam``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlocation.html#cfn-medialive-channel-inputlocation-passwordparam
            """
            result = self._values.get("password_param")
            return result

        @builtins.property
        def uri(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.InputLocationProperty.Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlocation.html#cfn-medialive-channel-inputlocation-uri
            """
            result = self._values.get("uri")
            return result

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.InputLocationProperty.Username``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlocation.html#cfn-medialive-channel-inputlocation-username
            """
            result = self._values.get("username")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.InputLossBehaviorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "black_frame_msec": "blackFrameMsec",
            "input_loss_image_color": "inputLossImageColor",
            "input_loss_image_slate": "inputLossImageSlate",
            "input_loss_image_type": "inputLossImageType",
            "repeat_frame_msec": "repeatFrameMsec",
        },
    )
    class InputLossBehaviorProperty:
        def __init__(
            self,
            *,
            black_frame_msec: typing.Optional[jsii.Number] = None,
            input_loss_image_color: typing.Optional[builtins.str] = None,
            input_loss_image_slate: typing.Optional[typing.Union["CfnChannel.InputLocationProperty", _IResolvable_a771d0ef]] = None,
            input_loss_image_type: typing.Optional[builtins.str] = None,
            repeat_frame_msec: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param black_frame_msec: ``CfnChannel.InputLossBehaviorProperty.BlackFrameMsec``.
            :param input_loss_image_color: ``CfnChannel.InputLossBehaviorProperty.InputLossImageColor``.
            :param input_loss_image_slate: ``CfnChannel.InputLossBehaviorProperty.InputLossImageSlate``.
            :param input_loss_image_type: ``CfnChannel.InputLossBehaviorProperty.InputLossImageType``.
            :param repeat_frame_msec: ``CfnChannel.InputLossBehaviorProperty.RepeatFrameMsec``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if black_frame_msec is not None:
                self._values["black_frame_msec"] = black_frame_msec
            if input_loss_image_color is not None:
                self._values["input_loss_image_color"] = input_loss_image_color
            if input_loss_image_slate is not None:
                self._values["input_loss_image_slate"] = input_loss_image_slate
            if input_loss_image_type is not None:
                self._values["input_loss_image_type"] = input_loss_image_type
            if repeat_frame_msec is not None:
                self._values["repeat_frame_msec"] = repeat_frame_msec

        @builtins.property
        def black_frame_msec(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.InputLossBehaviorProperty.BlackFrameMsec``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html#cfn-medialive-channel-inputlossbehavior-blackframemsec
            """
            result = self._values.get("black_frame_msec")
            return result

        @builtins.property
        def input_loss_image_color(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.InputLossBehaviorProperty.InputLossImageColor``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html#cfn-medialive-channel-inputlossbehavior-inputlossimagecolor
            """
            result = self._values.get("input_loss_image_color")
            return result

        @builtins.property
        def input_loss_image_slate(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.InputLocationProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.InputLossBehaviorProperty.InputLossImageSlate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html#cfn-medialive-channel-inputlossbehavior-inputlossimageslate
            """
            result = self._values.get("input_loss_image_slate")
            return result

        @builtins.property
        def input_loss_image_type(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.InputLossBehaviorProperty.InputLossImageType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html#cfn-medialive-channel-inputlossbehavior-inputlossimagetype
            """
            result = self._values.get("input_loss_image_type")
            return result

        @builtins.property
        def repeat_frame_msec(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.InputLossBehaviorProperty.RepeatFrameMsec``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html#cfn-medialive-channel-inputlossbehavior-repeatframemsec
            """
            result = self._values.get("repeat_frame_msec")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputLossBehaviorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.InputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_selectors": "audioSelectors",
            "caption_selectors": "captionSelectors",
            "deblock_filter": "deblockFilter",
            "denoise_filter": "denoiseFilter",
            "filter_strength": "filterStrength",
            "input_filter": "inputFilter",
            "network_input_settings": "networkInputSettings",
            "smpte2038_data_preference": "smpte2038DataPreference",
            "source_end_behavior": "sourceEndBehavior",
            "video_selector": "videoSelector",
        },
    )
    class InputSettingsProperty:
        def __init__(
            self,
            *,
            audio_selectors: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.AudioSelectorProperty", _IResolvable_a771d0ef]]]] = None,
            caption_selectors: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.CaptionSelectorProperty", _IResolvable_a771d0ef]]]] = None,
            deblock_filter: typing.Optional[builtins.str] = None,
            denoise_filter: typing.Optional[builtins.str] = None,
            filter_strength: typing.Optional[jsii.Number] = None,
            input_filter: typing.Optional[builtins.str] = None,
            network_input_settings: typing.Optional[typing.Union["CfnChannel.NetworkInputSettingsProperty", _IResolvable_a771d0ef]] = None,
            smpte2038_data_preference: typing.Optional[builtins.str] = None,
            source_end_behavior: typing.Optional[builtins.str] = None,
            video_selector: typing.Optional[typing.Union["CfnChannel.VideoSelectorProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param audio_selectors: ``CfnChannel.InputSettingsProperty.AudioSelectors``.
            :param caption_selectors: ``CfnChannel.InputSettingsProperty.CaptionSelectors``.
            :param deblock_filter: ``CfnChannel.InputSettingsProperty.DeblockFilter``.
            :param denoise_filter: ``CfnChannel.InputSettingsProperty.DenoiseFilter``.
            :param filter_strength: ``CfnChannel.InputSettingsProperty.FilterStrength``.
            :param input_filter: ``CfnChannel.InputSettingsProperty.InputFilter``.
            :param network_input_settings: ``CfnChannel.InputSettingsProperty.NetworkInputSettings``.
            :param smpte2038_data_preference: ``CfnChannel.InputSettingsProperty.Smpte2038DataPreference``.
            :param source_end_behavior: ``CfnChannel.InputSettingsProperty.SourceEndBehavior``.
            :param video_selector: ``CfnChannel.InputSettingsProperty.VideoSelector``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_selectors is not None:
                self._values["audio_selectors"] = audio_selectors
            if caption_selectors is not None:
                self._values["caption_selectors"] = caption_selectors
            if deblock_filter is not None:
                self._values["deblock_filter"] = deblock_filter
            if denoise_filter is not None:
                self._values["denoise_filter"] = denoise_filter
            if filter_strength is not None:
                self._values["filter_strength"] = filter_strength
            if input_filter is not None:
                self._values["input_filter"] = input_filter
            if network_input_settings is not None:
                self._values["network_input_settings"] = network_input_settings
            if smpte2038_data_preference is not None:
                self._values["smpte2038_data_preference"] = smpte2038_data_preference
            if source_end_behavior is not None:
                self._values["source_end_behavior"] = source_end_behavior
            if video_selector is not None:
                self._values["video_selector"] = video_selector

        @builtins.property
        def audio_selectors(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.AudioSelectorProperty", _IResolvable_a771d0ef]]]]:
            """``CfnChannel.InputSettingsProperty.AudioSelectors``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-audioselectors
            """
            result = self._values.get("audio_selectors")
            return result

        @builtins.property
        def caption_selectors(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.CaptionSelectorProperty", _IResolvable_a771d0ef]]]]:
            """``CfnChannel.InputSettingsProperty.CaptionSelectors``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-captionselectors
            """
            result = self._values.get("caption_selectors")
            return result

        @builtins.property
        def deblock_filter(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.InputSettingsProperty.DeblockFilter``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-deblockfilter
            """
            result = self._values.get("deblock_filter")
            return result

        @builtins.property
        def denoise_filter(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.InputSettingsProperty.DenoiseFilter``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-denoisefilter
            """
            result = self._values.get("denoise_filter")
            return result

        @builtins.property
        def filter_strength(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.InputSettingsProperty.FilterStrength``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-filterstrength
            """
            result = self._values.get("filter_strength")
            return result

        @builtins.property
        def input_filter(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.InputSettingsProperty.InputFilter``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-inputfilter
            """
            result = self._values.get("input_filter")
            return result

        @builtins.property
        def network_input_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.NetworkInputSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.InputSettingsProperty.NetworkInputSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-networkinputsettings
            """
            result = self._values.get("network_input_settings")
            return result

        @builtins.property
        def smpte2038_data_preference(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.InputSettingsProperty.Smpte2038DataPreference``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-smpte2038datapreference
            """
            result = self._values.get("smpte2038_data_preference")
            return result

        @builtins.property
        def source_end_behavior(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.InputSettingsProperty.SourceEndBehavior``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-sourceendbehavior
            """
            result = self._values.get("source_end_behavior")
            return result

        @builtins.property
        def video_selector(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.VideoSelectorProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.InputSettingsProperty.VideoSelector``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-videoselector
            """
            result = self._values.get("video_selector")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.InputSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "codec": "codec",
            "maximum_bitrate": "maximumBitrate",
            "resolution": "resolution",
        },
    )
    class InputSpecificationProperty:
        def __init__(
            self,
            *,
            codec: typing.Optional[builtins.str] = None,
            maximum_bitrate: typing.Optional[builtins.str] = None,
            resolution: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param codec: ``CfnChannel.InputSpecificationProperty.Codec``.
            :param maximum_bitrate: ``CfnChannel.InputSpecificationProperty.MaximumBitrate``.
            :param resolution: ``CfnChannel.InputSpecificationProperty.Resolution``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputspecification.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if codec is not None:
                self._values["codec"] = codec
            if maximum_bitrate is not None:
                self._values["maximum_bitrate"] = maximum_bitrate
            if resolution is not None:
                self._values["resolution"] = resolution

        @builtins.property
        def codec(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.InputSpecificationProperty.Codec``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputspecification.html#cfn-medialive-channel-inputspecification-codec
            """
            result = self._values.get("codec")
            return result

        @builtins.property
        def maximum_bitrate(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.InputSpecificationProperty.MaximumBitrate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputspecification.html#cfn-medialive-channel-inputspecification-maximumbitrate
            """
            result = self._values.get("maximum_bitrate")
            return result

        @builtins.property
        def resolution(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.InputSpecificationProperty.Resolution``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputspecification.html#cfn-medialive-channel-inputspecification-resolution
            """
            result = self._values.get("resolution")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.KeyProviderSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"static_key_settings": "staticKeySettings"},
    )
    class KeyProviderSettingsProperty:
        def __init__(
            self,
            *,
            static_key_settings: typing.Optional[typing.Union["CfnChannel.StaticKeySettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param static_key_settings: ``CfnChannel.KeyProviderSettingsProperty.StaticKeySettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-keyprovidersettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if static_key_settings is not None:
                self._values["static_key_settings"] = static_key_settings

        @builtins.property
        def static_key_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.StaticKeySettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.KeyProviderSettingsProperty.StaticKeySettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-keyprovidersettings.html#cfn-medialive-channel-keyprovidersettings-statickeysettings
            """
            result = self._values.get("static_key_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyProviderSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.M2tsSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "absent_input_audio_behavior": "absentInputAudioBehavior",
            "arib": "arib",
            "arib_captions_pid": "aribCaptionsPid",
            "arib_captions_pid_control": "aribCaptionsPidControl",
            "audio_buffer_model": "audioBufferModel",
            "audio_frames_per_pes": "audioFramesPerPes",
            "audio_pids": "audioPids",
            "audio_stream_type": "audioStreamType",
            "bitrate": "bitrate",
            "buffer_model": "bufferModel",
            "cc_descriptor": "ccDescriptor",
            "dvb_nit_settings": "dvbNitSettings",
            "dvb_sdt_settings": "dvbSdtSettings",
            "dvb_sub_pids": "dvbSubPids",
            "dvb_tdt_settings": "dvbTdtSettings",
            "dvb_teletext_pid": "dvbTeletextPid",
            "ebif": "ebif",
            "ebp_audio_interval": "ebpAudioInterval",
            "ebp_lookahead_ms": "ebpLookaheadMs",
            "ebp_placement": "ebpPlacement",
            "ecm_pid": "ecmPid",
            "es_rate_in_pes": "esRateInPes",
            "etv_platform_pid": "etvPlatformPid",
            "etv_signal_pid": "etvSignalPid",
            "fragment_time": "fragmentTime",
            "klv": "klv",
            "klv_data_pids": "klvDataPids",
            "nielsen_id3_behavior": "nielsenId3Behavior",
            "null_packet_bitrate": "nullPacketBitrate",
            "pat_interval": "patInterval",
            "pcr_control": "pcrControl",
            "pcr_period": "pcrPeriod",
            "pcr_pid": "pcrPid",
            "pmt_interval": "pmtInterval",
            "pmt_pid": "pmtPid",
            "program_num": "programNum",
            "rate_mode": "rateMode",
            "scte27_pids": "scte27Pids",
            "scte35_control": "scte35Control",
            "scte35_pid": "scte35Pid",
            "segmentation_markers": "segmentationMarkers",
            "segmentation_style": "segmentationStyle",
            "segmentation_time": "segmentationTime",
            "timed_metadata_behavior": "timedMetadataBehavior",
            "timed_metadata_pid": "timedMetadataPid",
            "transport_stream_id": "transportStreamId",
            "video_pid": "videoPid",
        },
    )
    class M2tsSettingsProperty:
        def __init__(
            self,
            *,
            absent_input_audio_behavior: typing.Optional[builtins.str] = None,
            arib: typing.Optional[builtins.str] = None,
            arib_captions_pid: typing.Optional[builtins.str] = None,
            arib_captions_pid_control: typing.Optional[builtins.str] = None,
            audio_buffer_model: typing.Optional[builtins.str] = None,
            audio_frames_per_pes: typing.Optional[jsii.Number] = None,
            audio_pids: typing.Optional[builtins.str] = None,
            audio_stream_type: typing.Optional[builtins.str] = None,
            bitrate: typing.Optional[jsii.Number] = None,
            buffer_model: typing.Optional[builtins.str] = None,
            cc_descriptor: typing.Optional[builtins.str] = None,
            dvb_nit_settings: typing.Optional[typing.Union["CfnChannel.DvbNitSettingsProperty", _IResolvable_a771d0ef]] = None,
            dvb_sdt_settings: typing.Optional[typing.Union["CfnChannel.DvbSdtSettingsProperty", _IResolvable_a771d0ef]] = None,
            dvb_sub_pids: typing.Optional[builtins.str] = None,
            dvb_tdt_settings: typing.Optional[typing.Union["CfnChannel.DvbTdtSettingsProperty", _IResolvable_a771d0ef]] = None,
            dvb_teletext_pid: typing.Optional[builtins.str] = None,
            ebif: typing.Optional[builtins.str] = None,
            ebp_audio_interval: typing.Optional[builtins.str] = None,
            ebp_lookahead_ms: typing.Optional[jsii.Number] = None,
            ebp_placement: typing.Optional[builtins.str] = None,
            ecm_pid: typing.Optional[builtins.str] = None,
            es_rate_in_pes: typing.Optional[builtins.str] = None,
            etv_platform_pid: typing.Optional[builtins.str] = None,
            etv_signal_pid: typing.Optional[builtins.str] = None,
            fragment_time: typing.Optional[jsii.Number] = None,
            klv: typing.Optional[builtins.str] = None,
            klv_data_pids: typing.Optional[builtins.str] = None,
            nielsen_id3_behavior: typing.Optional[builtins.str] = None,
            null_packet_bitrate: typing.Optional[jsii.Number] = None,
            pat_interval: typing.Optional[jsii.Number] = None,
            pcr_control: typing.Optional[builtins.str] = None,
            pcr_period: typing.Optional[jsii.Number] = None,
            pcr_pid: typing.Optional[builtins.str] = None,
            pmt_interval: typing.Optional[jsii.Number] = None,
            pmt_pid: typing.Optional[builtins.str] = None,
            program_num: typing.Optional[jsii.Number] = None,
            rate_mode: typing.Optional[builtins.str] = None,
            scte27_pids: typing.Optional[builtins.str] = None,
            scte35_control: typing.Optional[builtins.str] = None,
            scte35_pid: typing.Optional[builtins.str] = None,
            segmentation_markers: typing.Optional[builtins.str] = None,
            segmentation_style: typing.Optional[builtins.str] = None,
            segmentation_time: typing.Optional[jsii.Number] = None,
            timed_metadata_behavior: typing.Optional[builtins.str] = None,
            timed_metadata_pid: typing.Optional[builtins.str] = None,
            transport_stream_id: typing.Optional[jsii.Number] = None,
            video_pid: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param absent_input_audio_behavior: ``CfnChannel.M2tsSettingsProperty.AbsentInputAudioBehavior``.
            :param arib: ``CfnChannel.M2tsSettingsProperty.Arib``.
            :param arib_captions_pid: ``CfnChannel.M2tsSettingsProperty.AribCaptionsPid``.
            :param arib_captions_pid_control: ``CfnChannel.M2tsSettingsProperty.AribCaptionsPidControl``.
            :param audio_buffer_model: ``CfnChannel.M2tsSettingsProperty.AudioBufferModel``.
            :param audio_frames_per_pes: ``CfnChannel.M2tsSettingsProperty.AudioFramesPerPes``.
            :param audio_pids: ``CfnChannel.M2tsSettingsProperty.AudioPids``.
            :param audio_stream_type: ``CfnChannel.M2tsSettingsProperty.AudioStreamType``.
            :param bitrate: ``CfnChannel.M2tsSettingsProperty.Bitrate``.
            :param buffer_model: ``CfnChannel.M2tsSettingsProperty.BufferModel``.
            :param cc_descriptor: ``CfnChannel.M2tsSettingsProperty.CcDescriptor``.
            :param dvb_nit_settings: ``CfnChannel.M2tsSettingsProperty.DvbNitSettings``.
            :param dvb_sdt_settings: ``CfnChannel.M2tsSettingsProperty.DvbSdtSettings``.
            :param dvb_sub_pids: ``CfnChannel.M2tsSettingsProperty.DvbSubPids``.
            :param dvb_tdt_settings: ``CfnChannel.M2tsSettingsProperty.DvbTdtSettings``.
            :param dvb_teletext_pid: ``CfnChannel.M2tsSettingsProperty.DvbTeletextPid``.
            :param ebif: ``CfnChannel.M2tsSettingsProperty.Ebif``.
            :param ebp_audio_interval: ``CfnChannel.M2tsSettingsProperty.EbpAudioInterval``.
            :param ebp_lookahead_ms: ``CfnChannel.M2tsSettingsProperty.EbpLookaheadMs``.
            :param ebp_placement: ``CfnChannel.M2tsSettingsProperty.EbpPlacement``.
            :param ecm_pid: ``CfnChannel.M2tsSettingsProperty.EcmPid``.
            :param es_rate_in_pes: ``CfnChannel.M2tsSettingsProperty.EsRateInPes``.
            :param etv_platform_pid: ``CfnChannel.M2tsSettingsProperty.EtvPlatformPid``.
            :param etv_signal_pid: ``CfnChannel.M2tsSettingsProperty.EtvSignalPid``.
            :param fragment_time: ``CfnChannel.M2tsSettingsProperty.FragmentTime``.
            :param klv: ``CfnChannel.M2tsSettingsProperty.Klv``.
            :param klv_data_pids: ``CfnChannel.M2tsSettingsProperty.KlvDataPids``.
            :param nielsen_id3_behavior: ``CfnChannel.M2tsSettingsProperty.NielsenId3Behavior``.
            :param null_packet_bitrate: ``CfnChannel.M2tsSettingsProperty.NullPacketBitrate``.
            :param pat_interval: ``CfnChannel.M2tsSettingsProperty.PatInterval``.
            :param pcr_control: ``CfnChannel.M2tsSettingsProperty.PcrControl``.
            :param pcr_period: ``CfnChannel.M2tsSettingsProperty.PcrPeriod``.
            :param pcr_pid: ``CfnChannel.M2tsSettingsProperty.PcrPid``.
            :param pmt_interval: ``CfnChannel.M2tsSettingsProperty.PmtInterval``.
            :param pmt_pid: ``CfnChannel.M2tsSettingsProperty.PmtPid``.
            :param program_num: ``CfnChannel.M2tsSettingsProperty.ProgramNum``.
            :param rate_mode: ``CfnChannel.M2tsSettingsProperty.RateMode``.
            :param scte27_pids: ``CfnChannel.M2tsSettingsProperty.Scte27Pids``.
            :param scte35_control: ``CfnChannel.M2tsSettingsProperty.Scte35Control``.
            :param scte35_pid: ``CfnChannel.M2tsSettingsProperty.Scte35Pid``.
            :param segmentation_markers: ``CfnChannel.M2tsSettingsProperty.SegmentationMarkers``.
            :param segmentation_style: ``CfnChannel.M2tsSettingsProperty.SegmentationStyle``.
            :param segmentation_time: ``CfnChannel.M2tsSettingsProperty.SegmentationTime``.
            :param timed_metadata_behavior: ``CfnChannel.M2tsSettingsProperty.TimedMetadataBehavior``.
            :param timed_metadata_pid: ``CfnChannel.M2tsSettingsProperty.TimedMetadataPid``.
            :param transport_stream_id: ``CfnChannel.M2tsSettingsProperty.TransportStreamId``.
            :param video_pid: ``CfnChannel.M2tsSettingsProperty.VideoPid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if absent_input_audio_behavior is not None:
                self._values["absent_input_audio_behavior"] = absent_input_audio_behavior
            if arib is not None:
                self._values["arib"] = arib
            if arib_captions_pid is not None:
                self._values["arib_captions_pid"] = arib_captions_pid
            if arib_captions_pid_control is not None:
                self._values["arib_captions_pid_control"] = arib_captions_pid_control
            if audio_buffer_model is not None:
                self._values["audio_buffer_model"] = audio_buffer_model
            if audio_frames_per_pes is not None:
                self._values["audio_frames_per_pes"] = audio_frames_per_pes
            if audio_pids is not None:
                self._values["audio_pids"] = audio_pids
            if audio_stream_type is not None:
                self._values["audio_stream_type"] = audio_stream_type
            if bitrate is not None:
                self._values["bitrate"] = bitrate
            if buffer_model is not None:
                self._values["buffer_model"] = buffer_model
            if cc_descriptor is not None:
                self._values["cc_descriptor"] = cc_descriptor
            if dvb_nit_settings is not None:
                self._values["dvb_nit_settings"] = dvb_nit_settings
            if dvb_sdt_settings is not None:
                self._values["dvb_sdt_settings"] = dvb_sdt_settings
            if dvb_sub_pids is not None:
                self._values["dvb_sub_pids"] = dvb_sub_pids
            if dvb_tdt_settings is not None:
                self._values["dvb_tdt_settings"] = dvb_tdt_settings
            if dvb_teletext_pid is not None:
                self._values["dvb_teletext_pid"] = dvb_teletext_pid
            if ebif is not None:
                self._values["ebif"] = ebif
            if ebp_audio_interval is not None:
                self._values["ebp_audio_interval"] = ebp_audio_interval
            if ebp_lookahead_ms is not None:
                self._values["ebp_lookahead_ms"] = ebp_lookahead_ms
            if ebp_placement is not None:
                self._values["ebp_placement"] = ebp_placement
            if ecm_pid is not None:
                self._values["ecm_pid"] = ecm_pid
            if es_rate_in_pes is not None:
                self._values["es_rate_in_pes"] = es_rate_in_pes
            if etv_platform_pid is not None:
                self._values["etv_platform_pid"] = etv_platform_pid
            if etv_signal_pid is not None:
                self._values["etv_signal_pid"] = etv_signal_pid
            if fragment_time is not None:
                self._values["fragment_time"] = fragment_time
            if klv is not None:
                self._values["klv"] = klv
            if klv_data_pids is not None:
                self._values["klv_data_pids"] = klv_data_pids
            if nielsen_id3_behavior is not None:
                self._values["nielsen_id3_behavior"] = nielsen_id3_behavior
            if null_packet_bitrate is not None:
                self._values["null_packet_bitrate"] = null_packet_bitrate
            if pat_interval is not None:
                self._values["pat_interval"] = pat_interval
            if pcr_control is not None:
                self._values["pcr_control"] = pcr_control
            if pcr_period is not None:
                self._values["pcr_period"] = pcr_period
            if pcr_pid is not None:
                self._values["pcr_pid"] = pcr_pid
            if pmt_interval is not None:
                self._values["pmt_interval"] = pmt_interval
            if pmt_pid is not None:
                self._values["pmt_pid"] = pmt_pid
            if program_num is not None:
                self._values["program_num"] = program_num
            if rate_mode is not None:
                self._values["rate_mode"] = rate_mode
            if scte27_pids is not None:
                self._values["scte27_pids"] = scte27_pids
            if scte35_control is not None:
                self._values["scte35_control"] = scte35_control
            if scte35_pid is not None:
                self._values["scte35_pid"] = scte35_pid
            if segmentation_markers is not None:
                self._values["segmentation_markers"] = segmentation_markers
            if segmentation_style is not None:
                self._values["segmentation_style"] = segmentation_style
            if segmentation_time is not None:
                self._values["segmentation_time"] = segmentation_time
            if timed_metadata_behavior is not None:
                self._values["timed_metadata_behavior"] = timed_metadata_behavior
            if timed_metadata_pid is not None:
                self._values["timed_metadata_pid"] = timed_metadata_pid
            if transport_stream_id is not None:
                self._values["transport_stream_id"] = transport_stream_id
            if video_pid is not None:
                self._values["video_pid"] = video_pid

        @builtins.property
        def absent_input_audio_behavior(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.AbsentInputAudioBehavior``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-absentinputaudiobehavior
            """
            result = self._values.get("absent_input_audio_behavior")
            return result

        @builtins.property
        def arib(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.Arib``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-arib
            """
            result = self._values.get("arib")
            return result

        @builtins.property
        def arib_captions_pid(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.AribCaptionsPid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-aribcaptionspid
            """
            result = self._values.get("arib_captions_pid")
            return result

        @builtins.property
        def arib_captions_pid_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.AribCaptionsPidControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-aribcaptionspidcontrol
            """
            result = self._values.get("arib_captions_pid_control")
            return result

        @builtins.property
        def audio_buffer_model(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.AudioBufferModel``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-audiobuffermodel
            """
            result = self._values.get("audio_buffer_model")
            return result

        @builtins.property
        def audio_frames_per_pes(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.M2tsSettingsProperty.AudioFramesPerPes``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-audioframesperpes
            """
            result = self._values.get("audio_frames_per_pes")
            return result

        @builtins.property
        def audio_pids(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.AudioPids``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-audiopids
            """
            result = self._values.get("audio_pids")
            return result

        @builtins.property
        def audio_stream_type(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.AudioStreamType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-audiostreamtype
            """
            result = self._values.get("audio_stream_type")
            return result

        @builtins.property
        def bitrate(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.M2tsSettingsProperty.Bitrate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-bitrate
            """
            result = self._values.get("bitrate")
            return result

        @builtins.property
        def buffer_model(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.BufferModel``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-buffermodel
            """
            result = self._values.get("buffer_model")
            return result

        @builtins.property
        def cc_descriptor(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.CcDescriptor``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ccdescriptor
            """
            result = self._values.get("cc_descriptor")
            return result

        @builtins.property
        def dvb_nit_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.DvbNitSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.M2tsSettingsProperty.DvbNitSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-dvbnitsettings
            """
            result = self._values.get("dvb_nit_settings")
            return result

        @builtins.property
        def dvb_sdt_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.DvbSdtSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.M2tsSettingsProperty.DvbSdtSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-dvbsdtsettings
            """
            result = self._values.get("dvb_sdt_settings")
            return result

        @builtins.property
        def dvb_sub_pids(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.DvbSubPids``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-dvbsubpids
            """
            result = self._values.get("dvb_sub_pids")
            return result

        @builtins.property
        def dvb_tdt_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.DvbTdtSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.M2tsSettingsProperty.DvbTdtSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-dvbtdtsettings
            """
            result = self._values.get("dvb_tdt_settings")
            return result

        @builtins.property
        def dvb_teletext_pid(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.DvbTeletextPid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-dvbteletextpid
            """
            result = self._values.get("dvb_teletext_pid")
            return result

        @builtins.property
        def ebif(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.Ebif``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ebif
            """
            result = self._values.get("ebif")
            return result

        @builtins.property
        def ebp_audio_interval(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.EbpAudioInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ebpaudiointerval
            """
            result = self._values.get("ebp_audio_interval")
            return result

        @builtins.property
        def ebp_lookahead_ms(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.M2tsSettingsProperty.EbpLookaheadMs``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ebplookaheadms
            """
            result = self._values.get("ebp_lookahead_ms")
            return result

        @builtins.property
        def ebp_placement(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.EbpPlacement``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ebpplacement
            """
            result = self._values.get("ebp_placement")
            return result

        @builtins.property
        def ecm_pid(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.EcmPid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ecmpid
            """
            result = self._values.get("ecm_pid")
            return result

        @builtins.property
        def es_rate_in_pes(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.EsRateInPes``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-esrateinpes
            """
            result = self._values.get("es_rate_in_pes")
            return result

        @builtins.property
        def etv_platform_pid(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.EtvPlatformPid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-etvplatformpid
            """
            result = self._values.get("etv_platform_pid")
            return result

        @builtins.property
        def etv_signal_pid(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.EtvSignalPid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-etvsignalpid
            """
            result = self._values.get("etv_signal_pid")
            return result

        @builtins.property
        def fragment_time(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.M2tsSettingsProperty.FragmentTime``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-fragmenttime
            """
            result = self._values.get("fragment_time")
            return result

        @builtins.property
        def klv(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.Klv``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-klv
            """
            result = self._values.get("klv")
            return result

        @builtins.property
        def klv_data_pids(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.KlvDataPids``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-klvdatapids
            """
            result = self._values.get("klv_data_pids")
            return result

        @builtins.property
        def nielsen_id3_behavior(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.NielsenId3Behavior``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-nielsenid3behavior
            """
            result = self._values.get("nielsen_id3_behavior")
            return result

        @builtins.property
        def null_packet_bitrate(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.M2tsSettingsProperty.NullPacketBitrate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-nullpacketbitrate
            """
            result = self._values.get("null_packet_bitrate")
            return result

        @builtins.property
        def pat_interval(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.M2tsSettingsProperty.PatInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-patinterval
            """
            result = self._values.get("pat_interval")
            return result

        @builtins.property
        def pcr_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.PcrControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-pcrcontrol
            """
            result = self._values.get("pcr_control")
            return result

        @builtins.property
        def pcr_period(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.M2tsSettingsProperty.PcrPeriod``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-pcrperiod
            """
            result = self._values.get("pcr_period")
            return result

        @builtins.property
        def pcr_pid(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.PcrPid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-pcrpid
            """
            result = self._values.get("pcr_pid")
            return result

        @builtins.property
        def pmt_interval(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.M2tsSettingsProperty.PmtInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-pmtinterval
            """
            result = self._values.get("pmt_interval")
            return result

        @builtins.property
        def pmt_pid(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.PmtPid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-pmtpid
            """
            result = self._values.get("pmt_pid")
            return result

        @builtins.property
        def program_num(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.M2tsSettingsProperty.ProgramNum``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-programnum
            """
            result = self._values.get("program_num")
            return result

        @builtins.property
        def rate_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.RateMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ratemode
            """
            result = self._values.get("rate_mode")
            return result

        @builtins.property
        def scte27_pids(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.Scte27Pids``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-scte27pids
            """
            result = self._values.get("scte27_pids")
            return result

        @builtins.property
        def scte35_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.Scte35Control``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-scte35control
            """
            result = self._values.get("scte35_control")
            return result

        @builtins.property
        def scte35_pid(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.Scte35Pid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-scte35pid
            """
            result = self._values.get("scte35_pid")
            return result

        @builtins.property
        def segmentation_markers(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.SegmentationMarkers``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-segmentationmarkers
            """
            result = self._values.get("segmentation_markers")
            return result

        @builtins.property
        def segmentation_style(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.SegmentationStyle``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-segmentationstyle
            """
            result = self._values.get("segmentation_style")
            return result

        @builtins.property
        def segmentation_time(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.M2tsSettingsProperty.SegmentationTime``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-segmentationtime
            """
            result = self._values.get("segmentation_time")
            return result

        @builtins.property
        def timed_metadata_behavior(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.TimedMetadataBehavior``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-timedmetadatabehavior
            """
            result = self._values.get("timed_metadata_behavior")
            return result

        @builtins.property
        def timed_metadata_pid(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.TimedMetadataPid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-timedmetadatapid
            """
            result = self._values.get("timed_metadata_pid")
            return result

        @builtins.property
        def transport_stream_id(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.M2tsSettingsProperty.TransportStreamId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-transportstreamid
            """
            result = self._values.get("transport_stream_id")
            return result

        @builtins.property
        def video_pid(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M2tsSettingsProperty.VideoPid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-videopid
            """
            result = self._values.get("video_pid")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "M2tsSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.M3u8SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_frames_per_pes": "audioFramesPerPes",
            "audio_pids": "audioPids",
            "ecm_pid": "ecmPid",
            "nielsen_id3_behavior": "nielsenId3Behavior",
            "pat_interval": "patInterval",
            "pcr_control": "pcrControl",
            "pcr_period": "pcrPeriod",
            "pcr_pid": "pcrPid",
            "pmt_interval": "pmtInterval",
            "pmt_pid": "pmtPid",
            "program_num": "programNum",
            "scte35_behavior": "scte35Behavior",
            "scte35_pid": "scte35Pid",
            "timed_metadata_behavior": "timedMetadataBehavior",
            "timed_metadata_pid": "timedMetadataPid",
            "transport_stream_id": "transportStreamId",
            "video_pid": "videoPid",
        },
    )
    class M3u8SettingsProperty:
        def __init__(
            self,
            *,
            audio_frames_per_pes: typing.Optional[jsii.Number] = None,
            audio_pids: typing.Optional[builtins.str] = None,
            ecm_pid: typing.Optional[builtins.str] = None,
            nielsen_id3_behavior: typing.Optional[builtins.str] = None,
            pat_interval: typing.Optional[jsii.Number] = None,
            pcr_control: typing.Optional[builtins.str] = None,
            pcr_period: typing.Optional[jsii.Number] = None,
            pcr_pid: typing.Optional[builtins.str] = None,
            pmt_interval: typing.Optional[jsii.Number] = None,
            pmt_pid: typing.Optional[builtins.str] = None,
            program_num: typing.Optional[jsii.Number] = None,
            scte35_behavior: typing.Optional[builtins.str] = None,
            scte35_pid: typing.Optional[builtins.str] = None,
            timed_metadata_behavior: typing.Optional[builtins.str] = None,
            timed_metadata_pid: typing.Optional[builtins.str] = None,
            transport_stream_id: typing.Optional[jsii.Number] = None,
            video_pid: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param audio_frames_per_pes: ``CfnChannel.M3u8SettingsProperty.AudioFramesPerPes``.
            :param audio_pids: ``CfnChannel.M3u8SettingsProperty.AudioPids``.
            :param ecm_pid: ``CfnChannel.M3u8SettingsProperty.EcmPid``.
            :param nielsen_id3_behavior: ``CfnChannel.M3u8SettingsProperty.NielsenId3Behavior``.
            :param pat_interval: ``CfnChannel.M3u8SettingsProperty.PatInterval``.
            :param pcr_control: ``CfnChannel.M3u8SettingsProperty.PcrControl``.
            :param pcr_period: ``CfnChannel.M3u8SettingsProperty.PcrPeriod``.
            :param pcr_pid: ``CfnChannel.M3u8SettingsProperty.PcrPid``.
            :param pmt_interval: ``CfnChannel.M3u8SettingsProperty.PmtInterval``.
            :param pmt_pid: ``CfnChannel.M3u8SettingsProperty.PmtPid``.
            :param program_num: ``CfnChannel.M3u8SettingsProperty.ProgramNum``.
            :param scte35_behavior: ``CfnChannel.M3u8SettingsProperty.Scte35Behavior``.
            :param scte35_pid: ``CfnChannel.M3u8SettingsProperty.Scte35Pid``.
            :param timed_metadata_behavior: ``CfnChannel.M3u8SettingsProperty.TimedMetadataBehavior``.
            :param timed_metadata_pid: ``CfnChannel.M3u8SettingsProperty.TimedMetadataPid``.
            :param transport_stream_id: ``CfnChannel.M3u8SettingsProperty.TransportStreamId``.
            :param video_pid: ``CfnChannel.M3u8SettingsProperty.VideoPid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_frames_per_pes is not None:
                self._values["audio_frames_per_pes"] = audio_frames_per_pes
            if audio_pids is not None:
                self._values["audio_pids"] = audio_pids
            if ecm_pid is not None:
                self._values["ecm_pid"] = ecm_pid
            if nielsen_id3_behavior is not None:
                self._values["nielsen_id3_behavior"] = nielsen_id3_behavior
            if pat_interval is not None:
                self._values["pat_interval"] = pat_interval
            if pcr_control is not None:
                self._values["pcr_control"] = pcr_control
            if pcr_period is not None:
                self._values["pcr_period"] = pcr_period
            if pcr_pid is not None:
                self._values["pcr_pid"] = pcr_pid
            if pmt_interval is not None:
                self._values["pmt_interval"] = pmt_interval
            if pmt_pid is not None:
                self._values["pmt_pid"] = pmt_pid
            if program_num is not None:
                self._values["program_num"] = program_num
            if scte35_behavior is not None:
                self._values["scte35_behavior"] = scte35_behavior
            if scte35_pid is not None:
                self._values["scte35_pid"] = scte35_pid
            if timed_metadata_behavior is not None:
                self._values["timed_metadata_behavior"] = timed_metadata_behavior
            if timed_metadata_pid is not None:
                self._values["timed_metadata_pid"] = timed_metadata_pid
            if transport_stream_id is not None:
                self._values["transport_stream_id"] = transport_stream_id
            if video_pid is not None:
                self._values["video_pid"] = video_pid

        @builtins.property
        def audio_frames_per_pes(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.M3u8SettingsProperty.AudioFramesPerPes``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-audioframesperpes
            """
            result = self._values.get("audio_frames_per_pes")
            return result

        @builtins.property
        def audio_pids(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M3u8SettingsProperty.AudioPids``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-audiopids
            """
            result = self._values.get("audio_pids")
            return result

        @builtins.property
        def ecm_pid(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M3u8SettingsProperty.EcmPid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-ecmpid
            """
            result = self._values.get("ecm_pid")
            return result

        @builtins.property
        def nielsen_id3_behavior(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M3u8SettingsProperty.NielsenId3Behavior``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-nielsenid3behavior
            """
            result = self._values.get("nielsen_id3_behavior")
            return result

        @builtins.property
        def pat_interval(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.M3u8SettingsProperty.PatInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-patinterval
            """
            result = self._values.get("pat_interval")
            return result

        @builtins.property
        def pcr_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M3u8SettingsProperty.PcrControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-pcrcontrol
            """
            result = self._values.get("pcr_control")
            return result

        @builtins.property
        def pcr_period(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.M3u8SettingsProperty.PcrPeriod``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-pcrperiod
            """
            result = self._values.get("pcr_period")
            return result

        @builtins.property
        def pcr_pid(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M3u8SettingsProperty.PcrPid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-pcrpid
            """
            result = self._values.get("pcr_pid")
            return result

        @builtins.property
        def pmt_interval(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.M3u8SettingsProperty.PmtInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-pmtinterval
            """
            result = self._values.get("pmt_interval")
            return result

        @builtins.property
        def pmt_pid(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M3u8SettingsProperty.PmtPid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-pmtpid
            """
            result = self._values.get("pmt_pid")
            return result

        @builtins.property
        def program_num(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.M3u8SettingsProperty.ProgramNum``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-programnum
            """
            result = self._values.get("program_num")
            return result

        @builtins.property
        def scte35_behavior(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M3u8SettingsProperty.Scte35Behavior``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-scte35behavior
            """
            result = self._values.get("scte35_behavior")
            return result

        @builtins.property
        def scte35_pid(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M3u8SettingsProperty.Scte35Pid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-scte35pid
            """
            result = self._values.get("scte35_pid")
            return result

        @builtins.property
        def timed_metadata_behavior(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M3u8SettingsProperty.TimedMetadataBehavior``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-timedmetadatabehavior
            """
            result = self._values.get("timed_metadata_behavior")
            return result

        @builtins.property
        def timed_metadata_pid(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M3u8SettingsProperty.TimedMetadataPid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-timedmetadatapid
            """
            result = self._values.get("timed_metadata_pid")
            return result

        @builtins.property
        def transport_stream_id(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.M3u8SettingsProperty.TransportStreamId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-transportstreamid
            """
            result = self._values.get("transport_stream_id")
            return result

        @builtins.property
        def video_pid(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.M3u8SettingsProperty.VideoPid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-videopid
            """
            result = self._values.get("video_pid")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "M3u8SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.MediaPackageGroupSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination"},
    )
    class MediaPackageGroupSettingsProperty:
        def __init__(
            self,
            *,
            destination: typing.Optional[typing.Union["CfnChannel.OutputLocationRefProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param destination: ``CfnChannel.MediaPackageGroupSettingsProperty.Destination``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackagegroupsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if destination is not None:
                self._values["destination"] = destination

        @builtins.property
        def destination(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.OutputLocationRefProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.MediaPackageGroupSettingsProperty.Destination``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackagegroupsettings.html#cfn-medialive-channel-mediapackagegroupsettings-destination
            """
            result = self._values.get("destination")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaPackageGroupSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.MediaPackageOutputDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"channel_id": "channelId"},
    )
    class MediaPackageOutputDestinationSettingsProperty:
        def __init__(self, *, channel_id: typing.Optional[builtins.str] = None) -> None:
            """
            :param channel_id: ``CfnChannel.MediaPackageOutputDestinationSettingsProperty.ChannelId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackageoutputdestinationsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if channel_id is not None:
                self._values["channel_id"] = channel_id

        @builtins.property
        def channel_id(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.MediaPackageOutputDestinationSettingsProperty.ChannelId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackageoutputdestinationsettings.html#cfn-medialive-channel-mediapackageoutputdestinationsettings-channelid
            """
            result = self._values.get("channel_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaPackageOutputDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.MediaPackageOutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class MediaPackageOutputSettingsProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackageoutputsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaPackageOutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.Mp2SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bitrate": "bitrate",
            "coding_mode": "codingMode",
            "sample_rate": "sampleRate",
        },
    )
    class Mp2SettingsProperty:
        def __init__(
            self,
            *,
            bitrate: typing.Optional[jsii.Number] = None,
            coding_mode: typing.Optional[builtins.str] = None,
            sample_rate: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param bitrate: ``CfnChannel.Mp2SettingsProperty.Bitrate``.
            :param coding_mode: ``CfnChannel.Mp2SettingsProperty.CodingMode``.
            :param sample_rate: ``CfnChannel.Mp2SettingsProperty.SampleRate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if bitrate is not None:
                self._values["bitrate"] = bitrate
            if coding_mode is not None:
                self._values["coding_mode"] = coding_mode
            if sample_rate is not None:
                self._values["sample_rate"] = sample_rate

        @builtins.property
        def bitrate(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.Mp2SettingsProperty.Bitrate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html#cfn-medialive-channel-mp2settings-bitrate
            """
            result = self._values.get("bitrate")
            return result

        @builtins.property
        def coding_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Mp2SettingsProperty.CodingMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html#cfn-medialive-channel-mp2settings-codingmode
            """
            result = self._values.get("coding_mode")
            return result

        @builtins.property
        def sample_rate(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.Mp2SettingsProperty.SampleRate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html#cfn-medialive-channel-mp2settings-samplerate
            """
            result = self._values.get("sample_rate")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Mp2SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.MsSmoothGroupSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "acquisition_point_id": "acquisitionPointId",
            "audio_only_timecode_control": "audioOnlyTimecodeControl",
            "certificate_mode": "certificateMode",
            "connection_retry_interval": "connectionRetryInterval",
            "destination": "destination",
            "event_id": "eventId",
            "event_id_mode": "eventIdMode",
            "event_stop_behavior": "eventStopBehavior",
            "filecache_duration": "filecacheDuration",
            "fragment_length": "fragmentLength",
            "input_loss_action": "inputLossAction",
            "num_retries": "numRetries",
            "restart_delay": "restartDelay",
            "segmentation_mode": "segmentationMode",
            "send_delay_ms": "sendDelayMs",
            "sparse_track_type": "sparseTrackType",
            "stream_manifest_behavior": "streamManifestBehavior",
            "timestamp_offset": "timestampOffset",
            "timestamp_offset_mode": "timestampOffsetMode",
        },
    )
    class MsSmoothGroupSettingsProperty:
        def __init__(
            self,
            *,
            acquisition_point_id: typing.Optional[builtins.str] = None,
            audio_only_timecode_control: typing.Optional[builtins.str] = None,
            certificate_mode: typing.Optional[builtins.str] = None,
            connection_retry_interval: typing.Optional[jsii.Number] = None,
            destination: typing.Optional[typing.Union["CfnChannel.OutputLocationRefProperty", _IResolvable_a771d0ef]] = None,
            event_id: typing.Optional[builtins.str] = None,
            event_id_mode: typing.Optional[builtins.str] = None,
            event_stop_behavior: typing.Optional[builtins.str] = None,
            filecache_duration: typing.Optional[jsii.Number] = None,
            fragment_length: typing.Optional[jsii.Number] = None,
            input_loss_action: typing.Optional[builtins.str] = None,
            num_retries: typing.Optional[jsii.Number] = None,
            restart_delay: typing.Optional[jsii.Number] = None,
            segmentation_mode: typing.Optional[builtins.str] = None,
            send_delay_ms: typing.Optional[jsii.Number] = None,
            sparse_track_type: typing.Optional[builtins.str] = None,
            stream_manifest_behavior: typing.Optional[builtins.str] = None,
            timestamp_offset: typing.Optional[builtins.str] = None,
            timestamp_offset_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param acquisition_point_id: ``CfnChannel.MsSmoothGroupSettingsProperty.AcquisitionPointId``.
            :param audio_only_timecode_control: ``CfnChannel.MsSmoothGroupSettingsProperty.AudioOnlyTimecodeControl``.
            :param certificate_mode: ``CfnChannel.MsSmoothGroupSettingsProperty.CertificateMode``.
            :param connection_retry_interval: ``CfnChannel.MsSmoothGroupSettingsProperty.ConnectionRetryInterval``.
            :param destination: ``CfnChannel.MsSmoothGroupSettingsProperty.Destination``.
            :param event_id: ``CfnChannel.MsSmoothGroupSettingsProperty.EventId``.
            :param event_id_mode: ``CfnChannel.MsSmoothGroupSettingsProperty.EventIdMode``.
            :param event_stop_behavior: ``CfnChannel.MsSmoothGroupSettingsProperty.EventStopBehavior``.
            :param filecache_duration: ``CfnChannel.MsSmoothGroupSettingsProperty.FilecacheDuration``.
            :param fragment_length: ``CfnChannel.MsSmoothGroupSettingsProperty.FragmentLength``.
            :param input_loss_action: ``CfnChannel.MsSmoothGroupSettingsProperty.InputLossAction``.
            :param num_retries: ``CfnChannel.MsSmoothGroupSettingsProperty.NumRetries``.
            :param restart_delay: ``CfnChannel.MsSmoothGroupSettingsProperty.RestartDelay``.
            :param segmentation_mode: ``CfnChannel.MsSmoothGroupSettingsProperty.SegmentationMode``.
            :param send_delay_ms: ``CfnChannel.MsSmoothGroupSettingsProperty.SendDelayMs``.
            :param sparse_track_type: ``CfnChannel.MsSmoothGroupSettingsProperty.SparseTrackType``.
            :param stream_manifest_behavior: ``CfnChannel.MsSmoothGroupSettingsProperty.StreamManifestBehavior``.
            :param timestamp_offset: ``CfnChannel.MsSmoothGroupSettingsProperty.TimestampOffset``.
            :param timestamp_offset_mode: ``CfnChannel.MsSmoothGroupSettingsProperty.TimestampOffsetMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if acquisition_point_id is not None:
                self._values["acquisition_point_id"] = acquisition_point_id
            if audio_only_timecode_control is not None:
                self._values["audio_only_timecode_control"] = audio_only_timecode_control
            if certificate_mode is not None:
                self._values["certificate_mode"] = certificate_mode
            if connection_retry_interval is not None:
                self._values["connection_retry_interval"] = connection_retry_interval
            if destination is not None:
                self._values["destination"] = destination
            if event_id is not None:
                self._values["event_id"] = event_id
            if event_id_mode is not None:
                self._values["event_id_mode"] = event_id_mode
            if event_stop_behavior is not None:
                self._values["event_stop_behavior"] = event_stop_behavior
            if filecache_duration is not None:
                self._values["filecache_duration"] = filecache_duration
            if fragment_length is not None:
                self._values["fragment_length"] = fragment_length
            if input_loss_action is not None:
                self._values["input_loss_action"] = input_loss_action
            if num_retries is not None:
                self._values["num_retries"] = num_retries
            if restart_delay is not None:
                self._values["restart_delay"] = restart_delay
            if segmentation_mode is not None:
                self._values["segmentation_mode"] = segmentation_mode
            if send_delay_ms is not None:
                self._values["send_delay_ms"] = send_delay_ms
            if sparse_track_type is not None:
                self._values["sparse_track_type"] = sparse_track_type
            if stream_manifest_behavior is not None:
                self._values["stream_manifest_behavior"] = stream_manifest_behavior
            if timestamp_offset is not None:
                self._values["timestamp_offset"] = timestamp_offset
            if timestamp_offset_mode is not None:
                self._values["timestamp_offset_mode"] = timestamp_offset_mode

        @builtins.property
        def acquisition_point_id(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.MsSmoothGroupSettingsProperty.AcquisitionPointId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-acquisitionpointid
            """
            result = self._values.get("acquisition_point_id")
            return result

        @builtins.property
        def audio_only_timecode_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.MsSmoothGroupSettingsProperty.AudioOnlyTimecodeControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-audioonlytimecodecontrol
            """
            result = self._values.get("audio_only_timecode_control")
            return result

        @builtins.property
        def certificate_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.MsSmoothGroupSettingsProperty.CertificateMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-certificatemode
            """
            result = self._values.get("certificate_mode")
            return result

        @builtins.property
        def connection_retry_interval(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.MsSmoothGroupSettingsProperty.ConnectionRetryInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-connectionretryinterval
            """
            result = self._values.get("connection_retry_interval")
            return result

        @builtins.property
        def destination(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.OutputLocationRefProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.MsSmoothGroupSettingsProperty.Destination``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-destination
            """
            result = self._values.get("destination")
            return result

        @builtins.property
        def event_id(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.MsSmoothGroupSettingsProperty.EventId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-eventid
            """
            result = self._values.get("event_id")
            return result

        @builtins.property
        def event_id_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.MsSmoothGroupSettingsProperty.EventIdMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-eventidmode
            """
            result = self._values.get("event_id_mode")
            return result

        @builtins.property
        def event_stop_behavior(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.MsSmoothGroupSettingsProperty.EventStopBehavior``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-eventstopbehavior
            """
            result = self._values.get("event_stop_behavior")
            return result

        @builtins.property
        def filecache_duration(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.MsSmoothGroupSettingsProperty.FilecacheDuration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-filecacheduration
            """
            result = self._values.get("filecache_duration")
            return result

        @builtins.property
        def fragment_length(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.MsSmoothGroupSettingsProperty.FragmentLength``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-fragmentlength
            """
            result = self._values.get("fragment_length")
            return result

        @builtins.property
        def input_loss_action(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.MsSmoothGroupSettingsProperty.InputLossAction``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-inputlossaction
            """
            result = self._values.get("input_loss_action")
            return result

        @builtins.property
        def num_retries(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.MsSmoothGroupSettingsProperty.NumRetries``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-numretries
            """
            result = self._values.get("num_retries")
            return result

        @builtins.property
        def restart_delay(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.MsSmoothGroupSettingsProperty.RestartDelay``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-restartdelay
            """
            result = self._values.get("restart_delay")
            return result

        @builtins.property
        def segmentation_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.MsSmoothGroupSettingsProperty.SegmentationMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-segmentationmode
            """
            result = self._values.get("segmentation_mode")
            return result

        @builtins.property
        def send_delay_ms(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.MsSmoothGroupSettingsProperty.SendDelayMs``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-senddelayms
            """
            result = self._values.get("send_delay_ms")
            return result

        @builtins.property
        def sparse_track_type(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.MsSmoothGroupSettingsProperty.SparseTrackType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-sparsetracktype
            """
            result = self._values.get("sparse_track_type")
            return result

        @builtins.property
        def stream_manifest_behavior(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.MsSmoothGroupSettingsProperty.StreamManifestBehavior``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-streammanifestbehavior
            """
            result = self._values.get("stream_manifest_behavior")
            return result

        @builtins.property
        def timestamp_offset(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.MsSmoothGroupSettingsProperty.TimestampOffset``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-timestampoffset
            """
            result = self._values.get("timestamp_offset")
            return result

        @builtins.property
        def timestamp_offset_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.MsSmoothGroupSettingsProperty.TimestampOffsetMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-timestampoffsetmode
            """
            result = self._values.get("timestamp_offset_mode")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MsSmoothGroupSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.MsSmoothOutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "h265_packaging_type": "h265PackagingType",
            "name_modifier": "nameModifier",
        },
    )
    class MsSmoothOutputSettingsProperty:
        def __init__(
            self,
            *,
            h265_packaging_type: typing.Optional[builtins.str] = None,
            name_modifier: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param h265_packaging_type: ``CfnChannel.MsSmoothOutputSettingsProperty.H265PackagingType``.
            :param name_modifier: ``CfnChannel.MsSmoothOutputSettingsProperty.NameModifier``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothoutputsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if h265_packaging_type is not None:
                self._values["h265_packaging_type"] = h265_packaging_type
            if name_modifier is not None:
                self._values["name_modifier"] = name_modifier

        @builtins.property
        def h265_packaging_type(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.MsSmoothOutputSettingsProperty.H265PackagingType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothoutputsettings.html#cfn-medialive-channel-mssmoothoutputsettings-h265packagingtype
            """
            result = self._values.get("h265_packaging_type")
            return result

        @builtins.property
        def name_modifier(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.MsSmoothOutputSettingsProperty.NameModifier``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothoutputsettings.html#cfn-medialive-channel-mssmoothoutputsettings-namemodifier
            """
            result = self._values.get("name_modifier")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MsSmoothOutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.MultiplexGroupSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class MultiplexGroupSettingsProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexgroupsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MultiplexGroupSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.MultiplexOutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination"},
    )
    class MultiplexOutputSettingsProperty:
        def __init__(
            self,
            *,
            destination: typing.Optional[typing.Union["CfnChannel.OutputLocationRefProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param destination: ``CfnChannel.MultiplexOutputSettingsProperty.Destination``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexoutputsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if destination is not None:
                self._values["destination"] = destination

        @builtins.property
        def destination(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.OutputLocationRefProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.MultiplexOutputSettingsProperty.Destination``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexoutputsettings.html#cfn-medialive-channel-multiplexoutputsettings-destination
            """
            result = self._values.get("destination")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MultiplexOutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.MultiplexProgramChannelDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"multiplex_id": "multiplexId", "program_name": "programName"},
    )
    class MultiplexProgramChannelDestinationSettingsProperty:
        def __init__(
            self,
            *,
            multiplex_id: typing.Optional[builtins.str] = None,
            program_name: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param multiplex_id: ``CfnChannel.MultiplexProgramChannelDestinationSettingsProperty.MultiplexId``.
            :param program_name: ``CfnChannel.MultiplexProgramChannelDestinationSettingsProperty.ProgramName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if multiplex_id is not None:
                self._values["multiplex_id"] = multiplex_id
            if program_name is not None:
                self._values["program_name"] = program_name

        @builtins.property
        def multiplex_id(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.MultiplexProgramChannelDestinationSettingsProperty.MultiplexId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html#cfn-medialive-channel-multiplexprogramchanneldestinationsettings-multiplexid
            """
            result = self._values.get("multiplex_id")
            return result

        @builtins.property
        def program_name(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.MultiplexProgramChannelDestinationSettingsProperty.ProgramName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html#cfn-medialive-channel-multiplexprogramchanneldestinationsettings-programname
            """
            result = self._values.get("program_name")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MultiplexProgramChannelDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.NetworkInputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hls_input_settings": "hlsInputSettings",
            "server_validation": "serverValidation",
        },
    )
    class NetworkInputSettingsProperty:
        def __init__(
            self,
            *,
            hls_input_settings: typing.Optional[typing.Union["CfnChannel.HlsInputSettingsProperty", _IResolvable_a771d0ef]] = None,
            server_validation: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param hls_input_settings: ``CfnChannel.NetworkInputSettingsProperty.HlsInputSettings``.
            :param server_validation: ``CfnChannel.NetworkInputSettingsProperty.ServerValidation``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-networkinputsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if hls_input_settings is not None:
                self._values["hls_input_settings"] = hls_input_settings
            if server_validation is not None:
                self._values["server_validation"] = server_validation

        @builtins.property
        def hls_input_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.HlsInputSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.NetworkInputSettingsProperty.HlsInputSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-networkinputsettings.html#cfn-medialive-channel-networkinputsettings-hlsinputsettings
            """
            result = self._values.get("hls_input_settings")
            return result

        @builtins.property
        def server_validation(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.NetworkInputSettingsProperty.ServerValidation``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-networkinputsettings.html#cfn-medialive-channel-networkinputsettings-servervalidation
            """
            result = self._values.get("server_validation")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkInputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.NielsenConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "distributor_id": "distributorId",
            "nielsen_pcm_to_id3_tagging": "nielsenPcmToId3Tagging",
        },
    )
    class NielsenConfigurationProperty:
        def __init__(
            self,
            *,
            distributor_id: typing.Optional[builtins.str] = None,
            nielsen_pcm_to_id3_tagging: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param distributor_id: ``CfnChannel.NielsenConfigurationProperty.DistributorId``.
            :param nielsen_pcm_to_id3_tagging: ``CfnChannel.NielsenConfigurationProperty.NielsenPcmToId3Tagging``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if distributor_id is not None:
                self._values["distributor_id"] = distributor_id
            if nielsen_pcm_to_id3_tagging is not None:
                self._values["nielsen_pcm_to_id3_tagging"] = nielsen_pcm_to_id3_tagging

        @builtins.property
        def distributor_id(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.NielsenConfigurationProperty.DistributorId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenconfiguration.html#cfn-medialive-channel-nielsenconfiguration-distributorid
            """
            result = self._values.get("distributor_id")
            return result

        @builtins.property
        def nielsen_pcm_to_id3_tagging(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.NielsenConfigurationProperty.NielsenPcmToId3Tagging``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenconfiguration.html#cfn-medialive-channel-nielsenconfiguration-nielsenpcmtoid3tagging
            """
            result = self._values.get("nielsen_pcm_to_id3_tagging")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NielsenConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.OutputDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id": "id",
            "media_package_settings": "mediaPackageSettings",
            "multiplex_settings": "multiplexSettings",
            "settings": "settings",
        },
    )
    class OutputDestinationProperty:
        def __init__(
            self,
            *,
            id: typing.Optional[builtins.str] = None,
            media_package_settings: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.MediaPackageOutputDestinationSettingsProperty", _IResolvable_a771d0ef]]]] = None,
            multiplex_settings: typing.Optional[typing.Union["CfnChannel.MultiplexProgramChannelDestinationSettingsProperty", _IResolvable_a771d0ef]] = None,
            settings: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.OutputDestinationSettingsProperty", _IResolvable_a771d0ef]]]] = None,
        ) -> None:
            """
            :param id: ``CfnChannel.OutputDestinationProperty.Id``.
            :param media_package_settings: ``CfnChannel.OutputDestinationProperty.MediaPackageSettings``.
            :param multiplex_settings: ``CfnChannel.OutputDestinationProperty.MultiplexSettings``.
            :param settings: ``CfnChannel.OutputDestinationProperty.Settings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestination.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if id is not None:
                self._values["id"] = id
            if media_package_settings is not None:
                self._values["media_package_settings"] = media_package_settings
            if multiplex_settings is not None:
                self._values["multiplex_settings"] = multiplex_settings
            if settings is not None:
                self._values["settings"] = settings

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.OutputDestinationProperty.Id``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestination.html#cfn-medialive-channel-outputdestination-id
            """
            result = self._values.get("id")
            return result

        @builtins.property
        def media_package_settings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.MediaPackageOutputDestinationSettingsProperty", _IResolvable_a771d0ef]]]]:
            """``CfnChannel.OutputDestinationProperty.MediaPackageSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestination.html#cfn-medialive-channel-outputdestination-mediapackagesettings
            """
            result = self._values.get("media_package_settings")
            return result

        @builtins.property
        def multiplex_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.MultiplexProgramChannelDestinationSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.OutputDestinationProperty.MultiplexSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestination.html#cfn-medialive-channel-outputdestination-multiplexsettings
            """
            result = self._values.get("multiplex_settings")
            return result

        @builtins.property
        def settings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.OutputDestinationSettingsProperty", _IResolvable_a771d0ef]]]]:
            """``CfnChannel.OutputDestinationProperty.Settings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestination.html#cfn-medialive-channel-outputdestination-settings
            """
            result = self._values.get("settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.OutputDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "password_param": "passwordParam",
            "stream_name": "streamName",
            "url": "url",
            "username": "username",
        },
    )
    class OutputDestinationSettingsProperty:
        def __init__(
            self,
            *,
            password_param: typing.Optional[builtins.str] = None,
            stream_name: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param password_param: ``CfnChannel.OutputDestinationSettingsProperty.PasswordParam``.
            :param stream_name: ``CfnChannel.OutputDestinationSettingsProperty.StreamName``.
            :param url: ``CfnChannel.OutputDestinationSettingsProperty.Url``.
            :param username: ``CfnChannel.OutputDestinationSettingsProperty.Username``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestinationsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if password_param is not None:
                self._values["password_param"] = password_param
            if stream_name is not None:
                self._values["stream_name"] = stream_name
            if url is not None:
                self._values["url"] = url
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def password_param(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.OutputDestinationSettingsProperty.PasswordParam``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestinationsettings.html#cfn-medialive-channel-outputdestinationsettings-passwordparam
            """
            result = self._values.get("password_param")
            return result

        @builtins.property
        def stream_name(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.OutputDestinationSettingsProperty.StreamName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestinationsettings.html#cfn-medialive-channel-outputdestinationsettings-streamname
            """
            result = self._values.get("stream_name")
            return result

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.OutputDestinationSettingsProperty.Url``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestinationsettings.html#cfn-medialive-channel-outputdestinationsettings-url
            """
            result = self._values.get("url")
            return result

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.OutputDestinationSettingsProperty.Username``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestinationsettings.html#cfn-medialive-channel-outputdestinationsettings-username
            """
            result = self._values.get("username")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.OutputGroupProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "output_group_settings": "outputGroupSettings",
            "outputs": "outputs",
        },
    )
    class OutputGroupProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            output_group_settings: typing.Optional[typing.Union["CfnChannel.OutputGroupSettingsProperty", _IResolvable_a771d0ef]] = None,
            outputs: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.OutputProperty", _IResolvable_a771d0ef]]]] = None,
        ) -> None:
            """
            :param name: ``CfnChannel.OutputGroupProperty.Name``.
            :param output_group_settings: ``CfnChannel.OutputGroupProperty.OutputGroupSettings``.
            :param outputs: ``CfnChannel.OutputGroupProperty.Outputs``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroup.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if output_group_settings is not None:
                self._values["output_group_settings"] = output_group_settings
            if outputs is not None:
                self._values["outputs"] = outputs

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.OutputGroupProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroup.html#cfn-medialive-channel-outputgroup-name
            """
            result = self._values.get("name")
            return result

        @builtins.property
        def output_group_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.OutputGroupSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.OutputGroupProperty.OutputGroupSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroup.html#cfn-medialive-channel-outputgroup-outputgroupsettings
            """
            result = self._values.get("output_group_settings")
            return result

        @builtins.property
        def outputs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.OutputProperty", _IResolvable_a771d0ef]]]]:
            """``CfnChannel.OutputGroupProperty.Outputs``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroup.html#cfn-medialive-channel-outputgroup-outputs
            """
            result = self._values.get("outputs")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.OutputGroupSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "archive_group_settings": "archiveGroupSettings",
            "frame_capture_group_settings": "frameCaptureGroupSettings",
            "hls_group_settings": "hlsGroupSettings",
            "media_package_group_settings": "mediaPackageGroupSettings",
            "ms_smooth_group_settings": "msSmoothGroupSettings",
            "multiplex_group_settings": "multiplexGroupSettings",
            "rtmp_group_settings": "rtmpGroupSettings",
            "udp_group_settings": "udpGroupSettings",
        },
    )
    class OutputGroupSettingsProperty:
        def __init__(
            self,
            *,
            archive_group_settings: typing.Optional[typing.Union["CfnChannel.ArchiveGroupSettingsProperty", _IResolvable_a771d0ef]] = None,
            frame_capture_group_settings: typing.Optional[typing.Union["CfnChannel.FrameCaptureGroupSettingsProperty", _IResolvable_a771d0ef]] = None,
            hls_group_settings: typing.Optional[typing.Union["CfnChannel.HlsGroupSettingsProperty", _IResolvable_a771d0ef]] = None,
            media_package_group_settings: typing.Optional[typing.Union["CfnChannel.MediaPackageGroupSettingsProperty", _IResolvable_a771d0ef]] = None,
            ms_smooth_group_settings: typing.Optional[typing.Union["CfnChannel.MsSmoothGroupSettingsProperty", _IResolvable_a771d0ef]] = None,
            multiplex_group_settings: typing.Optional[typing.Union["CfnChannel.MultiplexGroupSettingsProperty", _IResolvable_a771d0ef]] = None,
            rtmp_group_settings: typing.Optional[typing.Union["CfnChannel.RtmpGroupSettingsProperty", _IResolvable_a771d0ef]] = None,
            udp_group_settings: typing.Optional[typing.Union["CfnChannel.UdpGroupSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param archive_group_settings: ``CfnChannel.OutputGroupSettingsProperty.ArchiveGroupSettings``.
            :param frame_capture_group_settings: ``CfnChannel.OutputGroupSettingsProperty.FrameCaptureGroupSettings``.
            :param hls_group_settings: ``CfnChannel.OutputGroupSettingsProperty.HlsGroupSettings``.
            :param media_package_group_settings: ``CfnChannel.OutputGroupSettingsProperty.MediaPackageGroupSettings``.
            :param ms_smooth_group_settings: ``CfnChannel.OutputGroupSettingsProperty.MsSmoothGroupSettings``.
            :param multiplex_group_settings: ``CfnChannel.OutputGroupSettingsProperty.MultiplexGroupSettings``.
            :param rtmp_group_settings: ``CfnChannel.OutputGroupSettingsProperty.RtmpGroupSettings``.
            :param udp_group_settings: ``CfnChannel.OutputGroupSettingsProperty.UdpGroupSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if archive_group_settings is not None:
                self._values["archive_group_settings"] = archive_group_settings
            if frame_capture_group_settings is not None:
                self._values["frame_capture_group_settings"] = frame_capture_group_settings
            if hls_group_settings is not None:
                self._values["hls_group_settings"] = hls_group_settings
            if media_package_group_settings is not None:
                self._values["media_package_group_settings"] = media_package_group_settings
            if ms_smooth_group_settings is not None:
                self._values["ms_smooth_group_settings"] = ms_smooth_group_settings
            if multiplex_group_settings is not None:
                self._values["multiplex_group_settings"] = multiplex_group_settings
            if rtmp_group_settings is not None:
                self._values["rtmp_group_settings"] = rtmp_group_settings
            if udp_group_settings is not None:
                self._values["udp_group_settings"] = udp_group_settings

        @builtins.property
        def archive_group_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.ArchiveGroupSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.OutputGroupSettingsProperty.ArchiveGroupSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-archivegroupsettings
            """
            result = self._values.get("archive_group_settings")
            return result

        @builtins.property
        def frame_capture_group_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.FrameCaptureGroupSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.OutputGroupSettingsProperty.FrameCaptureGroupSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-framecapturegroupsettings
            """
            result = self._values.get("frame_capture_group_settings")
            return result

        @builtins.property
        def hls_group_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.HlsGroupSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.OutputGroupSettingsProperty.HlsGroupSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-hlsgroupsettings
            """
            result = self._values.get("hls_group_settings")
            return result

        @builtins.property
        def media_package_group_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.MediaPackageGroupSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.OutputGroupSettingsProperty.MediaPackageGroupSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-mediapackagegroupsettings
            """
            result = self._values.get("media_package_group_settings")
            return result

        @builtins.property
        def ms_smooth_group_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.MsSmoothGroupSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.OutputGroupSettingsProperty.MsSmoothGroupSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-mssmoothgroupsettings
            """
            result = self._values.get("ms_smooth_group_settings")
            return result

        @builtins.property
        def multiplex_group_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.MultiplexGroupSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.OutputGroupSettingsProperty.MultiplexGroupSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-multiplexgroupsettings
            """
            result = self._values.get("multiplex_group_settings")
            return result

        @builtins.property
        def rtmp_group_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.RtmpGroupSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.OutputGroupSettingsProperty.RtmpGroupSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-rtmpgroupsettings
            """
            result = self._values.get("rtmp_group_settings")
            return result

        @builtins.property
        def udp_group_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.UdpGroupSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.OutputGroupSettingsProperty.UdpGroupSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-udpgroupsettings
            """
            result = self._values.get("udp_group_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputGroupSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.OutputLocationRefProperty",
        jsii_struct_bases=[],
        name_mapping={"destination_ref_id": "destinationRefId"},
    )
    class OutputLocationRefProperty:
        def __init__(
            self,
            *,
            destination_ref_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param destination_ref_id: ``CfnChannel.OutputLocationRefProperty.DestinationRefId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputlocationref.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if destination_ref_id is not None:
                self._values["destination_ref_id"] = destination_ref_id

        @builtins.property
        def destination_ref_id(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.OutputLocationRefProperty.DestinationRefId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputlocationref.html#cfn-medialive-channel-outputlocationref-destinationrefid
            """
            result = self._values.get("destination_ref_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputLocationRefProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_description_names": "audioDescriptionNames",
            "caption_description_names": "captionDescriptionNames",
            "output_name": "outputName",
            "output_settings": "outputSettings",
            "video_description_name": "videoDescriptionName",
        },
    )
    class OutputProperty:
        def __init__(
            self,
            *,
            audio_description_names: typing.Optional[typing.List[builtins.str]] = None,
            caption_description_names: typing.Optional[typing.List[builtins.str]] = None,
            output_name: typing.Optional[builtins.str] = None,
            output_settings: typing.Optional[typing.Union["CfnChannel.OutputSettingsProperty", _IResolvable_a771d0ef]] = None,
            video_description_name: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param audio_description_names: ``CfnChannel.OutputProperty.AudioDescriptionNames``.
            :param caption_description_names: ``CfnChannel.OutputProperty.CaptionDescriptionNames``.
            :param output_name: ``CfnChannel.OutputProperty.OutputName``.
            :param output_settings: ``CfnChannel.OutputProperty.OutputSettings``.
            :param video_description_name: ``CfnChannel.OutputProperty.VideoDescriptionName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_description_names is not None:
                self._values["audio_description_names"] = audio_description_names
            if caption_description_names is not None:
                self._values["caption_description_names"] = caption_description_names
            if output_name is not None:
                self._values["output_name"] = output_name
            if output_settings is not None:
                self._values["output_settings"] = output_settings
            if video_description_name is not None:
                self._values["video_description_name"] = video_description_name

        @builtins.property
        def audio_description_names(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnChannel.OutputProperty.AudioDescriptionNames``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html#cfn-medialive-channel-output-audiodescriptionnames
            """
            result = self._values.get("audio_description_names")
            return result

        @builtins.property
        def caption_description_names(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnChannel.OutputProperty.CaptionDescriptionNames``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html#cfn-medialive-channel-output-captiondescriptionnames
            """
            result = self._values.get("caption_description_names")
            return result

        @builtins.property
        def output_name(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.OutputProperty.OutputName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html#cfn-medialive-channel-output-outputname
            """
            result = self._values.get("output_name")
            return result

        @builtins.property
        def output_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.OutputSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.OutputProperty.OutputSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html#cfn-medialive-channel-output-outputsettings
            """
            result = self._values.get("output_settings")
            return result

        @builtins.property
        def video_description_name(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.OutputProperty.VideoDescriptionName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html#cfn-medialive-channel-output-videodescriptionname
            """
            result = self._values.get("video_description_name")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.OutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "archive_output_settings": "archiveOutputSettings",
            "frame_capture_output_settings": "frameCaptureOutputSettings",
            "hls_output_settings": "hlsOutputSettings",
            "media_package_output_settings": "mediaPackageOutputSettings",
            "ms_smooth_output_settings": "msSmoothOutputSettings",
            "multiplex_output_settings": "multiplexOutputSettings",
            "rtmp_output_settings": "rtmpOutputSettings",
            "udp_output_settings": "udpOutputSettings",
        },
    )
    class OutputSettingsProperty:
        def __init__(
            self,
            *,
            archive_output_settings: typing.Optional[typing.Union["CfnChannel.ArchiveOutputSettingsProperty", _IResolvable_a771d0ef]] = None,
            frame_capture_output_settings: typing.Optional[typing.Union["CfnChannel.FrameCaptureOutputSettingsProperty", _IResolvable_a771d0ef]] = None,
            hls_output_settings: typing.Optional[typing.Union["CfnChannel.HlsOutputSettingsProperty", _IResolvable_a771d0ef]] = None,
            media_package_output_settings: typing.Optional[typing.Union["CfnChannel.MediaPackageOutputSettingsProperty", _IResolvable_a771d0ef]] = None,
            ms_smooth_output_settings: typing.Optional[typing.Union["CfnChannel.MsSmoothOutputSettingsProperty", _IResolvable_a771d0ef]] = None,
            multiplex_output_settings: typing.Optional[typing.Union["CfnChannel.MultiplexOutputSettingsProperty", _IResolvable_a771d0ef]] = None,
            rtmp_output_settings: typing.Optional[typing.Union["CfnChannel.RtmpOutputSettingsProperty", _IResolvable_a771d0ef]] = None,
            udp_output_settings: typing.Optional[typing.Union["CfnChannel.UdpOutputSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param archive_output_settings: ``CfnChannel.OutputSettingsProperty.ArchiveOutputSettings``.
            :param frame_capture_output_settings: ``CfnChannel.OutputSettingsProperty.FrameCaptureOutputSettings``.
            :param hls_output_settings: ``CfnChannel.OutputSettingsProperty.HlsOutputSettings``.
            :param media_package_output_settings: ``CfnChannel.OutputSettingsProperty.MediaPackageOutputSettings``.
            :param ms_smooth_output_settings: ``CfnChannel.OutputSettingsProperty.MsSmoothOutputSettings``.
            :param multiplex_output_settings: ``CfnChannel.OutputSettingsProperty.MultiplexOutputSettings``.
            :param rtmp_output_settings: ``CfnChannel.OutputSettingsProperty.RtmpOutputSettings``.
            :param udp_output_settings: ``CfnChannel.OutputSettingsProperty.UdpOutputSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if archive_output_settings is not None:
                self._values["archive_output_settings"] = archive_output_settings
            if frame_capture_output_settings is not None:
                self._values["frame_capture_output_settings"] = frame_capture_output_settings
            if hls_output_settings is not None:
                self._values["hls_output_settings"] = hls_output_settings
            if media_package_output_settings is not None:
                self._values["media_package_output_settings"] = media_package_output_settings
            if ms_smooth_output_settings is not None:
                self._values["ms_smooth_output_settings"] = ms_smooth_output_settings
            if multiplex_output_settings is not None:
                self._values["multiplex_output_settings"] = multiplex_output_settings
            if rtmp_output_settings is not None:
                self._values["rtmp_output_settings"] = rtmp_output_settings
            if udp_output_settings is not None:
                self._values["udp_output_settings"] = udp_output_settings

        @builtins.property
        def archive_output_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.ArchiveOutputSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.OutputSettingsProperty.ArchiveOutputSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-archiveoutputsettings
            """
            result = self._values.get("archive_output_settings")
            return result

        @builtins.property
        def frame_capture_output_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.FrameCaptureOutputSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.OutputSettingsProperty.FrameCaptureOutputSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-framecaptureoutputsettings
            """
            result = self._values.get("frame_capture_output_settings")
            return result

        @builtins.property
        def hls_output_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.HlsOutputSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.OutputSettingsProperty.HlsOutputSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-hlsoutputsettings
            """
            result = self._values.get("hls_output_settings")
            return result

        @builtins.property
        def media_package_output_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.MediaPackageOutputSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.OutputSettingsProperty.MediaPackageOutputSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-mediapackageoutputsettings
            """
            result = self._values.get("media_package_output_settings")
            return result

        @builtins.property
        def ms_smooth_output_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.MsSmoothOutputSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.OutputSettingsProperty.MsSmoothOutputSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-mssmoothoutputsettings
            """
            result = self._values.get("ms_smooth_output_settings")
            return result

        @builtins.property
        def multiplex_output_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.MultiplexOutputSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.OutputSettingsProperty.MultiplexOutputSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-multiplexoutputsettings
            """
            result = self._values.get("multiplex_output_settings")
            return result

        @builtins.property
        def rtmp_output_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.RtmpOutputSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.OutputSettingsProperty.RtmpOutputSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-rtmpoutputsettings
            """
            result = self._values.get("rtmp_output_settings")
            return result

        @builtins.property
        def udp_output_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.UdpOutputSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.OutputSettingsProperty.UdpOutputSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-udpoutputsettings
            """
            result = self._values.get("udp_output_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.PassThroughSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class PassThroughSettingsProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-passthroughsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PassThroughSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.Rec601SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class Rec601SettingsProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rec601settings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Rec601SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.Rec709SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class Rec709SettingsProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rec709settings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Rec709SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.RemixSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "channel_mappings": "channelMappings",
            "channels_in": "channelsIn",
            "channels_out": "channelsOut",
        },
    )
    class RemixSettingsProperty:
        def __init__(
            self,
            *,
            channel_mappings: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.AudioChannelMappingProperty", _IResolvable_a771d0ef]]]] = None,
            channels_in: typing.Optional[jsii.Number] = None,
            channels_out: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param channel_mappings: ``CfnChannel.RemixSettingsProperty.ChannelMappings``.
            :param channels_in: ``CfnChannel.RemixSettingsProperty.ChannelsIn``.
            :param channels_out: ``CfnChannel.RemixSettingsProperty.ChannelsOut``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-remixsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if channel_mappings is not None:
                self._values["channel_mappings"] = channel_mappings
            if channels_in is not None:
                self._values["channels_in"] = channels_in
            if channels_out is not None:
                self._values["channels_out"] = channels_out

        @builtins.property
        def channel_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnChannel.AudioChannelMappingProperty", _IResolvable_a771d0ef]]]]:
            """``CfnChannel.RemixSettingsProperty.ChannelMappings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-remixsettings.html#cfn-medialive-channel-remixsettings-channelmappings
            """
            result = self._values.get("channel_mappings")
            return result

        @builtins.property
        def channels_in(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.RemixSettingsProperty.ChannelsIn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-remixsettings.html#cfn-medialive-channel-remixsettings-channelsin
            """
            result = self._values.get("channels_in")
            return result

        @builtins.property
        def channels_out(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.RemixSettingsProperty.ChannelsOut``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-remixsettings.html#cfn-medialive-channel-remixsettings-channelsout
            """
            result = self._values.get("channels_out")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RemixSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.RtmpCaptionInfoDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class RtmpCaptionInfoDestinationSettingsProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpcaptioninfodestinationsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RtmpCaptionInfoDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.RtmpGroupSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authentication_scheme": "authenticationScheme",
            "cache_full_behavior": "cacheFullBehavior",
            "cache_length": "cacheLength",
            "caption_data": "captionData",
            "input_loss_action": "inputLossAction",
            "restart_delay": "restartDelay",
        },
    )
    class RtmpGroupSettingsProperty:
        def __init__(
            self,
            *,
            authentication_scheme: typing.Optional[builtins.str] = None,
            cache_full_behavior: typing.Optional[builtins.str] = None,
            cache_length: typing.Optional[jsii.Number] = None,
            caption_data: typing.Optional[builtins.str] = None,
            input_loss_action: typing.Optional[builtins.str] = None,
            restart_delay: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param authentication_scheme: ``CfnChannel.RtmpGroupSettingsProperty.AuthenticationScheme``.
            :param cache_full_behavior: ``CfnChannel.RtmpGroupSettingsProperty.CacheFullBehavior``.
            :param cache_length: ``CfnChannel.RtmpGroupSettingsProperty.CacheLength``.
            :param caption_data: ``CfnChannel.RtmpGroupSettingsProperty.CaptionData``.
            :param input_loss_action: ``CfnChannel.RtmpGroupSettingsProperty.InputLossAction``.
            :param restart_delay: ``CfnChannel.RtmpGroupSettingsProperty.RestartDelay``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if authentication_scheme is not None:
                self._values["authentication_scheme"] = authentication_scheme
            if cache_full_behavior is not None:
                self._values["cache_full_behavior"] = cache_full_behavior
            if cache_length is not None:
                self._values["cache_length"] = cache_length
            if caption_data is not None:
                self._values["caption_data"] = caption_data
            if input_loss_action is not None:
                self._values["input_loss_action"] = input_loss_action
            if restart_delay is not None:
                self._values["restart_delay"] = restart_delay

        @builtins.property
        def authentication_scheme(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.RtmpGroupSettingsProperty.AuthenticationScheme``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-authenticationscheme
            """
            result = self._values.get("authentication_scheme")
            return result

        @builtins.property
        def cache_full_behavior(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.RtmpGroupSettingsProperty.CacheFullBehavior``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-cachefullbehavior
            """
            result = self._values.get("cache_full_behavior")
            return result

        @builtins.property
        def cache_length(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.RtmpGroupSettingsProperty.CacheLength``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-cachelength
            """
            result = self._values.get("cache_length")
            return result

        @builtins.property
        def caption_data(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.RtmpGroupSettingsProperty.CaptionData``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-captiondata
            """
            result = self._values.get("caption_data")
            return result

        @builtins.property
        def input_loss_action(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.RtmpGroupSettingsProperty.InputLossAction``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-inputlossaction
            """
            result = self._values.get("input_loss_action")
            return result

        @builtins.property
        def restart_delay(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.RtmpGroupSettingsProperty.RestartDelay``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-restartdelay
            """
            result = self._values.get("restart_delay")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RtmpGroupSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.RtmpOutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_mode": "certificateMode",
            "connection_retry_interval": "connectionRetryInterval",
            "destination": "destination",
            "num_retries": "numRetries",
        },
    )
    class RtmpOutputSettingsProperty:
        def __init__(
            self,
            *,
            certificate_mode: typing.Optional[builtins.str] = None,
            connection_retry_interval: typing.Optional[jsii.Number] = None,
            destination: typing.Optional[typing.Union["CfnChannel.OutputLocationRefProperty", _IResolvable_a771d0ef]] = None,
            num_retries: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param certificate_mode: ``CfnChannel.RtmpOutputSettingsProperty.CertificateMode``.
            :param connection_retry_interval: ``CfnChannel.RtmpOutputSettingsProperty.ConnectionRetryInterval``.
            :param destination: ``CfnChannel.RtmpOutputSettingsProperty.Destination``.
            :param num_retries: ``CfnChannel.RtmpOutputSettingsProperty.NumRetries``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if certificate_mode is not None:
                self._values["certificate_mode"] = certificate_mode
            if connection_retry_interval is not None:
                self._values["connection_retry_interval"] = connection_retry_interval
            if destination is not None:
                self._values["destination"] = destination
            if num_retries is not None:
                self._values["num_retries"] = num_retries

        @builtins.property
        def certificate_mode(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.RtmpOutputSettingsProperty.CertificateMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html#cfn-medialive-channel-rtmpoutputsettings-certificatemode
            """
            result = self._values.get("certificate_mode")
            return result

        @builtins.property
        def connection_retry_interval(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.RtmpOutputSettingsProperty.ConnectionRetryInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html#cfn-medialive-channel-rtmpoutputsettings-connectionretryinterval
            """
            result = self._values.get("connection_retry_interval")
            return result

        @builtins.property
        def destination(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.OutputLocationRefProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.RtmpOutputSettingsProperty.Destination``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html#cfn-medialive-channel-rtmpoutputsettings-destination
            """
            result = self._values.get("destination")
            return result

        @builtins.property
        def num_retries(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.RtmpOutputSettingsProperty.NumRetries``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html#cfn-medialive-channel-rtmpoutputsettings-numretries
            """
            result = self._values.get("num_retries")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RtmpOutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.Scte20PlusEmbeddedDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class Scte20PlusEmbeddedDestinationSettingsProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20plusembeddeddestinationsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Scte20PlusEmbeddedDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.Scte20SourceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "convert608_to708": "convert608To708",
            "source608_channel_number": "source608ChannelNumber",
        },
    )
    class Scte20SourceSettingsProperty:
        def __init__(
            self,
            *,
            convert608_to708: typing.Optional[builtins.str] = None,
            source608_channel_number: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param convert608_to708: ``CfnChannel.Scte20SourceSettingsProperty.Convert608To708``.
            :param source608_channel_number: ``CfnChannel.Scte20SourceSettingsProperty.Source608ChannelNumber``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20sourcesettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if convert608_to708 is not None:
                self._values["convert608_to708"] = convert608_to708
            if source608_channel_number is not None:
                self._values["source608_channel_number"] = source608_channel_number

        @builtins.property
        def convert608_to708(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Scte20SourceSettingsProperty.Convert608To708``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20sourcesettings.html#cfn-medialive-channel-scte20sourcesettings-convert608to708
            """
            result = self._values.get("convert608_to708")
            return result

        @builtins.property
        def source608_channel_number(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.Scte20SourceSettingsProperty.Source608ChannelNumber``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20sourcesettings.html#cfn-medialive-channel-scte20sourcesettings-source608channelnumber
            """
            result = self._values.get("source608_channel_number")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Scte20SourceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.Scte27DestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class Scte27DestinationSettingsProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte27destinationsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Scte27DestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.Scte27SourceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"pid": "pid"},
    )
    class Scte27SourceSettingsProperty:
        def __init__(self, *, pid: typing.Optional[jsii.Number] = None) -> None:
            """
            :param pid: ``CfnChannel.Scte27SourceSettingsProperty.Pid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte27sourcesettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if pid is not None:
                self._values["pid"] = pid

        @builtins.property
        def pid(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.Scte27SourceSettingsProperty.Pid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte27sourcesettings.html#cfn-medialive-channel-scte27sourcesettings-pid
            """
            result = self._values.get("pid")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Scte27SourceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.Scte35SpliceInsertProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ad_avail_offset": "adAvailOffset",
            "no_regional_blackout_flag": "noRegionalBlackoutFlag",
            "web_delivery_allowed_flag": "webDeliveryAllowedFlag",
        },
    )
    class Scte35SpliceInsertProperty:
        def __init__(
            self,
            *,
            ad_avail_offset: typing.Optional[jsii.Number] = None,
            no_regional_blackout_flag: typing.Optional[builtins.str] = None,
            web_delivery_allowed_flag: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param ad_avail_offset: ``CfnChannel.Scte35SpliceInsertProperty.AdAvailOffset``.
            :param no_regional_blackout_flag: ``CfnChannel.Scte35SpliceInsertProperty.NoRegionalBlackoutFlag``.
            :param web_delivery_allowed_flag: ``CfnChannel.Scte35SpliceInsertProperty.WebDeliveryAllowedFlag``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35spliceinsert.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if ad_avail_offset is not None:
                self._values["ad_avail_offset"] = ad_avail_offset
            if no_regional_blackout_flag is not None:
                self._values["no_regional_blackout_flag"] = no_regional_blackout_flag
            if web_delivery_allowed_flag is not None:
                self._values["web_delivery_allowed_flag"] = web_delivery_allowed_flag

        @builtins.property
        def ad_avail_offset(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.Scte35SpliceInsertProperty.AdAvailOffset``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35spliceinsert.html#cfn-medialive-channel-scte35spliceinsert-adavailoffset
            """
            result = self._values.get("ad_avail_offset")
            return result

        @builtins.property
        def no_regional_blackout_flag(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Scte35SpliceInsertProperty.NoRegionalBlackoutFlag``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35spliceinsert.html#cfn-medialive-channel-scte35spliceinsert-noregionalblackoutflag
            """
            result = self._values.get("no_regional_blackout_flag")
            return result

        @builtins.property
        def web_delivery_allowed_flag(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Scte35SpliceInsertProperty.WebDeliveryAllowedFlag``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35spliceinsert.html#cfn-medialive-channel-scte35spliceinsert-webdeliveryallowedflag
            """
            result = self._values.get("web_delivery_allowed_flag")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Scte35SpliceInsertProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.Scte35TimeSignalAposProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ad_avail_offset": "adAvailOffset",
            "no_regional_blackout_flag": "noRegionalBlackoutFlag",
            "web_delivery_allowed_flag": "webDeliveryAllowedFlag",
        },
    )
    class Scte35TimeSignalAposProperty:
        def __init__(
            self,
            *,
            ad_avail_offset: typing.Optional[jsii.Number] = None,
            no_regional_blackout_flag: typing.Optional[builtins.str] = None,
            web_delivery_allowed_flag: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param ad_avail_offset: ``CfnChannel.Scte35TimeSignalAposProperty.AdAvailOffset``.
            :param no_regional_blackout_flag: ``CfnChannel.Scte35TimeSignalAposProperty.NoRegionalBlackoutFlag``.
            :param web_delivery_allowed_flag: ``CfnChannel.Scte35TimeSignalAposProperty.WebDeliveryAllowedFlag``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35timesignalapos.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if ad_avail_offset is not None:
                self._values["ad_avail_offset"] = ad_avail_offset
            if no_regional_blackout_flag is not None:
                self._values["no_regional_blackout_flag"] = no_regional_blackout_flag
            if web_delivery_allowed_flag is not None:
                self._values["web_delivery_allowed_flag"] = web_delivery_allowed_flag

        @builtins.property
        def ad_avail_offset(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.Scte35TimeSignalAposProperty.AdAvailOffset``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35timesignalapos.html#cfn-medialive-channel-scte35timesignalapos-adavailoffset
            """
            result = self._values.get("ad_avail_offset")
            return result

        @builtins.property
        def no_regional_blackout_flag(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Scte35TimeSignalAposProperty.NoRegionalBlackoutFlag``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35timesignalapos.html#cfn-medialive-channel-scte35timesignalapos-noregionalblackoutflag
            """
            result = self._values.get("no_regional_blackout_flag")
            return result

        @builtins.property
        def web_delivery_allowed_flag(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.Scte35TimeSignalAposProperty.WebDeliveryAllowedFlag``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35timesignalapos.html#cfn-medialive-channel-scte35timesignalapos-webdeliveryallowedflag
            """
            result = self._values.get("web_delivery_allowed_flag")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Scte35TimeSignalAposProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.SmpteTtDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class SmpteTtDestinationSettingsProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-smptettdestinationsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SmpteTtDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.StandardHlsSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_rendition_sets": "audioRenditionSets",
            "m3_u8_settings": "m3U8Settings",
        },
    )
    class StandardHlsSettingsProperty:
        def __init__(
            self,
            *,
            audio_rendition_sets: typing.Optional[builtins.str] = None,
            m3_u8_settings: typing.Optional[typing.Union["CfnChannel.M3u8SettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param audio_rendition_sets: ``CfnChannel.StandardHlsSettingsProperty.AudioRenditionSets``.
            :param m3_u8_settings: ``CfnChannel.StandardHlsSettingsProperty.M3u8Settings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-standardhlssettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_rendition_sets is not None:
                self._values["audio_rendition_sets"] = audio_rendition_sets
            if m3_u8_settings is not None:
                self._values["m3_u8_settings"] = m3_u8_settings

        @builtins.property
        def audio_rendition_sets(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.StandardHlsSettingsProperty.AudioRenditionSets``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-standardhlssettings.html#cfn-medialive-channel-standardhlssettings-audiorenditionsets
            """
            result = self._values.get("audio_rendition_sets")
            return result

        @builtins.property
        def m3_u8_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.M3u8SettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.StandardHlsSettingsProperty.M3u8Settings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-standardhlssettings.html#cfn-medialive-channel-standardhlssettings-m3u8settings
            """
            result = self._values.get("m3_u8_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StandardHlsSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.StaticKeySettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "key_provider_server": "keyProviderServer",
            "static_key_value": "staticKeyValue",
        },
    )
    class StaticKeySettingsProperty:
        def __init__(
            self,
            *,
            key_provider_server: typing.Optional[typing.Union["CfnChannel.InputLocationProperty", _IResolvable_a771d0ef]] = None,
            static_key_value: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param key_provider_server: ``CfnChannel.StaticKeySettingsProperty.KeyProviderServer``.
            :param static_key_value: ``CfnChannel.StaticKeySettingsProperty.StaticKeyValue``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-statickeysettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if key_provider_server is not None:
                self._values["key_provider_server"] = key_provider_server
            if static_key_value is not None:
                self._values["static_key_value"] = static_key_value

        @builtins.property
        def key_provider_server(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.InputLocationProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.StaticKeySettingsProperty.KeyProviderServer``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-statickeysettings.html#cfn-medialive-channel-statickeysettings-keyproviderserver
            """
            result = self._values.get("key_provider_server")
            return result

        @builtins.property
        def static_key_value(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.StaticKeySettingsProperty.StaticKeyValue``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-statickeysettings.html#cfn-medialive-channel-statickeysettings-statickeyvalue
            """
            result = self._values.get("static_key_value")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StaticKeySettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.TeletextDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class TeletextDestinationSettingsProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-teletextdestinationsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TeletextDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.TeletextSourceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"page_number": "pageNumber"},
    )
    class TeletextSourceSettingsProperty:
        def __init__(
            self,
            *,
            page_number: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param page_number: ``CfnChannel.TeletextSourceSettingsProperty.PageNumber``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-teletextsourcesettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if page_number is not None:
                self._values["page_number"] = page_number

        @builtins.property
        def page_number(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.TeletextSourceSettingsProperty.PageNumber``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-teletextsourcesettings.html#cfn-medialive-channel-teletextsourcesettings-pagenumber
            """
            result = self._values.get("page_number")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TeletextSourceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.TemporalFilterSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "post_filter_sharpening": "postFilterSharpening",
            "strength": "strength",
        },
    )
    class TemporalFilterSettingsProperty:
        def __init__(
            self,
            *,
            post_filter_sharpening: typing.Optional[builtins.str] = None,
            strength: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param post_filter_sharpening: ``CfnChannel.TemporalFilterSettingsProperty.PostFilterSharpening``.
            :param strength: ``CfnChannel.TemporalFilterSettingsProperty.Strength``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-temporalfiltersettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if post_filter_sharpening is not None:
                self._values["post_filter_sharpening"] = post_filter_sharpening
            if strength is not None:
                self._values["strength"] = strength

        @builtins.property
        def post_filter_sharpening(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.TemporalFilterSettingsProperty.PostFilterSharpening``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-temporalfiltersettings.html#cfn-medialive-channel-temporalfiltersettings-postfiltersharpening
            """
            result = self._values.get("post_filter_sharpening")
            return result

        @builtins.property
        def strength(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.TemporalFilterSettingsProperty.Strength``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-temporalfiltersettings.html#cfn-medialive-channel-temporalfiltersettings-strength
            """
            result = self._values.get("strength")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemporalFilterSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.TimecodeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"source": "source", "sync_threshold": "syncThreshold"},
    )
    class TimecodeConfigProperty:
        def __init__(
            self,
            *,
            source: typing.Optional[builtins.str] = None,
            sync_threshold: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param source: ``CfnChannel.TimecodeConfigProperty.Source``.
            :param sync_threshold: ``CfnChannel.TimecodeConfigProperty.SyncThreshold``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-timecodeconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if source is not None:
                self._values["source"] = source
            if sync_threshold is not None:
                self._values["sync_threshold"] = sync_threshold

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.TimecodeConfigProperty.Source``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-timecodeconfig.html#cfn-medialive-channel-timecodeconfig-source
            """
            result = self._values.get("source")
            return result

        @builtins.property
        def sync_threshold(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.TimecodeConfigProperty.SyncThreshold``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-timecodeconfig.html#cfn-medialive-channel-timecodeconfig-syncthreshold
            """
            result = self._values.get("sync_threshold")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimecodeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.TtmlDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"style_control": "styleControl"},
    )
    class TtmlDestinationSettingsProperty:
        def __init__(
            self,
            *,
            style_control: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param style_control: ``CfnChannel.TtmlDestinationSettingsProperty.StyleControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ttmldestinationsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if style_control is not None:
                self._values["style_control"] = style_control

        @builtins.property
        def style_control(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.TtmlDestinationSettingsProperty.StyleControl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ttmldestinationsettings.html#cfn-medialive-channel-ttmldestinationsettings-stylecontrol
            """
            result = self._values.get("style_control")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TtmlDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.UdpContainerSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"m2_ts_settings": "m2TsSettings"},
    )
    class UdpContainerSettingsProperty:
        def __init__(
            self,
            *,
            m2_ts_settings: typing.Optional[typing.Union["CfnChannel.M2tsSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param m2_ts_settings: ``CfnChannel.UdpContainerSettingsProperty.M2tsSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpcontainersettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if m2_ts_settings is not None:
                self._values["m2_ts_settings"] = m2_ts_settings

        @builtins.property
        def m2_ts_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.M2tsSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.UdpContainerSettingsProperty.M2tsSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpcontainersettings.html#cfn-medialive-channel-udpcontainersettings-m2tssettings
            """
            result = self._values.get("m2_ts_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UdpContainerSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.UdpGroupSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "input_loss_action": "inputLossAction",
            "timed_metadata_id3_frame": "timedMetadataId3Frame",
            "timed_metadata_id3_period": "timedMetadataId3Period",
        },
    )
    class UdpGroupSettingsProperty:
        def __init__(
            self,
            *,
            input_loss_action: typing.Optional[builtins.str] = None,
            timed_metadata_id3_frame: typing.Optional[builtins.str] = None,
            timed_metadata_id3_period: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param input_loss_action: ``CfnChannel.UdpGroupSettingsProperty.InputLossAction``.
            :param timed_metadata_id3_frame: ``CfnChannel.UdpGroupSettingsProperty.TimedMetadataId3Frame``.
            :param timed_metadata_id3_period: ``CfnChannel.UdpGroupSettingsProperty.TimedMetadataId3Period``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpgroupsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if input_loss_action is not None:
                self._values["input_loss_action"] = input_loss_action
            if timed_metadata_id3_frame is not None:
                self._values["timed_metadata_id3_frame"] = timed_metadata_id3_frame
            if timed_metadata_id3_period is not None:
                self._values["timed_metadata_id3_period"] = timed_metadata_id3_period

        @builtins.property
        def input_loss_action(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.UdpGroupSettingsProperty.InputLossAction``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpgroupsettings.html#cfn-medialive-channel-udpgroupsettings-inputlossaction
            """
            result = self._values.get("input_loss_action")
            return result

        @builtins.property
        def timed_metadata_id3_frame(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.UdpGroupSettingsProperty.TimedMetadataId3Frame``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpgroupsettings.html#cfn-medialive-channel-udpgroupsettings-timedmetadataid3frame
            """
            result = self._values.get("timed_metadata_id3_frame")
            return result

        @builtins.property
        def timed_metadata_id3_period(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.UdpGroupSettingsProperty.TimedMetadataId3Period``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpgroupsettings.html#cfn-medialive-channel-udpgroupsettings-timedmetadataid3period
            """
            result = self._values.get("timed_metadata_id3_period")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UdpGroupSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.UdpOutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "buffer_msec": "bufferMsec",
            "container_settings": "containerSettings",
            "destination": "destination",
            "fec_output_settings": "fecOutputSettings",
        },
    )
    class UdpOutputSettingsProperty:
        def __init__(
            self,
            *,
            buffer_msec: typing.Optional[jsii.Number] = None,
            container_settings: typing.Optional[typing.Union["CfnChannel.UdpContainerSettingsProperty", _IResolvable_a771d0ef]] = None,
            destination: typing.Optional[typing.Union["CfnChannel.OutputLocationRefProperty", _IResolvable_a771d0ef]] = None,
            fec_output_settings: typing.Optional[typing.Union["CfnChannel.FecOutputSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param buffer_msec: ``CfnChannel.UdpOutputSettingsProperty.BufferMsec``.
            :param container_settings: ``CfnChannel.UdpOutputSettingsProperty.ContainerSettings``.
            :param destination: ``CfnChannel.UdpOutputSettingsProperty.Destination``.
            :param fec_output_settings: ``CfnChannel.UdpOutputSettingsProperty.FecOutputSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if buffer_msec is not None:
                self._values["buffer_msec"] = buffer_msec
            if container_settings is not None:
                self._values["container_settings"] = container_settings
            if destination is not None:
                self._values["destination"] = destination
            if fec_output_settings is not None:
                self._values["fec_output_settings"] = fec_output_settings

        @builtins.property
        def buffer_msec(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.UdpOutputSettingsProperty.BufferMsec``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html#cfn-medialive-channel-udpoutputsettings-buffermsec
            """
            result = self._values.get("buffer_msec")
            return result

        @builtins.property
        def container_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.UdpContainerSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.UdpOutputSettingsProperty.ContainerSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html#cfn-medialive-channel-udpoutputsettings-containersettings
            """
            result = self._values.get("container_settings")
            return result

        @builtins.property
        def destination(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.OutputLocationRefProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.UdpOutputSettingsProperty.Destination``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html#cfn-medialive-channel-udpoutputsettings-destination
            """
            result = self._values.get("destination")
            return result

        @builtins.property
        def fec_output_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.FecOutputSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.UdpOutputSettingsProperty.FecOutputSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html#cfn-medialive-channel-udpoutputsettings-fecoutputsettings
            """
            result = self._values.get("fec_output_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UdpOutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.VideoCodecSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "frame_capture_settings": "frameCaptureSettings",
            "h264_settings": "h264Settings",
            "h265_settings": "h265Settings",
        },
    )
    class VideoCodecSettingsProperty:
        def __init__(
            self,
            *,
            frame_capture_settings: typing.Optional[typing.Union["CfnChannel.FrameCaptureSettingsProperty", _IResolvable_a771d0ef]] = None,
            h264_settings: typing.Optional[typing.Union["CfnChannel.H264SettingsProperty", _IResolvable_a771d0ef]] = None,
            h265_settings: typing.Optional[typing.Union["CfnChannel.H265SettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param frame_capture_settings: ``CfnChannel.VideoCodecSettingsProperty.FrameCaptureSettings``.
            :param h264_settings: ``CfnChannel.VideoCodecSettingsProperty.H264Settings``.
            :param h265_settings: ``CfnChannel.VideoCodecSettingsProperty.H265Settings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if frame_capture_settings is not None:
                self._values["frame_capture_settings"] = frame_capture_settings
            if h264_settings is not None:
                self._values["h264_settings"] = h264_settings
            if h265_settings is not None:
                self._values["h265_settings"] = h265_settings

        @builtins.property
        def frame_capture_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.FrameCaptureSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.VideoCodecSettingsProperty.FrameCaptureSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html#cfn-medialive-channel-videocodecsettings-framecapturesettings
            """
            result = self._values.get("frame_capture_settings")
            return result

        @builtins.property
        def h264_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.H264SettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.VideoCodecSettingsProperty.H264Settings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html#cfn-medialive-channel-videocodecsettings-h264settings
            """
            result = self._values.get("h264_settings")
            return result

        @builtins.property
        def h265_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.H265SettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.VideoCodecSettingsProperty.H265Settings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html#cfn-medialive-channel-videocodecsettings-h265settings
            """
            result = self._values.get("h265_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VideoCodecSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.VideoDescriptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "codec_settings": "codecSettings",
            "height": "height",
            "name": "name",
            "respond_to_afd": "respondToAfd",
            "scaling_behavior": "scalingBehavior",
            "sharpness": "sharpness",
            "width": "width",
        },
    )
    class VideoDescriptionProperty:
        def __init__(
            self,
            *,
            codec_settings: typing.Optional[typing.Union["CfnChannel.VideoCodecSettingsProperty", _IResolvable_a771d0ef]] = None,
            height: typing.Optional[jsii.Number] = None,
            name: typing.Optional[builtins.str] = None,
            respond_to_afd: typing.Optional[builtins.str] = None,
            scaling_behavior: typing.Optional[builtins.str] = None,
            sharpness: typing.Optional[jsii.Number] = None,
            width: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param codec_settings: ``CfnChannel.VideoDescriptionProperty.CodecSettings``.
            :param height: ``CfnChannel.VideoDescriptionProperty.Height``.
            :param name: ``CfnChannel.VideoDescriptionProperty.Name``.
            :param respond_to_afd: ``CfnChannel.VideoDescriptionProperty.RespondToAfd``.
            :param scaling_behavior: ``CfnChannel.VideoDescriptionProperty.ScalingBehavior``.
            :param sharpness: ``CfnChannel.VideoDescriptionProperty.Sharpness``.
            :param width: ``CfnChannel.VideoDescriptionProperty.Width``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if codec_settings is not None:
                self._values["codec_settings"] = codec_settings
            if height is not None:
                self._values["height"] = height
            if name is not None:
                self._values["name"] = name
            if respond_to_afd is not None:
                self._values["respond_to_afd"] = respond_to_afd
            if scaling_behavior is not None:
                self._values["scaling_behavior"] = scaling_behavior
            if sharpness is not None:
                self._values["sharpness"] = sharpness
            if width is not None:
                self._values["width"] = width

        @builtins.property
        def codec_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.VideoCodecSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.VideoDescriptionProperty.CodecSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-codecsettings
            """
            result = self._values.get("codec_settings")
            return result

        @builtins.property
        def height(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.VideoDescriptionProperty.Height``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-height
            """
            result = self._values.get("height")
            return result

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.VideoDescriptionProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-name
            """
            result = self._values.get("name")
            return result

        @builtins.property
        def respond_to_afd(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.VideoDescriptionProperty.RespondToAfd``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-respondtoafd
            """
            result = self._values.get("respond_to_afd")
            return result

        @builtins.property
        def scaling_behavior(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.VideoDescriptionProperty.ScalingBehavior``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-scalingbehavior
            """
            result = self._values.get("scaling_behavior")
            return result

        @builtins.property
        def sharpness(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.VideoDescriptionProperty.Sharpness``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-sharpness
            """
            result = self._values.get("sharpness")
            return result

        @builtins.property
        def width(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.VideoDescriptionProperty.Width``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-width
            """
            result = self._values.get("width")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VideoDescriptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.VideoSelectorPidProperty",
        jsii_struct_bases=[],
        name_mapping={"pid": "pid"},
    )
    class VideoSelectorPidProperty:
        def __init__(self, *, pid: typing.Optional[jsii.Number] = None) -> None:
            """
            :param pid: ``CfnChannel.VideoSelectorPidProperty.Pid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorpid.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if pid is not None:
                self._values["pid"] = pid

        @builtins.property
        def pid(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.VideoSelectorPidProperty.Pid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorpid.html#cfn-medialive-channel-videoselectorpid-pid
            """
            result = self._values.get("pid")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VideoSelectorPidProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.VideoSelectorProgramIdProperty",
        jsii_struct_bases=[],
        name_mapping={"program_id": "programId"},
    )
    class VideoSelectorProgramIdProperty:
        def __init__(self, *, program_id: typing.Optional[jsii.Number] = None) -> None:
            """
            :param program_id: ``CfnChannel.VideoSelectorProgramIdProperty.ProgramId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorprogramid.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if program_id is not None:
                self._values["program_id"] = program_id

        @builtins.property
        def program_id(self) -> typing.Optional[jsii.Number]:
            """``CfnChannel.VideoSelectorProgramIdProperty.ProgramId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorprogramid.html#cfn-medialive-channel-videoselectorprogramid-programid
            """
            result = self._values.get("program_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VideoSelectorProgramIdProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.VideoSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "color_space": "colorSpace",
            "color_space_usage": "colorSpaceUsage",
            "selector_settings": "selectorSettings",
        },
    )
    class VideoSelectorProperty:
        def __init__(
            self,
            *,
            color_space: typing.Optional[builtins.str] = None,
            color_space_usage: typing.Optional[builtins.str] = None,
            selector_settings: typing.Optional[typing.Union["CfnChannel.VideoSelectorSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param color_space: ``CfnChannel.VideoSelectorProperty.ColorSpace``.
            :param color_space_usage: ``CfnChannel.VideoSelectorProperty.ColorSpaceUsage``.
            :param selector_settings: ``CfnChannel.VideoSelectorProperty.SelectorSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselector.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if color_space is not None:
                self._values["color_space"] = color_space
            if color_space_usage is not None:
                self._values["color_space_usage"] = color_space_usage
            if selector_settings is not None:
                self._values["selector_settings"] = selector_settings

        @builtins.property
        def color_space(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.VideoSelectorProperty.ColorSpace``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselector.html#cfn-medialive-channel-videoselector-colorspace
            """
            result = self._values.get("color_space")
            return result

        @builtins.property
        def color_space_usage(self) -> typing.Optional[builtins.str]:
            """``CfnChannel.VideoSelectorProperty.ColorSpaceUsage``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselector.html#cfn-medialive-channel-videoselector-colorspaceusage
            """
            result = self._values.get("color_space_usage")
            return result

        @builtins.property
        def selector_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.VideoSelectorSettingsProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.VideoSelectorProperty.SelectorSettings``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselector.html#cfn-medialive-channel-videoselector-selectorsettings
            """
            result = self._values.get("selector_settings")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VideoSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.VideoSelectorSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "video_selector_pid": "videoSelectorPid",
            "video_selector_program_id": "videoSelectorProgramId",
        },
    )
    class VideoSelectorSettingsProperty:
        def __init__(
            self,
            *,
            video_selector_pid: typing.Optional[typing.Union["CfnChannel.VideoSelectorPidProperty", _IResolvable_a771d0ef]] = None,
            video_selector_program_id: typing.Optional[typing.Union["CfnChannel.VideoSelectorProgramIdProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param video_selector_pid: ``CfnChannel.VideoSelectorSettingsProperty.VideoSelectorPid``.
            :param video_selector_program_id: ``CfnChannel.VideoSelectorSettingsProperty.VideoSelectorProgramId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if video_selector_pid is not None:
                self._values["video_selector_pid"] = video_selector_pid
            if video_selector_program_id is not None:
                self._values["video_selector_program_id"] = video_selector_program_id

        @builtins.property
        def video_selector_pid(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.VideoSelectorPidProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.VideoSelectorSettingsProperty.VideoSelectorPid``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorsettings.html#cfn-medialive-channel-videoselectorsettings-videoselectorpid
            """
            result = self._values.get("video_selector_pid")
            return result

        @builtins.property
        def video_selector_program_id(
            self,
        ) -> typing.Optional[typing.Union["CfnChannel.VideoSelectorProgramIdProperty", _IResolvable_a771d0ef]]:
            """``CfnChannel.VideoSelectorSettingsProperty.VideoSelectorProgramId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorsettings.html#cfn-medialive-channel-videoselectorsettings-videoselectorprogramid
            """
            result = self._values.get("video_selector_program_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VideoSelectorSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnChannel.WebvttDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class WebvttDestinationSettingsProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-webvttdestinationsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WebvttDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_medialive.CfnChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "channel_class": "channelClass",
        "destinations": "destinations",
        "encoder_settings": "encoderSettings",
        "input_attachments": "inputAttachments",
        "input_specification": "inputSpecification",
        "log_level": "logLevel",
        "name": "name",
        "role_arn": "roleArn",
        "tags": "tags",
    },
)
class CfnChannelProps:
    def __init__(
        self,
        *,
        channel_class: typing.Optional[builtins.str] = None,
        destinations: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnChannel.OutputDestinationProperty, _IResolvable_a771d0ef]]]] = None,
        encoder_settings: typing.Optional[typing.Union[CfnChannel.EncoderSettingsProperty, _IResolvable_a771d0ef]] = None,
        input_attachments: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnChannel.InputAttachmentProperty, _IResolvable_a771d0ef]]]] = None,
        input_specification: typing.Optional[typing.Union[CfnChannel.InputSpecificationProperty, _IResolvable_a771d0ef]] = None,
        log_level: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        """Properties for defining a ``AWS::MediaLive::Channel``.

        :param channel_class: ``AWS::MediaLive::Channel.ChannelClass``.
        :param destinations: ``AWS::MediaLive::Channel.Destinations``.
        :param encoder_settings: ``AWS::MediaLive::Channel.EncoderSettings``.
        :param input_attachments: ``AWS::MediaLive::Channel.InputAttachments``.
        :param input_specification: ``AWS::MediaLive::Channel.InputSpecification``.
        :param log_level: ``AWS::MediaLive::Channel.LogLevel``.
        :param name: ``AWS::MediaLive::Channel.Name``.
        :param role_arn: ``AWS::MediaLive::Channel.RoleArn``.
        :param tags: ``AWS::MediaLive::Channel.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if channel_class is not None:
            self._values["channel_class"] = channel_class
        if destinations is not None:
            self._values["destinations"] = destinations
        if encoder_settings is not None:
            self._values["encoder_settings"] = encoder_settings
        if input_attachments is not None:
            self._values["input_attachments"] = input_attachments
        if input_specification is not None:
            self._values["input_specification"] = input_specification
        if log_level is not None:
            self._values["log_level"] = log_level
        if name is not None:
            self._values["name"] = name
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def channel_class(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaLive::Channel.ChannelClass``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-channelclass
        """
        result = self._values.get("channel_class")
        return result

    @builtins.property
    def destinations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnChannel.OutputDestinationProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::MediaLive::Channel.Destinations``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-destinations
        """
        result = self._values.get("destinations")
        return result

    @builtins.property
    def encoder_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnChannel.EncoderSettingsProperty, _IResolvable_a771d0ef]]:
        """``AWS::MediaLive::Channel.EncoderSettings``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-encodersettings
        """
        result = self._values.get("encoder_settings")
        return result

    @builtins.property
    def input_attachments(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnChannel.InputAttachmentProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::MediaLive::Channel.InputAttachments``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-inputattachments
        """
        result = self._values.get("input_attachments")
        return result

    @builtins.property
    def input_specification(
        self,
    ) -> typing.Optional[typing.Union[CfnChannel.InputSpecificationProperty, _IResolvable_a771d0ef]]:
        """``AWS::MediaLive::Channel.InputSpecification``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-inputspecification
        """
        result = self._values.get("input_specification")
        return result

    @builtins.property
    def log_level(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaLive::Channel.LogLevel``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-loglevel
        """
        result = self._values.get("log_level")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaLive::Channel.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaLive::Channel.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-rolearn
        """
        result = self._values.get("role_arn")
        return result

    @builtins.property
    def tags(self) -> typing.Any:
        """``AWS::MediaLive::Channel.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnInput(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_medialive.CfnInput",
):
    """A CloudFormation ``AWS::MediaLive::Input``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html
    :cloudformationResource: AWS::MediaLive::Input
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        destinations: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnInput.InputDestinationRequestProperty", _IResolvable_a771d0ef]]]] = None,
        input_devices: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnInput.InputDeviceSettingsProperty", _IResolvable_a771d0ef]]]] = None,
        input_security_groups: typing.Optional[typing.List[builtins.str]] = None,
        media_connect_flows: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnInput.MediaConnectFlowRequestProperty", _IResolvable_a771d0ef]]]] = None,
        name: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        sources: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnInput.InputSourceRequestProperty", _IResolvable_a771d0ef]]]] = None,
        tags: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
        vpc: typing.Optional[typing.Union["CfnInput.InputVpcRequestProperty", _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Create a new ``AWS::MediaLive::Input``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param destinations: ``AWS::MediaLive::Input.Destinations``.
        :param input_devices: ``AWS::MediaLive::Input.InputDevices``.
        :param input_security_groups: ``AWS::MediaLive::Input.InputSecurityGroups``.
        :param media_connect_flows: ``AWS::MediaLive::Input.MediaConnectFlows``.
        :param name: ``AWS::MediaLive::Input.Name``.
        :param role_arn: ``AWS::MediaLive::Input.RoleArn``.
        :param sources: ``AWS::MediaLive::Input.Sources``.
        :param tags: ``AWS::MediaLive::Input.Tags``.
        :param type: ``AWS::MediaLive::Input.Type``.
        :param vpc: ``AWS::MediaLive::Input.Vpc``.
        """
        props = CfnInputProps(
            destinations=destinations,
            input_devices=input_devices,
            input_security_groups=input_security_groups,
            media_connect_flows=media_connect_flows,
            name=name,
            role_arn=role_arn,
            sources=sources,
            tags=tags,
            type=type,
            vpc=vpc,
        )

        jsii.create(CfnInput, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrDestinations")
    def attr_destinations(self) -> typing.List[builtins.str]:
        """
        :cloudformationAttribute: Destinations
        """
        return jsii.get(self, "attrDestinations")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrSources")
    def attr_sources(self) -> typing.List[builtins.str]:
        """
        :cloudformationAttribute: Sources
        """
        return jsii.get(self, "attrSources")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::MediaLive::Input.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="destinations")
    def destinations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnInput.InputDestinationRequestProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::MediaLive::Input.Destinations``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-destinations
        """
        return jsii.get(self, "destinations")

    @destinations.setter # type: ignore
    def destinations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnInput.InputDestinationRequestProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "destinations", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="inputDevices")
    def input_devices(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnInput.InputDeviceSettingsProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::MediaLive::Input.InputDevices``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-inputdevices
        """
        return jsii.get(self, "inputDevices")

    @input_devices.setter # type: ignore
    def input_devices(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnInput.InputDeviceSettingsProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "inputDevices", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="inputSecurityGroups")
    def input_security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::MediaLive::Input.InputSecurityGroups``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-inputsecuritygroups
        """
        return jsii.get(self, "inputSecurityGroups")

    @input_security_groups.setter # type: ignore
    def input_security_groups(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "inputSecurityGroups", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="mediaConnectFlows")
    def media_connect_flows(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnInput.MediaConnectFlowRequestProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::MediaLive::Input.MediaConnectFlows``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-mediaconnectflows
        """
        return jsii.get(self, "mediaConnectFlows")

    @media_connect_flows.setter # type: ignore
    def media_connect_flows(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnInput.MediaConnectFlowRequestProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "mediaConnectFlows", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaLive::Input.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaLive::Input.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-rolearn
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter # type: ignore
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="sources")
    def sources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnInput.InputSourceRequestProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::MediaLive::Input.Sources``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-sources
        """
        return jsii.get(self, "sources")

    @sources.setter # type: ignore
    def sources(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnInput.InputSourceRequestProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "sources", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaLive::Input.Type``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-type
        """
        return jsii.get(self, "type")

    @type.setter # type: ignore
    def type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="vpc")
    def vpc(
        self,
    ) -> typing.Optional[typing.Union["CfnInput.InputVpcRequestProperty", _IResolvable_a771d0ef]]:
        """``AWS::MediaLive::Input.Vpc``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-vpc
        """
        return jsii.get(self, "vpc")

    @vpc.setter # type: ignore
    def vpc(
        self,
        value: typing.Optional[typing.Union["CfnInput.InputVpcRequestProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "vpc", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnInput.InputDestinationRequestProperty",
        jsii_struct_bases=[],
        name_mapping={"stream_name": "streamName"},
    )
    class InputDestinationRequestProperty:
        def __init__(
            self,
            *,
            stream_name: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param stream_name: ``CfnInput.InputDestinationRequestProperty.StreamName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdestinationrequest.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if stream_name is not None:
                self._values["stream_name"] = stream_name

        @builtins.property
        def stream_name(self) -> typing.Optional[builtins.str]:
            """``CfnInput.InputDestinationRequestProperty.StreamName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdestinationrequest.html#cfn-medialive-input-inputdestinationrequest-streamname
            """
            result = self._values.get("stream_name")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputDestinationRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnInput.InputDeviceRequestProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id"},
    )
    class InputDeviceRequestProperty:
        def __init__(self, *, id: typing.Optional[builtins.str] = None) -> None:
            """
            :param id: ``CfnInput.InputDeviceRequestProperty.Id``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicerequest.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if id is not None:
                self._values["id"] = id

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            """``CfnInput.InputDeviceRequestProperty.Id``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicerequest.html#cfn-medialive-input-inputdevicerequest-id
            """
            result = self._values.get("id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputDeviceRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnInput.InputDeviceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id"},
    )
    class InputDeviceSettingsProperty:
        def __init__(self, *, id: typing.Optional[builtins.str] = None) -> None:
            """
            :param id: ``CfnInput.InputDeviceSettingsProperty.Id``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicesettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if id is not None:
                self._values["id"] = id

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            """``CfnInput.InputDeviceSettingsProperty.Id``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicesettings.html#cfn-medialive-input-inputdevicesettings-id
            """
            result = self._values.get("id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputDeviceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnInput.InputSourceRequestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "password_param": "passwordParam",
            "url": "url",
            "username": "username",
        },
    )
    class InputSourceRequestProperty:
        def __init__(
            self,
            *,
            password_param: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param password_param: ``CfnInput.InputSourceRequestProperty.PasswordParam``.
            :param url: ``CfnInput.InputSourceRequestProperty.Url``.
            :param username: ``CfnInput.InputSourceRequestProperty.Username``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputsourcerequest.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if password_param is not None:
                self._values["password_param"] = password_param
            if url is not None:
                self._values["url"] = url
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def password_param(self) -> typing.Optional[builtins.str]:
            """``CfnInput.InputSourceRequestProperty.PasswordParam``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputsourcerequest.html#cfn-medialive-input-inputsourcerequest-passwordparam
            """
            result = self._values.get("password_param")
            return result

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            """``CfnInput.InputSourceRequestProperty.Url``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputsourcerequest.html#cfn-medialive-input-inputsourcerequest-url
            """
            result = self._values.get("url")
            return result

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            """``CfnInput.InputSourceRequestProperty.Username``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputsourcerequest.html#cfn-medialive-input-inputsourcerequest-username
            """
            result = self._values.get("username")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputSourceRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnInput.InputVpcRequestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class InputVpcRequestProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Optional[typing.List[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.List[builtins.str]] = None,
        ) -> None:
            """
            :param security_group_ids: ``CfnInput.InputVpcRequestProperty.SecurityGroupIds``.
            :param subnet_ids: ``CfnInput.InputVpcRequestProperty.SubnetIds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputvpcrequest.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnInput.InputVpcRequestProperty.SecurityGroupIds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputvpcrequest.html#cfn-medialive-input-inputvpcrequest-securitygroupids
            """
            result = self._values.get("security_group_ids")
            return result

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnInput.InputVpcRequestProperty.SubnetIds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputvpcrequest.html#cfn-medialive-input-inputvpcrequest-subnetids
            """
            result = self._values.get("subnet_ids")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputVpcRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnInput.MediaConnectFlowRequestProperty",
        jsii_struct_bases=[],
        name_mapping={"flow_arn": "flowArn"},
    )
    class MediaConnectFlowRequestProperty:
        def __init__(self, *, flow_arn: typing.Optional[builtins.str] = None) -> None:
            """
            :param flow_arn: ``CfnInput.MediaConnectFlowRequestProperty.FlowArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-mediaconnectflowrequest.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if flow_arn is not None:
                self._values["flow_arn"] = flow_arn

        @builtins.property
        def flow_arn(self) -> typing.Optional[builtins.str]:
            """``CfnInput.MediaConnectFlowRequestProperty.FlowArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-mediaconnectflowrequest.html#cfn-medialive-input-mediaconnectflowrequest-flowarn
            """
            result = self._values.get("flow_arn")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaConnectFlowRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_medialive.CfnInputProps",
    jsii_struct_bases=[],
    name_mapping={
        "destinations": "destinations",
        "input_devices": "inputDevices",
        "input_security_groups": "inputSecurityGroups",
        "media_connect_flows": "mediaConnectFlows",
        "name": "name",
        "role_arn": "roleArn",
        "sources": "sources",
        "tags": "tags",
        "type": "type",
        "vpc": "vpc",
    },
)
class CfnInputProps:
    def __init__(
        self,
        *,
        destinations: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnInput.InputDestinationRequestProperty, _IResolvable_a771d0ef]]]] = None,
        input_devices: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnInput.InputDeviceSettingsProperty, _IResolvable_a771d0ef]]]] = None,
        input_security_groups: typing.Optional[typing.List[builtins.str]] = None,
        media_connect_flows: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnInput.MediaConnectFlowRequestProperty, _IResolvable_a771d0ef]]]] = None,
        name: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        sources: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnInput.InputSourceRequestProperty, _IResolvable_a771d0ef]]]] = None,
        tags: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
        vpc: typing.Optional[typing.Union[CfnInput.InputVpcRequestProperty, _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Properties for defining a ``AWS::MediaLive::Input``.

        :param destinations: ``AWS::MediaLive::Input.Destinations``.
        :param input_devices: ``AWS::MediaLive::Input.InputDevices``.
        :param input_security_groups: ``AWS::MediaLive::Input.InputSecurityGroups``.
        :param media_connect_flows: ``AWS::MediaLive::Input.MediaConnectFlows``.
        :param name: ``AWS::MediaLive::Input.Name``.
        :param role_arn: ``AWS::MediaLive::Input.RoleArn``.
        :param sources: ``AWS::MediaLive::Input.Sources``.
        :param tags: ``AWS::MediaLive::Input.Tags``.
        :param type: ``AWS::MediaLive::Input.Type``.
        :param vpc: ``AWS::MediaLive::Input.Vpc``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if destinations is not None:
            self._values["destinations"] = destinations
        if input_devices is not None:
            self._values["input_devices"] = input_devices
        if input_security_groups is not None:
            self._values["input_security_groups"] = input_security_groups
        if media_connect_flows is not None:
            self._values["media_connect_flows"] = media_connect_flows
        if name is not None:
            self._values["name"] = name
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if sources is not None:
            self._values["sources"] = sources
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def destinations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnInput.InputDestinationRequestProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::MediaLive::Input.Destinations``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-destinations
        """
        result = self._values.get("destinations")
        return result

    @builtins.property
    def input_devices(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnInput.InputDeviceSettingsProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::MediaLive::Input.InputDevices``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-inputdevices
        """
        result = self._values.get("input_devices")
        return result

    @builtins.property
    def input_security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::MediaLive::Input.InputSecurityGroups``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-inputsecuritygroups
        """
        result = self._values.get("input_security_groups")
        return result

    @builtins.property
    def media_connect_flows(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnInput.MediaConnectFlowRequestProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::MediaLive::Input.MediaConnectFlows``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-mediaconnectflows
        """
        result = self._values.get("media_connect_flows")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaLive::Input.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaLive::Input.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-rolearn
        """
        result = self._values.get("role_arn")
        return result

    @builtins.property
    def sources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnInput.InputSourceRequestProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::MediaLive::Input.Sources``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-sources
        """
        result = self._values.get("sources")
        return result

    @builtins.property
    def tags(self) -> typing.Any:
        """``AWS::MediaLive::Input.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-tags
        """
        result = self._values.get("tags")
        return result

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaLive::Input.Type``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-type
        """
        result = self._values.get("type")
        return result

    @builtins.property
    def vpc(
        self,
    ) -> typing.Optional[typing.Union[CfnInput.InputVpcRequestProperty, _IResolvable_a771d0ef]]:
        """``AWS::MediaLive::Input.Vpc``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-vpc
        """
        result = self._values.get("vpc")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInputProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnInputSecurityGroup(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_medialive.CfnInputSecurityGroup",
):
    """A CloudFormation ``AWS::MediaLive::InputSecurityGroup``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html
    :cloudformationResource: AWS::MediaLive::InputSecurityGroup
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        tags: typing.Any = None,
        whitelist_rules: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnInputSecurityGroup.InputWhitelistRuleCidrProperty", _IResolvable_a771d0ef]]]] = None,
    ) -> None:
        """Create a new ``AWS::MediaLive::InputSecurityGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param tags: ``AWS::MediaLive::InputSecurityGroup.Tags``.
        :param whitelist_rules: ``AWS::MediaLive::InputSecurityGroup.WhitelistRules``.
        """
        props = CfnInputSecurityGroupProps(tags=tags, whitelist_rules=whitelist_rules)

        jsii.create(CfnInputSecurityGroup, self, [scope, id, props])

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
        """``AWS::MediaLive::InputSecurityGroup.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html#cfn-medialive-inputsecuritygroup-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="whitelistRules")
    def whitelist_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnInputSecurityGroup.InputWhitelistRuleCidrProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::MediaLive::InputSecurityGroup.WhitelistRules``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html#cfn-medialive-inputsecuritygroup-whitelistrules
        """
        return jsii.get(self, "whitelistRules")

    @whitelist_rules.setter # type: ignore
    def whitelist_rules(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnInputSecurityGroup.InputWhitelistRuleCidrProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "whitelistRules", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_medialive.CfnInputSecurityGroup.InputWhitelistRuleCidrProperty",
        jsii_struct_bases=[],
        name_mapping={"cidr": "cidr"},
    )
    class InputWhitelistRuleCidrProperty:
        def __init__(self, *, cidr: typing.Optional[builtins.str] = None) -> None:
            """
            :param cidr: ``CfnInputSecurityGroup.InputWhitelistRuleCidrProperty.Cidr``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-inputsecuritygroup-inputwhitelistrulecidr.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if cidr is not None:
                self._values["cidr"] = cidr

        @builtins.property
        def cidr(self) -> typing.Optional[builtins.str]:
            """``CfnInputSecurityGroup.InputWhitelistRuleCidrProperty.Cidr``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-inputsecuritygroup-inputwhitelistrulecidr.html#cfn-medialive-inputsecuritygroup-inputwhitelistrulecidr-cidr
            """
            result = self._values.get("cidr")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputWhitelistRuleCidrProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_medialive.CfnInputSecurityGroupProps",
    jsii_struct_bases=[],
    name_mapping={"tags": "tags", "whitelist_rules": "whitelistRules"},
)
class CfnInputSecurityGroupProps:
    def __init__(
        self,
        *,
        tags: typing.Any = None,
        whitelist_rules: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnInputSecurityGroup.InputWhitelistRuleCidrProperty, _IResolvable_a771d0ef]]]] = None,
    ) -> None:
        """Properties for defining a ``AWS::MediaLive::InputSecurityGroup``.

        :param tags: ``AWS::MediaLive::InputSecurityGroup.Tags``.
        :param whitelist_rules: ``AWS::MediaLive::InputSecurityGroup.WhitelistRules``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if tags is not None:
            self._values["tags"] = tags
        if whitelist_rules is not None:
            self._values["whitelist_rules"] = whitelist_rules

    @builtins.property
    def tags(self) -> typing.Any:
        """``AWS::MediaLive::InputSecurityGroup.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html#cfn-medialive-inputsecuritygroup-tags
        """
        result = self._values.get("tags")
        return result

    @builtins.property
    def whitelist_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnInputSecurityGroup.InputWhitelistRuleCidrProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::MediaLive::InputSecurityGroup.WhitelistRules``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html#cfn-medialive-inputsecuritygroup-whitelistrules
        """
        result = self._values.get("whitelist_rules")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInputSecurityGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnChannel",
    "CfnChannelProps",
    "CfnInput",
    "CfnInputProps",
    "CfnInputSecurityGroup",
    "CfnInputSecurityGroupProps",
]

publication.publish()
