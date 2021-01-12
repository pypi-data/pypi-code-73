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

__all__ = ['Slo']


class Slo(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 basic_sli: Optional[pulumi.Input[pulumi.InputType['SloBasicSliArgs']]] = None,
                 calendar_period: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 goal: Optional[pulumi.Input[float]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_based_sli: Optional[pulumi.Input[pulumi.InputType['SloRequestBasedSliArgs']]] = None,
                 rolling_period_days: Optional[pulumi.Input[int]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 slo_id: Optional[pulumi.Input[str]] = None,
                 windows_based_sli: Optional[pulumi.Input[pulumi.InputType['SloWindowsBasedSliArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        A Service-Level Objective (SLO) describes the level of desired good
        service. It consists of a service-level indicator (SLI), a performance
        goal, and a period over which the objective is to be evaluated against
        that goal. The SLO can use SLIs defined in a number of different manners.
        Typical SLOs might include "99% of requests in each rolling week have
        latency below 200 milliseconds" or "99.5% of requests in each calendar
        month return successfully."

        To get more information about Slo, see:

        * [API documentation](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives)
        * How-to Guides
            * [Service Monitoring](https://cloud.google.com/monitoring/service-monitoring)
            * [Monitoring API Documentation](https://cloud.google.com/monitoring/api/v3/)

        ## Example Usage
        ### Monitoring Slo Appengine

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.monitoring.get_app_engine_service(module_id="default")
        appeng_slo = gcp.monitoring.Slo("appengSlo",
            service=default.service_id,
            slo_id="ae-slo",
            display_name="Test SLO for App Engine",
            goal=0.9,
            calendar_period="DAY",
            basic_sli=gcp.monitoring.SloBasicSliArgs(
                latency=gcp.monitoring.SloBasicSliLatencyArgs(
                    threshold="1s",
                ),
            ))
        ```
        ### Monitoring Slo Request Based

        ```python
        import pulumi
        import pulumi_gcp as gcp

        customsrv = gcp.monitoring.CustomService("customsrv",
            service_id="custom-srv-request-slos",
            display_name="My Custom Service")
        request_based_slo = gcp.monitoring.Slo("requestBasedSlo",
            service=customsrv.service_id,
            slo_id="consumed-api-slo",
            display_name="Test SLO with request based SLI (good total ratio)",
            goal=0.9,
            rolling_period_days=30,
            request_based_sli=gcp.monitoring.SloRequestBasedSliArgs(
                distribution_cut=gcp.monitoring.SloRequestBasedSliDistributionCutArgs(
                    distribution_filter="metric.type=\"serviceruntime.googleapis.com/api/request_latencies\" resource.type=\"api\"  ",
                    range=gcp.monitoring.SloRequestBasedSliDistributionCutRangeArgs(
                        max=0.5,
                    ),
                ),
            ))
        ```

        ## Import

        Slo can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:monitoring/slo:Slo default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SloBasicSliArgs']] basic_sli: Basic Service-Level Indicator (SLI) on a well-known service type.
               Performance will be computed on the basis of pre-defined metrics.
               SLIs are used to measure and calculate the quality of the Service's
               performance with respect to a single aspect of service quality.
               Exactly one of the following must be set:
               `basic_sli`, `request_based_sli`, `windows_based_sli`
               Structure is documented below.
        :param pulumi.Input[str] calendar_period: A calendar period, semantically "since the start of the current
               <calendarPeriod>".
               Possible values are `DAY`, `WEEK`, `FORTNIGHT`, and `MONTH`.
        :param pulumi.Input[str] display_name: Name used for UI elements listing this SLO.
        :param pulumi.Input[float] goal: The fraction of service that must be good in order for this objective
               to be met. 0 < goal <= 0.999
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['SloRequestBasedSliArgs']] request_based_sli: A request-based SLI defines a SLI for which atomic units of
               service are counted directly.
               A SLI describes a good service.
               It is used to measure and calculate the quality of the Service's
               performance with respect to a single aspect of service quality.
               Exactly one of the following must be set:
               `basic_sli`, `request_based_sli`, `windows_based_sli`
               Structure is documented below.
        :param pulumi.Input[int] rolling_period_days: A rolling time period, semantically "in the past X days".
               Must be between 1 to 30 days, inclusive.
        :param pulumi.Input[str] service: ID of the service to which this SLO belongs.
        :param pulumi.Input[str] slo_id: The id to use for this ServiceLevelObjective. If omitted, an id will be generated instead.
        :param pulumi.Input[pulumi.InputType['SloWindowsBasedSliArgs']] windows_based_sli: A windows-based SLI defines the criteria for time windows.
               good_service is defined based off the count of these time windows
               for which the provided service was of good quality.
               A SLI describes a good service. It is used to measure and calculate
               the quality of the Service's performance with respect to a single
               aspect of service quality.
               Exactly one of the following must be set:
               `basic_sli`, `request_based_sli`, `windows_based_sli`
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

            __props__['basic_sli'] = basic_sli
            __props__['calendar_period'] = calendar_period
            __props__['display_name'] = display_name
            if goal is None and not opts.urn:
                raise TypeError("Missing required property 'goal'")
            __props__['goal'] = goal
            __props__['project'] = project
            __props__['request_based_sli'] = request_based_sli
            __props__['rolling_period_days'] = rolling_period_days
            if service is None and not opts.urn:
                raise TypeError("Missing required property 'service'")
            __props__['service'] = service
            __props__['slo_id'] = slo_id
            __props__['windows_based_sli'] = windows_based_sli
            __props__['name'] = None
        super(Slo, __self__).__init__(
            'gcp:monitoring/slo:Slo',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            basic_sli: Optional[pulumi.Input[pulumi.InputType['SloBasicSliArgs']]] = None,
            calendar_period: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            goal: Optional[pulumi.Input[float]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            request_based_sli: Optional[pulumi.Input[pulumi.InputType['SloRequestBasedSliArgs']]] = None,
            rolling_period_days: Optional[pulumi.Input[int]] = None,
            service: Optional[pulumi.Input[str]] = None,
            slo_id: Optional[pulumi.Input[str]] = None,
            windows_based_sli: Optional[pulumi.Input[pulumi.InputType['SloWindowsBasedSliArgs']]] = None) -> 'Slo':
        """
        Get an existing Slo resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SloBasicSliArgs']] basic_sli: Basic Service-Level Indicator (SLI) on a well-known service type.
               Performance will be computed on the basis of pre-defined metrics.
               SLIs are used to measure and calculate the quality of the Service's
               performance with respect to a single aspect of service quality.
               Exactly one of the following must be set:
               `basic_sli`, `request_based_sli`, `windows_based_sli`
               Structure is documented below.
        :param pulumi.Input[str] calendar_period: A calendar period, semantically "since the start of the current
               <calendarPeriod>".
               Possible values are `DAY`, `WEEK`, `FORTNIGHT`, and `MONTH`.
        :param pulumi.Input[str] display_name: Name used for UI elements listing this SLO.
        :param pulumi.Input[float] goal: The fraction of service that must be good in order for this objective
               to be met. 0 < goal <= 0.999
        :param pulumi.Input[str] name: The full resource name for this service. The syntax is:
               projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]/serviceLevelObjectives/[SLO_NAME]
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['SloRequestBasedSliArgs']] request_based_sli: A request-based SLI defines a SLI for which atomic units of
               service are counted directly.
               A SLI describes a good service.
               It is used to measure and calculate the quality of the Service's
               performance with respect to a single aspect of service quality.
               Exactly one of the following must be set:
               `basic_sli`, `request_based_sli`, `windows_based_sli`
               Structure is documented below.
        :param pulumi.Input[int] rolling_period_days: A rolling time period, semantically "in the past X days".
               Must be between 1 to 30 days, inclusive.
        :param pulumi.Input[str] service: ID of the service to which this SLO belongs.
        :param pulumi.Input[str] slo_id: The id to use for this ServiceLevelObjective. If omitted, an id will be generated instead.
        :param pulumi.Input[pulumi.InputType['SloWindowsBasedSliArgs']] windows_based_sli: A windows-based SLI defines the criteria for time windows.
               good_service is defined based off the count of these time windows
               for which the provided service was of good quality.
               A SLI describes a good service. It is used to measure and calculate
               the quality of the Service's performance with respect to a single
               aspect of service quality.
               Exactly one of the following must be set:
               `basic_sli`, `request_based_sli`, `windows_based_sli`
               Structure is documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["basic_sli"] = basic_sli
        __props__["calendar_period"] = calendar_period
        __props__["display_name"] = display_name
        __props__["goal"] = goal
        __props__["name"] = name
        __props__["project"] = project
        __props__["request_based_sli"] = request_based_sli
        __props__["rolling_period_days"] = rolling_period_days
        __props__["service"] = service
        __props__["slo_id"] = slo_id
        __props__["windows_based_sli"] = windows_based_sli
        return Slo(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="basicSli")
    def basic_sli(self) -> pulumi.Output[Optional['outputs.SloBasicSli']]:
        """
        Basic Service-Level Indicator (SLI) on a well-known service type.
        Performance will be computed on the basis of pre-defined metrics.
        SLIs are used to measure and calculate the quality of the Service's
        performance with respect to a single aspect of service quality.
        Exactly one of the following must be set:
        `basic_sli`, `request_based_sli`, `windows_based_sli`
        Structure is documented below.
        """
        return pulumi.get(self, "basic_sli")

    @property
    @pulumi.getter(name="calendarPeriod")
    def calendar_period(self) -> pulumi.Output[Optional[str]]:
        """
        A calendar period, semantically "since the start of the current
        <calendarPeriod>".
        Possible values are `DAY`, `WEEK`, `FORTNIGHT`, and `MONTH`.
        """
        return pulumi.get(self, "calendar_period")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name used for UI elements listing this SLO.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def goal(self) -> pulumi.Output[float]:
        """
        The fraction of service that must be good in order for this objective
        to be met. 0 < goal <= 0.999
        """
        return pulumi.get(self, "goal")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The full resource name for this service. The syntax is:
        projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]/serviceLevelObjectives/[SLO_NAME]
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="requestBasedSli")
    def request_based_sli(self) -> pulumi.Output[Optional['outputs.SloRequestBasedSli']]:
        """
        A request-based SLI defines a SLI for which atomic units of
        service are counted directly.
        A SLI describes a good service.
        It is used to measure and calculate the quality of the Service's
        performance with respect to a single aspect of service quality.
        Exactly one of the following must be set:
        `basic_sli`, `request_based_sli`, `windows_based_sli`
        Structure is documented below.
        """
        return pulumi.get(self, "request_based_sli")

    @property
    @pulumi.getter(name="rollingPeriodDays")
    def rolling_period_days(self) -> pulumi.Output[Optional[int]]:
        """
        A rolling time period, semantically "in the past X days".
        Must be between 1 to 30 days, inclusive.
        """
        return pulumi.get(self, "rolling_period_days")

    @property
    @pulumi.getter
    def service(self) -> pulumi.Output[str]:
        """
        ID of the service to which this SLO belongs.
        """
        return pulumi.get(self, "service")

    @property
    @pulumi.getter(name="sloId")
    def slo_id(self) -> pulumi.Output[str]:
        """
        The id to use for this ServiceLevelObjective. If omitted, an id will be generated instead.
        """
        return pulumi.get(self, "slo_id")

    @property
    @pulumi.getter(name="windowsBasedSli")
    def windows_based_sli(self) -> pulumi.Output[Optional['outputs.SloWindowsBasedSli']]:
        """
        A windows-based SLI defines the criteria for time windows.
        good_service is defined based off the count of these time windows
        for which the provided service was of good quality.
        A SLI describes a good service. It is used to measure and calculate
        the quality of the Service's performance with respect to a single
        aspect of service quality.
        Exactly one of the following must be set:
        `basic_sli`, `request_based_sli`, `windows_based_sli`
        Structure is documented below.
        """
        return pulumi.get(self, "windows_based_sli")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

