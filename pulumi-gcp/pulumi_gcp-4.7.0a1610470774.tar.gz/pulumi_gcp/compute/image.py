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

__all__ = ['Image']


class Image(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disk_size_gb: Optional[pulumi.Input[int]] = None,
                 family: Optional[pulumi.Input[str]] = None,
                 guest_os_features: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ImageGuestOsFeatureArgs']]]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 licenses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 raw_disk: Optional[pulumi.Input[pulumi.InputType['ImageRawDiskArgs']]] = None,
                 source_disk: Optional[pulumi.Input[str]] = None,
                 source_image: Optional[pulumi.Input[str]] = None,
                 source_snapshot: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Represents an Image resource.

        Google Compute Engine uses operating system images to create the root
        persistent disks for your instances. You specify an image when you create
        an instance. Images contain a boot loader, an operating system, and a
        root file system. Linux operating system images are also capable of
        running containers on Compute Engine.

        Images can be either public or custom.

        Public images are provided and maintained by Google, open-source
        communities, and third-party vendors. By default, all projects have
        access to these images and can use them to create instances.  Custom
        images are available only to your project. You can create a custom image
        from root persistent disks and other images. Then, use the custom image
        to create an instance.

        To get more information about Image, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/v1/images)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/compute/docs/images)

        ## Example Usage
        ### Image Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.compute.Image("example", raw_disk=gcp.compute.ImageRawDiskArgs(
            source="https://storage.googleapis.com/bosh-gce-raw-stemcells/bosh-stemcell-97.98-google-kvm-ubuntu-xenial-go_agent-raw-1557960142.tar.gz",
        ))
        ```
        ### Image Guest Os

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.compute.Image("example",
            guest_os_features=[
                gcp.compute.ImageGuestOsFeatureArgs(
                    type="SECURE_BOOT",
                ),
                gcp.compute.ImageGuestOsFeatureArgs(
                    type="MULTI_IP_SUBNET",
                ),
            ],
            raw_disk=gcp.compute.ImageRawDiskArgs(
                source="https://storage.googleapis.com/bosh-gce-raw-stemcells/bosh-stemcell-97.98-google-kvm-ubuntu-xenial-go_agent-raw-1557960142.tar.gz",
            ))
        ```

        ## Import

        Image can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:compute/image:Image default projects/{{project}}/global/images/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/image:Image default {{project}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/image:Image default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when
               you create the resource.
        :param pulumi.Input[int] disk_size_gb: Size of the image when restored onto a persistent disk (in GB).
        :param pulumi.Input[str] family: The name of the image family to which this image belongs. You can
               create disks by specifying an image family instead of a specific
               image name. The image family always returns its latest image that is
               not deprecated. The name of the image family must comply with
               RFC1035.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ImageGuestOsFeatureArgs']]]] guest_os_features: A list of features to enable on the guest operating system.
               Applicable only for bootable images.
               Structure is documented below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels to apply to this Image.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] licenses: Any applicable license URI.
        :param pulumi.Input[str] name: Name of the resource; provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and
               match the regular expression `a-z?` which means
               the first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the
               last character, which cannot be a dash.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['ImageRawDiskArgs']] raw_disk: The parameters of the raw disk image.
               Structure is documented below.
        :param pulumi.Input[str] source_disk: The source disk to create this image based on.
               You must provide either this property or the
               rawDisk.source property but not both to create an image.
        :param pulumi.Input[str] source_image: URL of the source image used to create this image. In order to create an image, you must provide the full or partial
               URL of one of the following:
               * The selfLink URL
               * This property
               * The rawDisk.source URL
               * The sourceDisk URL
        :param pulumi.Input[str] source_snapshot: URL of the source snapshot used to create this image.
               In order to create an image, you must provide the full or partial URL of one of the following:
               * The selfLink URL
               * This property
               * The sourceImage URL
               * The rawDisk.source URL
               * The sourceDisk URL
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

            __props__['description'] = description
            __props__['disk_size_gb'] = disk_size_gb
            __props__['family'] = family
            __props__['guest_os_features'] = guest_os_features
            __props__['labels'] = labels
            __props__['licenses'] = licenses
            __props__['name'] = name
            __props__['project'] = project
            __props__['raw_disk'] = raw_disk
            __props__['source_disk'] = source_disk
            __props__['source_image'] = source_image
            __props__['source_snapshot'] = source_snapshot
            __props__['archive_size_bytes'] = None
            __props__['creation_timestamp'] = None
            __props__['label_fingerprint'] = None
            __props__['self_link'] = None
        super(Image, __self__).__init__(
            'gcp:compute/image:Image',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            archive_size_bytes: Optional[pulumi.Input[int]] = None,
            creation_timestamp: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            disk_size_gb: Optional[pulumi.Input[int]] = None,
            family: Optional[pulumi.Input[str]] = None,
            guest_os_features: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ImageGuestOsFeatureArgs']]]]] = None,
            label_fingerprint: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            licenses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            raw_disk: Optional[pulumi.Input[pulumi.InputType['ImageRawDiskArgs']]] = None,
            self_link: Optional[pulumi.Input[str]] = None,
            source_disk: Optional[pulumi.Input[str]] = None,
            source_image: Optional[pulumi.Input[str]] = None,
            source_snapshot: Optional[pulumi.Input[str]] = None) -> 'Image':
        """
        Get an existing Image resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] archive_size_bytes: Size of the image tar.gz archive stored in Google Cloud Storage (in bytes).
        :param pulumi.Input[str] creation_timestamp: Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when
               you create the resource.
        :param pulumi.Input[int] disk_size_gb: Size of the image when restored onto a persistent disk (in GB).
        :param pulumi.Input[str] family: The name of the image family to which this image belongs. You can
               create disks by specifying an image family instead of a specific
               image name. The image family always returns its latest image that is
               not deprecated. The name of the image family must comply with
               RFC1035.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ImageGuestOsFeatureArgs']]]] guest_os_features: A list of features to enable on the guest operating system.
               Applicable only for bootable images.
               Structure is documented below.
        :param pulumi.Input[str] label_fingerprint: The fingerprint used for optimistic locking of this resource. Used internally during updates.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels to apply to this Image.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] licenses: Any applicable license URI.
        :param pulumi.Input[str] name: Name of the resource; provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and
               match the regular expression `a-z?` which means
               the first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the
               last character, which cannot be a dash.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['ImageRawDiskArgs']] raw_disk: The parameters of the raw disk image.
               Structure is documented below.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        :param pulumi.Input[str] source_disk: The source disk to create this image based on.
               You must provide either this property or the
               rawDisk.source property but not both to create an image.
        :param pulumi.Input[str] source_image: URL of the source image used to create this image. In order to create an image, you must provide the full or partial
               URL of one of the following:
               * The selfLink URL
               * This property
               * The rawDisk.source URL
               * The sourceDisk URL
        :param pulumi.Input[str] source_snapshot: URL of the source snapshot used to create this image.
               In order to create an image, you must provide the full or partial URL of one of the following:
               * The selfLink URL
               * This property
               * The sourceImage URL
               * The rawDisk.source URL
               * The sourceDisk URL
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["archive_size_bytes"] = archive_size_bytes
        __props__["creation_timestamp"] = creation_timestamp
        __props__["description"] = description
        __props__["disk_size_gb"] = disk_size_gb
        __props__["family"] = family
        __props__["guest_os_features"] = guest_os_features
        __props__["label_fingerprint"] = label_fingerprint
        __props__["labels"] = labels
        __props__["licenses"] = licenses
        __props__["name"] = name
        __props__["project"] = project
        __props__["raw_disk"] = raw_disk
        __props__["self_link"] = self_link
        __props__["source_disk"] = source_disk
        __props__["source_image"] = source_image
        __props__["source_snapshot"] = source_snapshot
        return Image(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="archiveSizeBytes")
    def archive_size_bytes(self) -> pulumi.Output[int]:
        """
        Size of the image tar.gz archive stored in Google Cloud Storage (in bytes).
        """
        return pulumi.get(self, "archive_size_bytes")

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
        An optional description of this resource. Provide this property when
        you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> pulumi.Output[int]:
        """
        Size of the image when restored onto a persistent disk (in GB).
        """
        return pulumi.get(self, "disk_size_gb")

    @property
    @pulumi.getter
    def family(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the image family to which this image belongs. You can
        create disks by specifying an image family instead of a specific
        image name. The image family always returns its latest image that is
        not deprecated. The name of the image family must comply with
        RFC1035.
        """
        return pulumi.get(self, "family")

    @property
    @pulumi.getter(name="guestOsFeatures")
    def guest_os_features(self) -> pulumi.Output[Sequence['outputs.ImageGuestOsFeature']]:
        """
        A list of features to enable on the guest operating system.
        Applicable only for bootable images.
        Structure is documented below.
        """
        return pulumi.get(self, "guest_os_features")

    @property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> pulumi.Output[str]:
        """
        The fingerprint used for optimistic locking of this resource. Used internally during updates.
        """
        return pulumi.get(self, "label_fingerprint")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Labels to apply to this Image.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def licenses(self) -> pulumi.Output[Sequence[str]]:
        """
        Any applicable license URI.
        """
        return pulumi.get(self, "licenses")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource; provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and
        match the regular expression `a-z?` which means
        the first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the
        last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="rawDisk")
    def raw_disk(self) -> pulumi.Output[Optional['outputs.ImageRawDisk']]:
        """
        The parameters of the raw disk image.
        Structure is documented below.
        """
        return pulumi.get(self, "raw_disk")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> pulumi.Output[Optional[str]]:
        """
        The source disk to create this image based on.
        You must provide either this property or the
        rawDisk.source property but not both to create an image.
        """
        return pulumi.get(self, "source_disk")

    @property
    @pulumi.getter(name="sourceImage")
    def source_image(self) -> pulumi.Output[Optional[str]]:
        """
        URL of the source image used to create this image. In order to create an image, you must provide the full or partial
        URL of one of the following:
        * The selfLink URL
        * This property
        * The rawDisk.source URL
        * The sourceDisk URL
        """
        return pulumi.get(self, "source_image")

    @property
    @pulumi.getter(name="sourceSnapshot")
    def source_snapshot(self) -> pulumi.Output[Optional[str]]:
        """
        URL of the source snapshot used to create this image.
        In order to create an image, you must provide the full or partial URL of one of the following:
        * The selfLink URL
        * This property
        * The sourceImage URL
        * The rawDisk.source URL
        * The sourceDisk URL
        """
        return pulumi.get(self, "source_snapshot")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

