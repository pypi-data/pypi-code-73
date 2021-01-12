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

__all__ = ['Schedule']


class Schedule(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expiry_time: Optional[pulumi.Input[str]] = None,
                 frequency: Optional[pulumi.Input[str]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 month_days: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 monthly_occurrences: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScheduleMonthlyOccurrenceArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 timezone: Optional[pulumi.Input[str]] = None,
                 week_days: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Automation Schedule.

        ## Import

        Automation Schedule can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:automation/schedule:Schedule schedule1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Automation/automationAccounts/account1/schedules/schedule1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account in which the Schedule is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] description: A description for this Schedule.
        :param pulumi.Input[str] expiry_time: The end time of the schedule.
        :param pulumi.Input[str] frequency: The frequency of the schedule. - can be either `OneTime`, `Day`, `Hour`, `Week`, or `Month`.
        :param pulumi.Input[int] interval: The number of `frequency`s between runs. Only valid when frequency is `Day`, `Hour`, `Week`, or `Month` and defaults to `1`.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] month_days: List of days of the month that the job should execute on. Must be between `1` and `31`. `-1` for last day of the month. Only valid when frequency is `Month`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScheduleMonthlyOccurrenceArgs']]]] monthly_occurrences: List of occurrences of days within a month. Only valid when frequency is `Month`. The `monthly_occurrence` block supports fields documented below.
        :param pulumi.Input[str] name: Specifies the name of the Schedule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Schedule is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] start_time: Start time of the schedule. Must be at least five minutes in the future. Defaults to seven minutes in the future from the time the resource is created.
        :param pulumi.Input[str] timezone: The timezone of the start time. Defaults to `UTC`. For possible values see: https://s2.automation.ext.azure.com/api/Orchestrator/TimeZones?_=1594792230258
        :param pulumi.Input[Sequence[pulumi.Input[str]]] week_days: List of days of the week that the job should execute on. Only valid when frequency is `Week`.
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

            if automation_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'automation_account_name'")
            __props__['automation_account_name'] = automation_account_name
            __props__['description'] = description
            __props__['expiry_time'] = expiry_time
            if frequency is None and not opts.urn:
                raise TypeError("Missing required property 'frequency'")
            __props__['frequency'] = frequency
            __props__['interval'] = interval
            __props__['month_days'] = month_days
            __props__['monthly_occurrences'] = monthly_occurrences
            __props__['name'] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['start_time'] = start_time
            __props__['timezone'] = timezone
            __props__['week_days'] = week_days
        super(Schedule, __self__).__init__(
            'azure:automation/schedule:Schedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            automation_account_name: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            expiry_time: Optional[pulumi.Input[str]] = None,
            frequency: Optional[pulumi.Input[str]] = None,
            interval: Optional[pulumi.Input[int]] = None,
            month_days: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            monthly_occurrences: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScheduleMonthlyOccurrenceArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            start_time: Optional[pulumi.Input[str]] = None,
            timezone: Optional[pulumi.Input[str]] = None,
            week_days: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'Schedule':
        """
        Get an existing Schedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account in which the Schedule is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] description: A description for this Schedule.
        :param pulumi.Input[str] expiry_time: The end time of the schedule.
        :param pulumi.Input[str] frequency: The frequency of the schedule. - can be either `OneTime`, `Day`, `Hour`, `Week`, or `Month`.
        :param pulumi.Input[int] interval: The number of `frequency`s between runs. Only valid when frequency is `Day`, `Hour`, `Week`, or `Month` and defaults to `1`.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] month_days: List of days of the month that the job should execute on. Must be between `1` and `31`. `-1` for last day of the month. Only valid when frequency is `Month`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScheduleMonthlyOccurrenceArgs']]]] monthly_occurrences: List of occurrences of days within a month. Only valid when frequency is `Month`. The `monthly_occurrence` block supports fields documented below.
        :param pulumi.Input[str] name: Specifies the name of the Schedule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Schedule is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] start_time: Start time of the schedule. Must be at least five minutes in the future. Defaults to seven minutes in the future from the time the resource is created.
        :param pulumi.Input[str] timezone: The timezone of the start time. Defaults to `UTC`. For possible values see: https://s2.automation.ext.azure.com/api/Orchestrator/TimeZones?_=1594792230258
        :param pulumi.Input[Sequence[pulumi.Input[str]]] week_days: List of days of the week that the job should execute on. Only valid when frequency is `Week`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["automation_account_name"] = automation_account_name
        __props__["description"] = description
        __props__["expiry_time"] = expiry_time
        __props__["frequency"] = frequency
        __props__["interval"] = interval
        __props__["month_days"] = month_days
        __props__["monthly_occurrences"] = monthly_occurrences
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["start_time"] = start_time
        __props__["timezone"] = timezone
        __props__["week_days"] = week_days
        return Schedule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Output[str]:
        """
        The name of the automation account in which the Schedule is created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "automation_account_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for this Schedule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> pulumi.Output[str]:
        """
        The end time of the schedule.
        """
        return pulumi.get(self, "expiry_time")

    @property
    @pulumi.getter
    def frequency(self) -> pulumi.Output[str]:
        """
        The frequency of the schedule. - can be either `OneTime`, `Day`, `Hour`, `Week`, or `Month`.
        """
        return pulumi.get(self, "frequency")

    @property
    @pulumi.getter
    def interval(self) -> pulumi.Output[int]:
        """
        The number of `frequency`s between runs. Only valid when frequency is `Day`, `Hour`, `Week`, or `Month` and defaults to `1`.
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter(name="monthDays")
    def month_days(self) -> pulumi.Output[Optional[Sequence[int]]]:
        """
        List of days of the month that the job should execute on. Must be between `1` and `31`. `-1` for last day of the month. Only valid when frequency is `Month`.
        """
        return pulumi.get(self, "month_days")

    @property
    @pulumi.getter(name="monthlyOccurrences")
    def monthly_occurrences(self) -> pulumi.Output[Optional[Sequence['outputs.ScheduleMonthlyOccurrence']]]:
        """
        List of occurrences of days within a month. Only valid when frequency is `Month`. The `monthly_occurrence` block supports fields documented below.
        """
        return pulumi.get(self, "monthly_occurrences")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Schedule. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which the Schedule is created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[str]:
        """
        Start time of the schedule. Must be at least five minutes in the future. Defaults to seven minutes in the future from the time the resource is created.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def timezone(self) -> pulumi.Output[Optional[str]]:
        """
        The timezone of the start time. Defaults to `UTC`. For possible values see: https://s2.automation.ext.azure.com/api/Orchestrator/TimeZones?_=1594792230258
        """
        return pulumi.get(self, "timezone")

    @property
    @pulumi.getter(name="weekDays")
    def week_days(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of days of the week that the job should execute on. Only valid when frequency is `Week`.
        """
        return pulumi.get(self, "week_days")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

