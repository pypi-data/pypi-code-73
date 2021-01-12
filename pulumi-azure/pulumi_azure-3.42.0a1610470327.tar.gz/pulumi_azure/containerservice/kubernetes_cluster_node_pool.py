# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['KubernetesClusterNodePool']


class KubernetesClusterNodePool(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enable_auto_scaling: Optional[pulumi.Input[bool]] = None,
                 enable_node_public_ip: Optional[pulumi.Input[bool]] = None,
                 eviction_policy: Optional[pulumi.Input[str]] = None,
                 kubernetes_cluster_id: Optional[pulumi.Input[str]] = None,
                 max_count: Optional[pulumi.Input[int]] = None,
                 max_pods: Optional[pulumi.Input[int]] = None,
                 min_count: Optional[pulumi.Input[int]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_count: Optional[pulumi.Input[int]] = None,
                 node_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 node_taints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 orchestrator_version: Optional[pulumi.Input[str]] = None,
                 os_disk_size_gb: Optional[pulumi.Input[int]] = None,
                 os_disk_type: Optional[pulumi.Input[str]] = None,
                 os_type: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[str]] = None,
                 proximity_placement_group_id: Optional[pulumi.Input[str]] = None,
                 spot_max_price: Optional[pulumi.Input[float]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vm_size: Optional[pulumi.Input[str]] = None,
                 vnet_subnet_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Node Pool within a Kubernetes Cluster

        > **NOTE:** Multiple Node Pools are only supported when the Kubernetes Cluster is using Virtual Machine Scale Sets.

        ## Example Usage

        This example provisions a basic Kubernetes Node Pool.

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_kubernetes_cluster = azure.containerservice.KubernetesCluster("exampleKubernetesCluster",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            dns_prefix="exampleaks1",
            default_node_pool=azure.containerservice.KubernetesClusterDefaultNodePoolArgs(
                name="default",
                node_count=1,
                vm_size="Standard_D2_v2",
            ),
            service_principal=azure.containerservice.KubernetesClusterServicePrincipalArgs(
                client_id="00000000-0000-0000-0000-000000000000",
                client_secret="00000000000000000000000000000000",
            ))
        example_kubernetes_cluster_node_pool = azure.containerservice.KubernetesClusterNodePool("exampleKubernetesClusterNodePool",
            kubernetes_cluster_id=example_kubernetes_cluster.id,
            vm_size="Standard_DS2_v2",
            node_count=1,
            tags={
                "Environment": "Production",
            })
        ```

        ## Import

        Kubernetes Cluster Node Pools can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:containerservice/kubernetesClusterNodePool:KubernetesClusterNodePool pool1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.ContainerService/managedClusters/cluster1/agentPools/pool1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] availability_zones: A list of Availability Zones where the Nodes in this Node Pool should be created in. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] enable_auto_scaling: Whether to enable [auto-scaler](https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler). Defaults to `false`.
        :param pulumi.Input[bool] enable_node_public_ip: Should each node have a Public IP Address? Defaults to `false`.
        :param pulumi.Input[str] eviction_policy: The Eviction Policy which should be used for Virtual Machines within the Virtual Machine Scale Set powering this Node Pool. Possible values are `Deallocate` and `Delete`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kubernetes_cluster_id: The ID of the Kubernetes Cluster where this Node Pool should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[int] max_count: The maximum number of nodes which should exist within this Node Pool. Valid values are between `0` and `1000` and must be greater than or equal to `min_count`.
        :param pulumi.Input[int] max_pods: The maximum number of pods that can run on each agent. Changing this forces a new resource to be created.
        :param pulumi.Input[int] min_count: The minimum number of nodes which should exist within this Node Pool. Valid values are between `0` and `1000` and must be less than or equal to `max_count`.
        :param pulumi.Input[str] mode: Should this Node Pool be used for System or User resources? Possible values are `System` and `User`. Defaults to `User`.
        :param pulumi.Input[str] name: The name of the Node Pool which should be created within the Kubernetes Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[int] node_count: The initial number of nodes which should exist within this Node Pool. Valid values are between `0` and `1000` and must be a value in the range `min_count` - `max_count`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] node_labels: A map of Kubernetes labels which should be applied to nodes in this Node Pool. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] node_taints: A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g `key=value:NoSchedule`). Changing this forces a new resource to be created.
        :param pulumi.Input[str] orchestrator_version: Version of Kubernetes used for the Agents. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade)
        :param pulumi.Input[int] os_disk_size_gb: The Agent Operating System disk size in GB. Changing this forces a new resource to be created.
        :param pulumi.Input[str] os_disk_type: The type of disk which should be used for the Operating System. Possible values are `Ephemeral` and `Managed`. Defaults to `Managed`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] os_type: The Operating System which should be used for this Node Pool. Changing this forces a new resource to be created. Possible values are `Linux` and `Windows`. Defaults to `Linux`.
        :param pulumi.Input[str] priority: The Priority for Virtual Machines within the Virtual Machine Scale Set that powers this Node Pool. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] proximity_placement_group_id: The ID of the Proximity Placement Group where the Virtual Machine Scale Set that powers this Node Pool will be placed. Changing this forces a new resource to be created.
        :param pulumi.Input[float] spot_max_price: The maximum price you're willing to pay in USD per Virtual Machine. Valid values are `-1` (the current on-demand price for a Virtual Machine) or a positive value with up to five decimal places. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] vm_size: The SKU which should be used for the Virtual Machines used in this Node Pool. Changing this forces a new resource to be created.
        :param pulumi.Input[str] vnet_subnet_id: The ID of the Subnet where this Node Pool should exist.
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

            __props__['availability_zones'] = availability_zones
            __props__['enable_auto_scaling'] = enable_auto_scaling
            __props__['enable_node_public_ip'] = enable_node_public_ip
            __props__['eviction_policy'] = eviction_policy
            if kubernetes_cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'kubernetes_cluster_id'")
            __props__['kubernetes_cluster_id'] = kubernetes_cluster_id
            __props__['max_count'] = max_count
            __props__['max_pods'] = max_pods
            __props__['min_count'] = min_count
            __props__['mode'] = mode
            __props__['name'] = name
            __props__['node_count'] = node_count
            __props__['node_labels'] = node_labels
            __props__['node_taints'] = node_taints
            __props__['orchestrator_version'] = orchestrator_version
            __props__['os_disk_size_gb'] = os_disk_size_gb
            __props__['os_disk_type'] = os_disk_type
            __props__['os_type'] = os_type
            __props__['priority'] = priority
            __props__['proximity_placement_group_id'] = proximity_placement_group_id
            __props__['spot_max_price'] = spot_max_price
            __props__['tags'] = tags
            if vm_size is None and not opts.urn:
                raise TypeError("Missing required property 'vm_size'")
            __props__['vm_size'] = vm_size
            __props__['vnet_subnet_id'] = vnet_subnet_id
        super(KubernetesClusterNodePool, __self__).__init__(
            'azure:containerservice/kubernetesClusterNodePool:KubernetesClusterNodePool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            enable_auto_scaling: Optional[pulumi.Input[bool]] = None,
            enable_node_public_ip: Optional[pulumi.Input[bool]] = None,
            eviction_policy: Optional[pulumi.Input[str]] = None,
            kubernetes_cluster_id: Optional[pulumi.Input[str]] = None,
            max_count: Optional[pulumi.Input[int]] = None,
            max_pods: Optional[pulumi.Input[int]] = None,
            min_count: Optional[pulumi.Input[int]] = None,
            mode: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            node_count: Optional[pulumi.Input[int]] = None,
            node_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            node_taints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            orchestrator_version: Optional[pulumi.Input[str]] = None,
            os_disk_size_gb: Optional[pulumi.Input[int]] = None,
            os_disk_type: Optional[pulumi.Input[str]] = None,
            os_type: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[str]] = None,
            proximity_placement_group_id: Optional[pulumi.Input[str]] = None,
            spot_max_price: Optional[pulumi.Input[float]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            vm_size: Optional[pulumi.Input[str]] = None,
            vnet_subnet_id: Optional[pulumi.Input[str]] = None) -> 'KubernetesClusterNodePool':
        """
        Get an existing KubernetesClusterNodePool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] availability_zones: A list of Availability Zones where the Nodes in this Node Pool should be created in. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] enable_auto_scaling: Whether to enable [auto-scaler](https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler). Defaults to `false`.
        :param pulumi.Input[bool] enable_node_public_ip: Should each node have a Public IP Address? Defaults to `false`.
        :param pulumi.Input[str] eviction_policy: The Eviction Policy which should be used for Virtual Machines within the Virtual Machine Scale Set powering this Node Pool. Possible values are `Deallocate` and `Delete`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kubernetes_cluster_id: The ID of the Kubernetes Cluster where this Node Pool should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[int] max_count: The maximum number of nodes which should exist within this Node Pool. Valid values are between `0` and `1000` and must be greater than or equal to `min_count`.
        :param pulumi.Input[int] max_pods: The maximum number of pods that can run on each agent. Changing this forces a new resource to be created.
        :param pulumi.Input[int] min_count: The minimum number of nodes which should exist within this Node Pool. Valid values are between `0` and `1000` and must be less than or equal to `max_count`.
        :param pulumi.Input[str] mode: Should this Node Pool be used for System or User resources? Possible values are `System` and `User`. Defaults to `User`.
        :param pulumi.Input[str] name: The name of the Node Pool which should be created within the Kubernetes Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[int] node_count: The initial number of nodes which should exist within this Node Pool. Valid values are between `0` and `1000` and must be a value in the range `min_count` - `max_count`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] node_labels: A map of Kubernetes labels which should be applied to nodes in this Node Pool. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] node_taints: A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g `key=value:NoSchedule`). Changing this forces a new resource to be created.
        :param pulumi.Input[str] orchestrator_version: Version of Kubernetes used for the Agents. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade)
        :param pulumi.Input[int] os_disk_size_gb: The Agent Operating System disk size in GB. Changing this forces a new resource to be created.
        :param pulumi.Input[str] os_disk_type: The type of disk which should be used for the Operating System. Possible values are `Ephemeral` and `Managed`. Defaults to `Managed`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] os_type: The Operating System which should be used for this Node Pool. Changing this forces a new resource to be created. Possible values are `Linux` and `Windows`. Defaults to `Linux`.
        :param pulumi.Input[str] priority: The Priority for Virtual Machines within the Virtual Machine Scale Set that powers this Node Pool. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] proximity_placement_group_id: The ID of the Proximity Placement Group where the Virtual Machine Scale Set that powers this Node Pool will be placed. Changing this forces a new resource to be created.
        :param pulumi.Input[float] spot_max_price: The maximum price you're willing to pay in USD per Virtual Machine. Valid values are `-1` (the current on-demand price for a Virtual Machine) or a positive value with up to five decimal places. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] vm_size: The SKU which should be used for the Virtual Machines used in this Node Pool. Changing this forces a new resource to be created.
        :param pulumi.Input[str] vnet_subnet_id: The ID of the Subnet where this Node Pool should exist.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["availability_zones"] = availability_zones
        __props__["enable_auto_scaling"] = enable_auto_scaling
        __props__["enable_node_public_ip"] = enable_node_public_ip
        __props__["eviction_policy"] = eviction_policy
        __props__["kubernetes_cluster_id"] = kubernetes_cluster_id
        __props__["max_count"] = max_count
        __props__["max_pods"] = max_pods
        __props__["min_count"] = min_count
        __props__["mode"] = mode
        __props__["name"] = name
        __props__["node_count"] = node_count
        __props__["node_labels"] = node_labels
        __props__["node_taints"] = node_taints
        __props__["orchestrator_version"] = orchestrator_version
        __props__["os_disk_size_gb"] = os_disk_size_gb
        __props__["os_disk_type"] = os_disk_type
        __props__["os_type"] = os_type
        __props__["priority"] = priority
        __props__["proximity_placement_group_id"] = proximity_placement_group_id
        __props__["spot_max_price"] = spot_max_price
        __props__["tags"] = tags
        __props__["vm_size"] = vm_size
        __props__["vnet_subnet_id"] = vnet_subnet_id
        return KubernetesClusterNodePool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of Availability Zones where the Nodes in this Node Pool should be created in. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter(name="enableAutoScaling")
    def enable_auto_scaling(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to enable [auto-scaler](https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler). Defaults to `false`.
        """
        return pulumi.get(self, "enable_auto_scaling")

    @property
    @pulumi.getter(name="enableNodePublicIp")
    def enable_node_public_ip(self) -> pulumi.Output[Optional[bool]]:
        """
        Should each node have a Public IP Address? Defaults to `false`.
        """
        return pulumi.get(self, "enable_node_public_ip")

    @property
    @pulumi.getter(name="evictionPolicy")
    def eviction_policy(self) -> pulumi.Output[Optional[str]]:
        """
        The Eviction Policy which should be used for Virtual Machines within the Virtual Machine Scale Set powering this Node Pool. Possible values are `Deallocate` and `Delete`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "eviction_policy")

    @property
    @pulumi.getter(name="kubernetesClusterId")
    def kubernetes_cluster_id(self) -> pulumi.Output[str]:
        """
        The ID of the Kubernetes Cluster where this Node Pool should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "kubernetes_cluster_id")

    @property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> pulumi.Output[Optional[int]]:
        """
        The maximum number of nodes which should exist within this Node Pool. Valid values are between `0` and `1000` and must be greater than or equal to `min_count`.
        """
        return pulumi.get(self, "max_count")

    @property
    @pulumi.getter(name="maxPods")
    def max_pods(self) -> pulumi.Output[int]:
        """
        The maximum number of pods that can run on each agent. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "max_pods")

    @property
    @pulumi.getter(name="minCount")
    def min_count(self) -> pulumi.Output[Optional[int]]:
        """
        The minimum number of nodes which should exist within this Node Pool. Valid values are between `0` and `1000` and must be less than or equal to `max_count`.
        """
        return pulumi.get(self, "min_count")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[str]]:
        """
        Should this Node Pool be used for System or User resources? Possible values are `System` and `User`. Defaults to `User`.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Node Pool which should be created within the Kubernetes Cluster. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Output[int]:
        """
        The initial number of nodes which should exist within this Node Pool. Valid values are between `0` and `1000` and must be a value in the range `min_count` - `max_count`.
        """
        return pulumi.get(self, "node_count")

    @property
    @pulumi.getter(name="nodeLabels")
    def node_labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of Kubernetes labels which should be applied to nodes in this Node Pool. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "node_labels")

    @property
    @pulumi.getter(name="nodeTaints")
    def node_taints(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g `key=value:NoSchedule`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "node_taints")

    @property
    @pulumi.getter(name="orchestratorVersion")
    def orchestrator_version(self) -> pulumi.Output[str]:
        """
        Version of Kubernetes used for the Agents. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade)
        """
        return pulumi.get(self, "orchestrator_version")

    @property
    @pulumi.getter(name="osDiskSizeGb")
    def os_disk_size_gb(self) -> pulumi.Output[int]:
        """
        The Agent Operating System disk size in GB. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "os_disk_size_gb")

    @property
    @pulumi.getter(name="osDiskType")
    def os_disk_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of disk which should be used for the Operating System. Possible values are `Ephemeral` and `Managed`. Defaults to `Managed`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "os_disk_type")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Output[Optional[str]]:
        """
        The Operating System which should be used for this Node Pool. Changing this forces a new resource to be created. Possible values are `Linux` and `Windows`. Defaults to `Linux`.
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[str]]:
        """
        The Priority for Virtual Machines within the Virtual Machine Scale Set that powers this Node Pool. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="proximityPlacementGroupId")
    def proximity_placement_group_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the Proximity Placement Group where the Virtual Machine Scale Set that powers this Node Pool will be placed. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "proximity_placement_group_id")

    @property
    @pulumi.getter(name="spotMaxPrice")
    def spot_max_price(self) -> pulumi.Output[Optional[float]]:
        """
        The maximum price you're willing to pay in USD per Virtual Machine. Valid values are `-1` (the current on-demand price for a Virtual Machine) or a positive value with up to five decimal places. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "spot_max_price")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> pulumi.Output[str]:
        """
        The SKU which should be used for the Virtual Machines used in this Node Pool. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "vm_size")

    @property
    @pulumi.getter(name="vnetSubnetId")
    def vnet_subnet_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the Subnet where this Node Pool should exist.
        """
        return pulumi.get(self, "vnet_subnet_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

