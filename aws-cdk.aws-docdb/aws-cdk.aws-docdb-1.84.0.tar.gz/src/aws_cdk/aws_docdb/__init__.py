"""
# Amazon DocumentDB Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be
> announced in the release notes. This means that while you may use them, you may need to update
> your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

## Starting a Clustered Database

To set up a clustered DocumentDB database, define a `DatabaseCluster`. You must
always launch a database in a VPC. Use the `vpcSubnets` attribute to control whether
your instances will be launched privately or publicly:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
cluster = DatabaseCluster(self, "Database",
    master_user={
        "username": "admin"
    },
    instance_props={
        "instance_type": ec2.InstanceType.of(ec2.InstanceClass.R5, ec2.InstanceSize.LARGE),
        "vpc_subnets": {
            "subnet_type": ec2.SubnetType.PUBLIC
        },
        "vpc": vpc
    }
)
```

By default, the master password will be generated and stored in AWS Secrets Manager with auto-generated description.

Your cluster will be empty by default.

## Connecting

To control who can access the cluster, use the `.connections` attribute. DocumentDB databases have a default port, so
you don't need to specify the port:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
cluster.connections.allow_default_port_from_any_ipv4("Open to the world")
```

The endpoints to access your database cluster will be available as the `.clusterEndpoint` and `.clusterReadEndpoint`
attributes:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
write_address = cluster.cluster_endpoint.socket_address
```

## Rotating credentials

When the master password is generated and stored in AWS Secrets Manager, it can be rotated automatically:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
cluster.add_rotation_single_user()
```

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
cluster = docdb.DatabaseCluster(stack, "Database",
    master_user=Login(
        username="docdb"
    ),
    instance_props={
        "instance_type": ec2.InstanceType.of(ec2.InstanceClass.R5, ec2.InstanceSize.LARGE),
        "vpc": vpc
    },
    removal_policy=cdk.RemovalPolicy.DESTROY
)

cluster.add_rotation_single_user()
```

The multi user rotation scheme is also available:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
cluster.add_rotation_multi_user("MyUser",
    secret=my_imported_secret
)
```

It's also possible to create user credentials together with the cluster and add rotation:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
my_user_secret = docdb.DatabaseSecret(self, "MyUserSecret",
    username="myuser",
    master_secret=cluster.secret
)
my_user_secret_attached = my_user_secret.attach(cluster)# Adds DB connections information in the secret

cluster.add_rotation_multi_user("MyUser", # Add rotation using the multi user scheme
    secret=my_user_secret_attached)
```

**Note**: This user must be created manually in the database using the master credentials.
The rotation will start as soon as this user exists.

See also [@aws-cdk/aws-secretsmanager](https://github.com/aws/aws-cdk/blob/master/packages/%40aws-cdk/aws-secretsmanager/README.md) for credentials rotation of existing clusters.
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.aws_ec2
import aws_cdk.aws_kms
import aws_cdk.aws_secretsmanager
import aws_cdk.core
import constructs


@jsii.data_type(
    jsii_type="@aws-cdk/aws-docdb.BackupProps",
    jsii_struct_bases=[],
    name_mapping={"retention": "retention", "preferred_window": "preferredWindow"},
)
class BackupProps:
    def __init__(
        self,
        *,
        retention: aws_cdk.core.Duration,
        preferred_window: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Backup configuration for DocumentDB databases.

        :param retention: (experimental) How many days to retain the backup.
        :param preferred_window: (experimental) A daily time range in 24-hours UTC format in which backups preferably execute. Must be at least 30 minutes long. Example: '01:00-02:00' Default: - a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see https://docs.aws.amazon.com/documentdb/latest/developerguide/backup-restore.db-cluster-snapshots.html#backup-restore.backup-window

        :default:

        - The retention period for automated backups is 1 day.
        The preferred backup window will be a 30-minute window selected at random
        from an 8-hour block of time for each AWS Region.

        :see: https://docs.aws.amazon.com/documentdb/latest/developerguide/backup-restore.db-cluster-snapshots.html#backup-restore.backup-window
        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "retention": retention,
        }
        if preferred_window is not None:
            self._values["preferred_window"] = preferred_window

    @builtins.property
    def retention(self) -> aws_cdk.core.Duration:
        """(experimental) How many days to retain the backup.

        :stability: experimental
        """
        result = self._values.get("retention")
        assert result is not None, "Required property 'retention' is missing"
        return result

    @builtins.property
    def preferred_window(self) -> typing.Optional[builtins.str]:
        """(experimental) A daily time range in 24-hours UTC format in which backups preferably execute.

        Must be at least 30 minutes long.

        Example: '01:00-02:00'

        :default:

        - a 30-minute window selected at random from an 8-hour block of
        time for each AWS Region. To see the time blocks available, see
        https://docs.aws.amazon.com/documentdb/latest/developerguide/backup-restore.db-cluster-snapshots.html#backup-restore.backup-window

        :stability: experimental
        """
        result = self._values.get("preferred_window")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDBCluster(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-docdb.CfnDBCluster",
):
    """A CloudFormation ``AWS::DocDB::DBCluster``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html
    :cloudformationResource: AWS::DocDB::DBCluster
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        master_username: builtins.str,
        master_user_password: builtins.str,
        availability_zones: typing.Optional[typing.List[builtins.str]] = None,
        backup_retention_period: typing.Optional[jsii.Number] = None,
        db_cluster_identifier: typing.Optional[builtins.str] = None,
        db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        enable_cloudwatch_logs_exports: typing.Optional[typing.List[builtins.str]] = None,
        engine_version: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        snapshot_identifier: typing.Optional[builtins.str] = None,
        storage_encrypted: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
        vpc_security_group_ids: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """Create a new ``AWS::DocDB::DBCluster``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param master_username: ``AWS::DocDB::DBCluster.MasterUsername``.
        :param master_user_password: ``AWS::DocDB::DBCluster.MasterUserPassword``.
        :param availability_zones: ``AWS::DocDB::DBCluster.AvailabilityZones``.
        :param backup_retention_period: ``AWS::DocDB::DBCluster.BackupRetentionPeriod``.
        :param db_cluster_identifier: ``AWS::DocDB::DBCluster.DBClusterIdentifier``.
        :param db_cluster_parameter_group_name: ``AWS::DocDB::DBCluster.DBClusterParameterGroupName``.
        :param db_subnet_group_name: ``AWS::DocDB::DBCluster.DBSubnetGroupName``.
        :param deletion_protection: ``AWS::DocDB::DBCluster.DeletionProtection``.
        :param enable_cloudwatch_logs_exports: ``AWS::DocDB::DBCluster.EnableCloudwatchLogsExports``.
        :param engine_version: ``AWS::DocDB::DBCluster.EngineVersion``.
        :param kms_key_id: ``AWS::DocDB::DBCluster.KmsKeyId``.
        :param port: ``AWS::DocDB::DBCluster.Port``.
        :param preferred_backup_window: ``AWS::DocDB::DBCluster.PreferredBackupWindow``.
        :param preferred_maintenance_window: ``AWS::DocDB::DBCluster.PreferredMaintenanceWindow``.
        :param snapshot_identifier: ``AWS::DocDB::DBCluster.SnapshotIdentifier``.
        :param storage_encrypted: ``AWS::DocDB::DBCluster.StorageEncrypted``.
        :param tags: ``AWS::DocDB::DBCluster.Tags``.
        :param vpc_security_group_ids: ``AWS::DocDB::DBCluster.VpcSecurityGroupIds``.
        """
        props = CfnDBClusterProps(
            master_username=master_username,
            master_user_password=master_user_password,
            availability_zones=availability_zones,
            backup_retention_period=backup_retention_period,
            db_cluster_identifier=db_cluster_identifier,
            db_cluster_parameter_group_name=db_cluster_parameter_group_name,
            db_subnet_group_name=db_subnet_group_name,
            deletion_protection=deletion_protection,
            enable_cloudwatch_logs_exports=enable_cloudwatch_logs_exports,
            engine_version=engine_version,
            kms_key_id=kms_key_id,
            port=port,
            preferred_backup_window=preferred_backup_window,
            preferred_maintenance_window=preferred_maintenance_window,
            snapshot_identifier=snapshot_identifier,
            storage_encrypted=storage_encrypted,
            tags=tags,
            vpc_security_group_ids=vpc_security_group_ids,
        )

        jsii.create(CfnDBCluster, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrClusterResourceId")
    def attr_cluster_resource_id(self) -> builtins.str:
        """
        :cloudformationAttribute: ClusterResourceId
        """
        return jsii.get(self, "attrClusterResourceId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrEndpoint")
    def attr_endpoint(self) -> builtins.str:
        """
        :cloudformationAttribute: Endpoint
        """
        return jsii.get(self, "attrEndpoint")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrPort")
    def attr_port(self) -> builtins.str:
        """
        :cloudformationAttribute: Port
        """
        return jsii.get(self, "attrPort")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrReadEndpoint")
    def attr_read_endpoint(self) -> builtins.str:
        """
        :cloudformationAttribute: ReadEndpoint
        """
        return jsii.get(self, "attrReadEndpoint")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::DocDB::DBCluster.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="masterUsername")
    def master_username(self) -> builtins.str:
        """``AWS::DocDB::DBCluster.MasterUsername``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-masterusername
        """
        return jsii.get(self, "masterUsername")

    @master_username.setter # type: ignore
    def master_username(self, value: builtins.str) -> None:
        jsii.set(self, "masterUsername", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="masterUserPassword")
    def master_user_password(self) -> builtins.str:
        """``AWS::DocDB::DBCluster.MasterUserPassword``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-masteruserpassword
        """
        return jsii.get(self, "masterUserPassword")

    @master_user_password.setter # type: ignore
    def master_user_password(self, value: builtins.str) -> None:
        jsii.set(self, "masterUserPassword", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::DocDB::DBCluster.AvailabilityZones``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-availabilityzones
        """
        return jsii.get(self, "availabilityZones")

    @availability_zones.setter # type: ignore
    def availability_zones(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "availabilityZones", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="backupRetentionPeriod")
    def backup_retention_period(self) -> typing.Optional[jsii.Number]:
        """``AWS::DocDB::DBCluster.BackupRetentionPeriod``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-backupretentionperiod
        """
        return jsii.get(self, "backupRetentionPeriod")

    @backup_retention_period.setter # type: ignore
    def backup_retention_period(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "backupRetentionPeriod", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBCluster.DBClusterIdentifier``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-dbclusteridentifier
        """
        return jsii.get(self, "dbClusterIdentifier")

    @db_cluster_identifier.setter # type: ignore
    def db_cluster_identifier(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "dbClusterIdentifier", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dbClusterParameterGroupName")
    def db_cluster_parameter_group_name(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBCluster.DBClusterParameterGroupName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-dbclusterparametergroupname
        """
        return jsii.get(self, "dbClusterParameterGroupName")

    @db_cluster_parameter_group_name.setter # type: ignore
    def db_cluster_parameter_group_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "dbClusterParameterGroupName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBCluster.DBSubnetGroupName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-dbsubnetgroupname
        """
        return jsii.get(self, "dbSubnetGroupName")

    @db_subnet_group_name.setter # type: ignore
    def db_subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "dbSubnetGroupName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="deletionProtection")
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        """``AWS::DocDB::DBCluster.DeletionProtection``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-deletionprotection
        """
        return jsii.get(self, "deletionProtection")

    @deletion_protection.setter # type: ignore
    def deletion_protection(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "deletionProtection", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="enableCloudwatchLogsExports")
    def enable_cloudwatch_logs_exports(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::DocDB::DBCluster.EnableCloudwatchLogsExports``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-enablecloudwatchlogsexports
        """
        return jsii.get(self, "enableCloudwatchLogsExports")

    @enable_cloudwatch_logs_exports.setter # type: ignore
    def enable_cloudwatch_logs_exports(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "enableCloudwatchLogsExports", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBCluster.EngineVersion``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-engineversion
        """
        return jsii.get(self, "engineVersion")

    @engine_version.setter # type: ignore
    def engine_version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "engineVersion", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBCluster.KmsKeyId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-kmskeyid
        """
        return jsii.get(self, "kmsKeyId")

    @kms_key_id.setter # type: ignore
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        """``AWS::DocDB::DBCluster.Port``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-port
        """
        return jsii.get(self, "port")

    @port.setter # type: ignore
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "port", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="preferredBackupWindow")
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBCluster.PreferredBackupWindow``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-preferredbackupwindow
        """
        return jsii.get(self, "preferredBackupWindow")

    @preferred_backup_window.setter # type: ignore
    def preferred_backup_window(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "preferredBackupWindow", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBCluster.PreferredMaintenanceWindow``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-preferredmaintenancewindow
        """
        return jsii.get(self, "preferredMaintenanceWindow")

    @preferred_maintenance_window.setter # type: ignore
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="snapshotIdentifier")
    def snapshot_identifier(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBCluster.SnapshotIdentifier``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-snapshotidentifier
        """
        return jsii.get(self, "snapshotIdentifier")

    @snapshot_identifier.setter # type: ignore
    def snapshot_identifier(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "snapshotIdentifier", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="storageEncrypted")
    def storage_encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        """``AWS::DocDB::DBCluster.StorageEncrypted``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-storageencrypted
        """
        return jsii.get(self, "storageEncrypted")

    @storage_encrypted.setter # type: ignore
    def storage_encrypted(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "storageEncrypted", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::DocDB::DBCluster.VpcSecurityGroupIds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-vpcsecuritygroupids
        """
        return jsii.get(self, "vpcSecurityGroupIds")

    @vpc_security_group_ids.setter # type: ignore
    def vpc_security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "vpcSecurityGroupIds", value)


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDBClusterParameterGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-docdb.CfnDBClusterParameterGroup",
):
    """A CloudFormation ``AWS::DocDB::DBClusterParameterGroup``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html
    :cloudformationResource: AWS::DocDB::DBClusterParameterGroup
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        description: builtins.str,
        family: builtins.str,
        parameters: typing.Any,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::DocDB::DBClusterParameterGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::DocDB::DBClusterParameterGroup.Description``.
        :param family: ``AWS::DocDB::DBClusterParameterGroup.Family``.
        :param parameters: ``AWS::DocDB::DBClusterParameterGroup.Parameters``.
        :param name: ``AWS::DocDB::DBClusterParameterGroup.Name``.
        :param tags: ``AWS::DocDB::DBClusterParameterGroup.Tags``.
        """
        props = CfnDBClusterParameterGroupProps(
            description=description,
            family=family,
            parameters=parameters,
            name=name,
            tags=tags,
        )

        jsii.create(CfnDBClusterParameterGroup, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::DocDB::DBClusterParameterGroup.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        """``AWS::DocDB::DBClusterParameterGroup.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: builtins.str) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="family")
    def family(self) -> builtins.str:
        """``AWS::DocDB::DBClusterParameterGroup.Family``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-family
        """
        return jsii.get(self, "family")

    @family.setter # type: ignore
    def family(self, value: builtins.str) -> None:
        jsii.set(self, "family", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Any:
        """``AWS::DocDB::DBClusterParameterGroup.Parameters``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-parameters
        """
        return jsii.get(self, "parameters")

    @parameters.setter # type: ignore
    def parameters(self, value: typing.Any) -> None:
        jsii.set(self, "parameters", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBClusterParameterGroup.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-docdb.CfnDBClusterParameterGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "family": "family",
        "parameters": "parameters",
        "name": "name",
        "tags": "tags",
    },
)
class CfnDBClusterParameterGroupProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        family: builtins.str,
        parameters: typing.Any,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::DocDB::DBClusterParameterGroup``.

        :param description: ``AWS::DocDB::DBClusterParameterGroup.Description``.
        :param family: ``AWS::DocDB::DBClusterParameterGroup.Family``.
        :param parameters: ``AWS::DocDB::DBClusterParameterGroup.Parameters``.
        :param name: ``AWS::DocDB::DBClusterParameterGroup.Name``.
        :param tags: ``AWS::DocDB::DBClusterParameterGroup.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "family": family,
            "parameters": parameters,
        }
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> builtins.str:
        """``AWS::DocDB::DBClusterParameterGroup.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-description
        """
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return result

    @builtins.property
    def family(self) -> builtins.str:
        """``AWS::DocDB::DBClusterParameterGroup.Family``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-family
        """
        result = self._values.get("family")
        assert result is not None, "Required property 'family' is missing"
        return result

    @builtins.property
    def parameters(self) -> typing.Any:
        """``AWS::DocDB::DBClusterParameterGroup.Parameters``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-parameters
        """
        result = self._values.get("parameters")
        assert result is not None, "Required property 'parameters' is missing"
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBClusterParameterGroup.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::DocDB::DBClusterParameterGroup.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDBClusterParameterGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-docdb.CfnDBClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "master_username": "masterUsername",
        "master_user_password": "masterUserPassword",
        "availability_zones": "availabilityZones",
        "backup_retention_period": "backupRetentionPeriod",
        "db_cluster_identifier": "dbClusterIdentifier",
        "db_cluster_parameter_group_name": "dbClusterParameterGroupName",
        "db_subnet_group_name": "dbSubnetGroupName",
        "deletion_protection": "deletionProtection",
        "enable_cloudwatch_logs_exports": "enableCloudwatchLogsExports",
        "engine_version": "engineVersion",
        "kms_key_id": "kmsKeyId",
        "port": "port",
        "preferred_backup_window": "preferredBackupWindow",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "snapshot_identifier": "snapshotIdentifier",
        "storage_encrypted": "storageEncrypted",
        "tags": "tags",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
    },
)
class CfnDBClusterProps:
    def __init__(
        self,
        *,
        master_username: builtins.str,
        master_user_password: builtins.str,
        availability_zones: typing.Optional[typing.List[builtins.str]] = None,
        backup_retention_period: typing.Optional[jsii.Number] = None,
        db_cluster_identifier: typing.Optional[builtins.str] = None,
        db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        enable_cloudwatch_logs_exports: typing.Optional[typing.List[builtins.str]] = None,
        engine_version: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        snapshot_identifier: typing.Optional[builtins.str] = None,
        storage_encrypted: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
        vpc_security_group_ids: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """Properties for defining a ``AWS::DocDB::DBCluster``.

        :param master_username: ``AWS::DocDB::DBCluster.MasterUsername``.
        :param master_user_password: ``AWS::DocDB::DBCluster.MasterUserPassword``.
        :param availability_zones: ``AWS::DocDB::DBCluster.AvailabilityZones``.
        :param backup_retention_period: ``AWS::DocDB::DBCluster.BackupRetentionPeriod``.
        :param db_cluster_identifier: ``AWS::DocDB::DBCluster.DBClusterIdentifier``.
        :param db_cluster_parameter_group_name: ``AWS::DocDB::DBCluster.DBClusterParameterGroupName``.
        :param db_subnet_group_name: ``AWS::DocDB::DBCluster.DBSubnetGroupName``.
        :param deletion_protection: ``AWS::DocDB::DBCluster.DeletionProtection``.
        :param enable_cloudwatch_logs_exports: ``AWS::DocDB::DBCluster.EnableCloudwatchLogsExports``.
        :param engine_version: ``AWS::DocDB::DBCluster.EngineVersion``.
        :param kms_key_id: ``AWS::DocDB::DBCluster.KmsKeyId``.
        :param port: ``AWS::DocDB::DBCluster.Port``.
        :param preferred_backup_window: ``AWS::DocDB::DBCluster.PreferredBackupWindow``.
        :param preferred_maintenance_window: ``AWS::DocDB::DBCluster.PreferredMaintenanceWindow``.
        :param snapshot_identifier: ``AWS::DocDB::DBCluster.SnapshotIdentifier``.
        :param storage_encrypted: ``AWS::DocDB::DBCluster.StorageEncrypted``.
        :param tags: ``AWS::DocDB::DBCluster.Tags``.
        :param vpc_security_group_ids: ``AWS::DocDB::DBCluster.VpcSecurityGroupIds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "master_username": master_username,
            "master_user_password": master_user_password,
        }
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if backup_retention_period is not None:
            self._values["backup_retention_period"] = backup_retention_period
        if db_cluster_identifier is not None:
            self._values["db_cluster_identifier"] = db_cluster_identifier
        if db_cluster_parameter_group_name is not None:
            self._values["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        if db_subnet_group_name is not None:
            self._values["db_subnet_group_name"] = db_subnet_group_name
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if enable_cloudwatch_logs_exports is not None:
            self._values["enable_cloudwatch_logs_exports"] = enable_cloudwatch_logs_exports
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if port is not None:
            self._values["port"] = port
        if preferred_backup_window is not None:
            self._values["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if snapshot_identifier is not None:
            self._values["snapshot_identifier"] = snapshot_identifier
        if storage_encrypted is not None:
            self._values["storage_encrypted"] = storage_encrypted
        if tags is not None:
            self._values["tags"] = tags
        if vpc_security_group_ids is not None:
            self._values["vpc_security_group_ids"] = vpc_security_group_ids

    @builtins.property
    def master_username(self) -> builtins.str:
        """``AWS::DocDB::DBCluster.MasterUsername``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-masterusername
        """
        result = self._values.get("master_username")
        assert result is not None, "Required property 'master_username' is missing"
        return result

    @builtins.property
    def master_user_password(self) -> builtins.str:
        """``AWS::DocDB::DBCluster.MasterUserPassword``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-masteruserpassword
        """
        result = self._values.get("master_user_password")
        assert result is not None, "Required property 'master_user_password' is missing"
        return result

    @builtins.property
    def availability_zones(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::DocDB::DBCluster.AvailabilityZones``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-availabilityzones
        """
        result = self._values.get("availability_zones")
        return result

    @builtins.property
    def backup_retention_period(self) -> typing.Optional[jsii.Number]:
        """``AWS::DocDB::DBCluster.BackupRetentionPeriod``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-backupretentionperiod
        """
        result = self._values.get("backup_retention_period")
        return result

    @builtins.property
    def db_cluster_identifier(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBCluster.DBClusterIdentifier``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-dbclusteridentifier
        """
        result = self._values.get("db_cluster_identifier")
        return result

    @builtins.property
    def db_cluster_parameter_group_name(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBCluster.DBClusterParameterGroupName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-dbclusterparametergroupname
        """
        result = self._values.get("db_cluster_parameter_group_name")
        return result

    @builtins.property
    def db_subnet_group_name(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBCluster.DBSubnetGroupName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-dbsubnetgroupname
        """
        result = self._values.get("db_subnet_group_name")
        return result

    @builtins.property
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        """``AWS::DocDB::DBCluster.DeletionProtection``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-deletionprotection
        """
        result = self._values.get("deletion_protection")
        return result

    @builtins.property
    def enable_cloudwatch_logs_exports(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::DocDB::DBCluster.EnableCloudwatchLogsExports``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-enablecloudwatchlogsexports
        """
        result = self._values.get("enable_cloudwatch_logs_exports")
        return result

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBCluster.EngineVersion``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-engineversion
        """
        result = self._values.get("engine_version")
        return result

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBCluster.KmsKeyId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-kmskeyid
        """
        result = self._values.get("kms_key_id")
        return result

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        """``AWS::DocDB::DBCluster.Port``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-port
        """
        result = self._values.get("port")
        return result

    @builtins.property
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBCluster.PreferredBackupWindow``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-preferredbackupwindow
        """
        result = self._values.get("preferred_backup_window")
        return result

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBCluster.PreferredMaintenanceWindow``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-preferredmaintenancewindow
        """
        result = self._values.get("preferred_maintenance_window")
        return result

    @builtins.property
    def snapshot_identifier(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBCluster.SnapshotIdentifier``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-snapshotidentifier
        """
        result = self._values.get("snapshot_identifier")
        return result

    @builtins.property
    def storage_encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        """``AWS::DocDB::DBCluster.StorageEncrypted``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-storageencrypted
        """
        result = self._values.get("storage_encrypted")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::DocDB::DBCluster.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-tags
        """
        result = self._values.get("tags")
        return result

    @builtins.property
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::DocDB::DBCluster.VpcSecurityGroupIds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-vpcsecuritygroupids
        """
        result = self._values.get("vpc_security_group_ids")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDBClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDBInstance(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-docdb.CfnDBInstance",
):
    """A CloudFormation ``AWS::DocDB::DBInstance``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html
    :cloudformationResource: AWS::DocDB::DBInstance
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        db_cluster_identifier: builtins.str,
        db_instance_class: builtins.str,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        db_instance_identifier: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::DocDB::DBInstance``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param db_cluster_identifier: ``AWS::DocDB::DBInstance.DBClusterIdentifier``.
        :param db_instance_class: ``AWS::DocDB::DBInstance.DBInstanceClass``.
        :param auto_minor_version_upgrade: ``AWS::DocDB::DBInstance.AutoMinorVersionUpgrade``.
        :param availability_zone: ``AWS::DocDB::DBInstance.AvailabilityZone``.
        :param db_instance_identifier: ``AWS::DocDB::DBInstance.DBInstanceIdentifier``.
        :param preferred_maintenance_window: ``AWS::DocDB::DBInstance.PreferredMaintenanceWindow``.
        :param tags: ``AWS::DocDB::DBInstance.Tags``.
        """
        props = CfnDBInstanceProps(
            db_cluster_identifier=db_cluster_identifier,
            db_instance_class=db_instance_class,
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            availability_zone=availability_zone,
            db_instance_identifier=db_instance_identifier,
            preferred_maintenance_window=preferred_maintenance_window,
            tags=tags,
        )

        jsii.create(CfnDBInstance, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrEndpoint")
    def attr_endpoint(self) -> builtins.str:
        """
        :cloudformationAttribute: Endpoint
        """
        return jsii.get(self, "attrEndpoint")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrPort")
    def attr_port(self) -> builtins.str:
        """
        :cloudformationAttribute: Port
        """
        return jsii.get(self, "attrPort")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::DocDB::DBInstance.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> builtins.str:
        """``AWS::DocDB::DBInstance.DBClusterIdentifier``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-dbclusteridentifier
        """
        return jsii.get(self, "dbClusterIdentifier")

    @db_cluster_identifier.setter # type: ignore
    def db_cluster_identifier(self, value: builtins.str) -> None:
        jsii.set(self, "dbClusterIdentifier", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dbInstanceClass")
    def db_instance_class(self) -> builtins.str:
        """``AWS::DocDB::DBInstance.DBInstanceClass``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-dbinstanceclass
        """
        return jsii.get(self, "dbInstanceClass")

    @db_instance_class.setter # type: ignore
    def db_instance_class(self, value: builtins.str) -> None:
        jsii.set(self, "dbInstanceClass", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        """``AWS::DocDB::DBInstance.AutoMinorVersionUpgrade``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-autominorversionupgrade
        """
        return jsii.get(self, "autoMinorVersionUpgrade")

    @auto_minor_version_upgrade.setter # type: ignore
    def auto_minor_version_upgrade(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "autoMinorVersionUpgrade", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBInstance.AvailabilityZone``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-availabilityzone
        """
        return jsii.get(self, "availabilityZone")

    @availability_zone.setter # type: ignore
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "availabilityZone", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dbInstanceIdentifier")
    def db_instance_identifier(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBInstance.DBInstanceIdentifier``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-dbinstanceidentifier
        """
        return jsii.get(self, "dbInstanceIdentifier")

    @db_instance_identifier.setter # type: ignore
    def db_instance_identifier(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "dbInstanceIdentifier", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBInstance.PreferredMaintenanceWindow``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-preferredmaintenancewindow
        """
        return jsii.get(self, "preferredMaintenanceWindow")

    @preferred_maintenance_window.setter # type: ignore
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "preferredMaintenanceWindow", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-docdb.CfnDBInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "db_cluster_identifier": "dbClusterIdentifier",
        "db_instance_class": "dbInstanceClass",
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "availability_zone": "availabilityZone",
        "db_instance_identifier": "dbInstanceIdentifier",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "tags": "tags",
    },
)
class CfnDBInstanceProps:
    def __init__(
        self,
        *,
        db_cluster_identifier: builtins.str,
        db_instance_class: builtins.str,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        db_instance_identifier: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::DocDB::DBInstance``.

        :param db_cluster_identifier: ``AWS::DocDB::DBInstance.DBClusterIdentifier``.
        :param db_instance_class: ``AWS::DocDB::DBInstance.DBInstanceClass``.
        :param auto_minor_version_upgrade: ``AWS::DocDB::DBInstance.AutoMinorVersionUpgrade``.
        :param availability_zone: ``AWS::DocDB::DBInstance.AvailabilityZone``.
        :param db_instance_identifier: ``AWS::DocDB::DBInstance.DBInstanceIdentifier``.
        :param preferred_maintenance_window: ``AWS::DocDB::DBInstance.PreferredMaintenanceWindow``.
        :param tags: ``AWS::DocDB::DBInstance.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "db_cluster_identifier": db_cluster_identifier,
            "db_instance_class": db_instance_class,
        }
        if auto_minor_version_upgrade is not None:
            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if db_instance_identifier is not None:
            self._values["db_instance_identifier"] = db_instance_identifier
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def db_cluster_identifier(self) -> builtins.str:
        """``AWS::DocDB::DBInstance.DBClusterIdentifier``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-dbclusteridentifier
        """
        result = self._values.get("db_cluster_identifier")
        assert result is not None, "Required property 'db_cluster_identifier' is missing"
        return result

    @builtins.property
    def db_instance_class(self) -> builtins.str:
        """``AWS::DocDB::DBInstance.DBInstanceClass``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-dbinstanceclass
        """
        result = self._values.get("db_instance_class")
        assert result is not None, "Required property 'db_instance_class' is missing"
        return result

    @builtins.property
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        """``AWS::DocDB::DBInstance.AutoMinorVersionUpgrade``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-autominorversionupgrade
        """
        result = self._values.get("auto_minor_version_upgrade")
        return result

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBInstance.AvailabilityZone``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-availabilityzone
        """
        result = self._values.get("availability_zone")
        return result

    @builtins.property
    def db_instance_identifier(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBInstance.DBInstanceIdentifier``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-dbinstanceidentifier
        """
        result = self._values.get("db_instance_identifier")
        return result

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBInstance.PreferredMaintenanceWindow``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-preferredmaintenancewindow
        """
        result = self._values.get("preferred_maintenance_window")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::DocDB::DBInstance.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDBInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDBSubnetGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-docdb.CfnDBSubnetGroup",
):
    """A CloudFormation ``AWS::DocDB::DBSubnetGroup``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html
    :cloudformationResource: AWS::DocDB::DBSubnetGroup
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        db_subnet_group_description: builtins.str,
        subnet_ids: typing.List[builtins.str],
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::DocDB::DBSubnetGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param db_subnet_group_description: ``AWS::DocDB::DBSubnetGroup.DBSubnetGroupDescription``.
        :param subnet_ids: ``AWS::DocDB::DBSubnetGroup.SubnetIds``.
        :param db_subnet_group_name: ``AWS::DocDB::DBSubnetGroup.DBSubnetGroupName``.
        :param tags: ``AWS::DocDB::DBSubnetGroup.Tags``.
        """
        props = CfnDBSubnetGroupProps(
            db_subnet_group_description=db_subnet_group_description,
            subnet_ids=subnet_ids,
            db_subnet_group_name=db_subnet_group_name,
            tags=tags,
        )

        jsii.create(CfnDBSubnetGroup, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::DocDB::DBSubnetGroup.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dbSubnetGroupDescription")
    def db_subnet_group_description(self) -> builtins.str:
        """``AWS::DocDB::DBSubnetGroup.DBSubnetGroupDescription``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-dbsubnetgroupdescription
        """
        return jsii.get(self, "dbSubnetGroupDescription")

    @db_subnet_group_description.setter # type: ignore
    def db_subnet_group_description(self, value: builtins.str) -> None:
        jsii.set(self, "dbSubnetGroupDescription", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        """``AWS::DocDB::DBSubnetGroup.SubnetIds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-subnetids
        """
        return jsii.get(self, "subnetIds")

    @subnet_ids.setter # type: ignore
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "subnetIds", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBSubnetGroup.DBSubnetGroupName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-dbsubnetgroupname
        """
        return jsii.get(self, "dbSubnetGroupName")

    @db_subnet_group_name.setter # type: ignore
    def db_subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "dbSubnetGroupName", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-docdb.CfnDBSubnetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "db_subnet_group_description": "dbSubnetGroupDescription",
        "subnet_ids": "subnetIds",
        "db_subnet_group_name": "dbSubnetGroupName",
        "tags": "tags",
    },
)
class CfnDBSubnetGroupProps:
    def __init__(
        self,
        *,
        db_subnet_group_description: builtins.str,
        subnet_ids: typing.List[builtins.str],
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::DocDB::DBSubnetGroup``.

        :param db_subnet_group_description: ``AWS::DocDB::DBSubnetGroup.DBSubnetGroupDescription``.
        :param subnet_ids: ``AWS::DocDB::DBSubnetGroup.SubnetIds``.
        :param db_subnet_group_name: ``AWS::DocDB::DBSubnetGroup.DBSubnetGroupName``.
        :param tags: ``AWS::DocDB::DBSubnetGroup.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "db_subnet_group_description": db_subnet_group_description,
            "subnet_ids": subnet_ids,
        }
        if db_subnet_group_name is not None:
            self._values["db_subnet_group_name"] = db_subnet_group_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def db_subnet_group_description(self) -> builtins.str:
        """``AWS::DocDB::DBSubnetGroup.DBSubnetGroupDescription``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-dbsubnetgroupdescription
        """
        result = self._values.get("db_subnet_group_description")
        assert result is not None, "Required property 'db_subnet_group_description' is missing"
        return result

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        """``AWS::DocDB::DBSubnetGroup.SubnetIds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-subnetids
        """
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return result

    @builtins.property
    def db_subnet_group_name(self) -> typing.Optional[builtins.str]:
        """``AWS::DocDB::DBSubnetGroup.DBSubnetGroupName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-dbsubnetgroupname
        """
        result = self._values.get("db_subnet_group_name")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::DocDB::DBSubnetGroup.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDBSubnetGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-docdb.ClusterParameterGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "family": "family",
        "parameters": "parameters",
        "db_cluster_parameter_group_name": "dbClusterParameterGroupName",
        "description": "description",
    },
)
class ClusterParameterGroupProps:
    def __init__(
        self,
        *,
        family: builtins.str,
        parameters: typing.Mapping[builtins.str, builtins.str],
        db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Properties for a cluster parameter group.

        :param family: (experimental) Database family of this parameter group.
        :param parameters: (experimental) The parameters in this parameter group.
        :param db_cluster_parameter_group_name: (experimental) The name of the cluster parameter group. Default: A CDK generated name for the cluster parameter group
        :param description: (experimental) Description for this parameter group. Default: a CDK generated description

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "family": family,
            "parameters": parameters,
        }
        if db_cluster_parameter_group_name is not None:
            self._values["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def family(self) -> builtins.str:
        """(experimental) Database family of this parameter group.

        :stability: experimental
        """
        result = self._values.get("family")
        assert result is not None, "Required property 'family' is missing"
        return result

    @builtins.property
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        """(experimental) The parameters in this parameter group.

        :stability: experimental
        """
        result = self._values.get("parameters")
        assert result is not None, "Required property 'parameters' is missing"
        return result

    @builtins.property
    def db_cluster_parameter_group_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the cluster parameter group.

        :default: A CDK generated name for the cluster parameter group

        :stability: experimental
        """
        result = self._values.get("db_cluster_parameter_group_name")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) Description for this parameter group.

        :default: a CDK generated description

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterParameterGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-docdb.DatabaseClusterAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_endpoint_address": "clusterEndpointAddress",
        "cluster_identifier": "clusterIdentifier",
        "instance_endpoint_addresses": "instanceEndpointAddresses",
        "instance_identifiers": "instanceIdentifiers",
        "port": "port",
        "reader_endpoint_address": "readerEndpointAddress",
        "security_group": "securityGroup",
    },
)
class DatabaseClusterAttributes:
    def __init__(
        self,
        *,
        cluster_endpoint_address: builtins.str,
        cluster_identifier: builtins.str,
        instance_endpoint_addresses: typing.List[builtins.str],
        instance_identifiers: typing.List[builtins.str],
        port: jsii.Number,
        reader_endpoint_address: builtins.str,
        security_group: aws_cdk.aws_ec2.ISecurityGroup,
    ) -> None:
        """(experimental) Properties that describe an existing cluster instance.

        :param cluster_endpoint_address: (experimental) Cluster endpoint address.
        :param cluster_identifier: (experimental) Identifier for the cluster.
        :param instance_endpoint_addresses: (experimental) Endpoint addresses of individual instances.
        :param instance_identifiers: (experimental) Identifier for the instances.
        :param port: (experimental) The database port.
        :param reader_endpoint_address: (experimental) Reader endpoint address.
        :param security_group: (experimental) The security group of the database cluster.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_endpoint_address": cluster_endpoint_address,
            "cluster_identifier": cluster_identifier,
            "instance_endpoint_addresses": instance_endpoint_addresses,
            "instance_identifiers": instance_identifiers,
            "port": port,
            "reader_endpoint_address": reader_endpoint_address,
            "security_group": security_group,
        }

    @builtins.property
    def cluster_endpoint_address(self) -> builtins.str:
        """(experimental) Cluster endpoint address.

        :stability: experimental
        """
        result = self._values.get("cluster_endpoint_address")
        assert result is not None, "Required property 'cluster_endpoint_address' is missing"
        return result

    @builtins.property
    def cluster_identifier(self) -> builtins.str:
        """(experimental) Identifier for the cluster.

        :stability: experimental
        """
        result = self._values.get("cluster_identifier")
        assert result is not None, "Required property 'cluster_identifier' is missing"
        return result

    @builtins.property
    def instance_endpoint_addresses(self) -> typing.List[builtins.str]:
        """(experimental) Endpoint addresses of individual instances.

        :stability: experimental
        """
        result = self._values.get("instance_endpoint_addresses")
        assert result is not None, "Required property 'instance_endpoint_addresses' is missing"
        return result

    @builtins.property
    def instance_identifiers(self) -> typing.List[builtins.str]:
        """(experimental) Identifier for the instances.

        :stability: experimental
        """
        result = self._values.get("instance_identifiers")
        assert result is not None, "Required property 'instance_identifiers' is missing"
        return result

    @builtins.property
    def port(self) -> jsii.Number:
        """(experimental) The database port.

        :stability: experimental
        """
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return result

    @builtins.property
    def reader_endpoint_address(self) -> builtins.str:
        """(experimental) Reader endpoint address.

        :stability: experimental
        """
        result = self._values.get("reader_endpoint_address")
        assert result is not None, "Required property 'reader_endpoint_address' is missing"
        return result

    @builtins.property
    def security_group(self) -> aws_cdk.aws_ec2.ISecurityGroup:
        """(experimental) The security group of the database cluster.

        :stability: experimental
        """
        result = self._values.get("security_group")
        assert result is not None, "Required property 'security_group' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseClusterAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-docdb.DatabaseClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_props": "instanceProps",
        "master_user": "masterUser",
        "backup": "backup",
        "db_cluster_name": "dbClusterName",
        "engine_version": "engineVersion",
        "instance_identifier_base": "instanceIdentifierBase",
        "instances": "instances",
        "kms_key": "kmsKey",
        "parameter_group": "parameterGroup",
        "port": "port",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "removal_policy": "removalPolicy",
        "storage_encrypted": "storageEncrypted",
    },
)
class DatabaseClusterProps:
    def __init__(
        self,
        *,
        instance_props: "InstanceProps",
        master_user: "Login",
        backup: typing.Optional[BackupProps] = None,
        db_cluster_name: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        instance_identifier_base: typing.Optional[builtins.str] = None,
        instances: typing.Optional[jsii.Number] = None,
        kms_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        parameter_group: typing.Optional["IClusterParameterGroup"] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
        storage_encrypted: typing.Optional[builtins.bool] = None,
    ) -> None:
        """(experimental) Properties for a new database cluster.

        :param instance_props: (experimental) Settings for the individual instances that are launched.
        :param master_user: (experimental) Username and password for the administrative user.
        :param backup: (experimental) Backup settings. Default: - Backup retention period for automated backups is 1 day. Backup preferred window is set to a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
        :param db_cluster_name: (experimental) An optional identifier for the cluster. Default: - A name is automatically generated.
        :param engine_version: (experimental) What version of the database to start. Default: - The default engine version.
        :param instance_identifier_base: (experimental) Base identifier for instances. Every replica is named by appending the replica number to this string, 1-based. Default: - ``dbClusterName`` is used with the word "Instance" appended. If ``dbClusterName`` is not provided, the identifier is automatically generated.
        :param instances: (experimental) Number of DocDB compute instances. Default: 1
        :param kms_key: (experimental) The KMS key for storage encryption. Default: - default master key.
        :param parameter_group: (experimental) Additional parameters to pass to the database engine. Default: - No parameter group.
        :param port: (experimental) The port the DocumentDB cluster will listen on. Default: DatabaseCluster.DEFAULT_PORT
        :param preferred_maintenance_window: (experimental) A weekly time range in which maintenance should preferably execute. Must be at least 30 minutes long. Example: 'tue:04:17-tue:04:47' Default: - 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
        :param removal_policy: (experimental) The removal policy to apply when the cluster and its instances are removed or replaced during a stack update, or when the stack is deleted. This removal policy also applies to the implicit security group created for the cluster if one is not supplied as a parameter. Default: - Retain cluster.
        :param storage_encrypted: (experimental) Whether to enable storage encryption. Default: true

        :stability: experimental
        """
        if isinstance(instance_props, dict):
            instance_props = InstanceProps(**instance_props)
        if isinstance(master_user, dict):
            master_user = Login(**master_user)
        if isinstance(backup, dict):
            backup = BackupProps(**backup)
        self._values: typing.Dict[str, typing.Any] = {
            "instance_props": instance_props,
            "master_user": master_user,
        }
        if backup is not None:
            self._values["backup"] = backup
        if db_cluster_name is not None:
            self._values["db_cluster_name"] = db_cluster_name
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if instance_identifier_base is not None:
            self._values["instance_identifier_base"] = instance_identifier_base
        if instances is not None:
            self._values["instances"] = instances
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if parameter_group is not None:
            self._values["parameter_group"] = parameter_group
        if port is not None:
            self._values["port"] = port
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if storage_encrypted is not None:
            self._values["storage_encrypted"] = storage_encrypted

    @builtins.property
    def instance_props(self) -> "InstanceProps":
        """(experimental) Settings for the individual instances that are launched.

        :stability: experimental
        """
        result = self._values.get("instance_props")
        assert result is not None, "Required property 'instance_props' is missing"
        return result

    @builtins.property
    def master_user(self) -> "Login":
        """(experimental) Username and password for the administrative user.

        :stability: experimental
        """
        result = self._values.get("master_user")
        assert result is not None, "Required property 'master_user' is missing"
        return result

    @builtins.property
    def backup(self) -> typing.Optional[BackupProps]:
        """(experimental) Backup settings.

        :default:

        - Backup retention period for automated backups is 1 day.
        Backup preferred window is set to a 30-minute window selected at random from an
        8-hour block of time for each AWS Region, occurring on a random day of the week.

        :see: https://docs.aws.amazon.com/documentdb/latest/developerguide/backup-restore.db-cluster-snapshots.html#backup-restore.backup-window
        :stability: experimental
        """
        result = self._values.get("backup")
        return result

    @builtins.property
    def db_cluster_name(self) -> typing.Optional[builtins.str]:
        """(experimental) An optional identifier for the cluster.

        :default: - A name is automatically generated.

        :stability: experimental
        """
        result = self._values.get("db_cluster_name")
        return result

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        """(experimental) What version of the database to start.

        :default: - The default engine version.

        :stability: experimental
        """
        result = self._values.get("engine_version")
        return result

    @builtins.property
    def instance_identifier_base(self) -> typing.Optional[builtins.str]:
        """(experimental) Base identifier for instances.

        Every replica is named by appending the replica number to this string, 1-based.

        :default:

        - ``dbClusterName`` is used with the word "Instance" appended. If ``dbClusterName`` is not provided, the
        identifier is automatically generated.

        :stability: experimental
        """
        result = self._values.get("instance_identifier_base")
        return result

    @builtins.property
    def instances(self) -> typing.Optional[jsii.Number]:
        """(experimental) Number of DocDB compute instances.

        :default: 1

        :stability: experimental
        """
        result = self._values.get("instances")
        return result

    @builtins.property
    def kms_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        """(experimental) The KMS key for storage encryption.

        :default: - default master key.

        :stability: experimental
        """
        result = self._values.get("kms_key")
        return result

    @builtins.property
    def parameter_group(self) -> typing.Optional["IClusterParameterGroup"]:
        """(experimental) Additional parameters to pass to the database engine.

        :default: - No parameter group.

        :stability: experimental
        """
        result = self._values.get("parameter_group")
        return result

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        """(experimental) The port the DocumentDB cluster will listen on.

        :default: DatabaseCluster.DEFAULT_PORT

        :stability: experimental
        """
        result = self._values.get("port")
        return result

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        """(experimental) A weekly time range in which maintenance should preferably execute.

        Must be at least 30 minutes long.

        Example: 'tue:04:17-tue:04:47'

        :default:

        - 30-minute window selected at random from an 8-hour block of time for
        each AWS Region, occurring on a random day of the week.

        :see: https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-maintain.html#maintenance-window
        :stability: experimental
        """
        result = self._values.get("preferred_maintenance_window")
        return result

    @builtins.property
    def removal_policy(self) -> typing.Optional[aws_cdk.core.RemovalPolicy]:
        """(experimental) The removal policy to apply when the cluster and its instances are removed or replaced during a stack update, or when the stack is deleted.

        This
        removal policy also applies to the implicit security group created for the
        cluster if one is not supplied as a parameter.

        :default: - Retain cluster.

        :stability: experimental
        """
        result = self._values.get("removal_policy")
        return result

    @builtins.property
    def storage_encrypted(self) -> typing.Optional[builtins.bool]:
        """(experimental) Whether to enable storage encryption.

        :default: true

        :stability: experimental
        """
        result = self._values.get("storage_encrypted")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-docdb.DatabaseInstanceAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "instance_endpoint_address": "instanceEndpointAddress",
        "instance_identifier": "instanceIdentifier",
        "port": "port",
    },
)
class DatabaseInstanceAttributes:
    def __init__(
        self,
        *,
        instance_endpoint_address: builtins.str,
        instance_identifier: builtins.str,
        port: jsii.Number,
    ) -> None:
        """(experimental) Properties that describe an existing instance.

        :param instance_endpoint_address: (experimental) The endpoint address.
        :param instance_identifier: (experimental) The instance identifier.
        :param port: (experimental) The database port.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "instance_endpoint_address": instance_endpoint_address,
            "instance_identifier": instance_identifier,
            "port": port,
        }

    @builtins.property
    def instance_endpoint_address(self) -> builtins.str:
        """(experimental) The endpoint address.

        :stability: experimental
        """
        result = self._values.get("instance_endpoint_address")
        assert result is not None, "Required property 'instance_endpoint_address' is missing"
        return result

    @builtins.property
    def instance_identifier(self) -> builtins.str:
        """(experimental) The instance identifier.

        :stability: experimental
        """
        result = self._values.get("instance_identifier")
        assert result is not None, "Required property 'instance_identifier' is missing"
        return result

    @builtins.property
    def port(self) -> jsii.Number:
        """(experimental) The database port.

        :stability: experimental
        """
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseInstanceAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-docdb.DatabaseInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster": "cluster",
        "instance_class": "instanceClass",
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "availability_zone": "availabilityZone",
        "db_instance_name": "dbInstanceName",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "removal_policy": "removalPolicy",
    },
)
class DatabaseInstanceProps:
    def __init__(
        self,
        *,
        cluster: "IDatabaseCluster",
        instance_class: aws_cdk.aws_ec2.InstanceType,
        auto_minor_version_upgrade: typing.Optional[builtins.bool] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        db_instance_name: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
    ) -> None:
        """(experimental) Construction properties for a DatabaseInstanceNew.

        :param cluster: (experimental) The DocumentDB database cluster the instance should launch into.
        :param instance_class: (experimental) The name of the compute and memory capacity classes.
        :param auto_minor_version_upgrade: (experimental) Indicates that minor engine upgrades are applied automatically to the DB instance during the maintenance window. Default: true
        :param availability_zone: (experimental) The name of the Availability Zone where the DB instance will be located. Default: - no preference
        :param db_instance_name: (experimental) A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. Default: - a CloudFormation generated name
        :param preferred_maintenance_window: (experimental) The weekly time range (in UTC) during which system maintenance can occur. Format: ``ddd:hh24:mi-ddd:hh24:mi`` Constraint: Minimum 30-minute window Default: - a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-maintain.html#maintenance-window
        :param removal_policy: (experimental) The CloudFormation policy to apply when the instance is removed from the stack or replaced during an update. Default: RemovalPolicy.Retain

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "cluster": cluster,
            "instance_class": instance_class,
        }
        if auto_minor_version_upgrade is not None:
            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if db_instance_name is not None:
            self._values["db_instance_name"] = db_instance_name
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy

    @builtins.property
    def cluster(self) -> "IDatabaseCluster":
        """(experimental) The DocumentDB database cluster the instance should launch into.

        :stability: experimental
        """
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return result

    @builtins.property
    def instance_class(self) -> aws_cdk.aws_ec2.InstanceType:
        """(experimental) The name of the compute and memory capacity classes.

        :stability: experimental
        """
        result = self._values.get("instance_class")
        assert result is not None, "Required property 'instance_class' is missing"
        return result

    @builtins.property
    def auto_minor_version_upgrade(self) -> typing.Optional[builtins.bool]:
        """(experimental) Indicates that minor engine upgrades are applied automatically to the DB instance during the maintenance window.

        :default: true

        :stability: experimental
        """
        result = self._values.get("auto_minor_version_upgrade")
        return result

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the Availability Zone where the DB instance will be located.

        :default: - no preference

        :stability: experimental
        """
        result = self._values.get("availability_zone")
        return result

    @builtins.property
    def db_instance_name(self) -> typing.Optional[builtins.str]:
        """(experimental) A name for the DB instance.

        If you specify a name, AWS CloudFormation
        converts it to lowercase.

        :default: - a CloudFormation generated name

        :stability: experimental
        """
        result = self._values.get("db_instance_name")
        return result

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        """(experimental) The weekly time range (in UTC) during which system maintenance can occur.

        Format: ``ddd:hh24:mi-ddd:hh24:mi``
        Constraint: Minimum 30-minute window

        :default:

        - a 30-minute window selected at random from an 8-hour block of
        time for each AWS Region, occurring on a random day of the week. To see
        the time blocks available, see https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-maintain.html#maintenance-window

        :stability: experimental
        """
        result = self._values.get("preferred_maintenance_window")
        return result

    @builtins.property
    def removal_policy(self) -> typing.Optional[aws_cdk.core.RemovalPolicy]:
        """(experimental) The CloudFormation policy to apply when the instance is removed from the stack or replaced during an update.

        :default: RemovalPolicy.Retain

        :stability: experimental
        """
        result = self._values.get("removal_policy")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecret(
    aws_cdk.aws_secretsmanager.Secret,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-docdb.DatabaseSecret",
):
    """(experimental) A database secret.

    :stability: experimental
    :resource: AWS::SecretsManager::Secret
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        username: builtins.str,
        encryption_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        master_secret: typing.Optional[aws_cdk.aws_secretsmanager.ISecret] = None,
        secret_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param username: (experimental) The username.
        :param encryption_key: (experimental) The KMS key to use to encrypt the secret. Default: default master key
        :param master_secret: (experimental) The master secret which will be used to rotate this secret. Default: - no master secret information will be included
        :param secret_name: (experimental) The physical name of the secret. Default: Secretsmanager will generate a physical name for the secret

        :stability: experimental
        """
        props = DatabaseSecretProps(
            username=username,
            encryption_key=encryption_key,
            master_secret=master_secret,
            secret_name=secret_name,
        )

        jsii.create(DatabaseSecret, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@aws-cdk/aws-docdb.DatabaseSecretProps",
    jsii_struct_bases=[],
    name_mapping={
        "username": "username",
        "encryption_key": "encryptionKey",
        "master_secret": "masterSecret",
        "secret_name": "secretName",
    },
)
class DatabaseSecretProps:
    def __init__(
        self,
        *,
        username: builtins.str,
        encryption_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        master_secret: typing.Optional[aws_cdk.aws_secretsmanager.ISecret] = None,
        secret_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Construction properties for a DatabaseSecret.

        :param username: (experimental) The username.
        :param encryption_key: (experimental) The KMS key to use to encrypt the secret. Default: default master key
        :param master_secret: (experimental) The master secret which will be used to rotate this secret. Default: - no master secret information will be included
        :param secret_name: (experimental) The physical name of the secret. Default: Secretsmanager will generate a physical name for the secret

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "username": username,
        }
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if master_secret is not None:
            self._values["master_secret"] = master_secret
        if secret_name is not None:
            self._values["secret_name"] = secret_name

    @builtins.property
    def username(self) -> builtins.str:
        """(experimental) The username.

        :stability: experimental
        """
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return result

    @builtins.property
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        """(experimental) The KMS key to use to encrypt the secret.

        :default: default master key

        :stability: experimental
        """
        result = self._values.get("encryption_key")
        return result

    @builtins.property
    def master_secret(self) -> typing.Optional[aws_cdk.aws_secretsmanager.ISecret]:
        """(experimental) The master secret which will be used to rotate this secret.

        :default: - no master secret information will be included

        :stability: experimental
        """
        result = self._values.get("master_secret")
        return result

    @builtins.property
    def secret_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The physical name of the secret.

        :default: Secretsmanager will generate a physical name for the secret

        :stability: experimental
        """
        result = self._values.get("secret_name")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Endpoint(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-docdb.Endpoint"):
    """(experimental) Connection endpoint of a database cluster or instance.

    Consists of a combination of hostname and port.

    :stability: experimental
    """

    def __init__(self, address: builtins.str, port: jsii.Number) -> None:
        """(experimental) Constructs an Endpoint instance.

        :param address: - The hostname or address of the endpoint.
        :param port: - The port number of the endpoint.

        :stability: experimental
        """
        jsii.create(Endpoint, self, [address, port])

    @jsii.member(jsii_name="portAsString")
    def port_as_string(self) -> builtins.str:
        """(experimental) Returns the port number as a string representation that can be used for embedding within other strings.

        This is intended to deal with CDK's token system. Numeric CDK tokens are not expanded when their string
        representation is embedded in a string. This function returns the port either as an unresolved string token or
        as a resolved string representation of the port value.

        :return: An (un)resolved string representation of the endpoint's port number

        :stability: experimental
        """
        return jsii.invoke(self, "portAsString", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        """(experimental) The hostname of the endpoint.

        :stability: experimental
        """
        return jsii.get(self, "hostname")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        """(experimental) The port number of the endpoint.

        This can potentially be a CDK token. If you need to embed the port in a string (e.g. instance user data script),
        use {@link Endpoint.portAsString}.

        :stability: experimental
        """
        return jsii.get(self, "port")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="socketAddress")
    def socket_address(self) -> builtins.str:
        """(experimental) The combination of "HOSTNAME:PORT" for this endpoint.

        :stability: experimental
        """
        return jsii.get(self, "socketAddress")


@jsii.interface(jsii_type="@aws-cdk/aws-docdb.IClusterParameterGroup")
class IClusterParameterGroup(aws_cdk.core.IResource, typing_extensions.Protocol):
    """(experimental) A parameter group.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IClusterParameterGroupProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> builtins.str:
        """(experimental) The name of this parameter group.

        :stability: experimental
        """
        ...


class _IClusterParameterGroupProxy(
    jsii.proxy_for(aws_cdk.core.IResource) # type: ignore
):
    """(experimental) A parameter group.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-docdb.IClusterParameterGroup"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> builtins.str:
        """(experimental) The name of this parameter group.

        :stability: experimental
        """
        return jsii.get(self, "parameterGroupName")


@jsii.interface(jsii_type="@aws-cdk/aws-docdb.IDatabaseCluster")
class IDatabaseCluster(
    aws_cdk.core.IResource,
    aws_cdk.aws_ec2.IConnectable,
    aws_cdk.aws_secretsmanager.ISecretAttachmentTarget,
    typing_extensions.Protocol,
):
    """(experimental) Create a clustered database with a given number of instances.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IDatabaseClusterProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> Endpoint:
        """(experimental) The endpoint to use for read/write operations.

        :stability: experimental
        :attribute: Endpoint,Port
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        """(experimental) Identifier of the cluster.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="clusterReadEndpoint")
    def cluster_read_endpoint(self) -> Endpoint:
        """(experimental) Endpoint to use for load-balanced read-only operations.

        :stability: experimental
        :attribute: ReadEndpoint
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="instanceEndpoints")
    def instance_endpoints(self) -> typing.List[Endpoint]:
        """(experimental) Endpoints which address each individual replica.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="instanceIdentifiers")
    def instance_identifiers(self) -> typing.List[builtins.str]:
        """(experimental) Identifiers of the replicas.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="securityGroupId")
    def security_group_id(self) -> builtins.str:
        """(experimental) The security group for this database cluster.

        :stability: experimental
        """
        ...


