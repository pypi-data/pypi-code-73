# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .get_namespace import *
from .get_namespace_authorization_rule import *
from .get_queue_authorization_rule import *
from .get_subscription import *
from .get_topic_authorization_rule import *
from .namespace import *
from .namespace_authorization_rule import *
from .namespace_network_rule_set import *
from .queue import *
from .queue_authorization_rule import *
from .subscription import *
from .subscription_rule import *
from .topic import *
from .topic_authorization_rule import *
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
            if typ == "azure:servicebus/namespace:Namespace":
                return Namespace(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:servicebus/namespaceAuthorizationRule:NamespaceAuthorizationRule":
                return NamespaceAuthorizationRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:servicebus/namespaceNetworkRuleSet:NamespaceNetworkRuleSet":
                return NamespaceNetworkRuleSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:servicebus/queue:Queue":
                return Queue(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:servicebus/queueAuthorizationRule:QueueAuthorizationRule":
                return QueueAuthorizationRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:servicebus/subscription:Subscription":
                return Subscription(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:servicebus/subscriptionRule:SubscriptionRule":
                return SubscriptionRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:servicebus/topic:Topic":
                return Topic(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:servicebus/topicAuthorizationRule:TopicAuthorizationRule":
                return TopicAuthorizationRule(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure", "servicebus/namespace", _module_instance)
    pulumi.runtime.register_resource_module("azure", "servicebus/namespaceAuthorizationRule", _module_instance)
    pulumi.runtime.register_resource_module("azure", "servicebus/namespaceNetworkRuleSet", _module_instance)
    pulumi.runtime.register_resource_module("azure", "servicebus/queue", _module_instance)
    pulumi.runtime.register_resource_module("azure", "servicebus/queueAuthorizationRule", _module_instance)
    pulumi.runtime.register_resource_module("azure", "servicebus/subscription", _module_instance)
    pulumi.runtime.register_resource_module("azure", "servicebus/subscriptionRule", _module_instance)
    pulumi.runtime.register_resource_module("azure", "servicebus/topic", _module_instance)
    pulumi.runtime.register_resource_module("azure", "servicebus/topicAuthorizationRule", _module_instance)

_register_module()
