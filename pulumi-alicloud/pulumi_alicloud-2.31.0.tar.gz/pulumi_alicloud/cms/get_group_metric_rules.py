# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'GetGroupMetricRulesResult',
    'AwaitableGetGroupMetricRulesResult',
    'get_group_metric_rules',
]

@pulumi.output_type
class GetGroupMetricRulesResult:
    """
    A collection of values returned by getGroupMetricRules.
    """
    def __init__(__self__, dimensions=None, enable_state=None, group_id=None, group_metric_rule_name=None, id=None, ids=None, metric_name=None, name_regex=None, names=None, namespace=None, output_file=None, rules=None, status=None):
        if dimensions and not isinstance(dimensions, str):
            raise TypeError("Expected argument 'dimensions' to be a str")
        pulumi.set(__self__, "dimensions", dimensions)
        if enable_state and not isinstance(enable_state, bool):
            raise TypeError("Expected argument 'enable_state' to be a bool")
        pulumi.set(__self__, "enable_state", enable_state)
        if group_id and not isinstance(group_id, str):
            raise TypeError("Expected argument 'group_id' to be a str")
        pulumi.set(__self__, "group_id", group_id)
        if group_metric_rule_name and not isinstance(group_metric_rule_name, str):
            raise TypeError("Expected argument 'group_metric_rule_name' to be a str")
        pulumi.set(__self__, "group_metric_rule_name", group_metric_rule_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if metric_name and not isinstance(metric_name, str):
            raise TypeError("Expected argument 'metric_name' to be a str")
        pulumi.set(__self__, "metric_name", metric_name)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[str]:
        return pulumi.get(self, "dimensions")

    @property
    @pulumi.getter(name="enableState")
    def enable_state(self) -> Optional[bool]:
        return pulumi.get(self, "enable_state")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[str]:
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="groupMetricRuleName")
    def group_metric_rule_name(self) -> Optional[str]:
        return pulumi.get(self, "group_metric_rule_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[str]:
        return pulumi.get(self, "metric_name")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        return pulumi.get(self, "names")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def rules(self) -> Sequence['outputs.GetGroupMetricRulesRuleResult']:
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")


class AwaitableGetGroupMetricRulesResult(GetGroupMetricRulesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGroupMetricRulesResult(
            dimensions=self.dimensions,
            enable_state=self.enable_state,
            group_id=self.group_id,
            group_metric_rule_name=self.group_metric_rule_name,
            id=self.id,
            ids=self.ids,
            metric_name=self.metric_name,
            name_regex=self.name_regex,
            names=self.names,
            namespace=self.namespace,
            output_file=self.output_file,
            rules=self.rules,
            status=self.status)


def get_group_metric_rules(dimensions: Optional[str] = None,
                           enable_state: Optional[bool] = None,
                           group_id: Optional[str] = None,
                           group_metric_rule_name: Optional[str] = None,
                           ids: Optional[Sequence[str]] = None,
                           metric_name: Optional[str] = None,
                           name_regex: Optional[str] = None,
                           namespace: Optional[str] = None,
                           output_file: Optional[str] = None,
                           status: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGroupMetricRulesResult:
    """
    This data source provides the Cms Group Metric Rules of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.104.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    example = alicloud.cms.get_group_metric_rules(ids=["4a9a8978-a9cc-55ca-aa7c-530ccd91ae57"],
        name_regex="the_resource_name")
    pulumi.export("firstCmsGroupMetricRuleId", example.rules[0].id)
    ```


    :param str dimensions: The dimensions that specify the resources to be associated with the alert rule.
    :param bool enable_state: Indicates whether the alert rule is enabled.
    :param str group_id: The ID of the application group.
    :param str group_metric_rule_name: The name of the alert rule.
    :param Sequence[str] ids: A list of Group Metric Rule IDs.
    :param str metric_name: The name of the metric.
    :param str name_regex: A regex string to filter results by Group Metric Rule name.
    :param str namespace: The namespace of the service.
    :param str status: The status of Group Metric Rule..
    """
    __args__ = dict()
    __args__['dimensions'] = dimensions
    __args__['enableState'] = enable_state
    __args__['groupId'] = group_id
    __args__['groupMetricRuleName'] = group_metric_rule_name
    __args__['ids'] = ids
    __args__['metricName'] = metric_name
    __args__['nameRegex'] = name_regex
    __args__['namespace'] = namespace
    __args__['outputFile'] = output_file
    __args__['status'] = status
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:cms/getGroupMetricRules:getGroupMetricRules', __args__, opts=opts, typ=GetGroupMetricRulesResult).value

    return AwaitableGetGroupMetricRulesResult(
        dimensions=__ret__.dimensions,
        enable_state=__ret__.enable_state,
        group_id=__ret__.group_id,
        group_metric_rule_name=__ret__.group_metric_rule_name,
        id=__ret__.id,
        ids=__ret__.ids,
        metric_name=__ret__.metric_name,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        namespace=__ret__.namespace,
        output_file=__ret__.output_file,
        rules=__ret__.rules,
        status=__ret__.status)