class _IDatabaseClusterProxy(
    jsii.proxy_for(aws_cdk.core.IResource), # type: ignore
    jsii.proxy_for(aws_cdk.aws_ec2.IConnectable), # type: ignore
    jsii.proxy_for(aws_cdk.aws_secretsmanager.ISecretAttachmentTarget), # type: ignore
):
    """(experimental) Create a clustered database with a given number of instances.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-docdb.IDatabaseCluster"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> Endpoint:
        """(experimental) The endpoint to use for read/write operations.

        :stability: experimental
        :attribute: Endpoint,Port
        """
        return jsii.get(self, "clusterEndpoint")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        """(experimental) Identifier of the cluster.

        :stability: experimental
        """
        return jsii.get(self, "clusterIdentifier")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="clusterReadEndpoint")
    def cluster_read_endpoint(self) -> Endpoint:
        """(experimental) Endpoint to use for load-balanced read-only operations.

        :stability: experimental
        :attribute: ReadEndpoint
        """
        return jsii.get(self, "clusterReadEndpoint")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="instanceEndpoints")
    def instance_endpoints(self) -> typing.List[Endpoint]:
        """(experimental) Endpoints which address each individual replica.

        :stability: experimental
        """
        return jsii.get(self, "instanceEndpoints")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="instanceIdentifiers")
    def instance_identifiers(self) -> typing.List[builtins.str]:
        """(experimental) Identifiers of the replicas.

        :stability: experimental
        """
        return jsii.get(self, "instanceIdentifiers")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="securityGroupId")
    def security_group_id(self) -> builtins.str:
        """(experimental) The security group for this database cluster.

        :stability: experimental
        """
        return jsii.get(self, "securityGroupId")


@jsii.interface(jsii_type="@aws-cdk/aws-docdb.IDatabaseInstance")
class IDatabaseInstance(aws_cdk.core.IResource, typing_extensions.Protocol):
    """(experimental) A database instance.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IDatabaseInstanceProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dbInstanceEndpointAddress")
    def db_instance_endpoint_address(self) -> builtins.str:
        """(experimental) The instance endpoint address.

        :stability: experimental
        :attribute: Endpoint
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dbInstanceEndpointPort")
    def db_instance_endpoint_port(self) -> builtins.str:
        """(experimental) The instance endpoint port.

        :stability: experimental
        :attribute: Port
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        """(experimental) The instance arn.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="instanceEndpoint")
    def instance_endpoint(self) -> Endpoint:
        """(experimental) The instance endpoint.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="instanceIdentifier")
    def instance_identifier(self) -> builtins.str:
        """(experimental) The instance identifier.

        :stability: experimental
        """
        ...


