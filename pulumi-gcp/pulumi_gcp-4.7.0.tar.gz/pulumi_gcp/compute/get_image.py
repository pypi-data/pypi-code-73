# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

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
    def __init__(__self__, archive_size_bytes=None, creation_timestamp=None, description=None, disk_size_gb=None, family=None, filter=None, id=None, image_encryption_key_sha256=None, image_id=None, label_fingerprint=None, labels=None, licenses=None, name=None, project=None, self_link=None, source_disk=None, source_disk_encryption_key_sha256=None, source_disk_id=None, source_image_id=None, status=None):
        if archive_size_bytes and not isinstance(archive_size_bytes, int):
            raise TypeError("Expected argument 'archive_size_bytes' to be a int")
        pulumi.set(__self__, "archive_size_bytes", archive_size_bytes)
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disk_size_gb and not isinstance(disk_size_gb, int):
            raise TypeError("Expected argument 'disk_size_gb' to be a int")
        pulumi.set(__self__, "disk_size_gb", disk_size_gb)
        if family and not isinstance(family, str):
            raise TypeError("Expected argument 'family' to be a str")
        pulumi.set(__self__, "family", family)
        if filter and not isinstance(filter, str):
            raise TypeError("Expected argument 'filter' to be a str")
        pulumi.set(__self__, "filter", filter)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_encryption_key_sha256 and not isinstance(image_encryption_key_sha256, str):
            raise TypeError("Expected argument 'image_encryption_key_sha256' to be a str")
        pulumi.set(__self__, "image_encryption_key_sha256", image_encryption_key_sha256)
        if image_id and not isinstance(image_id, str):
            raise TypeError("Expected argument 'image_id' to be a str")
        pulumi.set(__self__, "image_id", image_id)
        if label_fingerprint and not isinstance(label_fingerprint, str):
            raise TypeError("Expected argument 'label_fingerprint' to be a str")
        pulumi.set(__self__, "label_fingerprint", label_fingerprint)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if licenses and not isinstance(licenses, list):
            raise TypeError("Expected argument 'licenses' to be a list")
        pulumi.set(__self__, "licenses", licenses)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if source_disk and not isinstance(source_disk, str):
            raise TypeError("Expected argument 'source_disk' to be a str")
        pulumi.set(__self__, "source_disk", source_disk)
        if source_disk_encryption_key_sha256 and not isinstance(source_disk_encryption_key_sha256, str):
            raise TypeError("Expected argument 'source_disk_encryption_key_sha256' to be a str")
        pulumi.set(__self__, "source_disk_encryption_key_sha256", source_disk_encryption_key_sha256)
        if source_disk_id and not isinstance(source_disk_id, str):
            raise TypeError("Expected argument 'source_disk_id' to be a str")
        pulumi.set(__self__, "source_disk_id", source_disk_id)
        if source_image_id and not isinstance(source_image_id, str):
            raise TypeError("Expected argument 'source_image_id' to be a str")
        pulumi.set(__self__, "source_image_id", source_image_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="archiveSizeBytes")
    def archive_size_bytes(self) -> int:
        """
        The size of the image tar.gz archive stored in Google Cloud Storage in bytes.
        """
        return pulumi.get(self, "archive_size_bytes")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> str:
        """
        The creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        An optional description of this image.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> int:
        """
        The size of the image when restored onto a persistent disk in gigabytes.
        """
        return pulumi.get(self, "disk_size_gb")

    @property
    @pulumi.getter
    def family(self) -> str:
        """
        The family name of the image.
        """
        return pulumi.get(self, "family")

    @property
    @pulumi.getter
    def filter(self) -> Optional[str]:
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageEncryptionKeySha256")
    def image_encryption_key_sha256(self) -> str:
        """
        The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
        encoded SHA-256 hash of the [customer-supplied encryption key](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
        that protects this image.
        """
        return pulumi.get(self, "image_encryption_key_sha256")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> str:
        """
        The unique identifier for the image.
        """
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> str:
        """
        A fingerprint for the labels being applied to this image.
        """
        return pulumi.get(self, "label_fingerprint")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        A map of labels applied to this image.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def licenses(self) -> Sequence[str]:
        """
        A list of applicable license URI.
        """
        return pulumi.get(self, "licenses")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the image.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        The URI of the image.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> str:
        """
        The URL of the source disk used to create this image.
        """
        return pulumi.get(self, "source_disk")

    @property
    @pulumi.getter(name="sourceDiskEncryptionKeySha256")
    def source_disk_encryption_key_sha256(self) -> str:
        """
        The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
        encoded SHA-256 hash of the [customer-supplied encryption key](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
        that protects this image.
        """
        return pulumi.get(self, "source_disk_encryption_key_sha256")

    @property
    @pulumi.getter(name="sourceDiskId")
    def source_disk_id(self) -> str:
        """
        The ID value of the disk used to create this image.
        """
        return pulumi.get(self, "source_disk_id")

    @property
    @pulumi.getter(name="sourceImageId")
    def source_image_id(self) -> str:
        """
        The ID value of the image used to create this image.
        """
        return pulumi.get(self, "source_image_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the image. Possible values are **FAILED**, **PENDING**, or **READY**.
        """
        return pulumi.get(self, "status")


class AwaitableGetImageResult(GetImageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetImageResult(
            archive_size_bytes=self.archive_size_bytes,
            creation_timestamp=self.creation_timestamp,
            description=self.description,
            disk_size_gb=self.disk_size_gb,
            family=self.family,
            filter=self.filter,
            id=self.id,
            image_encryption_key_sha256=self.image_encryption_key_sha256,
            image_id=self.image_id,
            label_fingerprint=self.label_fingerprint,
            labels=self.labels,
            licenses=self.licenses,
            name=self.name,
            project=self.project,
            self_link=self.self_link,
            source_disk=self.source_disk,
            source_disk_encryption_key_sha256=self.source_disk_encryption_key_sha256,
            source_disk_id=self.source_disk_id,
            source_image_id=self.source_image_id,
            status=self.status)


def get_image(family: Optional[str] = None,
              filter: Optional[str] = None,
              name: Optional[str] = None,
              project: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetImageResult:
    """
    Get information about a Google Compute Image. Check that your service account has the `compute.imageUser` role if you want to share [custom images](https://cloud.google.com/compute/docs/images/sharing-images-across-projects) from another project. If you want to use [public images][pubimg], do not forget to specify the dedicated project. For more information see
    [the official documentation](https://cloud.google.com/compute/docs/images) and its [API](https://cloud.google.com/compute/docs/reference/latest/images).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    my_image = gcp.compute.get_image(family="debian-9",
        project="debian-cloud")
    # ...
    default = gcp.compute.Instance("default", boot_disk=gcp.compute.InstanceBootDiskArgs(
        initialize_params=gcp.compute.InstanceBootDiskInitializeParamsArgs(
            image=my_image.self_link,
        ),
    ))
    ```


    :param str family: The family name of the image.
    :param str name: The name of the image.
    :param str project: The project in which the resource belongs. If it is not
           provided, the provider project is used. If you are using a
           [public base image][pubimg], be sure to specify the correct Image Project.
    """
    __args__ = dict()
    __args__['family'] = family
    __args__['filter'] = filter
    __args__['name'] = name
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('gcp:compute/getImage:getImage', __args__, opts=opts, typ=GetImageResult).value

    return AwaitableGetImageResult(
        archive_size_bytes=__ret__.archive_size_bytes,
        creation_timestamp=__ret__.creation_timestamp,
        description=__ret__.description,
        disk_size_gb=__ret__.disk_size_gb,
        family=__ret__.family,
        filter=__ret__.filter,
        id=__ret__.id,
        image_encryption_key_sha256=__ret__.image_encryption_key_sha256,
        image_id=__ret__.image_id,
        label_fingerprint=__ret__.label_fingerprint,
        labels=__ret__.labels,
        licenses=__ret__.licenses,
        name=__ret__.name,
        project=__ret__.project,
        self_link=__ret__.self_link,
        source_disk=__ret__.source_disk,
        source_disk_encryption_key_sha256=__ret__.source_disk_encryption_key_sha256,
        source_disk_id=__ret__.source_disk_id,
        source_image_id=__ret__.source_image_id,
        status=__ret__.status)
