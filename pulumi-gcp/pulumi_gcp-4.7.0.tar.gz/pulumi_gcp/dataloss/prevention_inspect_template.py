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

__all__ = ['PreventionInspectTemplate']


class PreventionInspectTemplate(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 inspect_config: Optional[pulumi.Input[pulumi.InputType['PreventionInspectTemplateInspectConfigArgs']]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        An inspect job template.

        To get more information about InspectTemplate, see:

        * [API documentation](https://cloud.google.com/dlp/docs/reference/rest/v2/projects.inspectTemplates)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/dlp/docs/creating-templates-inspect)

        ## Example Usage
        ### Dlp Inspect Template Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        basic = gcp.dataloss.PreventionInspectTemplate("basic",
            description="My description",
            display_name="display_name",
            inspect_config=gcp.dataloss.PreventionInspectTemplateInspectConfigArgs(
                info_types=[
                    gcp.dataloss.PreventionInspectTemplateInspectConfigInfoTypeArgs(
                        name="EMAIL_ADDRESS",
                    ),
                    gcp.dataloss.PreventionInspectTemplateInspectConfigInfoTypeArgs(
                        name="PERSON_NAME",
                    ),
                    gcp.dataloss.PreventionInspectTemplateInspectConfigInfoTypeArgs(
                        name="LAST_NAME",
                    ),
                    gcp.dataloss.PreventionInspectTemplateInspectConfigInfoTypeArgs(
                        name="DOMAIN_NAME",
                    ),
                    gcp.dataloss.PreventionInspectTemplateInspectConfigInfoTypeArgs(
                        name="PHONE_NUMBER",
                    ),
                    gcp.dataloss.PreventionInspectTemplateInspectConfigInfoTypeArgs(
                        name="FIRST_NAME",
                    ),
                ],
                limits=gcp.dataloss.PreventionInspectTemplateInspectConfigLimitsArgs(
                    max_findings_per_info_type=[
                        {
                            "infoType": {
                                "name": "PERSON_NAME",
                            },
                            "maxFindings": "75",
                        },
                        {
                            "infoType": {
                                "name": "LAST_NAME",
                            },
                            "maxFindings": "80",
                        },
                    ],
                    max_findings_per_item=10,
                    max_findings_per_request=50,
                ),
                min_likelihood="UNLIKELY",
                rule_sets=[
                    gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetArgs(
                        info_types=[gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetInfoTypeArgs(
                            name="EMAIL_ADDRESS",
                        )],
                        rules=[gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleArgs(
                            exclusion_rule=gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleArgs(
                                matching_type="MATCHING_TYPE_FULL_MATCH",
                                regex=gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleRegexArgs(
                                    pattern=".+@example.com",
                                ),
                            ),
                        )],
                    ),
                    gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetArgs(
                        info_types=[
                            gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetInfoTypeArgs(
                                name="EMAIL_ADDRESS",
                            ),
                            gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetInfoTypeArgs(
                                name="DOMAIN_NAME",
                            ),
                            gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetInfoTypeArgs(
                                name="PHONE_NUMBER",
                            ),
                            gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetInfoTypeArgs(
                                name="PERSON_NAME",
                            ),
                            gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetInfoTypeArgs(
                                name="FIRST_NAME",
                            ),
                        ],
                        rules=[gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleArgs(
                            exclusion_rule=gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleArgs(
                                dictionary=gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryArgs(
                                    word_list=gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryWordListArgs(
                                        words=["TEST"],
                                    ),
                                ),
                                matching_type="MATCHING_TYPE_PARTIAL_MATCH",
                            ),
                        )],
                    ),
                    gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetArgs(
                        info_types=[gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetInfoTypeArgs(
                            name="PERSON_NAME",
                        )],
                        rules=[gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleArgs(
                            hotword_rule=gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleArgs(
                                hotword_regex=gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleHotwordRegexArgs(
                                    pattern="patient",
                                ),
                                likelihood_adjustment=gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustmentArgs(
                                    fixed_likelihood="VERY_LIKELY",
                                ),
                                proximity=gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleProximityArgs(
                                    window_before=50,
                                ),
                            ),
                        )],
                    ),
                ],
            ),
            parent="projects/my-project-name")
        ```
        ### Dlp Inspect Template Custom Type

        ```python
        import pulumi
        import pulumi_gcp as gcp

        custom = gcp.dataloss.PreventionInspectTemplate("custom",
            description="My description",
            display_name="display_name",
            inspect_config=gcp.dataloss.PreventionInspectTemplateInspectConfigArgs(
                custom_info_types=[gcp.dataloss.PreventionInspectTemplateInspectConfigCustomInfoTypeArgs(
                    info_type=gcp.dataloss.PreventionInspectTemplateInspectConfigCustomInfoTypeInfoTypeArgs(
                        name="MY_CUSTOM_TYPE",
                    ),
                    likelihood="UNLIKELY",
                    regex=gcp.dataloss.PreventionInspectTemplateInspectConfigCustomInfoTypeRegexArgs(
                        pattern="test*",
                    ),
                )],
                info_types=[gcp.dataloss.PreventionInspectTemplateInspectConfigInfoTypeArgs(
                    name="EMAIL_ADDRESS",
                )],
                limits=gcp.dataloss.PreventionInspectTemplateInspectConfigLimitsArgs(
                    max_findings_per_item=10,
                    max_findings_per_request=50,
                ),
                min_likelihood="UNLIKELY",
                rule_sets=[
                    gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetArgs(
                        info_types=[gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetInfoTypeArgs(
                            name="EMAIL_ADDRESS",
                        )],
                        rules=[gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleArgs(
                            exclusion_rule=gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleArgs(
                                matching_type="MATCHING_TYPE_FULL_MATCH",
                                regex=gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleRegexArgs(
                                    pattern=".+@example.com",
                                ),
                            ),
                        )],
                    ),
                    gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetArgs(
                        info_types=[gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetInfoTypeArgs(
                            name="MY_CUSTOM_TYPE",
                        )],
                        rules=[gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleArgs(
                            hotword_rule=gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleArgs(
                                hotword_regex=gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleHotwordRegexArgs(
                                    pattern="example*",
                                ),
                                likelihood_adjustment=gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustmentArgs(
                                    fixed_likelihood="VERY_LIKELY",
                                ),
                                proximity=gcp.dataloss.PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleProximityArgs(
                                    window_before=50,
                                ),
                            ),
                        )],
                    ),
                ],
            ),
            parent="projects/my-project-name")
        ```

        ## Import

        InspectTemplate can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:dataloss/preventionInspectTemplate:PreventionInspectTemplate default {{parent}}/inspectTemplates/{{name}}
        ```

        ```sh
         $ pulumi import gcp:dataloss/preventionInspectTemplate:PreventionInspectTemplate default {{parent}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of the inspect template.
        :param pulumi.Input[str] display_name: User set display name of the inspect template.
        :param pulumi.Input[pulumi.InputType['PreventionInspectTemplateInspectConfigArgs']] inspect_config: The core content of the template.
               Structure is documented below.
        :param pulumi.Input[str] parent: The parent of the inspect template in any of the following formats:
               * `projects/{{project}}`
               * `projects/{{project}}/locations/{{location}}`
               * `organizations/{{organization_id}}`
               * `organizations/{{organization_id}}/locations/{{location}}`
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

            __props__['description'] = description
            __props__['display_name'] = display_name
            __props__['inspect_config'] = inspect_config
            if parent is None and not opts.urn:
                raise TypeError("Missing required property 'parent'")
            __props__['parent'] = parent
            __props__['name'] = None
        super(PreventionInspectTemplate, __self__).__init__(
            'gcp:dataloss/preventionInspectTemplate:PreventionInspectTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            inspect_config: Optional[pulumi.Input[pulumi.InputType['PreventionInspectTemplateInspectConfigArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parent: Optional[pulumi.Input[str]] = None) -> 'PreventionInspectTemplate':
        """
        Get an existing PreventionInspectTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of the inspect template.
        :param pulumi.Input[str] display_name: User set display name of the inspect template.
        :param pulumi.Input[pulumi.InputType['PreventionInspectTemplateInspectConfigArgs']] inspect_config: The core content of the template.
               Structure is documented below.
        :param pulumi.Input[str] name: Resource name of the requested StoredInfoType, for example `organizations/433245324/storedInfoTypes/432452342`
               or `projects/project-id/storedInfoTypes/432452342`.
        :param pulumi.Input[str] parent: The parent of the inspect template in any of the following formats:
               * `projects/{{project}}`
               * `projects/{{project}}/locations/{{location}}`
               * `organizations/{{organization_id}}`
               * `organizations/{{organization_id}}/locations/{{location}}`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["display_name"] = display_name
        __props__["inspect_config"] = inspect_config
        __props__["name"] = name
        __props__["parent"] = parent
        return PreventionInspectTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the inspect template.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        User set display name of the inspect template.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="inspectConfig")
    def inspect_config(self) -> pulumi.Output[Optional['outputs.PreventionInspectTemplateInspectConfig']]:
        """
        The core content of the template.
        Structure is documented below.
        """
        return pulumi.get(self, "inspect_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name of the requested StoredInfoType, for example `organizations/433245324/storedInfoTypes/432452342`
        or `projects/project-id/storedInfoTypes/432452342`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parent(self) -> pulumi.Output[str]:
        """
        The parent of the inspect template in any of the following formats:
        * `projects/{{project}}`
        * `projects/{{project}}/locations/{{location}}`
        * `organizations/{{organization_id}}`
        * `organizations/{{organization_id}}/locations/{{location}}`
        """
        return pulumi.get(self, "parent")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

