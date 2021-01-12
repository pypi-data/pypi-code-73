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

__all__ = ['NodeTemplate']


class NodeTemplate(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cpu_overcommit_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_affinity_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 node_type: Optional[pulumi.Input[str]] = None,
                 node_type_flexibility: Optional[pulumi.Input[pulumi.InputType['NodeTemplateNodeTypeFlexibilityArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 server_binding: Optional[pulumi.Input[pulumi.InputType['NodeTemplateServerBindingArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Represents a NodeTemplate resource. Node templates specify properties
        for creating sole-tenant nodes, such as node type, vCPU and memory
        requirements, node affinity labels, and region.

        To get more information about NodeTemplate, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/nodeTemplates)
        * How-to Guides
            * [Sole-Tenant Nodes](https://cloud.google.com/compute/docs/nodes/)

        ## Example Usage
        ### Node Template Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        template = gcp.compute.NodeTemplate("template",
            node_type="n1-node-96-624",
            region="us-central1")
        ```
        ### Node Template Server Binding

        ```python
        import pulumi
        import pulumi_gcp as gcp

        central1a = gcp.compute.get_node_types(zone="us-central1-a")
        template = gcp.compute.NodeTemplate("template",
            region="us-central1",
            node_type="n1-node-96-624",
            node_affinity_labels={
                "foo": "baz",
            },
            server_binding=gcp.compute.NodeTemplateServerBindingArgs(
                type="RESTART_NODE_ON_MINIMAL_SERVERS",
            ),
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```

        ## Import

        NodeTemplate can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:compute/nodeTemplate:NodeTemplate default projects/{{project}}/regions/{{region}}/nodeTemplates/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/nodeTemplate:NodeTemplate default {{project}}/{{region}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/nodeTemplate:NodeTemplate default {{region}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/nodeTemplate:NodeTemplate default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cpu_overcommit_type: CPU overcommit.
               Default value is `NONE`.
               Possible values are `ENABLED` and `NONE`.
        :param pulumi.Input[str] description: An optional textual description of the resource.
        :param pulumi.Input[str] name: Name of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] node_affinity_labels: Labels to use for node affinity, which will be used in
               instance scheduling.
        :param pulumi.Input[str] node_type: Node type to use for nodes group that are created from this template.
               Only one of nodeTypeFlexibility and nodeType can be specified.
        :param pulumi.Input[pulumi.InputType['NodeTemplateNodeTypeFlexibilityArgs']] node_type_flexibility: Flexible properties for the desired node type. Node groups that
               use this node template will create nodes of a type that matches
               these properties. Only one of nodeTypeFlexibility and nodeType can
               be specified.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: Region where nodes using the node template will be created.
               If it is not provided, the provider region is used.
        :param pulumi.Input[pulumi.InputType['NodeTemplateServerBindingArgs']] server_binding: The server binding policy for nodes using this template. Determines
               where the nodes should restart following a maintenance event.
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

            __props__['cpu_overcommit_type'] = cpu_overcommit_type
            __props__['description'] = description
            __props__['name'] = name
            __props__['node_affinity_labels'] = node_affinity_labels
            __props__['node_type'] = node_type
            __props__['node_type_flexibility'] = node_type_flexibility
            __props__['project'] = project
            __props__['region'] = region
            __props__['server_binding'] = server_binding
            __props__['creation_timestamp'] = None
            __props__['self_link'] = None
        super(NodeTemplate, __self__).__init__(
            'gcp:compute/nodeTemplate:NodeTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cpu_overcommit_type: Optional[pulumi.Input[str]] = None,
            creation_timestamp: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            node_affinity_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            node_type: Optional[pulumi.Input[str]] = None,
            node_type_flexibility: Optional[pulumi.Input[pulumi.InputType['NodeTemplateNodeTypeFlexibilityArgs']]] = None,
            project: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None,
            server_binding: Optional[pulumi.Input[pulumi.InputType['NodeTemplateServerBindingArgs']]] = None) -> 'NodeTemplate':
        """
        Get an existing NodeTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cpu_overcommit_type: CPU overcommit.
               Default value is `NONE`.
               Possible values are `ENABLED` and `NONE`.
        :param pulumi.Input[str] creation_timestamp: Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional textual description of the resource.
        :param pulumi.Input[str] name: Name of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] node_affinity_labels: Labels to use for node affinity, which will be used in
               instance scheduling.
        :param pulumi.Input[str] node_type: Node type to use for nodes group that are created from this template.
               Only one of nodeTypeFlexibility and nodeType can be specified.
        :param pulumi.Input[pulumi.InputType['NodeTemplateNodeTypeFlexibilityArgs']] node_type_flexibility: Flexible properties for the desired node type. Node groups that
               use this node template will create nodes of a type that matches
               these properties. Only one of nodeTypeFlexibility and nodeType can
               be specified.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: Region where nodes using the node template will be created.
               If it is not provided, the provider region is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        :param pulumi.Input[pulumi.InputType['NodeTemplateServerBindingArgs']] server_binding: The server binding policy for nodes using this template. Determines
               where the nodes should restart following a maintenance event.
               Structure is documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cpu_overcommit_type"] = cpu_overcommit_type
        __props__["creation_timestamp"] = creation_timestamp
        __props__["description"] = description
        __props__["name"] = name
        __props__["node_affinity_labels"] = node_affinity_labels
        __props__["node_type"] = node_type
        __props__["node_type_flexibility"] = node_type_flexibility
        __props__["project"] = project
        __props__["region"] = region
        __props__["self_link"] = self_link
        __props__["server_binding"] = server_binding
        return NodeTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cpuOvercommitType")
    def cpu_overcommit_type(self) -> pulumi.Output[Optional[str]]:
        """
        CPU overcommit.
        Default value is `NONE`.
        Possible values are `ENABLED` and `NONE`.
        """
        return pulumi.get(self, "cpu_overcommit_type")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional textual description of the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeAffinityLabels")
    def node_affinity_labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Labels to use for node affinity, which will be used in
        instance scheduling.
        """
        return pulumi.get(self, "node_affinity_labels")

    @property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Output[Optional[str]]:
        """
        Node type to use for nodes group that are created from this template.
        Only one of nodeTypeFlexibility and nodeType can be specified.
        """
        return pulumi.get(self, "node_type")

    @property
    @pulumi.getter(name="nodeTypeFlexibility")
    def node_type_flexibility(self) -> pulumi.Output[Optional['outputs.NodeTemplateNodeTypeFlexibility']]:
        """
        Flexible properties for the desired node type. Node groups that
        use this node template will create nodes of a type that matches
        these properties. Only one of nodeTypeFlexibility and nodeType can
        be specified.
        Structure is documented below.
        """
        return pulumi.get(self, "node_type_flexibility")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        Region where nodes using the node template will be created.
        If it is not provided, the provider region is used.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="serverBinding")
    def server_binding(self) -> pulumi.Output['outputs.NodeTemplateServerBinding']:
        """
        The server binding policy for nodes using this template. Determines
        where the nodes should restart following a maintenance event.
        Structure is documented below.
        """
        return pulumi.get(self, "server_binding")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