class _IDatabaseInstanceProxy(
    jsii.proxy_for(aws_cdk.core.IResource) # type: ignore
):
    """(experimental) A database instance.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-docdb.IDatabaseInstance"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dbInstanceEndpointAddress")
    def db_instance_endpoint_address(self) -> builtins.str:
        """(experimental) The instance endpoint address.

        :stability: experimental
        :attribute: Endpoint
        """
        return jsii.get(self, "dbInstanceEndpointAddress")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dbInstanceEndpointPort")
    def db_instance_endpoint_port(self) -> builtins.str:
        """(experimental) The instance endpoint port.

        :stability: experimental
        :attribute: Port
        """
        return jsii.get(self, "dbInstanceEndpointPort")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        """(experimental) The instance arn.

        :stability: experimental
        """
        return jsii.get(self, "instanceArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="instanceEndpoint")
    def instance_endpoint(self) -> Endpoint:
        """(experimental) The instance endpoint.

        :stability: experimental
        """
        return jsii.get(self, "instanceEndpoint")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="instanceIdentifier")
    def instance_identifier(self) -> builtins.str:
        """(experimental) The instance identifier.

        :stability: experimental
        """
        return jsii.get(self, "instanceIdentifier")


@jsii.data_type(
    jsii_type="@aws-cdk/aws-docdb.InstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "vpc": "vpc",
        "parameter_group": "parameterGroup",
        "security_group": "securityGroup",
        "vpc_subnets": "vpcSubnets",
    },
)
class InstanceProps:
    def __init__(
        self,
        *,
        instance_type: aws_cdk.aws_ec2.InstanceType,
        vpc: aws_cdk.aws_ec2.IVpc,
        parameter_group: typing.Optional[IClusterParameterGroup] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        vpc_subnets: typing.Optional[aws_cdk.aws_ec2.SubnetSelection] = None,
    ) -> None:
        """(experimental) Instance properties for database instances.

        :param instance_type: (experimental) What type of instance to start for the replicas.
        :param vpc: (experimental) What subnets to run the DocumentDB instances in. Must be at least 2 subnets in two different AZs.
        :param parameter_group: (experimental) The DB parameter group to associate with the instance. Default: no parameter group
        :param security_group: (experimental) Security group. Default: a new security group is created.
        :param vpc_subnets: (experimental) Where to place the instances within the VPC. Default: private subnets

        :stability: experimental
        """
        if isinstance(vpc_subnets, dict):
            vpc_subnets = aws_cdk.aws_ec2.SubnetSelection(**vpc_subnets)
        self._values: typing.Dict[str, typing.Any] = {
            "instance_type": instance_type,
            "vpc": vpc,
        }
        if parameter_group is not None:
            self._values["parameter_group"] = parameter_group
        if security_group is not None:
            self._values["security_group"] = security_group
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def instance_type(self) -> aws_cdk.aws_ec2.InstanceType:
        """(experimental) What type of instance to start for the replicas.

        :stability: experimental
        """
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return result

    @builtins.property
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        """(experimental) What subnets to run the DocumentDB instances in.

        Must be at least 2 subnets in two different AZs.

        :stability: experimental
        """
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return result

    @builtins.property
    def parameter_group(self) -> typing.Optional[IClusterParameterGroup]:
        """(experimental) The DB parameter group to associate with the instance.

        :default: no parameter group

        :stability: experimental
        """
        result = self._values.get("parameter_group")
        return result

    @builtins.property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        """(experimental) Security group.

        :default: a new security group is created.

        :stability: experimental
        """
        result = self._values.get("security_group")
        return result

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        """(experimental) Where to place the instances within the VPC.

        :default: private subnets

        :stability: experimental
        """
        result = self._values.get("vpc_subnets")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-docdb.Login",
    jsii_struct_bases=[],
    name_mapping={"username": "username", "kms_key": "kmsKey", "password": "password"},
)
class Login:
    def __init__(
        self,
        *,
        username: builtins.str,
        kms_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        password: typing.Optional[aws_cdk.core.SecretValue] = None,
    ) -> None:
        """(experimental) Login credentials for a database cluster.

        :param username: (experimental) Username.
        :param kms_key: (experimental) KMS encryption key to encrypt the generated secret. Default: default master key
        :param password: (experimental) Password. Do not put passwords in your CDK code directly. Default: a Secrets Manager generated password

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "username": username,
        }
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if password is not None:
            self._values["password"] = password

    @builtins.property
    def username(self) -> builtins.str:
        """(experimental) Username.

        :stability: experimental
        """
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return result

    @builtins.property
    def kms_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        """(experimental) KMS encryption key to encrypt the generated secret.

        :default: default master key

        :stability: experimental
        """
        result = self._values.get("kms_key")
        return result

    @builtins.property
    def password(self) -> typing.Optional[aws_cdk.core.SecretValue]:
        """(experimental) Password.

        Do not put passwords in your CDK code directly.

        :default: a Secrets Manager generated password

        :stability: experimental
        """
        result = self._values.get("password")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Login(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-docdb.RotationMultiUserOptions",
    jsii_struct_bases=[],
    name_mapping={"secret": "secret", "automatically_after": "automaticallyAfter"},
)
class RotationMultiUserOptions:
    def __init__(
        self,
        *,
        secret: aws_cdk.aws_secretsmanager.ISecret,
        automatically_after: typing.Optional[aws_cdk.core.Duration] = None,
    ) -> None:
        """(experimental) Options to add the multi user rotation.

        :param secret: (experimental) The secret to rotate. It must be a JSON string with the following format:: { "engine": <required: must be set to 'mongo'>, "host": <required: instance host name>, "username": <required: username>, "password": <required: password>, "dbname": <optional: database name>, "port": <optional: if not specified, default port 27017 will be used>, "masterarn": <required: the arn of the master secret which will be used to create users/change passwords> "ssl": <optional: if not specified, defaults to false. This must be true if being used for DocumentDB rotations where the cluster has TLS enabled> }
        :param automatically_after: (experimental) Specifies the number of days after the previous rotation before Secrets Manager triggers the next automatic rotation. Default: Duration.days(30)

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "secret": secret,
        }
        if automatically_after is not None:
            self._values["automatically_after"] = automatically_after

    @builtins.property
    def secret(self) -> aws_cdk.aws_secretsmanager.ISecret:
        """(experimental) The secret to rotate.

        It must be a JSON string with the following format::

           {
              "engine": <required: must be set to 'mongo'>,
              "host": <required: instance host name>,
              "username": <required: username>,
              "password": <required: password>,
              "dbname": <optional: database name>,
              "port": <optional: if not specified, default port 27017 will be used>,
              "masterarn": <required: the arn of the master secret which will be used to create users/change passwords>
              "ssl": <optional: if not specified, defaults to false. This must be true if being used for DocumentDB rotations
                     where the cluster has TLS enabled>
           }

        :stability: experimental
        """
        result = self._values.get("secret")
        assert result is not None, "Required property 'secret' is missing"
        return result

    @builtins.property
    def automatically_after(self) -> typing.Optional[aws_cdk.core.Duration]:
        """(experimental) Specifies the number of days after the previous rotation before Secrets Manager triggers the next automatic rotation.

        :default: Duration.days(30)

        :stability: experimental
        """
        result = self._values.get("automatically_after")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RotationMultiUserOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IClusterParameterGroup)
class ClusterParameterGroup(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-docdb.ClusterParameterGroup",
):
    """(experimental) A cluster parameter group.

    :stability: experimental
    :resource: AWS::DocDB::DBClusterParameterGroup
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        family: builtins.str,
        parameters: typing.Mapping[builtins.str, builtins.str],
        db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param family: (experimental) Database family of this parameter group.
        :param parameters: (experimental) The parameters in this parameter group.
        :param db_cluster_parameter_group_name: (experimental) The name of the cluster parameter group. Default: A CDK generated name for the cluster parameter group
        :param description: (experimental) Description for this parameter group. Default: a CDK generated description

        :stability: experimental
        """
        props = ClusterParameterGroupProps(
            family=family,
            parameters=parameters,
            db_cluster_parameter_group_name=db_cluster_parameter_group_name,
            description=description,
        )

        jsii.create(ClusterParameterGroup, self, [scope, id, props])

    @jsii.member(jsii_name="fromParameterGroupName")
    @builtins.classmethod
    def from_parameter_group_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        parameter_group_name: builtins.str,
    ) -> IClusterParameterGroup:
        """(experimental) Imports a parameter group.

        :param scope: -
        :param id: -
        :param parameter_group_name: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromParameterGroupName", [scope, id, parameter_group_name])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> builtins.str:
        """(experimental) The name of the parameter group.

        :stability: experimental
        """
        return jsii.get(self, "parameterGroupName")


