# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .advanced_threat_protection import *
from .auto_provisioning import *
from .automation import *
from .contact import *
from .setting import *
from .subscription_pricing import *
from .workspace import *
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
            if typ == "azure:securitycenter/advancedThreatProtection:AdvancedThreatProtection":
                return AdvancedThreatProtection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:securitycenter/autoProvisioning:AutoProvisioning":
                return AutoProvisioning(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:securitycenter/automation:Automation":
                return Automation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:securitycenter/contact:Contact":
                return Contact(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:securitycenter/setting:Setting":
                return Setting(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:securitycenter/subscriptionPricing:SubscriptionPricing":
                return SubscriptionPricing(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:securitycenter/workspace:Workspace":
                return Workspace(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure", "securitycenter/advancedThreatProtection", _module_instance)
    pulumi.runtime.register_resource_module("azure", "securitycenter/autoProvisioning", _module_instance)
    pulumi.runtime.register_resource_module("azure", "securitycenter/automation", _module_instance)
    pulumi.runtime.register_resource_module("azure", "securitycenter/contact", _module_instance)
    pulumi.runtime.register_resource_module("azure", "securitycenter/setting", _module_instance)
    pulumi.runtime.register_resource_module("azure", "securitycenter/subscriptionPricing", _module_instance)
    pulumi.runtime.register_resource_module("azure", "securitycenter/workspace", _module_instance)

_register_module()
