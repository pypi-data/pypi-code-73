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
class CfnJobTemplate(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_mediaconvert.CfnJobTemplate",
):
    """A CloudFormation ``AWS::MediaConvert::JobTemplate``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html
    :cloudformationResource: AWS::MediaConvert::JobTemplate
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        settings_json: typing.Any,
        acceleration_settings: typing.Optional[typing.Union["CfnJobTemplate.AccelerationSettingsProperty", _IResolvable_a771d0ef]] = None,
        category: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        hop_destinations: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnJobTemplate.HopDestinationProperty", _IResolvable_a771d0ef]]]] = None,
        name: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        queue: typing.Optional[builtins.str] = None,
        status_update_interval: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        """Create a new ``AWS::MediaConvert::JobTemplate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param settings_json: ``AWS::MediaConvert::JobTemplate.SettingsJson``.
        :param acceleration_settings: ``AWS::MediaConvert::JobTemplate.AccelerationSettings``.
        :param category: ``AWS::MediaConvert::JobTemplate.Category``.
        :param description: ``AWS::MediaConvert::JobTemplate.Description``.
        :param hop_destinations: ``AWS::MediaConvert::JobTemplate.HopDestinations``.
        :param name: ``AWS::MediaConvert::JobTemplate.Name``.
        :param priority: ``AWS::MediaConvert::JobTemplate.Priority``.
        :param queue: ``AWS::MediaConvert::JobTemplate.Queue``.
        :param status_update_interval: ``AWS::MediaConvert::JobTemplate.StatusUpdateInterval``.
        :param tags: ``AWS::MediaConvert::JobTemplate.Tags``.
        """
        props = CfnJobTemplateProps(
            settings_json=settings_json,
            acceleration_settings=acceleration_settings,
            category=category,
            description=description,
            hop_destinations=hop_destinations,
            name=name,
            priority=priority,
            queue=queue,
            status_update_interval=status_update_interval,
            tags=tags,
        )

        jsii.create(CfnJobTemplate, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        """
        :cloudformationAttribute: Name
        """
        return jsii.get(self, "attrName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::MediaConvert::JobTemplate.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="settingsJson")
    def settings_json(self) -> typing.Any:
        """``AWS::MediaConvert::JobTemplate.SettingsJson``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-settingsjson
        """
        return jsii.get(self, "settingsJson")

    @settings_json.setter # type: ignore
    def settings_json(self, value: typing.Any) -> None:
        jsii.set(self, "settingsJson", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="accelerationSettings")
    def acceleration_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnJobTemplate.AccelerationSettingsProperty", _IResolvable_a771d0ef]]:
        """``AWS::MediaConvert::JobTemplate.AccelerationSettings``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-accelerationsettings
        """
        return jsii.get(self, "accelerationSettings")

    @acceleration_settings.setter # type: ignore
    def acceleration_settings(
        self,
        value: typing.Optional[typing.Union["CfnJobTemplate.AccelerationSettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "accelerationSettings", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="category")
    def category(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::JobTemplate.Category``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-category
        """
        return jsii.get(self, "category")

    @category.setter # type: ignore
    def category(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "category", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::JobTemplate.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hopDestinations")
    def hop_destinations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnJobTemplate.HopDestinationProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::MediaConvert::JobTemplate.HopDestinations``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-hopdestinations
        """
        return jsii.get(self, "hopDestinations")

    @hop_destinations.setter # type: ignore
    def hop_destinations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnJobTemplate.HopDestinationProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "hopDestinations", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::JobTemplate.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="priority")
    def priority(self) -> typing.Optional[jsii.Number]:
        """``AWS::MediaConvert::JobTemplate.Priority``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-priority
        """
        return jsii.get(self, "priority")

    @priority.setter # type: ignore
    def priority(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "priority", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="queue")
    def queue(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::JobTemplate.Queue``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-queue
        """
        return jsii.get(self, "queue")

    @queue.setter # type: ignore
    def queue(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "queue", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="statusUpdateInterval")
    def status_update_interval(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::JobTemplate.StatusUpdateInterval``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-statusupdateinterval
        """
        return jsii.get(self, "statusUpdateInterval")

    @status_update_interval.setter # type: ignore
    def status_update_interval(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "statusUpdateInterval", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_mediaconvert.CfnJobTemplate.AccelerationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"mode": "mode"},
    )
    class AccelerationSettingsProperty:
        def __init__(self, *, mode: builtins.str) -> None:
            """
            :param mode: ``CfnJobTemplate.AccelerationSettingsProperty.Mode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-accelerationsettings.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "mode": mode,
            }

        @builtins.property
        def mode(self) -> builtins.str:
            """``CfnJobTemplate.AccelerationSettingsProperty.Mode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-accelerationsettings.html#cfn-mediaconvert-jobtemplate-accelerationsettings-mode
            """
            result = self._values.get("mode")
            assert result is not None, "Required property 'mode' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccelerationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_mediaconvert.CfnJobTemplate.HopDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "priority": "priority",
            "queue": "queue",
            "wait_minutes": "waitMinutes",
        },
    )
    class HopDestinationProperty:
        def __init__(
            self,
            *,
            priority: typing.Optional[jsii.Number] = None,
            queue: typing.Optional[builtins.str] = None,
            wait_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param priority: ``CfnJobTemplate.HopDestinationProperty.Priority``.
            :param queue: ``CfnJobTemplate.HopDestinationProperty.Queue``.
            :param wait_minutes: ``CfnJobTemplate.HopDestinationProperty.WaitMinutes``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-hopdestination.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if priority is not None:
                self._values["priority"] = priority
            if queue is not None:
                self._values["queue"] = queue
            if wait_minutes is not None:
                self._values["wait_minutes"] = wait_minutes

        @builtins.property
        def priority(self) -> typing.Optional[jsii.Number]:
            """``CfnJobTemplate.HopDestinationProperty.Priority``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-hopdestination.html#cfn-mediaconvert-jobtemplate-hopdestination-priority
            """
            result = self._values.get("priority")
            return result

        @builtins.property
        def queue(self) -> typing.Optional[builtins.str]:
            """``CfnJobTemplate.HopDestinationProperty.Queue``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-hopdestination.html#cfn-mediaconvert-jobtemplate-hopdestination-queue
            """
            result = self._values.get("queue")
            return result

        @builtins.property
        def wait_minutes(self) -> typing.Optional[jsii.Number]:
            """``CfnJobTemplate.HopDestinationProperty.WaitMinutes``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-hopdestination.html#cfn-mediaconvert-jobtemplate-hopdestination-waitminutes
            """
            result = self._values.get("wait_minutes")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HopDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_mediaconvert.CfnJobTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "settings_json": "settingsJson",
        "acceleration_settings": "accelerationSettings",
        "category": "category",
        "description": "description",
        "hop_destinations": "hopDestinations",
        "name": "name",
        "priority": "priority",
        "queue": "queue",
        "status_update_interval": "statusUpdateInterval",
        "tags": "tags",
    },
)
class CfnJobTemplateProps:
    def __init__(
        self,
        *,
        settings_json: typing.Any,
        acceleration_settings: typing.Optional[typing.Union[CfnJobTemplate.AccelerationSettingsProperty, _IResolvable_a771d0ef]] = None,
        category: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        hop_destinations: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnJobTemplate.HopDestinationProperty, _IResolvable_a771d0ef]]]] = None,
        name: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        queue: typing.Optional[builtins.str] = None,
        status_update_interval: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        """Properties for defining a ``AWS::MediaConvert::JobTemplate``.

        :param settings_json: ``AWS::MediaConvert::JobTemplate.SettingsJson``.
        :param acceleration_settings: ``AWS::MediaConvert::JobTemplate.AccelerationSettings``.
        :param category: ``AWS::MediaConvert::JobTemplate.Category``.
        :param description: ``AWS::MediaConvert::JobTemplate.Description``.
        :param hop_destinations: ``AWS::MediaConvert::JobTemplate.HopDestinations``.
        :param name: ``AWS::MediaConvert::JobTemplate.Name``.
        :param priority: ``AWS::MediaConvert::JobTemplate.Priority``.
        :param queue: ``AWS::MediaConvert::JobTemplate.Queue``.
        :param status_update_interval: ``AWS::MediaConvert::JobTemplate.StatusUpdateInterval``.
        :param tags: ``AWS::MediaConvert::JobTemplate.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "settings_json": settings_json,
        }
        if acceleration_settings is not None:
            self._values["acceleration_settings"] = acceleration_settings
        if category is not None:
            self._values["category"] = category
        if description is not None:
            self._values["description"] = description
        if hop_destinations is not None:
            self._values["hop_destinations"] = hop_destinations
        if name is not None:
            self._values["name"] = name
        if priority is not None:
            self._values["priority"] = priority
        if queue is not None:
            self._values["queue"] = queue
        if status_update_interval is not None:
            self._values["status_update_interval"] = status_update_interval
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def settings_json(self) -> typing.Any:
        """``AWS::MediaConvert::JobTemplate.SettingsJson``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-settingsjson
        """
        result = self._values.get("settings_json")
        assert result is not None, "Required property 'settings_json' is missing"
        return result

    @builtins.property
    def acceleration_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnJobTemplate.AccelerationSettingsProperty, _IResolvable_a771d0ef]]:
        """``AWS::MediaConvert::JobTemplate.AccelerationSettings``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-accelerationsettings
        """
        result = self._values.get("acceleration_settings")
        return result

    @builtins.property
    def category(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::JobTemplate.Category``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-category
        """
        result = self._values.get("category")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::JobTemplate.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def hop_destinations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnJobTemplate.HopDestinationProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::MediaConvert::JobTemplate.HopDestinations``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-hopdestinations
        """
        result = self._values.get("hop_destinations")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::JobTemplate.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        """``AWS::MediaConvert::JobTemplate.Priority``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-priority
        """
        result = self._values.get("priority")
        return result

    @builtins.property
    def queue(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::JobTemplate.Queue``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-queue
        """
        result = self._values.get("queue")
        return result

    @builtins.property
    def status_update_interval(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::JobTemplate.StatusUpdateInterval``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-statusupdateinterval
        """
        result = self._values.get("status_update_interval")
        return result

    @builtins.property
    def tags(self) -> typing.Any:
        """``AWS::MediaConvert::JobTemplate.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnJobTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnPreset(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_mediaconvert.CfnPreset",
):
    """A CloudFormation ``AWS::MediaConvert::Preset``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html
    :cloudformationResource: AWS::MediaConvert::Preset
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        settings_json: typing.Any,
        category: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        """Create a new ``AWS::MediaConvert::Preset``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param settings_json: ``AWS::MediaConvert::Preset.SettingsJson``.
        :param category: ``AWS::MediaConvert::Preset.Category``.
        :param description: ``AWS::MediaConvert::Preset.Description``.
        :param name: ``AWS::MediaConvert::Preset.Name``.
        :param tags: ``AWS::MediaConvert::Preset.Tags``.
        """
        props = CfnPresetProps(
            settings_json=settings_json,
            category=category,
            description=description,
            name=name,
            tags=tags,
        )

        jsii.create(CfnPreset, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        """
        :cloudformationAttribute: Name
        """
        return jsii.get(self, "attrName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::MediaConvert::Preset.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="settingsJson")
    def settings_json(self) -> typing.Any:
        """``AWS::MediaConvert::Preset.SettingsJson``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-settingsjson
        """
        return jsii.get(self, "settingsJson")

    @settings_json.setter # type: ignore
    def settings_json(self, value: typing.Any) -> None:
        jsii.set(self, "settingsJson", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="category")
    def category(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::Preset.Category``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-category
        """
        return jsii.get(self, "category")

    @category.setter # type: ignore
    def category(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "category", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::Preset.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::Preset.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="monocdk.aws_mediaconvert.CfnPresetProps",
    jsii_struct_bases=[],
    name_mapping={
        "settings_json": "settingsJson",
        "category": "category",
        "description": "description",
        "name": "name",
        "tags": "tags",
    },
)
class CfnPresetProps:
    def __init__(
        self,
        *,
        settings_json: typing.Any,
        category: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        """Properties for defining a ``AWS::MediaConvert::Preset``.

        :param settings_json: ``AWS::MediaConvert::Preset.SettingsJson``.
        :param category: ``AWS::MediaConvert::Preset.Category``.
        :param description: ``AWS::MediaConvert::Preset.Description``.
        :param name: ``AWS::MediaConvert::Preset.Name``.
        :param tags: ``AWS::MediaConvert::Preset.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "settings_json": settings_json,
        }
        if category is not None:
            self._values["category"] = category
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def settings_json(self) -> typing.Any:
        """``AWS::MediaConvert::Preset.SettingsJson``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-settingsjson
        """
        result = self._values.get("settings_json")
        assert result is not None, "Required property 'settings_json' is missing"
        return result

    @builtins.property
    def category(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::Preset.Category``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-category
        """
        result = self._values.get("category")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::Preset.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::Preset.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def tags(self) -> typing.Any:
        """``AWS::MediaConvert::Preset.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPresetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnQueue(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_mediaconvert.CfnQueue",
):
    """A CloudFormation ``AWS::MediaConvert::Queue``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html
    :cloudformationResource: AWS::MediaConvert::Queue
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        pricing_plan: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        """Create a new ``AWS::MediaConvert::Queue``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::MediaConvert::Queue.Description``.
        :param name: ``AWS::MediaConvert::Queue.Name``.
        :param pricing_plan: ``AWS::MediaConvert::Queue.PricingPlan``.
        :param status: ``AWS::MediaConvert::Queue.Status``.
        :param tags: ``AWS::MediaConvert::Queue.Tags``.
        """
        props = CfnQueueProps(
            description=description,
            name=name,
            pricing_plan=pricing_plan,
            status=status,
            tags=tags,
        )

        jsii.create(CfnQueue, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        """
        :cloudformationAttribute: Name
        """
        return jsii.get(self, "attrName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::MediaConvert::Queue.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::Queue.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::Queue.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="pricingPlan")
    def pricing_plan(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::Queue.PricingPlan``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-pricingplan
        """
        return jsii.get(self, "pricingPlan")

    @pricing_plan.setter # type: ignore
    def pricing_plan(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "pricingPlan", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::Queue.Status``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-status
        """
        return jsii.get(self, "status")

    @status.setter # type: ignore
    def status(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="monocdk.aws_mediaconvert.CfnQueueProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "name": "name",
        "pricing_plan": "pricingPlan",
        "status": "status",
        "tags": "tags",
    },
)
class CfnQueueProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        pricing_plan: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        """Properties for defining a ``AWS::MediaConvert::Queue``.

        :param description: ``AWS::MediaConvert::Queue.Description``.
        :param name: ``AWS::MediaConvert::Queue.Name``.
        :param pricing_plan: ``AWS::MediaConvert::Queue.PricingPlan``.
        :param status: ``AWS::MediaConvert::Queue.Status``.
        :param tags: ``AWS::MediaConvert::Queue.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if pricing_plan is not None:
            self._values["pricing_plan"] = pricing_plan
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::Queue.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::Queue.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def pricing_plan(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::Queue.PricingPlan``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-pricingplan
        """
        result = self._values.get("pricing_plan")
        return result

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        """``AWS::MediaConvert::Queue.Status``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-status
        """
        result = self._values.get("status")
        return result

    @builtins.property
    def tags(self) -> typing.Any:
        """``AWS::MediaConvert::Queue.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQueueProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnJobTemplate",
    "CfnJobTemplateProps",
    "CfnPreset",
    "CfnPresetProps",
    "CfnQueue",
    "CfnQueueProps",
]

publication.publish()