@jsii.implements(IDatabaseCluster)
class DatabaseCluster(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-docdb.DatabaseCluster",
):
    """(experimental) Create a clustered database with a given number of instances.

    :stability: experimental
    :resource: AWS::DocDB::DBCluster
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        instance_props: InstanceProps,
        master_user: Login,
        backup: typing.Optional[BackupProps] = None,
        db_cluster_name: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        instance_identifier_base: typing.Optional[builtins.str] = None,
        instances: typing.Optional[jsii.Number] = None,
        kms_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        parameter_group: typing.Optional[IClusterParameterGroup] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
        storage_encrypted: typing.Optional[builtins.bool] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param instance_props: (experimental) Settings for the individual instances that are launched.
        :param master_user: (experimental) Username and password for the administrative user.
        :param backup: (experimental) Backup settings. Default: - Backup retention period for automated backups is 1 day. Backup preferred window is set to a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
        :param db_cluster_name: (experimental) An optional identifier for the cluster. Default: - A name is automatically generated.
        :param engine_version: (experimental) What version of the database to start. Default: - The default engine version.
        :param instance_identifier_base: (experimental) Base identifier for instances. Every replica is named by appending the replica number to this string, 1-based. Default: - ``dbClusterName`` is used with the word "Instance" appended. If ``dbClusterName`` is not provided, the identifier is automatically generated.
        :param instances: (experimental) Number of DocDB compute instances. Default: 1
        :param kms_key: (experimental) The KMS key for storage encryption. Default: - default master key.
        :param parameter_group: (experimental) Additional parameters to pass to the database engine. Default: - No parameter group.
        :param port: (experimental) The port the DocumentDB cluster will listen on. Default: DatabaseCluster.DEFAULT_PORT
        :param preferred_maintenance_window: (experimental) A weekly time range in which maintenance should preferably execute. Must be at least 30 minutes long. Example: 'tue:04:17-tue:04:47' Default: - 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
        :param removal_policy: (experimental) The removal policy to apply when the cluster and its instances are removed or replaced during a stack update, or when the stack is deleted. This removal policy also applies to the implicit security group created for the cluster if one is not supplied as a parameter. Default: - Retain cluster.
        :param storage_encrypted: (experimental) Whether to enable storage encryption. Default: true

        :stability: experimental
        """
        props = DatabaseClusterProps(
            instance_props=instance_props,
            master_user=master_user,
            backup=backup,
            db_cluster_name=db_cluster_name,
            engine_version=engine_version,
            instance_identifier_base=instance_identifier_base,
            instances=instances,
            kms_key=kms_key,
            parameter_group=parameter_group,
            port=port,
            preferred_maintenance_window=preferred_maintenance_window,
            removal_policy=removal_policy,
            storage_encrypted=storage_encrypted,
        )

        jsii.create(DatabaseCluster, self, [scope, id, props])

    @jsii.member(jsii_name="fromDatabaseClusterAttributes")
    @builtins.classmethod
    def from_database_cluster_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        cluster_endpoint_address: builtins.str,
        cluster_identifier: builtins.str,
        instance_endpoint_addresses: typing.List[builtins.str],
        instance_identifiers: typing.List[builtins.str],
        port: jsii.Number,
        reader_endpoint_address: builtins.str,
        security_group: aws_cdk.aws_ec2.ISecurityGroup,
    ) -> IDatabaseCluster:
        """(experimental) Import an existing DatabaseCluster from properties.

        :param scope: -
        :param id: -
        :param cluster_endpoint_address: (experimental) Cluster endpoint address.
        :param cluster_identifier: (experimental) Identifier for the cluster.
        :param instance_endpoint_addresses: (experimental) Endpoint addresses of individual instances.
        :param instance_identifiers: (experimental) Identifier for the instances.
        :param port: (experimental) The database port.
        :param reader_endpoint_address: (experimental) Reader endpoint address.
        :param security_group: (experimental) The security group of the database cluster.

        :stability: experimental
        """
        attrs = DatabaseClusterAttributes(
            cluster_endpoint_address=cluster_endpoint_address,
            cluster_identifier=cluster_identifier,
            instance_endpoint_addresses=instance_endpoint_addresses,
            instance_identifiers=instance_identifiers,
            port=port,
            reader_endpoint_address=reader_endpoint_address,
            security_group=security_group,
        )

        return jsii.sinvoke(cls, "fromDatabaseClusterAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="addRotationMultiUser")
    def add_rotation_multi_user(
        self,
        id: builtins.str,
        *,
        secret: aws_cdk.aws_secretsmanager.ISecret,
        automatically_after: typing.Optional[aws_cdk.core.Duration] = None,
    ) -> aws_cdk.aws_secretsmanager.SecretRotation:
        """(experimental) Adds the multi user rotation to this cluster.

        :param id: -
        :param secret: (experimental) The secret to rotate. It must be a JSON string with the following format:: { "engine": <required: must be set to 'mongo'>, "host": <required: instance host name>, "username": <required: username>, "password": <required: password>, "dbname": <optional: database name>, "port": <optional: if not specified, default port 27017 will be used>, "masterarn": <required: the arn of the master secret which will be used to create users/change passwords> "ssl": <optional: if not specified, defaults to false. This must be true if being used for DocumentDB rotations where the cluster has TLS enabled> }
        :param automatically_after: (experimental) Specifies the number of days after the previous rotation before Secrets Manager triggers the next automatic rotation. Default: Duration.days(30)

        :stability: experimental
        """
        options = RotationMultiUserOptions(
            secret=secret, automatically_after=automatically_after
        )

        return jsii.invoke(self, "addRotationMultiUser", [id, options])

    @jsii.member(jsii_name="addRotationSingleUser")
    def add_rotation_single_user(
        self,
        automatically_after: typing.Optional[aws_cdk.core.Duration] = None,
    ) -> aws_cdk.aws_secretsmanager.SecretRotation:
        """(experimental) Adds the single user rotation of the master password to this cluster.

        :param automatically_after: Specifies the number of days after the previous rotation before Secrets Manager triggers the next automatic rotation.

        :stability: experimental
        """
        return jsii.invoke(self, "addRotationSingleUser", [automatically_after])

    @jsii.member(jsii_name="asSecretAttachmentTarget")
    def as_secret_attachment_target(
        self,
    ) -> aws_cdk.aws_secretsmanager.SecretAttachmentTargetProps:
        """(experimental) Renders the secret attachment target specifications.

        :stability: experimental
        """
        return jsii.invoke(self, "asSecretAttachmentTarget", [])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="DEFAULT_NUM_INSTANCES")
    def DEFAULT_NUM_INSTANCES(cls) -> jsii.Number:
        """(experimental) The default number of instances in the DocDB cluster if none are specified.

        :stability: experimental
        """
        return jsii.sget(cls, "DEFAULT_NUM_INSTANCES")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="DEFAULT_PORT")
    def DEFAULT_PORT(cls) -> jsii.Number:
        """(experimental) The default port Document DB listens on.

        :stability: experimental
        """
        return jsii.sget(cls, "DEFAULT_PORT")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> Endpoint:
        """(experimental) The endpoint to use for read/write operations.

        :stability: experimental
        """
        return jsii.get(self, "clusterEndpoint")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        """(experimental) Identifier of the cluster.

        :stability: experimental
        """
        return jsii.get(self, "clusterIdentifier")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="clusterReadEndpoint")
    def cluster_read_endpoint(self) -> Endpoint:
        """(experimental) Endpoint to use for load-balanced read-only operations.

        :stability: experimental
        """
        return jsii.get(self, "clusterReadEndpoint")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="clusterResourceIdentifier")
    def cluster_resource_identifier(self) -> builtins.str:
        """(experimental) The resource id for the cluster;

        for example: cluster-ABCD1234EFGH5678IJKL90MNOP. The cluster ID uniquely
        identifies the cluster and is used in things like IAM authentication policies.

        :stability: experimental
        :attribute: ClusterResourceId
        """
        return jsii.get(self, "clusterResourceIdentifier")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        """(experimental) The connections object to implement IConectable.

        :stability: experimental
        """
        return jsii.get(self, "connections")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="instanceEndpoints")
    def instance_endpoints(self) -> typing.List[Endpoint]:
        """(experimental) Endpoints which address each individual replica.

        :stability: experimental
        """
        return jsii.get(self, "instanceEndpoints")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="instanceIdentifiers")
    def instance_identifiers(self) -> typing.List[builtins.str]:
        """(experimental) Identifiers of the replicas.

        :stability: experimental
        """
        return jsii.get(self, "instanceIdentifiers")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="securityGroupId")
    def security_group_id(self) -> builtins.str:
        """(experimental) Security group identifier of this database.

        :stability: experimental
        """
        return jsii.get(self, "securityGroupId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="secret")
    def secret(self) -> typing.Optional[aws_cdk.aws_secretsmanager.ISecret]:
        """(experimental) The secret attached to this cluster.

        :stability: experimental
        """
        return jsii.get(self, "secret")


@jsii.implements(IDatabaseInstance)
class DatabaseInstance(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-docdb.DatabaseInstance",
):
    """(experimental) A database instance.

    :stability: experimental
    :resource: AWS::DocDB::DBInstance
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        cluster: IDatabaseCluster,
        instance_class: aws_cdk.aws_ec2.InstanceType,
        auto_minor_version_upgrade: typing.Optional[builtins.bool] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        db_instance_name: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param cluster: (experimental) The DocumentDB database cluster the instance should launch into.
        :param instance_class: (experimental) The name of the compute and memory capacity classes.
        :param auto_minor_version_upgrade: (experimental) Indicates that minor engine upgrades are applied automatically to the DB instance during the maintenance window. Default: true
        :param availability_zone: (experimental) The name of the Availability Zone where the DB instance will be located. Default: - no preference
        :param db_instance_name: (experimental) A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. Default: - a CloudFormation generated name
        :param preferred_maintenance_window: (experimental) The weekly time range (in UTC) during which system maintenance can occur. Format: ``ddd:hh24:mi-ddd:hh24:mi`` Constraint: Minimum 30-minute window Default: - a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-maintain.html#maintenance-window
        :param removal_policy: (experimental) The CloudFormation policy to apply when the instance is removed from the stack or replaced during an update. Default: RemovalPolicy.Retain

        :stability: experimental
        """
        props = DatabaseInstanceProps(
            cluster=cluster,
            instance_class=instance_class,
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            availability_zone=availability_zone,
            db_instance_name=db_instance_name,
            preferred_maintenance_window=preferred_maintenance_window,
            removal_policy=removal_policy,
        )

        jsii.create(DatabaseInstance, self, [scope, id, props])

    @jsii.member(jsii_name="fromDatabaseInstanceAttributes")
    @builtins.classmethod
    def from_database_instance_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        instance_endpoint_address: builtins.str,
        instance_identifier: builtins.str,
        port: jsii.Number,
    ) -> IDatabaseInstance:
        """(experimental) Import an existing database instance.

        :param scope: -
        :param id: -
        :param instance_endpoint_address: (experimental) The endpoint address.
        :param instance_identifier: (experimental) The instance identifier.
        :param port: (experimental) The database port.

        :stability: experimental
        """
        attrs = DatabaseInstanceAttributes(
            instance_endpoint_address=instance_endpoint_address,
            instance_identifier=instance_identifier,
            port=port,
        )

        return jsii.sinvoke(cls, "fromDatabaseInstanceAttributes", [scope, id, attrs])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> IDatabaseCluster:
        """(experimental) The instance's database cluster.

        :stability: experimental
        """
        return jsii.get(self, "cluster")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dbInstanceEndpointAddress")
    def db_instance_endpoint_address(self) -> builtins.str:
        """(experimental) The instance endpoint address.

        :stability: experimental
        :inheritdoc: true
        """
        return jsii.get(self, "dbInstanceEndpointAddress")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dbInstanceEndpointPort")
    def db_instance_endpoint_port(self) -> builtins.str:
        """(experimental) The instance endpoint port.

        :stability: experimental
        :inheritdoc: true
        """
        return jsii.get(self, "dbInstanceEndpointPort")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        """(experimental) The instance arn.

        :stability: experimental
        """
        return jsii.get(self, "instanceArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="instanceEndpoint")
    def instance_endpoint(self) -> Endpoint:
        """(experimental) The instance endpoint.

        :stability: experimental
        :inheritdoc: true
        """
        return jsii.get(self, "instanceEndpoint")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="instanceIdentifier")
    def instance_identifier(self) -> builtins.str:
        """(experimental) The instance identifier.

        :stability: experimental
        :inheritdoc: true
        """
        return jsii.get(self, "instanceIdentifier")


__all__ = [
    "BackupProps",
    "CfnDBCluster",
    "CfnDBClusterParameterGroup",
    "CfnDBClusterParameterGroupProps",
    "CfnDBClusterProps",
    "CfnDBInstance",
    "CfnDBInstanceProps",
    "CfnDBSubnetGroup",
    "CfnDBSubnetGroupProps",
    "ClusterParameterGroup",
    "ClusterParameterGroupProps",
    "DatabaseCluster",
    "DatabaseClusterAttributes",
    "DatabaseClusterProps",
    "DatabaseInstance",
    "DatabaseInstanceAttributes",
    "DatabaseInstanceProps",
    "DatabaseSecret",
    "DatabaseSecretProps",
    "Endpoint",
    "IClusterParameterGroup",
    "IDatabaseCluster",
    "IDatabaseInstance",
    "InstanceProps",
    "Login",
    "RotationMultiUserOptions",
]

publication.publish()
