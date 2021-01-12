# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetBucketObjectContentResult',
    'AwaitableGetBucketObjectContentResult',
    'get_bucket_object_content',
]

@pulumi.output_type
class GetBucketObjectContentResult:
    """
    A collection of values returned by getBucketObjectContent.
    """
    def __init__(__self__, bucket=None, cache_control=None, content=None, content_disposition=None, content_encoding=None, content_language=None, content_type=None, crc32c=None, detect_md5hash=None, id=None, md5hash=None, media_link=None, metadata=None, name=None, output_name=None, self_link=None, source=None, storage_class=None):
        if bucket and not isinstance(bucket, str):
            raise TypeError("Expected argument 'bucket' to be a str")
        pulumi.set(__self__, "bucket", bucket)
        if cache_control and not isinstance(cache_control, str):
            raise TypeError("Expected argument 'cache_control' to be a str")
        pulumi.set(__self__, "cache_control", cache_control)
        if content and not isinstance(content, str):
            raise TypeError("Expected argument 'content' to be a str")
        pulumi.set(__self__, "content", content)
        if content_disposition and not isinstance(content_disposition, str):
            raise TypeError("Expected argument 'content_disposition' to be a str")
        pulumi.set(__self__, "content_disposition", content_disposition)
        if content_encoding and not isinstance(content_encoding, str):
            raise TypeError("Expected argument 'content_encoding' to be a str")
        pulumi.set(__self__, "content_encoding", content_encoding)
        if content_language and not isinstance(content_language, str):
            raise TypeError("Expected argument 'content_language' to be a str")
        pulumi.set(__self__, "content_language", content_language)
        if content_type and not isinstance(content_type, str):
            raise TypeError("Expected argument 'content_type' to be a str")
        pulumi.set(__self__, "content_type", content_type)
        if crc32c and not isinstance(crc32c, str):
            raise TypeError("Expected argument 'crc32c' to be a str")
        pulumi.set(__self__, "crc32c", crc32c)
        if detect_md5hash and not isinstance(detect_md5hash, str):
            raise TypeError("Expected argument 'detect_md5hash' to be a str")
        pulumi.set(__self__, "detect_md5hash", detect_md5hash)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if md5hash and not isinstance(md5hash, str):
            raise TypeError("Expected argument 'md5hash' to be a str")
        pulumi.set(__self__, "md5hash", md5hash)
        if media_link and not isinstance(media_link, str):
            raise TypeError("Expected argument 'media_link' to be a str")
        pulumi.set(__self__, "media_link", media_link)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if output_name and not isinstance(output_name, str):
            raise TypeError("Expected argument 'output_name' to be a str")
        pulumi.set(__self__, "output_name", output_name)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if source and not isinstance(source, str):
            raise TypeError("Expected argument 'source' to be a str")
        pulumi.set(__self__, "source", source)
        if storage_class and not isinstance(storage_class, str):
            raise TypeError("Expected argument 'storage_class' to be a str")
        pulumi.set(__self__, "storage_class", storage_class)

    @property
    @pulumi.getter
    def bucket(self) -> str:
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="cacheControl")
    def cache_control(self) -> str:
        return pulumi.get(self, "cache_control")

    @property
    @pulumi.getter
    def content(self) -> Optional[str]:
        """
        (Computed) [Content-Language](https://tools.ietf.org/html/rfc7231#section-3.1.3.2) of the object content.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="contentDisposition")
    def content_disposition(self) -> str:
        return pulumi.get(self, "content_disposition")

    @property
    @pulumi.getter(name="contentEncoding")
    def content_encoding(self) -> str:
        return pulumi.get(self, "content_encoding")

    @property
    @pulumi.getter(name="contentLanguage")
    def content_language(self) -> str:
        return pulumi.get(self, "content_language")

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> str:
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter
    def crc32c(self) -> str:
        return pulumi.get(self, "crc32c")

    @property
    @pulumi.getter(name="detectMd5hash")
    def detect_md5hash(self) -> str:
        return pulumi.get(self, "detect_md5hash")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def md5hash(self) -> str:
        return pulumi.get(self, "md5hash")

    @property
    @pulumi.getter(name="mediaLink")
    def media_link(self) -> str:
        return pulumi.get(self, "media_link")

    @property
    @pulumi.getter
    def metadata(self) -> Mapping[str, str]:
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outputName")
    def output_name(self) -> str:
        return pulumi.get(self, "output_name")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def source(self) -> str:
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> str:
        return pulumi.get(self, "storage_class")


class AwaitableGetBucketObjectContentResult(GetBucketObjectContentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBucketObjectContentResult(
            bucket=self.bucket,
            cache_control=self.cache_control,
            content=self.content,
            content_disposition=self.content_disposition,
            content_encoding=self.content_encoding,
            content_language=self.content_language,
            content_type=self.content_type,
            crc32c=self.crc32c,
            detect_md5hash=self.detect_md5hash,
            id=self.id,
            md5hash=self.md5hash,
            media_link=self.media_link,
            metadata=self.metadata,
            name=self.name,
            output_name=self.output_name,
            self_link=self.self_link,
            source=self.source,
            storage_class=self.storage_class)


def get_bucket_object_content(bucket: Optional[str] = None,
                              content: Optional[str] = None,
                              name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBucketObjectContentResult:
    """
    Gets an existing object content inside an existing bucket in Google Cloud Storage service (GCS).
    See [the official documentation](https://cloud.google.com/storage/docs/key-terms#objects)
    and
    [API](https://cloud.google.com/storage/docs/json_api/v1/objects).

    > **Warning:** The object content will be saved in the state, and visiable to everyone who has access to the state file.

    ## Example Usage

    Example file object  stored within a folder.

    ```python
    import pulumi
    import pulumi_gcp as gcp

    key = gcp.storage.get_bucket_object_content(name="encryptedkey",
        bucket="keystore")
    pulumi.export("encrypted", key.content)
    ```


    :param str bucket: The name of the containing bucket.
    :param str content: (Computed) [Content-Language](https://tools.ietf.org/html/rfc7231#section-3.1.3.2) of the object content.
    :param str name: The name of the object.
    """
    __args__ = dict()
    __args__['bucket'] = bucket
    __args__['content'] = content
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('gcp:storage/getBucketObjectContent:getBucketObjectContent', __args__, opts=opts, typ=GetBucketObjectContentResult).value

    return AwaitableGetBucketObjectContentResult(
        bucket=__ret__.bucket,
        cache_control=__ret__.cache_control,
        content=__ret__.content,
        content_disposition=__ret__.content_disposition,
        content_encoding=__ret__.content_encoding,
        content_language=__ret__.content_language,
        content_type=__ret__.content_type,
        crc32c=__ret__.crc32c,
        detect_md5hash=__ret__.detect_md5hash,
        id=__ret__.id,
        md5hash=__ret__.md5hash,
        media_link=__ret__.media_link,
        metadata=__ret__.metadata,
        name=__ret__.name,
        output_name=__ret__.output_name,
        self_link=__ret__.self_link,
        source=__ret__.source,
        storage_class=__ret__.storage_class)
