# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = [
    'GetImageResult',
    'AwaitableGetImageResult',
    'get_image',
]

@pulumi.output_type
class GetImageResult:
    """
    A collection of values returned by getImage.
    """
    def __init__(__self__, created=None, deprecated=None, description=None, id=None, labels=None, most_recent=None, name=None, os_flavor=None, os_version=None, rapid_deploy=None, selector=None, type=None, with_selector=None, with_statuses=None):
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if deprecated and not isinstance(deprecated, str):
            raise TypeError("Expected argument 'deprecated' to be a str")
        pulumi.set(__self__, "deprecated", deprecated)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, int):
            raise TypeError("Expected argument 'id' to be a int")
        pulumi.set(__self__, "id", id)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if most_recent and not isinstance(most_recent, bool):
            raise TypeError("Expected argument 'most_recent' to be a bool")
        pulumi.set(__self__, "most_recent", most_recent)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if os_flavor and not isinstance(os_flavor, str):
            raise TypeError("Expected argument 'os_flavor' to be a str")
        pulumi.set(__self__, "os_flavor", os_flavor)
        if os_version and not isinstance(os_version, str):
            raise TypeError("Expected argument 'os_version' to be a str")
        pulumi.set(__self__, "os_version", os_version)
        if rapid_deploy and not isinstance(rapid_deploy, bool):
            raise TypeError("Expected argument 'rapid_deploy' to be a bool")
        pulumi.set(__self__, "rapid_deploy", rapid_deploy)
        if selector and not isinstance(selector, str):
            raise TypeError("Expected argument 'selector' to be a str")
        if selector is not None:
            warnings.warn("""Please use the with_selector property instead.""", DeprecationWarning)
            pulumi.log.warn("selector is deprecated: Please use the with_selector property instead.")

        pulumi.set(__self__, "selector", selector)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if with_selector and not isinstance(with_selector, str):
            raise TypeError("Expected argument 'with_selector' to be a str")
        pulumi.set(__self__, "with_selector", with_selector)
        if with_statuses and not isinstance(with_statuses, list):
            raise TypeError("Expected argument 'with_statuses' to be a list")
        pulumi.set(__self__, "with_statuses", with_statuses)

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        (string) Date when the Image was created (in ISO-8601 format).
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def deprecated(self) -> str:
        """
        (string) Point in time when the image is considered to be deprecated (in ISO-8601 format).
        """
        return pulumi.get(self, "deprecated")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        (string) Description of the Image.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[int]:
        """
        (int) Unique ID of the Image.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, Any]:
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[bool]:
        return pulumi.get(self, "most_recent")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        (string) Name of the Image, only present when the Image is of type `system`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="osFlavor")
    def os_flavor(self) -> str:
        """
        (string) Flavor of operating system contained in the image, could be `ubuntu`, `centos`, `debian`, `fedora` or `unknown`.
        """
        return pulumi.get(self, "os_flavor")

    @property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> str:
        """
        (string) Operating system version.
        """
        return pulumi.get(self, "os_version")

    @property
    @pulumi.getter(name="rapidDeploy")
    def rapid_deploy(self) -> bool:
        """
        (bool) Indicates that rapid deploy of the image is available.
        """
        return pulumi.get(self, "rapid_deploy")

    @property
    @pulumi.getter
    def selector(self) -> Optional[str]:
        return pulumi.get(self, "selector")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        (string) Type of the Image, could be `system`, `backup` or `snapshot`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="withSelector")
    def with_selector(self) -> Optional[str]:
        return pulumi.get(self, "with_selector")

    @property
    @pulumi.getter(name="withStatuses")
    def with_statuses(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "with_statuses")


class AwaitableGetImageResult(GetImageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetImageResult(
            created=self.created,
            deprecated=self.deprecated,
            description=self.description,
            id=self.id,
            labels=self.labels,
            most_recent=self.most_recent,
            name=self.name,
            os_flavor=self.os_flavor,
            os_version=self.os_version,
            rapid_deploy=self.rapid_deploy,
            selector=self.selector,
            type=self.type,
            with_selector=self.with_selector,
            with_statuses=self.with_statuses)


def get_image(id: Optional[int] = None,
              most_recent: Optional[bool] = None,
              name: Optional[str] = None,
              selector: Optional[str] = None,
              with_selector: Optional[str] = None,
              with_statuses: Optional[Sequence[str]] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetImageResult:
    """
    Use this data source to access information about an existing resource.

    :param int id: ID of the Image.
    :param bool most_recent: If more than one result is returned, use the most recent Image.
    :param str name: Name of the Image.
    :param str with_selector: [Label selector](https://docs.hetzner.cloud/#overview-label-selector)
    :param Sequence[str] with_statuses: List only images with the specified status, could contain `creating` or `available`.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['mostRecent'] = most_recent
    __args__['name'] = name
    __args__['selector'] = selector
    __args__['withSelector'] = with_selector
    __args__['withStatuses'] = with_statuses
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('hcloud:index/getImage:getImage', __args__, opts=opts, typ=GetImageResult).value

    return AwaitableGetImageResult(
        created=__ret__.created,
        deprecated=__ret__.deprecated,
        description=__ret__.description,
        id=__ret__.id,
        labels=__ret__.labels,
        most_recent=__ret__.most_recent,
        name=__ret__.name,
        os_flavor=__ret__.os_flavor,
        os_version=__ret__.os_version,
        rapid_deploy=__ret__.rapid_deploy,
        selector=__ret__.selector,
        type=__ret__.type,
        with_selector=__ret__.with_selector,
        with_statuses=__ret__.with_statuses)
