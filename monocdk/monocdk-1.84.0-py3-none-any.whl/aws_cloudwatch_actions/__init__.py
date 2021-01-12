import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

from .. import Construct as _Construct_e78e779f
from ..aws_applicationautoscaling import (
    StepScalingAction as _StepScalingAction_20c2d829
)
from ..aws_autoscaling import StepScalingAction as _StepScalingAction_569c9499
from ..aws_cloudwatch import (
    AlarmActionConfig as _AlarmActionConfig_aebdae35,
    IAlarm as _IAlarm_bf66c8d0,
    IAlarmAction as _IAlarmAction_22055cd4,
)
from ..aws_sns import ITopic as _ITopic_465e36b9


@jsii.implements(_IAlarmAction_22055cd4)
class ApplicationScalingAction(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudwatch_actions.ApplicationScalingAction",
):
    """(experimental) Use an ApplicationAutoScaling StepScalingAction as an Alarm Action.

    :stability: experimental
    """

    def __init__(self, step_scaling_action: _StepScalingAction_20c2d829) -> None:
        """
        :param step_scaling_action: -

        :stability: experimental
        """
        jsii.create(ApplicationScalingAction, self, [step_scaling_action])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _Construct_e78e779f,
        _alarm: _IAlarm_bf66c8d0,
    ) -> _AlarmActionConfig_aebdae35:
        """(experimental) Returns an alarm action configuration to use an ApplicationScaling StepScalingAction as an alarm action.

        :param _scope: -
        :param _alarm: -

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [_scope, _alarm])


@jsii.implements(_IAlarmAction_22055cd4)
class AutoScalingAction(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudwatch_actions.AutoScalingAction",
):
    """(experimental) Use an AutoScaling StepScalingAction as an Alarm Action.

    :stability: experimental
    """

    def __init__(self, step_scaling_action: _StepScalingAction_569c9499) -> None:
        """
        :param step_scaling_action: -

        :stability: experimental
        """
        jsii.create(AutoScalingAction, self, [step_scaling_action])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _Construct_e78e779f,
        _alarm: _IAlarm_bf66c8d0,
    ) -> _AlarmActionConfig_aebdae35:
        """(experimental) Returns an alarm action configuration to use an AutoScaling StepScalingAction as an alarm action.

        :param _scope: -
        :param _alarm: -

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [_scope, _alarm])


@jsii.implements(_IAlarmAction_22055cd4)
class SnsAction(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudwatch_actions.SnsAction",
):
    """(experimental) Use an SNS topic as an alarm action.

    :stability: experimental
    """

    def __init__(self, topic: _ITopic_465e36b9) -> None:
        """
        :param topic: -

        :stability: experimental
        """
        jsii.create(SnsAction, self, [topic])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _Construct_e78e779f,
        _alarm: _IAlarm_bf66c8d0,
    ) -> _AlarmActionConfig_aebdae35:
        """(experimental) Returns an alarm action configuration to use an SNS topic as an alarm action.

        :param _scope: -
        :param _alarm: -

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [_scope, _alarm])


__all__ = [
    "ApplicationScalingAction",
    "AutoScalingAction",
    "SnsAction",
]

publication.publish()
