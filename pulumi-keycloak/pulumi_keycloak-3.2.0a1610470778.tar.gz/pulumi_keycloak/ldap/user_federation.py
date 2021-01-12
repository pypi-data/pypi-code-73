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

__all__ = ['UserFederation']


class UserFederation(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 batch_size_for_sync: Optional[pulumi.Input[int]] = None,
                 bind_credential: Optional[pulumi.Input[str]] = None,
                 bind_dn: Optional[pulumi.Input[str]] = None,
                 cache: Optional[pulumi.Input[pulumi.InputType['UserFederationCacheArgs']]] = None,
                 cache_policy: Optional[pulumi.Input[str]] = None,
                 changed_sync_period: Optional[pulumi.Input[int]] = None,
                 connection_timeout: Optional[pulumi.Input[str]] = None,
                 connection_url: Optional[pulumi.Input[str]] = None,
                 custom_user_search_filter: Optional[pulumi.Input[str]] = None,
                 edit_mode: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 full_sync_period: Optional[pulumi.Input[int]] = None,
                 import_enabled: Optional[pulumi.Input[bool]] = None,
                 kerberos: Optional[pulumi.Input[pulumi.InputType['UserFederationKerberosArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pagination: Optional[pulumi.Input[bool]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 rdn_ldap_attribute: Optional[pulumi.Input[str]] = None,
                 read_timeout: Optional[pulumi.Input[str]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 search_scope: Optional[pulumi.Input[str]] = None,
                 sync_registrations: Optional[pulumi.Input[bool]] = None,
                 use_truststore_spi: Optional[pulumi.Input[str]] = None,
                 user_object_classes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 username_ldap_attribute: Optional[pulumi.Input[str]] = None,
                 users_dn: Optional[pulumi.Input[str]] = None,
                 uuid_ldap_attribute: Optional[pulumi.Input[str]] = None,
                 validate_password_policy: Optional[pulumi.Input[bool]] = None,
                 vendor: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Allows for creating and managing LDAP user federation providers within Keycloak.

        Keycloak can use an LDAP user federation provider to federate users to Keycloak
        from a directory system such as LDAP or Active Directory. Federated users
        will exist within the realm and will be able to log in to clients. Federated
        users can have their attributes defined using mappers.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="my-realm",
            enabled=True)
        ldap_user_federation = keycloak.ldap.UserFederation("ldapUserFederation",
            realm_id=realm.id,
            enabled=True,
            username_ldap_attribute="cn",
            rdn_ldap_attribute="cn",
            uuid_ldap_attribute="entryDN",
            user_object_classes=[
                "simpleSecurityObject",
                "organizationalRole",
            ],
            connection_url="ldap://openldap",
            users_dn="dc=example,dc=org",
            bind_dn="cn=admin,dc=example,dc=org",
            bind_credential="admin",
            connection_timeout="5s",
            read_timeout="10s",
            kerberos=keycloak.ldap.UserFederationKerberosArgs(
                kerberos_realm="FOO.LOCAL",
                server_principal="HTTP/host.foo.com@FOO.LOCAL",
                keytab="/etc/host.keytab",
            ))
        ```

        ## Import

        LDAP user federation providers can be imported using the format `{{realm_id}}/{{ldap_user_federation_id}}`. The ID of the LDAP user federation provider can be found within the Keycloak GUI and is typically a GUIDbash

        ```sh
         $ pulumi import keycloak:ldap/userFederation:UserFederation ldap_user_federation my-realm/af2a6ca3-e4d7-49c3-b08b-1b3c70b4b860
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] batch_size_for_sync: The number of users to sync within a single transaction. Defaults to `1000`.
        :param pulumi.Input[str] bind_credential: Password of LDAP admin. This attribute must be set if `bind_dn` is set.
        :param pulumi.Input[str] bind_dn: DN of LDAP admin, which will be used by Keycloak to access LDAP server. This attribute must be set if `bind_credential` is set.
        :param pulumi.Input[pulumi.InputType['UserFederationCacheArgs']] cache: A block containing the cache settings.
        :param pulumi.Input[str] cache_policy: **Deprecated** Can be one of `DEFAULT`, `EVICT_DAILY`, `EVICT_WEEKLY`, `MAX_LIFESPAN`, or `NO_CACHE`. Defaults to `DEFAULT`.
        :param pulumi.Input[int] changed_sync_period: How frequently Keycloak should sync changed LDAP users, in seconds. Omit this property to disable periodic changed users sync.
        :param pulumi.Input[str] connection_timeout: LDAP connection timeout in the format of a [Go duration string](https://golang.org/pkg/time/#Duration.String).
        :param pulumi.Input[str] connection_url: Connection URL to the LDAP server.
        :param pulumi.Input[str] custom_user_search_filter: Additional LDAP filter for filtering searched users. Must begin with `(` and end with `)`.
        :param pulumi.Input[str] edit_mode: Can be one of `READ_ONLY`, `WRITABLE`, or `UNSYNCED`. `UNSYNCED` allows user data to be imported but not synced back to LDAP. Defaults to `READ_ONLY`.
        :param pulumi.Input[bool] enabled: When `false`, this provider will not be used when performing queries for users. Defaults to `true`.
        :param pulumi.Input[int] full_sync_period: How frequently Keycloak should sync all LDAP users, in seconds. Omit this property to disable periodic full sync.
        :param pulumi.Input[bool] import_enabled: When `true`, LDAP users will be imported into the Keycloak database. Defaults to `true`.
        :param pulumi.Input[pulumi.InputType['UserFederationKerberosArgs']] kerberos: A block containing the kerberos settings.
        :param pulumi.Input[str] name: Display name of the provider when displayed in the console.
        :param pulumi.Input[bool] pagination: When true, Keycloak assumes the LDAP server supports pagination. Defaults to `true`.
        :param pulumi.Input[int] priority: Priority of this provider when looking up users. Lower values are first. Defaults to `0`.
        :param pulumi.Input[str] rdn_ldap_attribute: Name of the LDAP attribute to use as the relative distinguished name.
        :param pulumi.Input[str] read_timeout: LDAP read timeout in the format of a [Go duration string](https://golang.org/pkg/time/#Duration.String).
        :param pulumi.Input[str] realm_id: The realm that this provider will provide user federation for.
        :param pulumi.Input[str] search_scope: Can be one of `ONE_LEVEL` or `SUBTREE`:
               - `ONE_LEVEL`: Only search for users in the DN specified by `user_dn`.
               - `SUBTREE`: Search entire LDAP subtree.
        :param pulumi.Input[bool] sync_registrations: When `true`, newly created users will be synced back to LDAP. Defaults to `false`.
        :param pulumi.Input[str] use_truststore_spi: Can be one of `ALWAYS`, `ONLY_FOR_LDAPS`, or `NEVER`:
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_object_classes: Array of all values of LDAP objectClass attribute for users in LDAP. Must contain at least one.
        :param pulumi.Input[str] username_ldap_attribute: Name of the LDAP attribute to use as the Keycloak username.
        :param pulumi.Input[str] users_dn: Full DN of LDAP tree where your users are.
        :param pulumi.Input[str] uuid_ldap_attribute: Name of the LDAP attribute to use as a unique object identifier for objects in LDAP.
        :param pulumi.Input[bool] validate_password_policy: When `true`, Keycloak will validate passwords using the realm policy before updating it.
        :param pulumi.Input[str] vendor: Can be one of `OTHER`, `EDIRECTORY`, `AD`, `RHDS`, or `TIVOLI`. When this is selected in the GUI, it provides reasonable defaults for other fields. When used with the Keycloak API, this attribute does nothing, but is still required. Defaults to `OTHER`.
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

            __props__['batch_size_for_sync'] = batch_size_for_sync
            __props__['bind_credential'] = bind_credential
            __props__['bind_dn'] = bind_dn
            __props__['cache'] = cache
            if cache_policy is not None and not opts.urn:
                warnings.warn("""use cache.policy instead""", DeprecationWarning)
                pulumi.log.warn("cache_policy is deprecated: use cache.policy instead")
            __props__['cache_policy'] = cache_policy
            __props__['changed_sync_period'] = changed_sync_period
            __props__['connection_timeout'] = connection_timeout
            if connection_url is None and not opts.urn:
                raise TypeError("Missing required property 'connection_url'")
            __props__['connection_url'] = connection_url
            __props__['custom_user_search_filter'] = custom_user_search_filter
            __props__['edit_mode'] = edit_mode
            __props__['enabled'] = enabled
            __props__['full_sync_period'] = full_sync_period
            __props__['import_enabled'] = import_enabled
            __props__['kerberos'] = kerberos
            __props__['name'] = name
            __props__['pagination'] = pagination
            __props__['priority'] = priority
            if rdn_ldap_attribute is None and not opts.urn:
                raise TypeError("Missing required property 'rdn_ldap_attribute'")
            __props__['rdn_ldap_attribute'] = rdn_ldap_attribute
            __props__['read_timeout'] = read_timeout
            if realm_id is None and not opts.urn:
                raise TypeError("Missing required property 'realm_id'")
            __props__['realm_id'] = realm_id
            __props__['search_scope'] = search_scope
            __props__['sync_registrations'] = sync_registrations
            __props__['use_truststore_spi'] = use_truststore_spi
            if user_object_classes is None and not opts.urn:
                raise TypeError("Missing required property 'user_object_classes'")
            __props__['user_object_classes'] = user_object_classes
            if username_ldap_attribute is None and not opts.urn:
                raise TypeError("Missing required property 'username_ldap_attribute'")
            __props__['username_ldap_attribute'] = username_ldap_attribute
            if users_dn is None and not opts.urn:
                raise TypeError("Missing required property 'users_dn'")
            __props__['users_dn'] = users_dn
            if uuid_ldap_attribute is None and not opts.urn:
                raise TypeError("Missing required property 'uuid_ldap_attribute'")
            __props__['uuid_ldap_attribute'] = uuid_ldap_attribute
            __props__['validate_password_policy'] = validate_password_policy
            __props__['vendor'] = vendor
        super(UserFederation, __self__).__init__(
            'keycloak:ldap/userFederation:UserFederation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            batch_size_for_sync: Optional[pulumi.Input[int]] = None,
            bind_credential: Optional[pulumi.Input[str]] = None,
            bind_dn: Optional[pulumi.Input[str]] = None,
            cache: Optional[pulumi.Input[pulumi.InputType['UserFederationCacheArgs']]] = None,
            cache_policy: Optional[pulumi.Input[str]] = None,
            changed_sync_period: Optional[pulumi.Input[int]] = None,
            connection_timeout: Optional[pulumi.Input[str]] = None,
            connection_url: Optional[pulumi.Input[str]] = None,
            custom_user_search_filter: Optional[pulumi.Input[str]] = None,
            edit_mode: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            full_sync_period: Optional[pulumi.Input[int]] = None,
            import_enabled: Optional[pulumi.Input[bool]] = None,
            kerberos: Optional[pulumi.Input[pulumi.InputType['UserFederationKerberosArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            pagination: Optional[pulumi.Input[bool]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            rdn_ldap_attribute: Optional[pulumi.Input[str]] = None,
            read_timeout: Optional[pulumi.Input[str]] = None,
            realm_id: Optional[pulumi.Input[str]] = None,
            search_scope: Optional[pulumi.Input[str]] = None,
            sync_registrations: Optional[pulumi.Input[bool]] = None,
            use_truststore_spi: Optional[pulumi.Input[str]] = None,
            user_object_classes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            username_ldap_attribute: Optional[pulumi.Input[str]] = None,
            users_dn: Optional[pulumi.Input[str]] = None,
            uuid_ldap_attribute: Optional[pulumi.Input[str]] = None,
            validate_password_policy: Optional[pulumi.Input[bool]] = None,
            vendor: Optional[pulumi.Input[str]] = None) -> 'UserFederation':
        """
        Get an existing UserFederation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] batch_size_for_sync: The number of users to sync within a single transaction. Defaults to `1000`.
        :param pulumi.Input[str] bind_credential: Password of LDAP admin. This attribute must be set if `bind_dn` is set.
        :param pulumi.Input[str] bind_dn: DN of LDAP admin, which will be used by Keycloak to access LDAP server. This attribute must be set if `bind_credential` is set.
        :param pulumi.Input[pulumi.InputType['UserFederationCacheArgs']] cache: A block containing the cache settings.
        :param pulumi.Input[str] cache_policy: **Deprecated** Can be one of `DEFAULT`, `EVICT_DAILY`, `EVICT_WEEKLY`, `MAX_LIFESPAN`, or `NO_CACHE`. Defaults to `DEFAULT`.
        :param pulumi.Input[int] changed_sync_period: How frequently Keycloak should sync changed LDAP users, in seconds. Omit this property to disable periodic changed users sync.
        :param pulumi.Input[str] connection_timeout: LDAP connection timeout in the format of a [Go duration string](https://golang.org/pkg/time/#Duration.String).
        :param pulumi.Input[str] connection_url: Connection URL to the LDAP server.
        :param pulumi.Input[str] custom_user_search_filter: Additional LDAP filter for filtering searched users. Must begin with `(` and end with `)`.
        :param pulumi.Input[str] edit_mode: Can be one of `READ_ONLY`, `WRITABLE`, or `UNSYNCED`. `UNSYNCED` allows user data to be imported but not synced back to LDAP. Defaults to `READ_ONLY`.
        :param pulumi.Input[bool] enabled: When `false`, this provider will not be used when performing queries for users. Defaults to `true`.
        :param pulumi.Input[int] full_sync_period: How frequently Keycloak should sync all LDAP users, in seconds. Omit this property to disable periodic full sync.
        :param pulumi.Input[bool] import_enabled: When `true`, LDAP users will be imported into the Keycloak database. Defaults to `true`.
        :param pulumi.Input[pulumi.InputType['UserFederationKerberosArgs']] kerberos: A block containing the kerberos settings.
        :param pulumi.Input[str] name: Display name of the provider when displayed in the console.
        :param pulumi.Input[bool] pagination: When true, Keycloak assumes the LDAP server supports pagination. Defaults to `true`.
        :param pulumi.Input[int] priority: Priority of this provider when looking up users. Lower values are first. Defaults to `0`.
        :param pulumi.Input[str] rdn_ldap_attribute: Name of the LDAP attribute to use as the relative distinguished name.
        :param pulumi.Input[str] read_timeout: LDAP read timeout in the format of a [Go duration string](https://golang.org/pkg/time/#Duration.String).
        :param pulumi.Input[str] realm_id: The realm that this provider will provide user federation for.
        :param pulumi.Input[str] search_scope: Can be one of `ONE_LEVEL` or `SUBTREE`:
               - `ONE_LEVEL`: Only search for users in the DN specified by `user_dn`.
               - `SUBTREE`: Search entire LDAP subtree.
        :param pulumi.Input[bool] sync_registrations: When `true`, newly created users will be synced back to LDAP. Defaults to `false`.
        :param pulumi.Input[str] use_truststore_spi: Can be one of `ALWAYS`, `ONLY_FOR_LDAPS`, or `NEVER`:
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_object_classes: Array of all values of LDAP objectClass attribute for users in LDAP. Must contain at least one.
        :param pulumi.Input[str] username_ldap_attribute: Name of the LDAP attribute to use as the Keycloak username.
        :param pulumi.Input[str] users_dn: Full DN of LDAP tree where your users are.
        :param pulumi.Input[str] uuid_ldap_attribute: Name of the LDAP attribute to use as a unique object identifier for objects in LDAP.
        :param pulumi.Input[bool] validate_password_policy: When `true`, Keycloak will validate passwords using the realm policy before updating it.
        :param pulumi.Input[str] vendor: Can be one of `OTHER`, `EDIRECTORY`, `AD`, `RHDS`, or `TIVOLI`. When this is selected in the GUI, it provides reasonable defaults for other fields. When used with the Keycloak API, this attribute does nothing, but is still required. Defaults to `OTHER`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["batch_size_for_sync"] = batch_size_for_sync
        __props__["bind_credential"] = bind_credential
        __props__["bind_dn"] = bind_dn
        __props__["cache"] = cache
        __props__["cache_policy"] = cache_policy
        __props__["changed_sync_period"] = changed_sync_period
        __props__["connection_timeout"] = connection_timeout
        __props__["connection_url"] = connection_url
        __props__["custom_user_search_filter"] = custom_user_search_filter
        __props__["edit_mode"] = edit_mode
        __props__["enabled"] = enabled
        __props__["full_sync_period"] = full_sync_period
        __props__["import_enabled"] = import_enabled
        __props__["kerberos"] = kerberos
        __props__["name"] = name
        __props__["pagination"] = pagination
        __props__["priority"] = priority
        __props__["rdn_ldap_attribute"] = rdn_ldap_attribute
        __props__["read_timeout"] = read_timeout
        __props__["realm_id"] = realm_id
        __props__["search_scope"] = search_scope
        __props__["sync_registrations"] = sync_registrations
        __props__["use_truststore_spi"] = use_truststore_spi
        __props__["user_object_classes"] = user_object_classes
        __props__["username_ldap_attribute"] = username_ldap_attribute
        __props__["users_dn"] = users_dn
        __props__["uuid_ldap_attribute"] = uuid_ldap_attribute
        __props__["validate_password_policy"] = validate_password_policy
        __props__["vendor"] = vendor
        return UserFederation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="batchSizeForSync")
    def batch_size_for_sync(self) -> pulumi.Output[Optional[int]]:
        """
        The number of users to sync within a single transaction. Defaults to `1000`.
        """
        return pulumi.get(self, "batch_size_for_sync")

    @property
    @pulumi.getter(name="bindCredential")
    def bind_credential(self) -> pulumi.Output[Optional[str]]:
        """
        Password of LDAP admin. This attribute must be set if `bind_dn` is set.
        """
        return pulumi.get(self, "bind_credential")

    @property
    @pulumi.getter(name="bindDn")
    def bind_dn(self) -> pulumi.Output[Optional[str]]:
        """
        DN of LDAP admin, which will be used by Keycloak to access LDAP server. This attribute must be set if `bind_credential` is set.
        """
        return pulumi.get(self, "bind_dn")

    @property
    @pulumi.getter
    def cache(self) -> pulumi.Output[Optional['outputs.UserFederationCache']]:
        """
        A block containing the cache settings.
        """
        return pulumi.get(self, "cache")

    @property
    @pulumi.getter(name="cachePolicy")
    def cache_policy(self) -> pulumi.Output[Optional[str]]:
        """
        **Deprecated** Can be one of `DEFAULT`, `EVICT_DAILY`, `EVICT_WEEKLY`, `MAX_LIFESPAN`, or `NO_CACHE`. Defaults to `DEFAULT`.
        """
        return pulumi.get(self, "cache_policy")

    @property
    @pulumi.getter(name="changedSyncPeriod")
    def changed_sync_period(self) -> pulumi.Output[Optional[int]]:
        """
        How frequently Keycloak should sync changed LDAP users, in seconds. Omit this property to disable periodic changed users sync.
        """
        return pulumi.get(self, "changed_sync_period")

    @property
    @pulumi.getter(name="connectionTimeout")
    def connection_timeout(self) -> pulumi.Output[Optional[str]]:
        """
        LDAP connection timeout in the format of a [Go duration string](https://golang.org/pkg/time/#Duration.String).
        """
        return pulumi.get(self, "connection_timeout")

    @property
    @pulumi.getter(name="connectionUrl")
    def connection_url(self) -> pulumi.Output[str]:
        """
        Connection URL to the LDAP server.
        """
        return pulumi.get(self, "connection_url")

    @property
    @pulumi.getter(name="customUserSearchFilter")
    def custom_user_search_filter(self) -> pulumi.Output[Optional[str]]:
        """
        Additional LDAP filter for filtering searched users. Must begin with `(` and end with `)`.
        """
        return pulumi.get(self, "custom_user_search_filter")

    @property
    @pulumi.getter(name="editMode")
    def edit_mode(self) -> pulumi.Output[Optional[str]]:
        """
        Can be one of `READ_ONLY`, `WRITABLE`, or `UNSYNCED`. `UNSYNCED` allows user data to be imported but not synced back to LDAP. Defaults to `READ_ONLY`.
        """
        return pulumi.get(self, "edit_mode")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        When `false`, this provider will not be used when performing queries for users. Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="fullSyncPeriod")
    def full_sync_period(self) -> pulumi.Output[Optional[int]]:
        """
        How frequently Keycloak should sync all LDAP users, in seconds. Omit this property to disable periodic full sync.
        """
        return pulumi.get(self, "full_sync_period")

    @property
    @pulumi.getter(name="importEnabled")
    def import_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        When `true`, LDAP users will be imported into the Keycloak database. Defaults to `true`.
        """
        return pulumi.get(self, "import_enabled")

    @property
    @pulumi.getter
    def kerberos(self) -> pulumi.Output[Optional['outputs.UserFederationKerberos']]:
        """
        A block containing the kerberos settings.
        """
        return pulumi.get(self, "kerberos")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Display name of the provider when displayed in the console.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def pagination(self) -> pulumi.Output[Optional[bool]]:
        """
        When true, Keycloak assumes the LDAP server supports pagination. Defaults to `true`.
        """
        return pulumi.get(self, "pagination")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        Priority of this provider when looking up users. Lower values are first. Defaults to `0`.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="rdnLdapAttribute")
    def rdn_ldap_attribute(self) -> pulumi.Output[str]:
        """
        Name of the LDAP attribute to use as the relative distinguished name.
        """
        return pulumi.get(self, "rdn_ldap_attribute")

    @property
    @pulumi.getter(name="readTimeout")
    def read_timeout(self) -> pulumi.Output[Optional[str]]:
        """
        LDAP read timeout in the format of a [Go duration string](https://golang.org/pkg/time/#Duration.String).
        """
        return pulumi.get(self, "read_timeout")

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> pulumi.Output[str]:
        """
        The realm that this provider will provide user federation for.
        """
        return pulumi.get(self, "realm_id")

    @property
    @pulumi.getter(name="searchScope")
    def search_scope(self) -> pulumi.Output[Optional[str]]:
        """
        Can be one of `ONE_LEVEL` or `SUBTREE`:
        - `ONE_LEVEL`: Only search for users in the DN specified by `user_dn`.
        - `SUBTREE`: Search entire LDAP subtree.
        """
        return pulumi.get(self, "search_scope")

    @property
    @pulumi.getter(name="syncRegistrations")
    def sync_registrations(self) -> pulumi.Output[Optional[bool]]:
        """
        When `true`, newly created users will be synced back to LDAP. Defaults to `false`.
        """
        return pulumi.get(self, "sync_registrations")

    @property
    @pulumi.getter(name="useTruststoreSpi")
    def use_truststore_spi(self) -> pulumi.Output[Optional[str]]:
        """
        Can be one of `ALWAYS`, `ONLY_FOR_LDAPS`, or `NEVER`:
        """
        return pulumi.get(self, "use_truststore_spi")

    @property
    @pulumi.getter(name="userObjectClasses")
    def user_object_classes(self) -> pulumi.Output[Sequence[str]]:
        """
        Array of all values of LDAP objectClass attribute for users in LDAP. Must contain at least one.
        """
        return pulumi.get(self, "user_object_classes")

    @property
    @pulumi.getter(name="usernameLdapAttribute")
    def username_ldap_attribute(self) -> pulumi.Output[str]:
        """
        Name of the LDAP attribute to use as the Keycloak username.
        """
        return pulumi.get(self, "username_ldap_attribute")

    @property
    @pulumi.getter(name="usersDn")
    def users_dn(self) -> pulumi.Output[str]:
        """
        Full DN of LDAP tree where your users are.
        """
        return pulumi.get(self, "users_dn")

    @property
    @pulumi.getter(name="uuidLdapAttribute")
    def uuid_ldap_attribute(self) -> pulumi.Output[str]:
        """
        Name of the LDAP attribute to use as a unique object identifier for objects in LDAP.
        """
        return pulumi.get(self, "uuid_ldap_attribute")

    @property
    @pulumi.getter(name="validatePasswordPolicy")
    def validate_password_policy(self) -> pulumi.Output[Optional[bool]]:
        """
        When `true`, Keycloak will validate passwords using the realm policy before updating it.
        """
        return pulumi.get(self, "validate_password_policy")

    @property
    @pulumi.getter
    def vendor(self) -> pulumi.Output[Optional[str]]:
        """
        Can be one of `OTHER`, `EDIRECTORY`, `AD`, `RHDS`, or `TIVOLI`. When this is selected in the GUI, it provides reasonable defaults for other fields. When used with the Keycloak API, this attribute does nothing, but is still required. Defaults to `OTHER`.
        """
        return pulumi.get(self, "vendor")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

