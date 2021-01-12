# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .custom_provider import *
from .get_client_config import *
from .get_resource_group import *
from .get_resources import *
from .get_subscription import *
from .get_subscriptions import *
from .get_user_assigned_identity import *
from .resource_group import *
from .resource_group_template_deployment import *
from .resource_provider_registration import *
from .subscription_template_deployment import *
from .template_deployment import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "azure:core/customProvider:CustomProvider":
                return CustomProvider(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:core/resourceGroup:ResourceGroup":
                return ResourceGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:core/resourceGroupTemplateDeployment:ResourceGroupTemplateDeployment":
                return ResourceGroupTemplateDeployment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:core/resourceProviderRegistration:ResourceProviderRegistration":
                return ResourceProviderRegistration(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:core/subscriptionTemplateDeployment:SubscriptionTemplateDeployment":
                return SubscriptionTemplateDeployment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:core/templateDeployment:TemplateDeployment":
                return TemplateDeployment(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure", "core/customProvider", _module_instance)
    pulumi.runtime.register_resource_module("azure", "core/resourceGroup", _module_instance)
    pulumi.runtime.register_resource_module("azure", "core/resourceGroupTemplateDeployment", _module_instance)
    pulumi.runtime.register_resource_module("azure", "core/resourceProviderRegistration", _module_instance)
    pulumi.runtime.register_resource_module("azure", "core/subscriptionTemplateDeployment", _module_instance)
    pulumi.runtime.register_resource_module("azure", "core/templateDeployment", _module_instance)

_register_module()
