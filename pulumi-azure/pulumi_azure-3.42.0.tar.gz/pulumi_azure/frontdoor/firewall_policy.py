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

__all__ = ['FirewallPolicy']


class FirewallPolicy(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_block_response_body: Optional[pulumi.Input[str]] = None,
                 custom_block_response_status_code: Optional[pulumi.Input[int]] = None,
                 custom_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyCustomRuleArgs']]]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 managed_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyManagedRuleArgs']]]]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 redirect_url: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an Azure Front Door Web Application Firewall Policy instance.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West US 2")
        example_firewall_policy = azure.frontdoor.FirewallPolicy("exampleFirewallPolicy",
            resource_group_name=example_resource_group.name,
            enabled=True,
            mode="Prevention",
            redirect_url="https://www.contoso.com",
            custom_block_response_status_code=403,
            custom_block_response_body="PGh0bWw+CjxoZWFkZXI+PHRpdGxlPkhlbGxvPC90aXRsZT48L2hlYWRlcj4KPGJvZHk+CkhlbGxvIHdvcmxkCjwvYm9keT4KPC9odG1sPg==",
            custom_rules=[
                azure.frontdoor.FirewallPolicyCustomRuleArgs(
                    name="Rule1",
                    enabled=True,
                    priority=1,
                    rate_limit_duration_in_minutes=1,
                    rate_limit_threshold=10,
                    type="MatchRule",
                    action="Block",
                    match_conditions=[azure.frontdoor.FirewallPolicyCustomRuleMatchConditionArgs(
                        match_variable="RemoteAddr",
                        operator="IPMatch",
                        negation_condition=False,
                        match_values=[
                            "192.168.1.0/24",
                            "10.0.0.0/24",
                        ],
                    )],
                ),
                azure.frontdoor.FirewallPolicyCustomRuleArgs(
                    name="Rule2",
                    enabled=True,
                    priority=2,
                    rate_limit_duration_in_minutes=1,
                    rate_limit_threshold=10,
                    type="MatchRule",
                    action="Block",
                    match_conditions=[
                        azure.frontdoor.FirewallPolicyCustomRuleMatchConditionArgs(
                            match_variable="RemoteAddr",
                            operator="IPMatch",
                            negation_condition=False,
                            match_values=["192.168.1.0/24"],
                        ),
                        azure.frontdoor.FirewallPolicyCustomRuleMatchConditionArgs(
                            match_variable="RequestHeader",
                            selector="UserAgent",
                            operator="Contains",
                            negation_condition=False,
                            match_values=["windows"],
                            transforms=[
                                "Lowercase",
                                "Trim",
                            ],
                        ),
                    ],
                ),
            ],
            managed_rules=[
                azure.frontdoor.FirewallPolicyManagedRuleArgs(
                    type="DefaultRuleSet",
                    version="1.0",
                    exclusions=[azure.frontdoor.FirewallPolicyManagedRuleExclusionArgs(
                        match_variable="QueryStringArgNames",
                        operator="Equals",
                        selector="not_suspicious",
                    )],
                    overrides=[
                        azure.frontdoor.FirewallPolicyManagedRuleOverrideArgs(
                            rule_group_name="PHP",
                            rules=[azure.frontdoor.FirewallPolicyManagedRuleOverrideRuleArgs(
                                rule_id="933100",
                                enabled=False,
                                action="Block",
                            )],
                        ),
                        azure.frontdoor.FirewallPolicyManagedRuleOverrideArgs(
                            rule_group_name="SQLI",
                            exclusions=[azure.frontdoor.FirewallPolicyManagedRuleOverrideExclusionArgs(
                                match_variable="QueryStringArgNames",
                                operator="Equals",
                                selector="really_not_suspicious",
                            )],
                            rules=[azure.frontdoor.FirewallPolicyManagedRuleOverrideRuleArgs(
                                rule_id="942200",
                                action="Block",
                                exclusions=[azure.frontdoor.FirewallPolicyManagedRuleOverrideRuleExclusionArgs(
                                    match_variable="QueryStringArgNames",
                                    operator="Equals",
                                    selector="innocent",
                                )],
                            )],
                        ),
                    ],
                ),
                azure.frontdoor.FirewallPolicyManagedRuleArgs(
                    type="Microsoft_BotManagerRuleSet",
                    version="1.0",
                ),
            ])
        ```

        ## Import

        FrontDoor Web Application Firewall Policy can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:frontdoor/firewallPolicy:FirewallPolicy example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example-rg/providers/Microsoft.Network/frontDoorWebApplicationFirewallPolicies/example-fdwafpolicy
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] custom_block_response_body: If a `custom_rule` block's action type is `block`, this is the response body. The body must be specified in base64 encoding.
        :param pulumi.Input[int] custom_block_response_status_code: If a `custom_rule` block's action type is `block`, this is the response status code. Possible values are `200`, `403`, `405`, `406`, or `429`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyCustomRuleArgs']]]] custom_rules: One or more `custom_rule` blocks as defined below.
        :param pulumi.Input[bool] enabled: Is the policy a enabled state or disabled state. Defaults to `true`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyManagedRuleArgs']]]] managed_rules: One or more `managed_rule` blocks as defined below.
        :param pulumi.Input[str] mode: The firewall policy mode. Possible values are `Detection`, `Prevention` and defaults to `Prevention`.
        :param pulumi.Input[str] name: The name of the policy. Changing this forces a new resource to be created.
        :param pulumi.Input[str] redirect_url: If action type is redirect, this field represents redirect URL for the client.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the Web Application Firewall Policy.
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

            __props__['custom_block_response_body'] = custom_block_response_body
            __props__['custom_block_response_status_code'] = custom_block_response_status_code
            __props__['custom_rules'] = custom_rules
            __props__['enabled'] = enabled
            __props__['managed_rules'] = managed_rules
            __props__['mode'] = mode
            __props__['name'] = name
            __props__['redirect_url'] = redirect_url
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['tags'] = tags
            __props__['frontend_endpoint_ids'] = None
            __props__['location'] = None
        super(FirewallPolicy, __self__).__init__(
            'azure:frontdoor/firewallPolicy:FirewallPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            custom_block_response_body: Optional[pulumi.Input[str]] = None,
            custom_block_response_status_code: Optional[pulumi.Input[int]] = None,
            custom_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyCustomRuleArgs']]]]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            frontend_endpoint_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            managed_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyManagedRuleArgs']]]]] = None,
            mode: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            redirect_url: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'FirewallPolicy':
        """
        Get an existing FirewallPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] custom_block_response_body: If a `custom_rule` block's action type is `block`, this is the response body. The body must be specified in base64 encoding.
        :param pulumi.Input[int] custom_block_response_status_code: If a `custom_rule` block's action type is `block`, this is the response status code. Possible values are `200`, `403`, `405`, `406`, or `429`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyCustomRuleArgs']]]] custom_rules: One or more `custom_rule` blocks as defined below.
        :param pulumi.Input[bool] enabled: Is the policy a enabled state or disabled state. Defaults to `true`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] frontend_endpoint_ids: The Frontend Endpoints associated with this Front Door Web Application Firewall policy.
        :param pulumi.Input[str] location: The Azure Region where this FrontDoor Firewall Policy exists.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyManagedRuleArgs']]]] managed_rules: One or more `managed_rule` blocks as defined below.
        :param pulumi.Input[str] mode: The firewall policy mode. Possible values are `Detection`, `Prevention` and defaults to `Prevention`.
        :param pulumi.Input[str] name: The name of the policy. Changing this forces a new resource to be created.
        :param pulumi.Input[str] redirect_url: If action type is redirect, this field represents redirect URL for the client.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the Web Application Firewall Policy.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["custom_block_response_body"] = custom_block_response_body
        __props__["custom_block_response_status_code"] = custom_block_response_status_code
        __props__["custom_rules"] = custom_rules
        __props__["enabled"] = enabled
        __props__["frontend_endpoint_ids"] = frontend_endpoint_ids
        __props__["location"] = location
        __props__["managed_rules"] = managed_rules
        __props__["mode"] = mode
        __props__["name"] = name
        __props__["redirect_url"] = redirect_url
        __props__["resource_group_name"] = resource_group_name
        __props__["tags"] = tags
        return FirewallPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customBlockResponseBody")
    def custom_block_response_body(self) -> pulumi.Output[Optional[str]]:
        """
        If a `custom_rule` block's action type is `block`, this is the response body. The body must be specified in base64 encoding.
        """
        return pulumi.get(self, "custom_block_response_body")

    @property
    @pulumi.getter(name="customBlockResponseStatusCode")
    def custom_block_response_status_code(self) -> pulumi.Output[Optional[int]]:
        """
        If a `custom_rule` block's action type is `block`, this is the response status code. Possible values are `200`, `403`, `405`, `406`, or `429`.
        """
        return pulumi.get(self, "custom_block_response_status_code")

    @property
    @pulumi.getter(name="customRules")
    def custom_rules(self) -> pulumi.Output[Optional[Sequence['outputs.FirewallPolicyCustomRule']]]:
        """
        One or more `custom_rule` blocks as defined below.
        """
        return pulumi.get(self, "custom_rules")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Is the policy a enabled state or disabled state. Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="frontendEndpointIds")
    def frontend_endpoint_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The Frontend Endpoints associated with this Front Door Web Application Firewall policy.
        """
        return pulumi.get(self, "frontend_endpoint_ids")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The Azure Region where this FrontDoor Firewall Policy exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedRules")
    def managed_rules(self) -> pulumi.Output[Optional[Sequence['outputs.FirewallPolicyManagedRule']]]:
        """
        One or more `managed_rule` blocks as defined below.
        """
        return pulumi.get(self, "managed_rules")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[str]]:
        """
        The firewall policy mode. Possible values are `Detection`, `Prevention` and defaults to `Prevention`.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the policy. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> pulumi.Output[Optional[str]]:
        """
        If action type is redirect, this field represents redirect URL for the client.
        """
        return pulumi.get(self, "redirect_url")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the Web Application Firewall Policy.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

