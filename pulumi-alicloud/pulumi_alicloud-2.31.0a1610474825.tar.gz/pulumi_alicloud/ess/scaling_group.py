# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['ScalingGroup']


class ScalingGroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 db_instance_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_cooldown: Optional[pulumi.Input[int]] = None,
                 desired_capacity: Optional[pulumi.Input[int]] = None,
                 group_deletion_protection: Optional[pulumi.Input[bool]] = None,
                 loadbalancer_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 max_size: Optional[pulumi.Input[int]] = None,
                 min_size: Optional[pulumi.Input[int]] = None,
                 multi_az_policy: Optional[pulumi.Input[str]] = None,
                 on_demand_base_capacity: Optional[pulumi.Input[int]] = None,
                 on_demand_percentage_above_base_capacity: Optional[pulumi.Input[int]] = None,
                 removal_policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 scaling_group_name: Optional[pulumi.Input[str]] = None,
                 spot_instance_pools: Optional[pulumi.Input[int]] = None,
                 spot_instance_remedy: Optional[pulumi.Input[bool]] = None,
                 vswitch_id: Optional[pulumi.Input[str]] = None,
                 vswitch_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Import

        ESS scaling group can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ess/scalingGroup:ScalingGroup example asg-abc123456
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] db_instance_ids: If an RDS instance is specified in the scaling group, the scaling group automatically attaches the Intranet IP addresses of its ECS instances to the RDS access whitelist.
               - The specified RDS instance must be in running status.
               - The specified RDS instance’s whitelist must have room for more IP addresses.
        :param pulumi.Input[int] default_cooldown: Default cool-down time (in seconds) of the scaling group. Value range: [0, 86400]. The default value is 300s.
        :param pulumi.Input[int] desired_capacity: Expected number of ECS instances in the scaling group. Value range: [min_size, max_size].
        :param pulumi.Input[bool] group_deletion_protection: Specifies whether the scaling group deletion protection is enabled. `true` or `false`, Default value: `false`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] loadbalancer_ids: If a Server Load Balancer instance is specified in the scaling group, the scaling group automatically attaches its ECS instances to the Server Load Balancer instance.
               - The Server Load Balancer instance must be enabled.
               - At least one listener must be configured for each Server Load Balancer and it HealthCheck must be on. Otherwise, creation will fail (it may be useful to add a `depends_on` argument
               targeting your `slb.Listener` in order to make sure the listener with its HealthCheck configuration is ready before creating your scaling group).
               - The Server Load Balancer instance attached with VPC-type ECS instances cannot be attached to the scaling group.
               - The default weight of an ECS instance attached to the Server Load Balancer instance is 50.
        :param pulumi.Input[int] max_size: Maximum number of ECS instances in the scaling group. Value range: [0, 1000].
        :param pulumi.Input[int] min_size: Minimum number of ECS instances in the scaling group. Value range: [0, 1000].
        :param pulumi.Input[str] multi_az_policy: Multi-AZ scaling group ECS instance expansion and contraction strategy. PRIORITY, BALANCE or COST_OPTIMIZED(Available in 1.54.0+).
        :param pulumi.Input[int] on_demand_base_capacity: The minimum amount of the Auto Scaling group's capacity that must be fulfilled by On-Demand Instances. This base portion is provisioned first as your group scales.
        :param pulumi.Input[int] on_demand_percentage_above_base_capacity: Controls the percentages of On-Demand Instances and Spot Instances for your additional capacity beyond OnDemandBaseCapacity.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] removal_policies: RemovalPolicy is used to select the ECS instances you want to remove from the scaling group when multiple candidates for removal exist. Optional values:
               - OldestInstance: removes the ECS instance that is added to the scaling group at the earliest point in time.
               - NewestInstance: removes the ECS instance that is added to the scaling group at the latest point in time.
               - OldestScalingConfiguration: removes the ECS instance that is created based on the earliest scaling configuration.
               - Default values: Default value of RemovalPolicy.1: OldestScalingConfiguration. Default value of RemovalPolicy.2: OldestInstance.
        :param pulumi.Input[str] scaling_group_name: Name shown for the scaling group, which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain numbers, underscores `_`, hyphens `-`, and decimal points `.`. If this parameter is not specified, the default value is ScalingGroupId.
        :param pulumi.Input[int] spot_instance_pools: The number of Spot pools to use to allocate your Spot capacity. The Spot pools is composed of instance types of lowest price.
        :param pulumi.Input[bool] spot_instance_remedy: Whether to replace spot instances with newly created spot/onDemand instance when receive a spot recycling message.
        :param pulumi.Input[str] vswitch_id: It has been deprecated from version 1.7.1 and new field 'vswitch_ids' replaces it.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] vswitch_ids: List of virtual switch IDs in which the ecs instances to be launched.
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

            __props__['db_instance_ids'] = db_instance_ids
            __props__['default_cooldown'] = default_cooldown
            __props__['desired_capacity'] = desired_capacity
            __props__['group_deletion_protection'] = group_deletion_protection
            __props__['loadbalancer_ids'] = loadbalancer_ids
            if max_size is None:
                raise TypeError("Missing required property 'max_size'")
            __props__['max_size'] = max_size
            if min_size is None:
                raise TypeError("Missing required property 'min_size'")
            __props__['min_size'] = min_size
            __props__['multi_az_policy'] = multi_az_policy
            __props__['on_demand_base_capacity'] = on_demand_base_capacity
            __props__['on_demand_percentage_above_base_capacity'] = on_demand_percentage_above_base_capacity
            __props__['removal_policies'] = removal_policies
            __props__['scaling_group_name'] = scaling_group_name
            __props__['spot_instance_pools'] = spot_instance_pools
            __props__['spot_instance_remedy'] = spot_instance_remedy
            if vswitch_id is not None:
                warnings.warn("""Field 'vswitch_id' has been deprecated from provider version 1.7.1, and new field 'vswitch_ids' can replace it.""", DeprecationWarning)
                pulumi.log.warn("vswitch_id is deprecated: Field 'vswitch_id' has been deprecated from provider version 1.7.1, and new field 'vswitch_ids' can replace it.")
            __props__['vswitch_id'] = vswitch_id
            __props__['vswitch_ids'] = vswitch_ids
        super(ScalingGroup, __self__).__init__(
            'alicloud:ess/scalingGroup:ScalingGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            db_instance_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            default_cooldown: Optional[pulumi.Input[int]] = None,
            desired_capacity: Optional[pulumi.Input[int]] = None,
            group_deletion_protection: Optional[pulumi.Input[bool]] = None,
            loadbalancer_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            max_size: Optional[pulumi.Input[int]] = None,
            min_size: Optional[pulumi.Input[int]] = None,
            multi_az_policy: Optional[pulumi.Input[str]] = None,
            on_demand_base_capacity: Optional[pulumi.Input[int]] = None,
            on_demand_percentage_above_base_capacity: Optional[pulumi.Input[int]] = None,
            removal_policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            scaling_group_name: Optional[pulumi.Input[str]] = None,
            spot_instance_pools: Optional[pulumi.Input[int]] = None,
            spot_instance_remedy: Optional[pulumi.Input[bool]] = None,
            vswitch_id: Optional[pulumi.Input[str]] = None,
            vswitch_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'ScalingGroup':
        """
        Get an existing ScalingGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] db_instance_ids: If an RDS instance is specified in the scaling group, the scaling group automatically attaches the Intranet IP addresses of its ECS instances to the RDS access whitelist.
               - The specified RDS instance must be in running status.
               - The specified RDS instance’s whitelist must have room for more IP addresses.
        :param pulumi.Input[int] default_cooldown: Default cool-down time (in seconds) of the scaling group. Value range: [0, 86400]. The default value is 300s.
        :param pulumi.Input[int] desired_capacity: Expected number of ECS instances in the scaling group. Value range: [min_size, max_size].
        :param pulumi.Input[bool] group_deletion_protection: Specifies whether the scaling group deletion protection is enabled. `true` or `false`, Default value: `false`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] loadbalancer_ids: If a Server Load Balancer instance is specified in the scaling group, the scaling group automatically attaches its ECS instances to the Server Load Balancer instance.
               - The Server Load Balancer instance must be enabled.
               - At least one listener must be configured for each Server Load Balancer and it HealthCheck must be on. Otherwise, creation will fail (it may be useful to add a `depends_on` argument
               targeting your `slb.Listener` in order to make sure the listener with its HealthCheck configuration is ready before creating your scaling group).
               - The Server Load Balancer instance attached with VPC-type ECS instances cannot be attached to the scaling group.
               - The default weight of an ECS instance attached to the Server Load Balancer instance is 50.
        :param pulumi.Input[int] max_size: Maximum number of ECS instances in the scaling group. Value range: [0, 1000].
        :param pulumi.Input[int] min_size: Minimum number of ECS instances in the scaling group. Value range: [0, 1000].
        :param pulumi.Input[str] multi_az_policy: Multi-AZ scaling group ECS instance expansion and contraction strategy. PRIORITY, BALANCE or COST_OPTIMIZED(Available in 1.54.0+).
        :param pulumi.Input[int] on_demand_base_capacity: The minimum amount of the Auto Scaling group's capacity that must be fulfilled by On-Demand Instances. This base portion is provisioned first as your group scales.
        :param pulumi.Input[int] on_demand_percentage_above_base_capacity: Controls the percentages of On-Demand Instances and Spot Instances for your additional capacity beyond OnDemandBaseCapacity.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] removal_policies: RemovalPolicy is used to select the ECS instances you want to remove from the scaling group when multiple candidates for removal exist. Optional values:
               - OldestInstance: removes the ECS instance that is added to the scaling group at the earliest point in time.
               - NewestInstance: removes the ECS instance that is added to the scaling group at the latest point in time.
               - OldestScalingConfiguration: removes the ECS instance that is created based on the earliest scaling configuration.
               - Default values: Default value of RemovalPolicy.1: OldestScalingConfiguration. Default value of RemovalPolicy.2: OldestInstance.
        :param pulumi.Input[str] scaling_group_name: Name shown for the scaling group, which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain numbers, underscores `_`, hyphens `-`, and decimal points `.`. If this parameter is not specified, the default value is ScalingGroupId.
        :param pulumi.Input[int] spot_instance_pools: The number of Spot pools to use to allocate your Spot capacity. The Spot pools is composed of instance types of lowest price.
        :param pulumi.Input[bool] spot_instance_remedy: Whether to replace spot instances with newly created spot/onDemand instance when receive a spot recycling message.
        :param pulumi.Input[str] vswitch_id: It has been deprecated from version 1.7.1 and new field 'vswitch_ids' replaces it.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] vswitch_ids: List of virtual switch IDs in which the ecs instances to be launched.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["db_instance_ids"] = db_instance_ids
        __props__["default_cooldown"] = default_cooldown
        __props__["desired_capacity"] = desired_capacity
        __props__["group_deletion_protection"] = group_deletion_protection
        __props__["loadbalancer_ids"] = loadbalancer_ids
        __props__["max_size"] = max_size
        __props__["min_size"] = min_size
        __props__["multi_az_policy"] = multi_az_policy
        __props__["on_demand_base_capacity"] = on_demand_base_capacity
        __props__["on_demand_percentage_above_base_capacity"] = on_demand_percentage_above_base_capacity
        __props__["removal_policies"] = removal_policies
        __props__["scaling_group_name"] = scaling_group_name
        __props__["spot_instance_pools"] = spot_instance_pools
        __props__["spot_instance_remedy"] = spot_instance_remedy
        __props__["vswitch_id"] = vswitch_id
        __props__["vswitch_ids"] = vswitch_ids
        return ScalingGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dbInstanceIds")
    def db_instance_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        If an RDS instance is specified in the scaling group, the scaling group automatically attaches the Intranet IP addresses of its ECS instances to the RDS access whitelist.
        - The specified RDS instance must be in running status.
        - The specified RDS instance’s whitelist must have room for more IP addresses.
        """
        return pulumi.get(self, "db_instance_ids")

    @property
    @pulumi.getter(name="defaultCooldown")
    def default_cooldown(self) -> pulumi.Output[Optional[int]]:
        """
        Default cool-down time (in seconds) of the scaling group. Value range: [0, 86400]. The default value is 300s.
        """
        return pulumi.get(self, "default_cooldown")

    @property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> pulumi.Output[Optional[int]]:
        """
        Expected number of ECS instances in the scaling group. Value range: [min_size, max_size].
        """
        return pulumi.get(self, "desired_capacity")

    @property
    @pulumi.getter(name="groupDeletionProtection")
    def group_deletion_protection(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether the scaling group deletion protection is enabled. `true` or `false`, Default value: `false`.
        """
        return pulumi.get(self, "group_deletion_protection")

    @property
    @pulumi.getter(name="loadbalancerIds")
    def loadbalancer_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        If a Server Load Balancer instance is specified in the scaling group, the scaling group automatically attaches its ECS instances to the Server Load Balancer instance.
        - The Server Load Balancer instance must be enabled.
        - At least one listener must be configured for each Server Load Balancer and it HealthCheck must be on. Otherwise, creation will fail (it may be useful to add a `depends_on` argument
        targeting your `slb.Listener` in order to make sure the listener with its HealthCheck configuration is ready before creating your scaling group).
        - The Server Load Balancer instance attached with VPC-type ECS instances cannot be attached to the scaling group.
        - The default weight of an ECS instance attached to the Server Load Balancer instance is 50.
        """
        return pulumi.get(self, "loadbalancer_ids")

    @property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> pulumi.Output[int]:
        """
        Maximum number of ECS instances in the scaling group. Value range: [0, 1000].
        """
        return pulumi.get(self, "max_size")

    @property
    @pulumi.getter(name="minSize")
    def min_size(self) -> pulumi.Output[int]:
        """
        Minimum number of ECS instances in the scaling group. Value range: [0, 1000].
        """
        return pulumi.get(self, "min_size")

    @property
    @pulumi.getter(name="multiAzPolicy")
    def multi_az_policy(self) -> pulumi.Output[Optional[str]]:
        """
        Multi-AZ scaling group ECS instance expansion and contraction strategy. PRIORITY, BALANCE or COST_OPTIMIZED(Available in 1.54.0+).
        """
        return pulumi.get(self, "multi_az_policy")

    @property
    @pulumi.getter(name="onDemandBaseCapacity")
    def on_demand_base_capacity(self) -> pulumi.Output[int]:
        """
        The minimum amount of the Auto Scaling group's capacity that must be fulfilled by On-Demand Instances. This base portion is provisioned first as your group scales.
        """
        return pulumi.get(self, "on_demand_base_capacity")

    @property
    @pulumi.getter(name="onDemandPercentageAboveBaseCapacity")
    def on_demand_percentage_above_base_capacity(self) -> pulumi.Output[int]:
        """
        Controls the percentages of On-Demand Instances and Spot Instances for your additional capacity beyond OnDemandBaseCapacity.
        """
        return pulumi.get(self, "on_demand_percentage_above_base_capacity")

    @property
    @pulumi.getter(name="removalPolicies")
    def removal_policies(self) -> pulumi.Output[Sequence[str]]:
        """
        RemovalPolicy is used to select the ECS instances you want to remove from the scaling group when multiple candidates for removal exist. Optional values:
        - OldestInstance: removes the ECS instance that is added to the scaling group at the earliest point in time.
        - NewestInstance: removes the ECS instance that is added to the scaling group at the latest point in time.
        - OldestScalingConfiguration: removes the ECS instance that is created based on the earliest scaling configuration.
        - Default values: Default value of RemovalPolicy.1: OldestScalingConfiguration. Default value of RemovalPolicy.2: OldestInstance.
        """
        return pulumi.get(self, "removal_policies")

    @property
    @pulumi.getter(name="scalingGroupName")
    def scaling_group_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name shown for the scaling group, which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain numbers, underscores `_`, hyphens `-`, and decimal points `.`. If this parameter is not specified, the default value is ScalingGroupId.
        """
        return pulumi.get(self, "scaling_group_name")

    @property
    @pulumi.getter(name="spotInstancePools")
    def spot_instance_pools(self) -> pulumi.Output[int]:
        """
        The number of Spot pools to use to allocate your Spot capacity. The Spot pools is composed of instance types of lowest price.
        """
        return pulumi.get(self, "spot_instance_pools")

    @property
    @pulumi.getter(name="spotInstanceRemedy")
    def spot_instance_remedy(self) -> pulumi.Output[bool]:
        """
        Whether to replace spot instances with newly created spot/onDemand instance when receive a spot recycling message.
        """
        return pulumi.get(self, "spot_instance_remedy")

    @property
    @pulumi.getter(name="vswitchId")
    def vswitch_id(self) -> pulumi.Output[Optional[str]]:
        """
        It has been deprecated from version 1.7.1 and new field 'vswitch_ids' replaces it.
        """
        return pulumi.get(self, "vswitch_id")

    @property
    @pulumi.getter(name="vswitchIds")
    def vswitch_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of virtual switch IDs in which the ecs instances to be launched.
        """
        return pulumi.get(self, "vswitch_ids")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

