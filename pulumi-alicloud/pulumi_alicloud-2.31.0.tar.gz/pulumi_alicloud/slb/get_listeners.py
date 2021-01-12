# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'GetListenersResult',
    'AwaitableGetListenersResult',
    'get_listeners',
]

@pulumi.output_type
class GetListenersResult:
    """
    A collection of values returned by getListeners.
    """
    def __init__(__self__, description_regex=None, frontend_port=None, id=None, load_balancer_id=None, output_file=None, protocol=None, slb_listeners=None):
        if description_regex and not isinstance(description_regex, str):
            raise TypeError("Expected argument 'description_regex' to be a str")
        pulumi.set(__self__, "description_regex", description_regex)
        if frontend_port and not isinstance(frontend_port, int):
            raise TypeError("Expected argument 'frontend_port' to be a int")
        pulumi.set(__self__, "frontend_port", frontend_port)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if load_balancer_id and not isinstance(load_balancer_id, str):
            raise TypeError("Expected argument 'load_balancer_id' to be a str")
        pulumi.set(__self__, "load_balancer_id", load_balancer_id)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if protocol and not isinstance(protocol, str):
            raise TypeError("Expected argument 'protocol' to be a str")
        pulumi.set(__self__, "protocol", protocol)
        if slb_listeners and not isinstance(slb_listeners, list):
            raise TypeError("Expected argument 'slb_listeners' to be a list")
        pulumi.set(__self__, "slb_listeners", slb_listeners)

    @property
    @pulumi.getter(name="descriptionRegex")
    def description_regex(self) -> Optional[str]:
        return pulumi.get(self, "description_regex")

    @property
    @pulumi.getter(name="frontendPort")
    def frontend_port(self) -> Optional[int]:
        """
        Frontend port used to receive incoming traffic and distribute it to the backend servers.
        """
        return pulumi.get(self, "frontend_port")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="loadBalancerId")
    def load_balancer_id(self) -> str:
        return pulumi.get(self, "load_balancer_id")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def protocol(self) -> Optional[str]:
        """
        Listener protocol. Possible values: `http`, `https`, `tcp` and `udp`.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="slbListeners")
    def slb_listeners(self) -> Sequence['outputs.GetListenersSlbListenerResult']:
        """
        A list of SLB listeners. Each element contains the following attributes:
        """
        return pulumi.get(self, "slb_listeners")


class AwaitableGetListenersResult(GetListenersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetListenersResult(
            description_regex=self.description_regex,
            frontend_port=self.frontend_port,
            id=self.id,
            load_balancer_id=self.load_balancer_id,
            output_file=self.output_file,
            protocol=self.protocol,
            slb_listeners=self.slb_listeners)


def get_listeners(description_regex: Optional[str] = None,
                  frontend_port: Optional[int] = None,
                  load_balancer_id: Optional[str] = None,
                  output_file: Optional[str] = None,
                  protocol: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetListenersResult:
    """
    This data source provides the listeners related to a server load balancer of the current Alibaba Cloud user.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.slb.LoadBalancer("default")
    tcp = alicloud.slb.Listener("tcp",
        load_balancer_id=default.id,
        backend_port=22,
        frontend_port=22,
        protocol="tcp",
        bandwidth=10,
        health_check_type="tcp",
        persistence_timeout=3600,
        healthy_threshold=8,
        unhealthy_threshold=8,
        health_check_timeout=8,
        health_check_interval=5,
        health_check_http_code="http_2xx",
        health_check_connect_port=20,
        health_check_uri="/console",
        established_timeout=600)
    sample_ds = default.id.apply(lambda id: alicloud.slb.get_listeners(load_balancer_id=id))
    pulumi.export("firstSlbListenerProtocol", sample_ds.slb_listeners[0].protocol)
    ```


    :param str description_regex: A regex string to filter results by SLB listener description.
    :param int frontend_port: Filter listeners by the specified frontend port.
    :param str load_balancer_id: ID of the SLB with listeners.
    :param str protocol: Filter listeners by the specified protocol. Valid values: `http`, `https`, `tcp` and `udp`.
    """
    __args__ = dict()
    __args__['descriptionRegex'] = description_regex
    __args__['frontendPort'] = frontend_port
    __args__['loadBalancerId'] = load_balancer_id
    __args__['outputFile'] = output_file
    __args__['protocol'] = protocol
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:slb/getListeners:getListeners', __args__, opts=opts, typ=GetListenersResult).value

    return AwaitableGetListenersResult(
        description_regex=__ret__.description_regex,
        frontend_port=__ret__.frontend_port,
        id=__ret__.id,
        load_balancer_id=__ret__.load_balancer_id,
        output_file=__ret__.output_file,
        protocol=__ret__.protocol,
        slb_listeners=__ret__.slb_listeners)
