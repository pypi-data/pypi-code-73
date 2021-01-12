import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

import constructs
from .. import (
    CfnResource as _CfnResource_e0a482dc,
    CfnTag as _CfnTag_95fbdc29,
    Construct as _Construct_e78e779f,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    Resource as _Resource_abff4495,
    TagManager as _TagManager_0b7ab120,
    TreeInspector as _TreeInspector_1cd1894e,
)
from ..aws_events import (
    EventPattern as _EventPattern_a23fbf37,
    IRuleTarget as _IRuleTarget_d45ec729,
    OnEventOptions as _OnEventOptions_d5081088,
    Rule as _Rule_6cfff189,
)
from ..aws_kms import IKey as _IKey_36930160
from ..aws_lambda import IFunction as _IFunction_6e14f09e
from ..aws_logs import (
    ILogGroup as _ILogGroup_846e17a0, RetentionDays as _RetentionDays_6c560d31
)
from ..aws_s3 import IBucket as _IBucket_73486e29
from ..aws_sns import ITopic as _ITopic_465e36b9


@jsii.data_type(
    jsii_type="monocdk.aws_cloudtrail.AddEventSelectorOptions",
    jsii_struct_bases=[],
    name_mapping={
        "include_management_events": "includeManagementEvents",
        "read_write_type": "readWriteType",
    },
)
class AddEventSelectorOptions:
    def __init__(
        self,
        *,
        include_management_events: typing.Optional[builtins.bool] = None,
        read_write_type: typing.Optional["ReadWriteType"] = None,
    ) -> None:
        """(experimental) Options for adding an event selector.

        :param include_management_events: (experimental) Specifies whether the event selector includes management events for the trail. Default: true
        :param read_write_type: (experimental) Specifies whether to log read-only events, write-only events, or all events. Default: ReadWriteType.All

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if include_management_events is not None:
            self._values["include_management_events"] = include_management_events
        if read_write_type is not None:
            self._values["read_write_type"] = read_write_type

    @builtins.property
    def include_management_events(self) -> typing.Optional[builtins.bool]:
        """(experimental) Specifies whether the event selector includes management events for the trail.

        :default: true

        :stability: experimental
        """
        result = self._values.get("include_management_events")
        return result

    @builtins.property
    def read_write_type(self) -> typing.Optional["ReadWriteType"]:
        """(experimental) Specifies whether to log read-only events, write-only events, or all events.

        :default: ReadWriteType.All

        :stability: experimental
        """
        result = self._values.get("read_write_type")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddEventSelectorOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnTrail(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudtrail.CfnTrail",
):
    """A CloudFormation ``AWS::CloudTrail::Trail``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html
    :cloudformationResource: AWS::CloudTrail::Trail
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        is_logging: typing.Union[builtins.bool, _IResolvable_a771d0ef],
        s3_bucket_name: builtins.str,
        cloud_watch_logs_log_group_arn: typing.Optional[builtins.str] = None,
        cloud_watch_logs_role_arn: typing.Optional[builtins.str] = None,
        enable_log_file_validation: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        event_selectors: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTrail.EventSelectorProperty", _IResolvable_a771d0ef]]]] = None,
        include_global_service_events: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        is_multi_region_trail: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        sns_topic_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
        trail_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::CloudTrail::Trail``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param is_logging: ``AWS::CloudTrail::Trail.IsLogging``.
        :param s3_bucket_name: ``AWS::CloudTrail::Trail.S3BucketName``.
        :param cloud_watch_logs_log_group_arn: ``AWS::CloudTrail::Trail.CloudWatchLogsLogGroupArn``.
        :param cloud_watch_logs_role_arn: ``AWS::CloudTrail::Trail.CloudWatchLogsRoleArn``.
        :param enable_log_file_validation: ``AWS::CloudTrail::Trail.EnableLogFileValidation``.
        :param event_selectors: ``AWS::CloudTrail::Trail.EventSelectors``.
        :param include_global_service_events: ``AWS::CloudTrail::Trail.IncludeGlobalServiceEvents``.
        :param is_multi_region_trail: ``AWS::CloudTrail::Trail.IsMultiRegionTrail``.
        :param kms_key_id: ``AWS::CloudTrail::Trail.KMSKeyId``.
        :param s3_key_prefix: ``AWS::CloudTrail::Trail.S3KeyPrefix``.
        :param sns_topic_name: ``AWS::CloudTrail::Trail.SnsTopicName``.
        :param tags: ``AWS::CloudTrail::Trail.Tags``.
        :param trail_name: ``AWS::CloudTrail::Trail.TrailName``.
        """
        props = CfnTrailProps(
            is_logging=is_logging,
            s3_bucket_name=s3_bucket_name,
            cloud_watch_logs_log_group_arn=cloud_watch_logs_log_group_arn,
            cloud_watch_logs_role_arn=cloud_watch_logs_role_arn,
            enable_log_file_validation=enable_log_file_validation,
            event_selectors=event_selectors,
            include_global_service_events=include_global_service_events,
            is_multi_region_trail=is_multi_region_trail,
            kms_key_id=kms_key_id,
            s3_key_prefix=s3_key_prefix,
            sns_topic_name=sns_topic_name,
            tags=tags,
            trail_name=trail_name,
        )

        jsii.create(CfnTrail, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrSnsTopicArn")
    def attr_sns_topic_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: SnsTopicArn
        """
        return jsii.get(self, "attrSnsTopicArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::CloudTrail::Trail.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isLogging")
    def is_logging(self) -> typing.Union[builtins.bool, _IResolvable_a771d0ef]:
        """``AWS::CloudTrail::Trail.IsLogging``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-islogging
        """
        return jsii.get(self, "isLogging")

    @is_logging.setter # type: ignore
    def is_logging(
        self,
        value: typing.Union[builtins.bool, _IResolvable_a771d0ef],
    ) -> None:
        jsii.set(self, "isLogging", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="s3BucketName")
    def s3_bucket_name(self) -> builtins.str:
        """``AWS::CloudTrail::Trail.S3BucketName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3bucketname
        """
        return jsii.get(self, "s3BucketName")

    @s3_bucket_name.setter # type: ignore
    def s3_bucket_name(self, value: builtins.str) -> None:
        jsii.set(self, "s3BucketName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cloudWatchLogsLogGroupArn")
    def cloud_watch_logs_log_group_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::CloudTrail::Trail.CloudWatchLogsLogGroupArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsloggrouparn
        """
        return jsii.get(self, "cloudWatchLogsLogGroupArn")

    @cloud_watch_logs_log_group_arn.setter # type: ignore
    def cloud_watch_logs_log_group_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "cloudWatchLogsLogGroupArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cloudWatchLogsRoleArn")
    def cloud_watch_logs_role_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::CloudTrail::Trail.CloudWatchLogsRoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsrolearn
        """
        return jsii.get(self, "cloudWatchLogsRoleArn")

    @cloud_watch_logs_role_arn.setter # type: ignore
    def cloud_watch_logs_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "cloudWatchLogsRoleArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="enableLogFileValidation")
    def enable_log_file_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::CloudTrail::Trail.EnableLogFileValidation``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-enablelogfilevalidation
        """
        return jsii.get(self, "enableLogFileValidation")

    @enable_log_file_validation.setter # type: ignore
    def enable_log_file_validation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "enableLogFileValidation", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="eventSelectors")
    def event_selectors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTrail.EventSelectorProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::CloudTrail::Trail.EventSelectors``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-eventselectors
        """
        return jsii.get(self, "eventSelectors")

    @event_selectors.setter # type: ignore
    def event_selectors(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTrail.EventSelectorProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "eventSelectors", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="includeGlobalServiceEvents")
    def include_global_service_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::CloudTrail::Trail.IncludeGlobalServiceEvents``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-includeglobalserviceevents
        """
        return jsii.get(self, "includeGlobalServiceEvents")

    @include_global_service_events.setter # type: ignore
    def include_global_service_events(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "includeGlobalServiceEvents", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isMultiRegionTrail")
    def is_multi_region_trail(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::CloudTrail::Trail.IsMultiRegionTrail``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-ismultiregiontrail
        """
        return jsii.get(self, "isMultiRegionTrail")

    @is_multi_region_trail.setter # type: ignore
    def is_multi_region_trail(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "isMultiRegionTrail", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        """``AWS::CloudTrail::Trail.KMSKeyId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-kmskeyid
        """
        return jsii.get(self, "kmsKeyId")

    @kms_key_id.setter # type: ignore
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="s3KeyPrefix")
    def s3_key_prefix(self) -> typing.Optional[builtins.str]:
        """``AWS::CloudTrail::Trail.S3KeyPrefix``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3keyprefix
        """
        return jsii.get(self, "s3KeyPrefix")

    @s3_key_prefix.setter # type: ignore
    def s3_key_prefix(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "s3KeyPrefix", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="snsTopicName")
    def sns_topic_name(self) -> typing.Optional[builtins.str]:
        """``AWS::CloudTrail::Trail.SnsTopicName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-snstopicname
        """
        return jsii.get(self, "snsTopicName")

    @sns_topic_name.setter # type: ignore
    def sns_topic_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "snsTopicName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="trailName")
    def trail_name(self) -> typing.Optional[builtins.str]:
        """``AWS::CloudTrail::Trail.TrailName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-trailname
        """
        return jsii.get(self, "trailName")

    @trail_name.setter # type: ignore
    def trail_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "trailName", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_cloudtrail.CfnTrail.DataResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "values": "values"},
    )
    class DataResourceProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            values: typing.Optional[typing.List[builtins.str]] = None,
        ) -> None:
            """
            :param type: ``CfnTrail.DataResourceProperty.Type``.
            :param values: ``CfnTrail.DataResourceProperty.Values``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-dataresource.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
            }
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def type(self) -> builtins.str:
            """``CfnTrail.DataResourceProperty.Type``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-dataresource.html#cfn-cloudtrail-trail-dataresource-type
            """
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return result

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnTrail.DataResourceProperty.Values``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-dataresource.html#cfn-cloudtrail-trail-dataresource-values
            """
            result = self._values.get("values")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_cloudtrail.CfnTrail.EventSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_resources": "dataResources",
            "include_management_events": "includeManagementEvents",
            "read_write_type": "readWriteType",
        },
    )
    class EventSelectorProperty:
        def __init__(
            self,
            *,
            data_resources: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTrail.DataResourceProperty", _IResolvable_a771d0ef]]]] = None,
            include_management_events: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            read_write_type: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param data_resources: ``CfnTrail.EventSelectorProperty.DataResources``.
            :param include_management_events: ``CfnTrail.EventSelectorProperty.IncludeManagementEvents``.
            :param read_write_type: ``CfnTrail.EventSelectorProperty.ReadWriteType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if data_resources is not None:
                self._values["data_resources"] = data_resources
            if include_management_events is not None:
                self._values["include_management_events"] = include_management_events
            if read_write_type is not None:
                self._values["read_write_type"] = read_write_type

        @builtins.property
        def data_resources(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTrail.DataResourceProperty", _IResolvable_a771d0ef]]]]:
            """``CfnTrail.EventSelectorProperty.DataResources``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-dataresources
            """
            result = self._values.get("data_resources")
            return result

        @builtins.property
        def include_management_events(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnTrail.EventSelectorProperty.IncludeManagementEvents``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-includemanagementevents
            """
            result = self._values.get("include_management_events")
            return result

        @builtins.property
        def read_write_type(self) -> typing.Optional[builtins.str]:
            """``CfnTrail.EventSelectorProperty.ReadWriteType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-readwritetype
            """
            result = self._values.get("read_write_type")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_cloudtrail.CfnTrailProps",
    jsii_struct_bases=[],
    name_mapping={
        "is_logging": "isLogging",
        "s3_bucket_name": "s3BucketName",
        "cloud_watch_logs_log_group_arn": "cloudWatchLogsLogGroupArn",
        "cloud_watch_logs_role_arn": "cloudWatchLogsRoleArn",
        "enable_log_file_validation": "enableLogFileValidation",
        "event_selectors": "eventSelectors",
        "include_global_service_events": "includeGlobalServiceEvents",
        "is_multi_region_trail": "isMultiRegionTrail",
        "kms_key_id": "kmsKeyId",
        "s3_key_prefix": "s3KeyPrefix",
        "sns_topic_name": "snsTopicName",
        "tags": "tags",
        "trail_name": "trailName",
    },
)
class CfnTrailProps:
    def __init__(
        self,
        *,
        is_logging: typing.Union[builtins.bool, _IResolvable_a771d0ef],
        s3_bucket_name: builtins.str,
        cloud_watch_logs_log_group_arn: typing.Optional[builtins.str] = None,
        cloud_watch_logs_role_arn: typing.Optional[builtins.str] = None,
        enable_log_file_validation: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        event_selectors: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnTrail.EventSelectorProperty, _IResolvable_a771d0ef]]]] = None,
        include_global_service_events: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        is_multi_region_trail: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        sns_topic_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
        trail_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::CloudTrail::Trail``.

        :param is_logging: ``AWS::CloudTrail::Trail.IsLogging``.
        :param s3_bucket_name: ``AWS::CloudTrail::Trail.S3BucketName``.
        :param cloud_watch_logs_log_group_arn: ``AWS::CloudTrail::Trail.CloudWatchLogsLogGroupArn``.
        :param cloud_watch_logs_role_arn: ``AWS::CloudTrail::Trail.CloudWatchLogsRoleArn``.
        :param enable_log_file_validation: ``AWS::CloudTrail::Trail.EnableLogFileValidation``.
        :param event_selectors: ``AWS::CloudTrail::Trail.EventSelectors``.
        :param include_global_service_events: ``AWS::CloudTrail::Trail.IncludeGlobalServiceEvents``.
        :param is_multi_region_trail: ``AWS::CloudTrail::Trail.IsMultiRegionTrail``.
        :param kms_key_id: ``AWS::CloudTrail::Trail.KMSKeyId``.
        :param s3_key_prefix: ``AWS::CloudTrail::Trail.S3KeyPrefix``.
        :param sns_topic_name: ``AWS::CloudTrail::Trail.SnsTopicName``.
        :param tags: ``AWS::CloudTrail::Trail.Tags``.
        :param trail_name: ``AWS::CloudTrail::Trail.TrailName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "is_logging": is_logging,
            "s3_bucket_name": s3_bucket_name,
        }
        if cloud_watch_logs_log_group_arn is not None:
            self._values["cloud_watch_logs_log_group_arn"] = cloud_watch_logs_log_group_arn
        if cloud_watch_logs_role_arn is not None:
            self._values["cloud_watch_logs_role_arn"] = cloud_watch_logs_role_arn
        if enable_log_file_validation is not None:
            self._values["enable_log_file_validation"] = enable_log_file_validation
        if event_selectors is not None:
            self._values["event_selectors"] = event_selectors
        if include_global_service_events is not None:
            self._values["include_global_service_events"] = include_global_service_events
        if is_multi_region_trail is not None:
            self._values["is_multi_region_trail"] = is_multi_region_trail
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if s3_key_prefix is not None:
            self._values["s3_key_prefix"] = s3_key_prefix
        if sns_topic_name is not None:
            self._values["sns_topic_name"] = sns_topic_name
        if tags is not None:
            self._values["tags"] = tags
        if trail_name is not None:
            self._values["trail_name"] = trail_name

    @builtins.property
    def is_logging(self) -> typing.Union[builtins.bool, _IResolvable_a771d0ef]:
        """``AWS::CloudTrail::Trail.IsLogging``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-islogging
        """
        result = self._values.get("is_logging")
        assert result is not None, "Required property 'is_logging' is missing"
        return result

    @builtins.property
    def s3_bucket_name(self) -> builtins.str:
        """``AWS::CloudTrail::Trail.S3BucketName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3bucketname
        """
        result = self._values.get("s3_bucket_name")
        assert result is not None, "Required property 's3_bucket_name' is missing"
        return result

    @builtins.property
    def cloud_watch_logs_log_group_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::CloudTrail::Trail.CloudWatchLogsLogGroupArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsloggrouparn
        """
        result = self._values.get("cloud_watch_logs_log_group_arn")
        return result

    @builtins.property
    def cloud_watch_logs_role_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::CloudTrail::Trail.CloudWatchLogsRoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsrolearn
        """
        result = self._values.get("cloud_watch_logs_role_arn")
        return result

    @builtins.property
    def enable_log_file_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::CloudTrail::Trail.EnableLogFileValidation``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-enablelogfilevalidation
        """
        result = self._values.get("enable_log_file_validation")
        return result

    @builtins.property
    def event_selectors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnTrail.EventSelectorProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::CloudTrail::Trail.EventSelectors``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-eventselectors
        """
        result = self._values.get("event_selectors")
        return result

    @builtins.property
    def include_global_service_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::CloudTrail::Trail.IncludeGlobalServiceEvents``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-includeglobalserviceevents
        """
        result = self._values.get("include_global_service_events")
        return result

    @builtins.property
    def is_multi_region_trail(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::CloudTrail::Trail.IsMultiRegionTrail``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-ismultiregiontrail
        """
        result = self._values.get("is_multi_region_trail")
        return result

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        """``AWS::CloudTrail::Trail.KMSKeyId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-kmskeyid
        """
        result = self._values.get("kms_key_id")
        return result

    @builtins.property
    def s3_key_prefix(self) -> typing.Optional[builtins.str]:
        """``AWS::CloudTrail::Trail.S3KeyPrefix``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3keyprefix
        """
        result = self._values.get("s3_key_prefix")
        return result

    @builtins.property
    def sns_topic_name(self) -> typing.Optional[builtins.str]:
        """``AWS::CloudTrail::Trail.SnsTopicName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-snstopicname
        """
        result = self._values.get("sns_topic_name")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        """``AWS::CloudTrail::Trail.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-tags
        """
        result = self._values.get("tags")
        return result

    @builtins.property
    def trail_name(self) -> typing.Optional[builtins.str]:
        """``AWS::CloudTrail::Trail.TrailName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-trailname
        """
        result = self._values.get("trail_name")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTrailProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk.aws_cloudtrail.DataResourceType")
class DataResourceType(enum.Enum):
    """(experimental) Resource type for a data event.

    :stability: experimental
    """

    LAMBDA_FUNCTION = "LAMBDA_FUNCTION"
    """(experimental) Data resource type for Lambda function.

    :stability: experimental
    """
    S3_OBJECT = "S3_OBJECT"
    """(experimental) Data resource type for S3 objects.

    :stability: experimental
    """


@jsii.enum(jsii_type="monocdk.aws_cloudtrail.ReadWriteType")
class ReadWriteType(enum.Enum):
    """(experimental) Types of events that CloudTrail can log.

    :stability: experimental
    """

    READ_ONLY = "READ_ONLY"
    """(experimental) Read-only events include API operations that read your resources, but don't make changes.

    For example, read-only events include the Amazon EC2 DescribeSecurityGroups
    and DescribeSubnets API operations.

    :stability: experimental
    """
    WRITE_ONLY = "WRITE_ONLY"
    """(experimental) Write-only events include API operations that modify (or might modify) your resources.

    For example, the Amazon EC2 RunInstances and TerminateInstances API
    operations modify your instances.

    :stability: experimental
    """
    ALL = "ALL"
    """(experimental) All events.

    :stability: experimental
    """
    NONE = "NONE"
    """(experimental) No events.

    :stability: experimental
    """


@jsii.data_type(
    jsii_type="monocdk.aws_cloudtrail.S3EventSelector",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "object_prefix": "objectPrefix"},
)
class S3EventSelector:
    def __init__(
        self,
        *,
        bucket: _IBucket_73486e29,
        object_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Selecting an S3 bucket and an optional prefix to be logged for data events.

        :param bucket: (experimental) S3 bucket.
        :param object_prefix: (experimental) Data events for objects whose key matches this prefix will be logged. Default: - all objects

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
        }
        if object_prefix is not None:
            self._values["object_prefix"] = object_prefix

    @builtins.property
    def bucket(self) -> _IBucket_73486e29:
        """(experimental) S3 bucket.

        :stability: experimental
        """
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return result

    @builtins.property
    def object_prefix(self) -> typing.Optional[builtins.str]:
        """(experimental) Data events for objects whose key matches this prefix will be logged.

        :default: - all objects

        :stability: experimental
        """
        result = self._values.get("object_prefix")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3EventSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Trail(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudtrail.Trail",
):
    """(experimental) Cloud trail allows you to log events that happen in your AWS account For example:.

    import { CloudTrail } from '@aws-cdk/aws-cloudtrail'

    const cloudTrail = new CloudTrail(this, 'MyTrail');

    NOTE the above example creates an UNENCRYPTED bucket by default,
    If you are required to use an Encrypted bucket you can supply a preconfigured bucket
    via TrailProps

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        bucket: typing.Optional[_IBucket_73486e29] = None,
        cloud_watch_log_group: typing.Optional[_ILogGroup_846e17a0] = None,
        cloud_watch_logs_retention: typing.Optional[_RetentionDays_6c560d31] = None,
        enable_file_validation: typing.Optional[builtins.bool] = None,
        encryption_key: typing.Optional[_IKey_36930160] = None,
        include_global_service_events: typing.Optional[builtins.bool] = None,
        is_multi_region_trail: typing.Optional[builtins.bool] = None,
        kms_key: typing.Optional[_IKey_36930160] = None,
        management_events: typing.Optional[ReadWriteType] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        send_to_cloud_watch_logs: typing.Optional[builtins.bool] = None,
        sns_topic: typing.Optional[_ITopic_465e36b9] = None,
        trail_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param bucket: (experimental) The Amazon S3 bucket. Default: - if not supplied a bucket will be created with all the correct permisions
        :param cloud_watch_log_group: (experimental) Log Group to which CloudTrail to push logs to. Ignored if sendToCloudWatchLogs is set to false. Default: - a new log group is created and used.
        :param cloud_watch_logs_retention: (experimental) How long to retain logs in CloudWatchLogs. Ignored if sendToCloudWatchLogs is false or if cloudWatchLogGroup is set. Default: logs.RetentionDays.ONE_YEAR
        :param enable_file_validation: (experimental) To determine whether a log file was modified, deleted, or unchanged after CloudTrail delivered it, you can use CloudTrail log file integrity validation. This feature is built using industry standard algorithms: SHA-256 for hashing and SHA-256 with RSA for digital signing. This makes it computationally infeasible to modify, delete or forge CloudTrail log files without detection. You can use the AWS CLI to validate the files in the location where CloudTrail delivered them. Default: true
        :param encryption_key: (experimental) The AWS Key Management Service (AWS KMS) key ID that you want to use to encrypt CloudTrail logs. Default: - No encryption.
        :param include_global_service_events: (experimental) For most services, events are recorded in the region where the action occurred. For global services such as AWS Identity and Access Management (IAM), AWS STS, Amazon CloudFront, and Route 53, events are delivered to any trail that includes global services, and are logged as occurring in US East (N. Virginia) Region. Default: true
        :param is_multi_region_trail: (experimental) Whether or not this trail delivers log files from multiple regions to a single S3 bucket for a single account. Default: true
        :param kms_key: (deprecated) The AWS Key Management Service (AWS KMS) key ID that you want to use to encrypt CloudTrail logs. Default: - No encryption.
        :param management_events: (experimental) When an event occurs in your account, CloudTrail evaluates whether the event matches the settings for your trails. Only events that match your trail settings are delivered to your Amazon S3 bucket and Amazon CloudWatch Logs log group. This method sets the management configuration for this trail. Management events provide insight into management operations that are performed on resources in your AWS account. These are also known as control plane operations. Management events can also include non-API events that occur in your account. For example, when a user logs in to your account, CloudTrail logs the ConsoleLogin event. Default: ReadWriteType.ALL
        :param s3_key_prefix: (experimental) An Amazon S3 object key prefix that precedes the name of all log files. Default: - No prefix.
        :param send_to_cloud_watch_logs: (experimental) If CloudTrail pushes logs to CloudWatch Logs in addition to S3. Disabled for cost out of the box. Default: false
        :param sns_topic: (experimental) SNS topic that is notified when new log files are published. Default: - No notifications.
        :param trail_name: (experimental) The name of the trail. We recoomend customers do not set an explicit name. Default: - AWS CloudFormation generated name.

        :stability: experimental
        """
        props = TrailProps(
            bucket=bucket,
            cloud_watch_log_group=cloud_watch_log_group,
            cloud_watch_logs_retention=cloud_watch_logs_retention,
            enable_file_validation=enable_file_validation,
            encryption_key=encryption_key,
            include_global_service_events=include_global_service_events,
            is_multi_region_trail=is_multi_region_trail,
            kms_key=kms_key,
            management_events=management_events,
            s3_key_prefix=s3_key_prefix,
            send_to_cloud_watch_logs=send_to_cloud_watch_logs,
            sns_topic=sns_topic,
            trail_name=trail_name,
        )

        jsii.create(Trail, self, [scope, id, props])

    @jsii.member(jsii_name="onEvent")
    @builtins.classmethod
    def on_event(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[_EventPattern_a23fbf37] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[_IRuleTarget_d45ec729] = None,
    ) -> _Rule_6cfff189:
        """(experimental) Create an event rule for when an event is recorded by any Trail in the account.

        Note that the event doesn't necessarily have to come from this Trail, it can
        be captured from any one.

        Be sure to filter the event further down using an event pattern.

        :param scope: -
        :param id: -
        :param description: (experimental) A description of the rule's purpose. Default: - No description
        :param event_pattern: (experimental) Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: (experimental) A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: (experimental) The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.

        :stability: experimental
        """
        options = _OnEventOptions_d5081088(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return jsii.sinvoke(cls, "onEvent", [scope, id, options])

    @jsii.member(jsii_name="addEventSelector")
    def add_event_selector(
        self,
        data_resource_type: DataResourceType,
        data_resource_values: typing.List[builtins.str],
        *,
        include_management_events: typing.Optional[builtins.bool] = None,
        read_write_type: typing.Optional[ReadWriteType] = None,
    ) -> None:
        """(experimental) When an event occurs in your account, CloudTrail evaluates whether the event matches the settings for your trails.

        Only events that match your trail settings are delivered to your Amazon S3 bucket and Amazon CloudWatch Logs log group.

        This method adds an Event Selector for filtering events that match either S3 or Lambda function operations.

        Data events: These events provide insight into the resource operations performed on or within a resource.
        These are also known as data plane operations.

        :param data_resource_type: -
        :param data_resource_values: the list of data resource ARNs to include in logging (maximum 250 entries).
        :param include_management_events: (experimental) Specifies whether the event selector includes management events for the trail. Default: true
        :param read_write_type: (experimental) Specifies whether to log read-only events, write-only events, or all events. Default: ReadWriteType.All

        :stability: experimental
        """
        options = AddEventSelectorOptions(
            include_management_events=include_management_events,
            read_write_type=read_write_type,
        )

        return jsii.invoke(self, "addEventSelector", [data_resource_type, data_resource_values, options])

    @jsii.member(jsii_name="addLambdaEventSelector")
    def add_lambda_event_selector(
        self,
        handlers: typing.List[_IFunction_6e14f09e],
        *,
        include_management_events: typing.Optional[builtins.bool] = None,
        read_write_type: typing.Optional[ReadWriteType] = None,
    ) -> None:
        """(experimental) When an event occurs in your account, CloudTrail evaluates whether the event matches the settings for your trails.

        Only events that match your trail settings are delivered to your Amazon S3 bucket and Amazon CloudWatch Logs log group.

        This method adds a Lambda Data Event Selector for filtering events that match Lambda function operations.

        Data events: These events provide insight into the resource operations performed on or within a resource.
        These are also known as data plane operations.

        :param handlers: the list of lambda function handlers whose data events should be logged (maximum 250 entries).
        :param include_management_events: (experimental) Specifies whether the event selector includes management events for the trail. Default: true
        :param read_write_type: (experimental) Specifies whether to log read-only events, write-only events, or all events. Default: ReadWriteType.All

        :stability: experimental
        """
        options = AddEventSelectorOptions(
            include_management_events=include_management_events,
            read_write_type=read_write_type,
        )

        return jsii.invoke(self, "addLambdaEventSelector", [handlers, options])

    @jsii.member(jsii_name="addS3EventSelector")
    def add_s3_event_selector(
        self,
        s3_selector: typing.List[S3EventSelector],
        *,
        include_management_events: typing.Optional[builtins.bool] = None,
        read_write_type: typing.Optional[ReadWriteType] = None,
    ) -> None:
        """(experimental) When an event occurs in your account, CloudTrail evaluates whether the event matches the settings for your trails.

        Only events that match your trail settings are delivered to your Amazon S3 bucket and Amazon CloudWatch Logs log group.

        This method adds an S3 Data Event Selector for filtering events that match S3 operations.

        Data events: These events provide insight into the resource operations performed on or within a resource.
        These are also known as data plane operations.

        :param s3_selector: the list of S3 bucket with optional prefix to include in logging (maximum 250 entries).
        :param include_management_events: (experimental) Specifies whether the event selector includes management events for the trail. Default: true
        :param read_write_type: (experimental) Specifies whether to log read-only events, write-only events, or all events. Default: ReadWriteType.All

        :stability: experimental
        """
        options = AddEventSelectorOptions(
            include_management_events=include_management_events,
            read_write_type=read_write_type,
        )

        return jsii.invoke(self, "addS3EventSelector", [s3_selector, options])

    @jsii.member(jsii_name="logAllLambdaDataEvents")
    def log_all_lambda_data_events(
        self,
        *,
        include_management_events: typing.Optional[builtins.bool] = None,
        read_write_type: typing.Optional[ReadWriteType] = None,
    ) -> None:
        """(experimental) Log all Lamda data events for all lambda functions the account.

        :param include_management_events: (experimental) Specifies whether the event selector includes management events for the trail. Default: true
        :param read_write_type: (experimental) Specifies whether to log read-only events, write-only events, or all events. Default: ReadWriteType.All

        :default: false

        :see: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html
        :stability: experimental
        """
        options = AddEventSelectorOptions(
            include_management_events=include_management_events,
            read_write_type=read_write_type,
        )

        return jsii.invoke(self, "logAllLambdaDataEvents", [options])

    @jsii.member(jsii_name="logAllS3DataEvents")
    def log_all_s3_data_events(
        self,
        *,
        include_management_events: typing.Optional[builtins.bool] = None,
        read_write_type: typing.Optional[ReadWriteType] = None,
    ) -> None:
        """(experimental) Log all S3 data events for all objects for all buckets in the account.

        :param include_management_events: (experimental) Specifies whether the event selector includes management events for the trail. Default: true
        :param read_write_type: (experimental) Specifies whether to log read-only events, write-only events, or all events. Default: ReadWriteType.All

        :default: false

        :see: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html
        :stability: experimental
        """
        options = AddEventSelectorOptions(
            include_management_events=include_management_events,
            read_write_type=read_write_type,
        )

        return jsii.invoke(self, "logAllS3DataEvents", [options])

    @jsii.member(jsii_name="onCloudTrailEvent")
    def on_cloud_trail_event(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[_EventPattern_a23fbf37] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[_IRuleTarget_d45ec729] = None,
    ) -> _Rule_6cfff189:
        """(deprecated) Create an event rule for when an event is recorded by any Trail in the account.

        Note that the event doesn't necessarily have to come from this Trail, it can
        be captured from any one.

        Be sure to filter the event further down using an event pattern.

        :param id: -
        :param description: (experimental) A description of the rule's purpose. Default: - No description
        :param event_pattern: (experimental) Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: (experimental) A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: (experimental) The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.

        :deprecated: - use Trail.onEvent()

        :stability: deprecated
        """
        options = _OnEventOptions_d5081088(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return jsii.invoke(self, "onCloudTrailEvent", [id, options])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="trailArn")
    def trail_arn(self) -> builtins.str:
        """(experimental) ARN of the CloudTrail trail i.e. arn:aws:cloudtrail:us-east-2:123456789012:trail/myCloudTrail.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "trailArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="trailSnsTopicArn")
    def trail_sns_topic_arn(self) -> builtins.str:
        """(experimental) ARN of the Amazon SNS topic that's associated with the CloudTrail trail, i.e. arn:aws:sns:us-east-2:123456789012:mySNSTopic.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "trailSnsTopicArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="logGroup")
    def log_group(self) -> typing.Optional[_ILogGroup_846e17a0]:
        """(experimental) The CloudWatch log group to which CloudTrail events are sent.

        ``undefined`` if ``sendToCloudWatchLogs`` property is false.

        :stability: experimental
        """
        return jsii.get(self, "logGroup")


@jsii.data_type(
    jsii_type="monocdk.aws_cloudtrail.TrailProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "cloud_watch_log_group": "cloudWatchLogGroup",
        "cloud_watch_logs_retention": "cloudWatchLogsRetention",
        "enable_file_validation": "enableFileValidation",
        "encryption_key": "encryptionKey",
        "include_global_service_events": "includeGlobalServiceEvents",
        "is_multi_region_trail": "isMultiRegionTrail",
        "kms_key": "kmsKey",
        "management_events": "managementEvents",
        "s3_key_prefix": "s3KeyPrefix",
        "send_to_cloud_watch_logs": "sendToCloudWatchLogs",
        "sns_topic": "snsTopic",
        "trail_name": "trailName",
    },
)
class TrailProps:
    def __init__(
        self,
        *,
        bucket: typing.Optional[_IBucket_73486e29] = None,
        cloud_watch_log_group: typing.Optional[_ILogGroup_846e17a0] = None,
        cloud_watch_logs_retention: typing.Optional[_RetentionDays_6c560d31] = None,
        enable_file_validation: typing.Optional[builtins.bool] = None,
        encryption_key: typing.Optional[_IKey_36930160] = None,
        include_global_service_events: typing.Optional[builtins.bool] = None,
        is_multi_region_trail: typing.Optional[builtins.bool] = None,
        kms_key: typing.Optional[_IKey_36930160] = None,
        management_events: typing.Optional[ReadWriteType] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        send_to_cloud_watch_logs: typing.Optional[builtins.bool] = None,
        sns_topic: typing.Optional[_ITopic_465e36b9] = None,
        trail_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Properties for an AWS CloudTrail trail.

        :param bucket: (experimental) The Amazon S3 bucket. Default: - if not supplied a bucket will be created with all the correct permisions
        :param cloud_watch_log_group: (experimental) Log Group to which CloudTrail to push logs to. Ignored if sendToCloudWatchLogs is set to false. Default: - a new log group is created and used.
        :param cloud_watch_logs_retention: (experimental) How long to retain logs in CloudWatchLogs. Ignored if sendToCloudWatchLogs is false or if cloudWatchLogGroup is set. Default: logs.RetentionDays.ONE_YEAR
        :param enable_file_validation: (experimental) To determine whether a log file was modified, deleted, or unchanged after CloudTrail delivered it, you can use CloudTrail log file integrity validation. This feature is built using industry standard algorithms: SHA-256 for hashing and SHA-256 with RSA for digital signing. This makes it computationally infeasible to modify, delete or forge CloudTrail log files without detection. You can use the AWS CLI to validate the files in the location where CloudTrail delivered them. Default: true
        :param encryption_key: (experimental) The AWS Key Management Service (AWS KMS) key ID that you want to use to encrypt CloudTrail logs. Default: - No encryption.
        :param include_global_service_events: (experimental) For most services, events are recorded in the region where the action occurred. For global services such as AWS Identity and Access Management (IAM), AWS STS, Amazon CloudFront, and Route 53, events are delivered to any trail that includes global services, and are logged as occurring in US East (N. Virginia) Region. Default: true
        :param is_multi_region_trail: (experimental) Whether or not this trail delivers log files from multiple regions to a single S3 bucket for a single account. Default: true
        :param kms_key: (deprecated) The AWS Key Management Service (AWS KMS) key ID that you want to use to encrypt CloudTrail logs. Default: - No encryption.
        :param management_events: (experimental) When an event occurs in your account, CloudTrail evaluates whether the event matches the settings for your trails. Only events that match your trail settings are delivered to your Amazon S3 bucket and Amazon CloudWatch Logs log group. This method sets the management configuration for this trail. Management events provide insight into management operations that are performed on resources in your AWS account. These are also known as control plane operations. Management events can also include non-API events that occur in your account. For example, when a user logs in to your account, CloudTrail logs the ConsoleLogin event. Default: ReadWriteType.ALL
        :param s3_key_prefix: (experimental) An Amazon S3 object key prefix that precedes the name of all log files. Default: - No prefix.
        :param send_to_cloud_watch_logs: (experimental) If CloudTrail pushes logs to CloudWatch Logs in addition to S3. Disabled for cost out of the box. Default: false
        :param sns_topic: (experimental) SNS topic that is notified when new log files are published. Default: - No notifications.
        :param trail_name: (experimental) The name of the trail. We recoomend customers do not set an explicit name. Default: - AWS CloudFormation generated name.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket is not None:
            self._values["bucket"] = bucket
        if cloud_watch_log_group is not None:
            self._values["cloud_watch_log_group"] = cloud_watch_log_group
        if cloud_watch_logs_retention is not None:
            self._values["cloud_watch_logs_retention"] = cloud_watch_logs_retention
        if enable_file_validation is not None:
            self._values["enable_file_validation"] = enable_file_validation
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if include_global_service_events is not None:
            self._values["include_global_service_events"] = include_global_service_events
        if is_multi_region_trail is not None:
            self._values["is_multi_region_trail"] = is_multi_region_trail
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if management_events is not None:
            self._values["management_events"] = management_events
        if s3_key_prefix is not None:
            self._values["s3_key_prefix"] = s3_key_prefix
        if send_to_cloud_watch_logs is not None:
            self._values["send_to_cloud_watch_logs"] = send_to_cloud_watch_logs
        if sns_topic is not None:
            self._values["sns_topic"] = sns_topic
        if trail_name is not None:
            self._values["trail_name"] = trail_name

    @builtins.property
    def bucket(self) -> typing.Optional[_IBucket_73486e29]:
        """(experimental) The Amazon S3 bucket.

        :default: - if not supplied a bucket will be created with all the correct permisions

        :stability: experimental
        """
        result = self._values.get("bucket")
        return result

    @builtins.property
    def cloud_watch_log_group(self) -> typing.Optional[_ILogGroup_846e17a0]:
        """(experimental) Log Group to which CloudTrail to push logs to.

        Ignored if sendToCloudWatchLogs is set to false.

        :default: - a new log group is created and used.

        :stability: experimental
        """
        result = self._values.get("cloud_watch_log_group")
        return result

    @builtins.property
    def cloud_watch_logs_retention(self) -> typing.Optional[_RetentionDays_6c560d31]:
        """(experimental) How long to retain logs in CloudWatchLogs.

        Ignored if sendToCloudWatchLogs is false or if cloudWatchLogGroup is set.

        :default: logs.RetentionDays.ONE_YEAR

        :stability: experimental
        """
        result = self._values.get("cloud_watch_logs_retention")
        return result

    @builtins.property
    def enable_file_validation(self) -> typing.Optional[builtins.bool]:
        """(experimental) To determine whether a log file was modified, deleted, or unchanged after CloudTrail delivered it, you can use CloudTrail log file integrity validation.

        This feature is built using industry standard algorithms: SHA-256 for hashing and SHA-256 with RSA for digital signing.
        This makes it computationally infeasible to modify, delete or forge CloudTrail log files without detection.
        You can use the AWS CLI to validate the files in the location where CloudTrail delivered them.

        :default: true

        :stability: experimental
        """
        result = self._values.get("enable_file_validation")
        return result

    @builtins.property
    def encryption_key(self) -> typing.Optional[_IKey_36930160]:
        """(experimental) The AWS Key Management Service (AWS KMS) key ID that you want to use to encrypt CloudTrail logs.

        :default: - No encryption.

        :stability: experimental
        """
        result = self._values.get("encryption_key")
        return result

    @builtins.property
    def include_global_service_events(self) -> typing.Optional[builtins.bool]:
        """(experimental) For most services, events are recorded in the region where the action occurred.

        For global services such as AWS Identity and Access Management (IAM), AWS STS, Amazon CloudFront, and Route 53,
        events are delivered to any trail that includes global services, and are logged as occurring in US East (N. Virginia) Region.

        :default: true

        :stability: experimental
        """
        result = self._values.get("include_global_service_events")
        return result

    @builtins.property
    def is_multi_region_trail(self) -> typing.Optional[builtins.bool]:
        """(experimental) Whether or not this trail delivers log files from multiple regions to a single S3 bucket for a single account.

        :default: true

        :stability: experimental
        """
        result = self._values.get("is_multi_region_trail")
        return result

    @builtins.property
    def kms_key(self) -> typing.Optional[_IKey_36930160]:
        """(deprecated) The AWS Key Management Service (AWS KMS) key ID that you want to use to encrypt CloudTrail logs.

        :default: - No encryption.

        :deprecated: - use encryptionKey instead.

        :stability: deprecated
        """
        result = self._values.get("kms_key")
        return result

    @builtins.property
    def management_events(self) -> typing.Optional[ReadWriteType]:
        """(experimental) When an event occurs in your account, CloudTrail evaluates whether the event matches the settings for your trails.

        Only events that match your trail settings are delivered to your Amazon S3 bucket and Amazon CloudWatch Logs log group.

        This method sets the management configuration for this trail.

        Management events provide insight into management operations that are performed on resources in your AWS account.
        These are also known as control plane operations.
        Management events can also include non-API events that occur in your account.
        For example, when a user logs in to your account, CloudTrail logs the ConsoleLogin event.

        :default: ReadWriteType.ALL

        :stability: experimental
        """
        result = self._values.get("management_events")
        return result

    @builtins.property
    def s3_key_prefix(self) -> typing.Optional[builtins.str]:
        """(experimental) An Amazon S3 object key prefix that precedes the name of all log files.

        :default: - No prefix.

        :stability: experimental
        """
        result = self._values.get("s3_key_prefix")
        return result

    @builtins.property
    def send_to_cloud_watch_logs(self) -> typing.Optional[builtins.bool]:
        """(experimental) If CloudTrail pushes logs to CloudWatch Logs in addition to S3.

        Disabled for cost out of the box.

        :default: false

        :stability: experimental
        """
        result = self._values.get("send_to_cloud_watch_logs")
        return result

    @builtins.property
    def sns_topic(self) -> typing.Optional[_ITopic_465e36b9]:
        """(experimental) SNS topic that is notified when new log files are published.

        :default: - No notifications.

        :stability: experimental
        """
        result = self._values.get("sns_topic")
        return result

    @builtins.property
    def trail_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the trail.

        We recoomend customers do not set an explicit name.

        :default: - AWS CloudFormation generated name.

        :stability: experimental
        """
        result = self._values.get("trail_name")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrailProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AddEventSelectorOptions",
    "CfnTrail",
    "CfnTrailProps",
    "DataResourceType",
    "ReadWriteType",
    "S3EventSelector",
    "Trail",
    "TrailProps",
]

publication.publish()
