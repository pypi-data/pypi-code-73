# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['AccountPrivilege']


class AccountPrivilege(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 account_privilege: Optional[pulumi.Input[str]] = None,
                 db_cluster_id: Optional[pulumi.Input[str]] = None,
                 db_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a PolarDB account privilege resource and used to grant several database some access privilege. A database can be granted by multiple account.

        > **NOTE:** Available in v1.67.0+.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        creation = config.get("creation")
        if creation is None:
            creation = "PolarDB"
        name = config.get("name")
        if name is None:
            name = "dbaccountprivilegebasic"
        default_zones = alicloud.get_zones(available_resource_creation=creation)
        default_network = alicloud.vpc.Network("defaultNetwork", cidr_block="172.16.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vpc_id=default_network.id,
            cidr_block="172.16.0.0/24",
            availability_zone=default_zones.zones[0].id)
        cluster = alicloud.polardb.Cluster("cluster",
            db_type="MySQL",
            db_version="8.0",
            pay_type="PostPaid",
            db_node_class="polar.mysql.x4.large",
            vswitch_id=default_switch.id,
            description=name)
        db = alicloud.polardb.Database("db",
            db_cluster_id=cluster.id,
            db_name="tftestdatabase")
        account = alicloud.polardb.Account("account",
            db_cluster_id=cluster.id,
            account_name="tftestnormal",
            account_password="Test12345",
            account_description=name)
        privilege = alicloud.polardb.AccountPrivilege("privilege",
            db_cluster_id=cluster.id,
            account_name=account.account_name,
            account_privilege="ReadOnly",
            db_names=[db.db_name])
        ```

        ## Import

        PolarDB account privilege can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:polardb/accountPrivilege:AccountPrivilege example "pc-12345:tf_account:ReadOnly"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: A specified account name.
        :param pulumi.Input[str] account_privilege: The privilege of one account access database. Valid values: ["ReadOnly", "ReadWrite"], ["DMLOnly", "DDLOnly"] added since version v1.101.0. Default to "ReadOnly".
        :param pulumi.Input[str] db_cluster_id: The Id of cluster in which account belongs.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] db_names: List of specified database name.
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

            if account_name is None:
                raise TypeError("Missing required property 'account_name'")
            __props__['account_name'] = account_name
            __props__['account_privilege'] = account_privilege
            if db_cluster_id is None:
                raise TypeError("Missing required property 'db_cluster_id'")
            __props__['db_cluster_id'] = db_cluster_id
            if db_names is None:
                raise TypeError("Missing required property 'db_names'")
            __props__['db_names'] = db_names
        super(AccountPrivilege, __self__).__init__(
            'alicloud:polardb/accountPrivilege:AccountPrivilege',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_name: Optional[pulumi.Input[str]] = None,
            account_privilege: Optional[pulumi.Input[str]] = None,
            db_cluster_id: Optional[pulumi.Input[str]] = None,
            db_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'AccountPrivilege':
        """
        Get an existing AccountPrivilege resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: A specified account name.
        :param pulumi.Input[str] account_privilege: The privilege of one account access database. Valid values: ["ReadOnly", "ReadWrite"], ["DMLOnly", "DDLOnly"] added since version v1.101.0. Default to "ReadOnly".
        :param pulumi.Input[str] db_cluster_id: The Id of cluster in which account belongs.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] db_names: List of specified database name.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["account_name"] = account_name
        __props__["account_privilege"] = account_privilege
        __props__["db_cluster_id"] = db_cluster_id
        __props__["db_names"] = db_names
        return AccountPrivilege(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Output[str]:
        """
        A specified account name.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter(name="accountPrivilege")
    def account_privilege(self) -> pulumi.Output[Optional[str]]:
        """
        The privilege of one account access database. Valid values: ["ReadOnly", "ReadWrite"], ["DMLOnly", "DDLOnly"] added since version v1.101.0. Default to "ReadOnly".
        """
        return pulumi.get(self, "account_privilege")

    @property
    @pulumi.getter(name="dbClusterId")
    def db_cluster_id(self) -> pulumi.Output[str]:
        """
        The Id of cluster in which account belongs.
        """
        return pulumi.get(self, "db_cluster_id")

    @property
    @pulumi.getter(name="dbNames")
    def db_names(self) -> pulumi.Output[Sequence[str]]:
        """
        List of specified database name.
        """
        return pulumi.get(self, "db_names")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

