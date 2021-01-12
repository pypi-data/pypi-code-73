# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['Domain']


class Domain(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 axfr_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 expire_sec: Optional[pulumi.Input[int]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 master_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 refresh_sec: Optional[pulumi.Input[int]] = None,
                 retry_sec: Optional[pulumi.Input[int]] = None,
                 soa_email: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ttl_sec: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Linode Domain resource.  This can be used to create, modify, and delete Linode Domains through Linode's managed DNS service.
        For more information, see [DNS Manager](https://www.linode.com/docs/platform/manager/dns-manager/) and the [Linode APIv4 docs](https://developers.linode.com/api/v4#operation/createDomain).

        ## Example Usage

        The following example shows how one might use this resource to configure a Domain Record attached to a Linode Domain.

        ```python
        import pulumi
        import pulumi_linode as linode

        foobar_domain = linode.Domain("foobarDomain",
            domain="foobar.example",
            soa_email="example@foobar.example",
            tags=[
                "foo",
                "bar",
            ],
            type="master")
        foobar_domain_record = linode.DomainRecord("foobarDomainRecord",
            domain_id=foobar_domain.id,
            name="www",
            record_type="CNAME",
            target="foobar.example")
        ```
        ## Attributes

        This resource exports no additional attributes, however `status` may reflect degraded states.

        ## Import

        Linodes Domains can be imported using the Linode Domain `id`, e.g.

        ```sh
         $ pulumi import linode:index/domain:Domain foobar 1234567
        ```

         The Linode Guide, [Import Existing Infrastructure to Terraform](https://www.linode.com/docs/applications/configuration-management/import-existing-infrastructure-to-terraform/), offers resource importing examples for Domains and other Linode resource types.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] axfr_ips: The list of IPs that may perform a zone transfer for this Domain. This is potentially dangerous, and should be set to an empty list unless you intend to use it.
        :param pulumi.Input[str] description: A description for this Domain. This is for display purposes only.
        :param pulumi.Input[str] domain: The domain this Domain represents. These must be unique in our system; you cannot have two Domains representing the same domain.
        :param pulumi.Input[int] expire_sec: The amount of time in seconds that may pass before this Domain is no longer authoritative. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.
        :param pulumi.Input[str] group: The group this Domain belongs to. This is for display purposes only.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] master_ips: The IP addresses representing the master DNS for this Domain.
        :param pulumi.Input[int] refresh_sec: The amount of time in seconds before this Domain should be refreshed. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.
        :param pulumi.Input[int] retry_sec: The interval, in seconds, at which a failed refresh should be retried. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.
        :param pulumi.Input[str] soa_email: Start of Authority email address. This is required for master Domains.
        :param pulumi.Input[str] status: Used to control whether this Domain is currently being rendered (defaults to "active").
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of tags applied to this object. Tags are for organizational purposes only.
        :param pulumi.Input[int] ttl_sec: 'Time to Live' - the amount of time in seconds that this Domain's records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.
        :param pulumi.Input[str] type: If this Domain represents the authoritative source of information for the domain it describes, or if it is a read-only copy of a master (also called a slave).
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

            __props__['axfr_ips'] = axfr_ips
            __props__['description'] = description
            if domain is None and not opts.urn:
                raise TypeError("Missing required property 'domain'")
            __props__['domain'] = domain
            __props__['expire_sec'] = expire_sec
            __props__['group'] = group
            __props__['master_ips'] = master_ips
            __props__['refresh_sec'] = refresh_sec
            __props__['retry_sec'] = retry_sec
            __props__['soa_email'] = soa_email
            __props__['status'] = status
            __props__['tags'] = tags
            __props__['ttl_sec'] = ttl_sec
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
        super(Domain, __self__).__init__(
            'linode:index/domain:Domain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            axfr_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            expire_sec: Optional[pulumi.Input[int]] = None,
            group: Optional[pulumi.Input[str]] = None,
            master_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            refresh_sec: Optional[pulumi.Input[int]] = None,
            retry_sec: Optional[pulumi.Input[int]] = None,
            soa_email: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            ttl_sec: Optional[pulumi.Input[int]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Domain':
        """
        Get an existing Domain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] axfr_ips: The list of IPs that may perform a zone transfer for this Domain. This is potentially dangerous, and should be set to an empty list unless you intend to use it.
        :param pulumi.Input[str] description: A description for this Domain. This is for display purposes only.
        :param pulumi.Input[str] domain: The domain this Domain represents. These must be unique in our system; you cannot have two Domains representing the same domain.
        :param pulumi.Input[int] expire_sec: The amount of time in seconds that may pass before this Domain is no longer authoritative. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.
        :param pulumi.Input[str] group: The group this Domain belongs to. This is for display purposes only.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] master_ips: The IP addresses representing the master DNS for this Domain.
        :param pulumi.Input[int] refresh_sec: The amount of time in seconds before this Domain should be refreshed. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.
        :param pulumi.Input[int] retry_sec: The interval, in seconds, at which a failed refresh should be retried. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.
        :param pulumi.Input[str] soa_email: Start of Authority email address. This is required for master Domains.
        :param pulumi.Input[str] status: Used to control whether this Domain is currently being rendered (defaults to "active").
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of tags applied to this object. Tags are for organizational purposes only.
        :param pulumi.Input[int] ttl_sec: 'Time to Live' - the amount of time in seconds that this Domain's records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.
        :param pulumi.Input[str] type: If this Domain represents the authoritative source of information for the domain it describes, or if it is a read-only copy of a master (also called a slave).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["axfr_ips"] = axfr_ips
        __props__["description"] = description
        __props__["domain"] = domain
        __props__["expire_sec"] = expire_sec
        __props__["group"] = group
        __props__["master_ips"] = master_ips
        __props__["refresh_sec"] = refresh_sec
        __props__["retry_sec"] = retry_sec
        __props__["soa_email"] = soa_email
        __props__["status"] = status
        __props__["tags"] = tags
        __props__["ttl_sec"] = ttl_sec
        __props__["type"] = type
        return Domain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="axfrIps")
    def axfr_ips(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of IPs that may perform a zone transfer for this Domain. This is potentially dangerous, and should be set to an empty list unless you intend to use it.
        """
        return pulumi.get(self, "axfr_ips")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for this Domain. This is for display purposes only.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        """
        The domain this Domain represents. These must be unique in our system; you cannot have two Domains representing the same domain.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="expireSec")
    def expire_sec(self) -> pulumi.Output[Optional[int]]:
        """
        The amount of time in seconds that may pass before this Domain is no longer authoritative. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.
        """
        return pulumi.get(self, "expire_sec")

    @property
    @pulumi.getter
    def group(self) -> pulumi.Output[Optional[str]]:
        """
        The group this Domain belongs to. This is for display purposes only.
        """
        return pulumi.get(self, "group")

    @property
    @pulumi.getter(name="masterIps")
    def master_ips(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The IP addresses representing the master DNS for this Domain.
        """
        return pulumi.get(self, "master_ips")

    @property
    @pulumi.getter(name="refreshSec")
    def refresh_sec(self) -> pulumi.Output[Optional[int]]:
        """
        The amount of time in seconds before this Domain should be refreshed. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.
        """
        return pulumi.get(self, "refresh_sec")

    @property
    @pulumi.getter(name="retrySec")
    def retry_sec(self) -> pulumi.Output[Optional[int]]:
        """
        The interval, in seconds, at which a failed refresh should be retried. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.
        """
        return pulumi.get(self, "retry_sec")

    @property
    @pulumi.getter(name="soaEmail")
    def soa_email(self) -> pulumi.Output[Optional[str]]:
        """
        Start of Authority email address. This is required for master Domains.
        """
        return pulumi.get(self, "soa_email")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Used to control whether this Domain is currently being rendered (defaults to "active").
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of tags applied to this object. Tags are for organizational purposes only.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="ttlSec")
    def ttl_sec(self) -> pulumi.Output[Optional[int]]:
        """
        'Time to Live' - the amount of time in seconds that this Domain's records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.
        """
        return pulumi.get(self, "ttl_sec")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        If this Domain represents the authoritative source of information for the domain it describes, or if it is a read-only copy of a master (also called a slave).
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

