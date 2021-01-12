# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'ActionHttpRunAfterArgs',
]

@pulumi.input_type
class ActionHttpRunAfterArgs:
    def __init__(__self__, *,
                 action_name: pulumi.Input[str],
                 action_result: pulumi.Input[str]):
        """
        :param pulumi.Input[str] action_name: Specifies the name of the precedent HTTP Action.
        :param pulumi.Input[str] action_result: Specifies the expected result of the precedent HTTP Action, only after which the current HTTP Action will be triggered. Possible values include `Succeeded`, `Failed`, `Skipped` and `TimedOut`.
        """
        pulumi.set(__self__, "action_name", action_name)
        pulumi.set(__self__, "action_result", action_result)

    @property
    @pulumi.getter(name="actionName")
    def action_name(self) -> pulumi.Input[str]:
        """
        Specifies the name of the precedent HTTP Action.
        """
        return pulumi.get(self, "action_name")

    @action_name.setter
    def action_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "action_name", value)

    @property
    @pulumi.getter(name="actionResult")
    def action_result(self) -> pulumi.Input[str]:
        """
        Specifies the expected result of the precedent HTTP Action, only after which the current HTTP Action will be triggered. Possible values include `Succeeded`, `Failed`, `Skipped` and `TimedOut`.
        """
        return pulumi.get(self, "action_result")

    @action_result.setter
    def action_result(self, value: pulumi.Input[str]):
        pulumi.set(self, "action_result", value)


