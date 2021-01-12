# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['ObjectStorageObject']


class ObjectStorageObject(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_key: Optional[pulumi.Input[str]] = None,
                 acl: Optional[pulumi.Input[str]] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 cache_control: Optional[pulumi.Input[str]] = None,
                 cluster: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 content_base64: Optional[pulumi.Input[str]] = None,
                 content_disposition: Optional[pulumi.Input[str]] = None,
                 content_encoding: Optional[pulumi.Input[str]] = None,
                 content_language: Optional[pulumi.Input[str]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 secret_key: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 website_redirect: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Linode Object Storage Object resource. This can be used to create, modify, and delete Linodes Object Storage Objects for Buckets.

        ## Example Usage
        ### Uploading plaintext to a bucket

        ```python
        import pulumi
        import pulumi_linode as linode

        object = linode.ObjectStorageObject("object",
            bucket="my-bucket",
            cluster="us-east-1",
            key="my-object",
            secret_key=linode_object_storage_key["my_key"]["secret_key"],
            access_key=linode_object_storage_key["my_key"]["access_key"],
            content="This is the content of the Object...",
            content_type="text/plain",
            content_language="en")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_key: The access key to authenticate with.
        :param pulumi.Input[str] acl: The canned ACL to apply. Can be one of `private`, `public-read`, `authenticated-read`, `public-read-write`, and `custom` (defaults to `private`).
        :param pulumi.Input[str] bucket: The name of the bucket to put the object in.
        :param pulumi.Input[str] cache_control: Specifies caching behavior along the request/reply chain Read [w3c cache_control](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9) for further details.
        :param pulumi.Input[str] cluster: The cluster the bucket is in.
        :param pulumi.Input[str] content: Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.
        :param pulumi.Input[str] content_base64: Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the `gzipbase64` function with small text strings. For larger objects, use `source` to stream the content from a disk file.
        :param pulumi.Input[str] content_disposition: Specifies presentational information for the object. Read [w3c content_disposition](http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1) for further information.
        :param pulumi.Input[str] content_encoding: Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [w3c content encoding](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11) for further information.
        :param pulumi.Input[str] content_language: The language the content is in e.g. en-US or en-GB.
        :param pulumi.Input[str] content_type: A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
        :param pulumi.Input[bool] force_destroy: Allow the object to be deleted regardless of any legal hold or object lock (defaults to `false`).
        :param pulumi.Input[str] key: They name of the object once it is in the bucket.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: A map of keys/values to provision metadata.
        :param pulumi.Input[str] secret_key: The secret key to authenitcate with.
        :param pulumi.Input[str] source: The path to a file that will be read and uploaded as raw bytes for the object content. The path must either be relative to the root module or absolute.
        :param pulumi.Input[str] website_redirect: Specifies a target URL for website redirect.
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

            if access_key is None and not opts.urn:
                raise TypeError("Missing required property 'access_key'")
            __props__['access_key'] = access_key
            __props__['acl'] = acl
            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__['bucket'] = bucket
            __props__['cache_control'] = cache_control
            if cluster is None and not opts.urn:
                raise TypeError("Missing required property 'cluster'")
            __props__['cluster'] = cluster
            __props__['content'] = content
            __props__['content_base64'] = content_base64
            __props__['content_disposition'] = content_disposition
            __props__['content_encoding'] = content_encoding
            __props__['content_language'] = content_language
            __props__['content_type'] = content_type
            __props__['etag'] = etag
            __props__['force_destroy'] = force_destroy
            if key is None and not opts.urn:
                raise TypeError("Missing required property 'key'")
            __props__['key'] = key
            __props__['metadata'] = metadata
            if secret_key is None and not opts.urn:
                raise TypeError("Missing required property 'secret_key'")
            __props__['secret_key'] = secret_key
            __props__['source'] = source
            __props__['website_redirect'] = website_redirect
            __props__['version_id'] = None
        super(ObjectStorageObject, __self__).__init__(
            'linode:index/objectStorageObject:ObjectStorageObject',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_key: Optional[pulumi.Input[str]] = None,
            acl: Optional[pulumi.Input[str]] = None,
            bucket: Optional[pulumi.Input[str]] = None,
            cache_control: Optional[pulumi.Input[str]] = None,
            cluster: Optional[pulumi.Input[str]] = None,
            content: Optional[pulumi.Input[str]] = None,
            content_base64: Optional[pulumi.Input[str]] = None,
            content_disposition: Optional[pulumi.Input[str]] = None,
            content_encoding: Optional[pulumi.Input[str]] = None,
            content_language: Optional[pulumi.Input[str]] = None,
            content_type: Optional[pulumi.Input[str]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            force_destroy: Optional[pulumi.Input[bool]] = None,
            key: Optional[pulumi.Input[str]] = None,
            metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            secret_key: Optional[pulumi.Input[str]] = None,
            source: Optional[pulumi.Input[str]] = None,
            version_id: Optional[pulumi.Input[str]] = None,
            website_redirect: Optional[pulumi.Input[str]] = None) -> 'ObjectStorageObject':
        """
        Get an existing ObjectStorageObject resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_key: The access key to authenticate with.
        :param pulumi.Input[str] acl: The canned ACL to apply. Can be one of `private`, `public-read`, `authenticated-read`, `public-read-write`, and `custom` (defaults to `private`).
        :param pulumi.Input[str] bucket: The name of the bucket to put the object in.
        :param pulumi.Input[str] cache_control: Specifies caching behavior along the request/reply chain Read [w3c cache_control](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9) for further details.
        :param pulumi.Input[str] cluster: The cluster the bucket is in.
        :param pulumi.Input[str] content: Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.
        :param pulumi.Input[str] content_base64: Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the `gzipbase64` function with small text strings. For larger objects, use `source` to stream the content from a disk file.
        :param pulumi.Input[str] content_disposition: Specifies presentational information for the object. Read [w3c content_disposition](http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1) for further information.
        :param pulumi.Input[str] content_encoding: Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [w3c content encoding](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11) for further information.
        :param pulumi.Input[str] content_language: The language the content is in e.g. en-US or en-GB.
        :param pulumi.Input[str] content_type: A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
        :param pulumi.Input[bool] force_destroy: Allow the object to be deleted regardless of any legal hold or object lock (defaults to `false`).
        :param pulumi.Input[str] key: They name of the object once it is in the bucket.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: A map of keys/values to provision metadata.
        :param pulumi.Input[str] secret_key: The secret key to authenitcate with.
        :param pulumi.Input[str] source: The path to a file that will be read and uploaded as raw bytes for the object content. The path must either be relative to the root module or absolute.
        :param pulumi.Input[str] version_id: A unique version ID value for the object.
        :param pulumi.Input[str] website_redirect: Specifies a target URL for website redirect.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access_key"] = access_key
        __props__["acl"] = acl
        __props__["bucket"] = bucket
        __props__["cache_control"] = cache_control
        __props__["cluster"] = cluster
        __props__["content"] = content
        __props__["content_base64"] = content_base64
        __props__["content_disposition"] = content_disposition
        __props__["content_encoding"] = content_encoding
        __props__["content_language"] = content_language
        __props__["content_type"] = content_type
        __props__["etag"] = etag
        __props__["force_destroy"] = force_destroy
        __props__["key"] = key
        __props__["metadata"] = metadata
        __props__["secret_key"] = secret_key
        __props__["source"] = source
        __props__["version_id"] = version_id
        __props__["website_redirect"] = website_redirect
        return ObjectStorageObject(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> pulumi.Output[str]:
        """
        The access key to authenticate with.
        """
        return pulumi.get(self, "access_key")

    @property
    @pulumi.getter
    def acl(self) -> pulumi.Output[Optional[str]]:
        """
        The canned ACL to apply. Can be one of `private`, `public-read`, `authenticated-read`, `public-read-write`, and `custom` (defaults to `private`).
        """
        return pulumi.get(self, "acl")

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        The name of the bucket to put the object in.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="cacheControl")
    def cache_control(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies caching behavior along the request/reply chain Read [w3c cache_control](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9) for further details.
        """
        return pulumi.get(self, "cache_control")

    @property
    @pulumi.getter
    def cluster(self) -> pulumi.Output[str]:
        """
        The cluster the bucket is in.
        """
        return pulumi.get(self, "cluster")

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output[Optional[str]]:
        """
        Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="contentBase64")
    def content_base64(self) -> pulumi.Output[Optional[str]]:
        """
        Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the `gzipbase64` function with small text strings. For larger objects, use `source` to stream the content from a disk file.
        """
        return pulumi.get(self, "content_base64")

    @property
    @pulumi.getter(name="contentDisposition")
    def content_disposition(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies presentational information for the object. Read [w3c content_disposition](http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1) for further information.
        """
        return pulumi.get(self, "content_disposition")

    @property
    @pulumi.getter(name="contentEncoding")
    def content_encoding(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [w3c content encoding](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11) for further information.
        """
        return pulumi.get(self, "content_encoding")

    @property
    @pulumi.getter(name="contentLanguage")
    def content_language(self) -> pulumi.Output[Optional[str]]:
        """
        The language the content is in e.g. en-US or en-GB.
        """
        return pulumi.get(self, "content_language")

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[str]:
        """
        A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[bool]]:
        """
        Allow the object to be deleted regardless of any legal hold or object lock (defaults to `false`).
        """
        return pulumi.get(self, "force_destroy")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        They name of the object once it is in the bucket.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of keys/values to provision metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> pulumi.Output[str]:
        """
        The secret key to authenitcate with.
        """
        return pulumi.get(self, "secret_key")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[str]]:
        """
        The path to a file that will be read and uploaded as raw bytes for the object content. The path must either be relative to the root module or absolute.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[str]:
        """
        A unique version ID value for the object.
        """
        return pulumi.get(self, "version_id")

    @property
    @pulumi.getter(name="websiteRedirect")
    def website_redirect(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies a target URL for website redirect.
        """
        return pulumi.get(self, "website_redirect")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

