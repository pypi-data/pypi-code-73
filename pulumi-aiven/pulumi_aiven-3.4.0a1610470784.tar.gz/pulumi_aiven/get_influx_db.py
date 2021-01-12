# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = [
    'GetInfluxDbResult',
    'AwaitableGetInfluxDbResult',
    'get_influx_db',
]

@pulumi.output_type
class GetInfluxDbResult:
    """
    A collection of values returned by getInfluxDb.
    """
    def __init__(__self__, cloud_name=None, components=None, id=None, influxdb=None, influxdb_user_config=None, maintenance_window_dow=None, maintenance_window_time=None, plan=None, project=None, project_vpc_id=None, service_host=None, service_integrations=None, service_name=None, service_password=None, service_port=None, service_type=None, service_uri=None, service_username=None, state=None, termination_protection=None):
        if cloud_name and not isinstance(cloud_name, str):
            raise TypeError("Expected argument 'cloud_name' to be a str")
        pulumi.set(__self__, "cloud_name", cloud_name)
        if components and not isinstance(components, list):
            raise TypeError("Expected argument 'components' to be a list")
        pulumi.set(__self__, "components", components)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if influxdb and not isinstance(influxdb, dict):
            raise TypeError("Expected argument 'influxdb' to be a dict")
        pulumi.set(__self__, "influxdb", influxdb)
        if influxdb_user_config and not isinstance(influxdb_user_config, dict):
            raise TypeError("Expected argument 'influxdb_user_config' to be a dict")
        pulumi.set(__self__, "influxdb_user_config", influxdb_user_config)
        if maintenance_window_dow and not isinstance(maintenance_window_dow, str):
            raise TypeError("Expected argument 'maintenance_window_dow' to be a str")
        pulumi.set(__self__, "maintenance_window_dow", maintenance_window_dow)
        if maintenance_window_time and not isinstance(maintenance_window_time, str):
            raise TypeError("Expected argument 'maintenance_window_time' to be a str")
        pulumi.set(__self__, "maintenance_window_time", maintenance_window_time)
        if plan and not isinstance(plan, str):
            raise TypeError("Expected argument 'plan' to be a str")
        pulumi.set(__self__, "plan", plan)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if project_vpc_id and not isinstance(project_vpc_id, str):
            raise TypeError("Expected argument 'project_vpc_id' to be a str")
        pulumi.set(__self__, "project_vpc_id", project_vpc_id)
        if service_host and not isinstance(service_host, str):
            raise TypeError("Expected argument 'service_host' to be a str")
        pulumi.set(__self__, "service_host", service_host)
        if service_integrations and not isinstance(service_integrations, list):
            raise TypeError("Expected argument 'service_integrations' to be a list")
        pulumi.set(__self__, "service_integrations", service_integrations)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)
        if service_password and not isinstance(service_password, str):
            raise TypeError("Expected argument 'service_password' to be a str")
        pulumi.set(__self__, "service_password", service_password)
        if service_port and not isinstance(service_port, int):
            raise TypeError("Expected argument 'service_port' to be a int")
        pulumi.set(__self__, "service_port", service_port)
        if service_type and not isinstance(service_type, str):
            raise TypeError("Expected argument 'service_type' to be a str")
        pulumi.set(__self__, "service_type", service_type)
        if service_uri and not isinstance(service_uri, str):
            raise TypeError("Expected argument 'service_uri' to be a str")
        pulumi.set(__self__, "service_uri", service_uri)
        if service_username and not isinstance(service_username, str):
            raise TypeError("Expected argument 'service_username' to be a str")
        pulumi.set(__self__, "service_username", service_username)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if termination_protection and not isinstance(termination_protection, bool):
            raise TypeError("Expected argument 'termination_protection' to be a bool")
        pulumi.set(__self__, "termination_protection", termination_protection)

    @property
    @pulumi.getter(name="cloudName")
    def cloud_name(self) -> Optional[str]:
        """
        defines where the cloud provider and region where the service is hosted
        in. This can be changed freely after service is created. Changing the value will trigger
        a potentially lengthy migration process for the service. Format is cloud provider name
        (`aws`, `azure`, `do` `google`, `upcloud`, etc.), dash, and the cloud provider
        specific region name. These are documented on each Cloud provider's own support articles,
        like [here for Google](https://cloud.google.com/compute/docs/regions-zones/) and
        [here for AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html).
        """
        return pulumi.get(self, "cloud_name")

    @property
    @pulumi.getter
    def components(self) -> Sequence['outputs.GetInfluxDbComponentResult']:
        return pulumi.get(self, "components")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def influxdb(self) -> 'outputs.GetInfluxDbInfluxdbResult':
        """
        InfluxDB specific server provided values.
        """
        return pulumi.get(self, "influxdb")

    @property
    @pulumi.getter(name="influxdbUserConfig")
    def influxdb_user_config(self) -> Optional['outputs.GetInfluxDbInfluxdbUserConfigResult']:
        """
        defines InfluxDB specific additional configuration options. The following 
        configuration options available:
        """
        return pulumi.get(self, "influxdb_user_config")

    @property
    @pulumi.getter(name="maintenanceWindowDow")
    def maintenance_window_dow(self) -> Optional[str]:
        """
        day of week when maintenance operations should be performed. 
        On monday, tuesday, wednesday, etc.
        """
        return pulumi.get(self, "maintenance_window_dow")

    @property
    @pulumi.getter(name="maintenanceWindowTime")
    def maintenance_window_time(self) -> Optional[str]:
        """
        time of day when maintenance operations should be performed. 
        UTC time in HH:mm:ss format.
        """
        return pulumi.get(self, "maintenance_window_time")

    @property
    @pulumi.getter
    def plan(self) -> Optional[str]:
        """
        defines what kind of computing resources are allocated for the service. It can
        be changed after creation, though there are some restrictions when going to a smaller
        plan such as the new plan must have sufficient amount of disk space to store all current
        data and switching to a plan with fewer nodes might not be supported. The basic plan
        names are `hobbyist`, `startup-x`, `business-x` and `premium-x` where `x` is
        (roughly) the amount of memory on each node (also other attributes like number of CPUs
        and amount of disk space varies but naming is based on memory). The exact options can be
        seen from the Aiven web console's Create Service dialog.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="projectVpcId")
    def project_vpc_id(self) -> Optional[str]:
        """
        optionally specifies the VPC the service should run in. If the value
        is not set the service is not run inside a VPC. When set, the value should be given as a
        reference as shown above to set up dependencies correctly and the VPC must be in the same
        cloud and region as the service itself. Project can be freely moved to and from VPC after
        creation but doing so triggers migration to new servers so the operation can take
        significant amount of time to complete if the service has a lot of data.
        """
        return pulumi.get(self, "project_vpc_id")

    @property
    @pulumi.getter(name="serviceHost")
    def service_host(self) -> str:
        """
        InfluxDB hostname.
        """
        return pulumi.get(self, "service_host")

    @property
    @pulumi.getter(name="serviceIntegrations")
    def service_integrations(self) -> Optional[Sequence['outputs.GetInfluxDbServiceIntegrationResult']]:
        return pulumi.get(self, "service_integrations")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter(name="servicePassword")
    def service_password(self) -> str:
        """
        Password used for connecting to the InfluxDB service, if applicable.
        """
        return pulumi.get(self, "service_password")

    @property
    @pulumi.getter(name="servicePort")
    def service_port(self) -> int:
        """
        InfluxDB port.
        """
        return pulumi.get(self, "service_port")

    @property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> str:
        return pulumi.get(self, "service_type")

    @property
    @pulumi.getter(name="serviceUri")
    def service_uri(self) -> str:
        """
        URI for connecting to the InfluxDB service.
        """
        return pulumi.get(self, "service_uri")

    @property
    @pulumi.getter(name="serviceUsername")
    def service_username(self) -> str:
        """
        Username used for connecting to the InfluxDB service, if applicable.
        """
        return pulumi.get(self, "service_username")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Service state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="terminationProtection")
    def termination_protection(self) -> Optional[bool]:
        """
        prevents the service from being deleted. It is recommended to
        set this to `true` for all production services to prevent unintentional service
        deletion. This does not shield against deleting databases or topics but for services
        with backups much of the content can at least be restored from backup in case accidental
        deletion is done.
        """
        return pulumi.get(self, "termination_protection")


class AwaitableGetInfluxDbResult(GetInfluxDbResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInfluxDbResult(
            cloud_name=self.cloud_name,
            components=self.components,
            id=self.id,
            influxdb=self.influxdb,
            influxdb_user_config=self.influxdb_user_config,
            maintenance_window_dow=self.maintenance_window_dow,
            maintenance_window_time=self.maintenance_window_time,
            plan=self.plan,
            project=self.project,
            project_vpc_id=self.project_vpc_id,
            service_host=self.service_host,
            service_integrations=self.service_integrations,
            service_name=self.service_name,
            service_password=self.service_password,
            service_port=self.service_port,
            service_type=self.service_type,
            service_uri=self.service_uri,
            service_username=self.service_username,
            state=self.state,
            termination_protection=self.termination_protection)


def get_influx_db(cloud_name: Optional[str] = None,
                  components: Optional[Sequence[pulumi.InputType['GetInfluxDbComponentArgs']]] = None,
                  influxdb: Optional[pulumi.InputType['GetInfluxDbInfluxdbArgs']] = None,
                  influxdb_user_config: Optional[pulumi.InputType['GetInfluxDbInfluxdbUserConfigArgs']] = None,
                  maintenance_window_dow: Optional[str] = None,
                  maintenance_window_time: Optional[str] = None,
                  plan: Optional[str] = None,
                  project: Optional[str] = None,
                  project_vpc_id: Optional[str] = None,
                  service_host: Optional[str] = None,
                  service_integrations: Optional[Sequence[pulumi.InputType['GetInfluxDbServiceIntegrationArgs']]] = None,
                  service_name: Optional[str] = None,
                  service_password: Optional[str] = None,
                  service_port: Optional[int] = None,
                  service_type: Optional[str] = None,
                  service_uri: Optional[str] = None,
                  service_username: Optional[str] = None,
                  state: Optional[str] = None,
                  termination_protection: Optional[bool] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInfluxDbResult:
    """
    ## # InfluxDB Data Source

    The InfluxDB data source provides information about the existing Aiven InfluxDB service.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aiven as aiven

    inf1 = aiven.get_influx_db(project=data["aiven_project"]["pr1"]["project"],
        service_name="my-inf1")
    ```


    :param str cloud_name: defines where the cloud provider and region where the service is hosted
           in. This can be changed freely after service is created. Changing the value will trigger
           a potentially lengthy migration process for the service. Format is cloud provider name
           (`aws`, `azure`, `do` `google`, `upcloud`, etc.), dash, and the cloud provider
           specific region name. These are documented on each Cloud provider's own support articles,
           like [here for Google](https://cloud.google.com/compute/docs/regions-zones/) and
           [here for AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html).
    :param pulumi.InputType['GetInfluxDbInfluxdbArgs'] influxdb: InfluxDB specific server provided values.
    :param pulumi.InputType['GetInfluxDbInfluxdbUserConfigArgs'] influxdb_user_config: defines InfluxDB specific additional configuration options. The following 
           configuration options available:
    :param str maintenance_window_dow: day of week when maintenance operations should be performed. 
           On monday, tuesday, wednesday, etc.
    :param str maintenance_window_time: time of day when maintenance operations should be performed. 
           UTC time in HH:mm:ss format.
    :param str plan: defines what kind of computing resources are allocated for the service. It can
           be changed after creation, though there are some restrictions when going to a smaller
           plan such as the new plan must have sufficient amount of disk space to store all current
           data and switching to a plan with fewer nodes might not be supported. The basic plan
           names are `hobbyist`, `startup-x`, `business-x` and `premium-x` where `x` is
           (roughly) the amount of memory on each node (also other attributes like number of CPUs
           and amount of disk space varies but naming is based on memory). The exact options can be
           seen from the Aiven web console's Create Service dialog.
    :param str project: identifies the project the service belongs to. To set up proper dependency
           between the project and the service, refer to the project as shown in the above example.
           Project cannot be changed later without destroying and re-creating the service.
    :param str project_vpc_id: optionally specifies the VPC the service should run in. If the value
           is not set the service is not run inside a VPC. When set, the value should be given as a
           reference as shown above to set up dependencies correctly and the VPC must be in the same
           cloud and region as the service itself. Project can be freely moved to and from VPC after
           creation but doing so triggers migration to new servers so the operation can take
           significant amount of time to complete if the service has a lot of data.
    :param str service_host: InfluxDB hostname.
    :param str service_name: specifies the actual name of the service. The name cannot be changed
           later without destroying and re-creating the service so name should be picked based on
           intended service usage rather than current attributes.
    :param str service_password: Password used for connecting to the InfluxDB service, if applicable.
    :param int service_port: InfluxDB port.
    :param str service_uri: URI for connecting to the InfluxDB service.
    :param str service_username: Username used for connecting to the InfluxDB service, if applicable.
    :param str state: Service state.
    :param bool termination_protection: prevents the service from being deleted. It is recommended to
           set this to `true` for all production services to prevent unintentional service
           deletion. This does not shield against deleting databases or topics but for services
           with backups much of the content can at least be restored from backup in case accidental
           deletion is done.
    """
    __args__ = dict()
    __args__['cloudName'] = cloud_name
    __args__['components'] = components
    __args__['influxdb'] = influxdb
    __args__['influxdbUserConfig'] = influxdb_user_config
    __args__['maintenanceWindowDow'] = maintenance_window_dow
    __args__['maintenanceWindowTime'] = maintenance_window_time
    __args__['plan'] = plan
    __args__['project'] = project
    __args__['projectVpcId'] = project_vpc_id
    __args__['serviceHost'] = service_host
    __args__['serviceIntegrations'] = service_integrations
    __args__['serviceName'] = service_name
    __args__['servicePassword'] = service_password
    __args__['servicePort'] = service_port
    __args__['serviceType'] = service_type
    __args__['serviceUri'] = service_uri
    __args__['serviceUsername'] = service_username
    __args__['state'] = state
    __args__['terminationProtection'] = termination_protection
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aiven:index/getInfluxDb:getInfluxDb', __args__, opts=opts, typ=GetInfluxDbResult).value

    return AwaitableGetInfluxDbResult(
        cloud_name=__ret__.cloud_name,
        components=__ret__.components,
        id=__ret__.id,
        influxdb=__ret__.influxdb,
        influxdb_user_config=__ret__.influxdb_user_config,
        maintenance_window_dow=__ret__.maintenance_window_dow,
        maintenance_window_time=__ret__.maintenance_window_time,
        plan=__ret__.plan,
        project=__ret__.project,
        project_vpc_id=__ret__.project_vpc_id,
        service_host=__ret__.service_host,
        service_integrations=__ret__.service_integrations,
        service_name=__ret__.service_name,
        service_password=__ret__.service_password,
        service_port=__ret__.service_port,
        service_type=__ret__.service_type,
        service_uri=__ret__.service_uri,
        service_username=__ret__.service_username,
        state=__ret__.state,
        termination_protection=__ret__.termination_protection)
