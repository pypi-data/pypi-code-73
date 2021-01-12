# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['IdentityProvider']


class IdentityProvider(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 add_read_token_role_on_create: Optional[pulumi.Input[bool]] = None,
                 alias: Optional[pulumi.Input[str]] = None,
                 authenticate_by_default: Optional[pulumi.Input[bool]] = None,
                 backchannel_supported: Optional[pulumi.Input[bool]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 first_broker_login_flow_alias: Optional[pulumi.Input[str]] = None,
                 force_authn: Optional[pulumi.Input[bool]] = None,
                 hide_on_login_page: Optional[pulumi.Input[bool]] = None,
                 link_only: Optional[pulumi.Input[bool]] = None,
                 name_id_policy_format: Optional[pulumi.Input[str]] = None,
                 post_binding_authn_request: Optional[pulumi.Input[bool]] = None,
                 post_binding_logout: Optional[pulumi.Input[bool]] = None,
                 post_binding_response: Optional[pulumi.Input[bool]] = None,
                 post_broker_login_flow_alias: Optional[pulumi.Input[str]] = None,
                 realm: Optional[pulumi.Input[str]] = None,
                 signature_algorithm: Optional[pulumi.Input[str]] = None,
                 signing_certificate: Optional[pulumi.Input[str]] = None,
                 single_logout_service_url: Optional[pulumi.Input[str]] = None,
                 single_sign_on_service_url: Optional[pulumi.Input[str]] = None,
                 store_token: Optional[pulumi.Input[bool]] = None,
                 trust_email: Optional[pulumi.Input[bool]] = None,
                 validate_signature: Optional[pulumi.Input[bool]] = None,
                 want_assertions_encrypted: Optional[pulumi.Input[bool]] = None,
                 want_assertions_signed: Optional[pulumi.Input[bool]] = None,
                 xml_sign_key_info_key_name_transformer: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Allows for creating and managing SAML Identity Providers within Keycloak.

        SAML (Security Assertion Markup Language) identity providers allows users to authenticate through a third-party system using the SAML protocol.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="my-realm",
            enabled=True)
        realm_saml_identity_provider = keycloak.saml.IdentityProvider("realmSamlIdentityProvider",
            realm=realm.id,
            alias="my-saml-idp",
            single_sign_on_service_url="https://domain.com/adfs/ls/",
            single_logout_service_url="https://domain.com/adfs/ls/?wa=wsignout1.0",
            backchannel_supported=True,
            post_binding_response=True,
            post_binding_logout=True,
            post_binding_authn_request=True,
            store_token=False,
            trust_email=True,
            force_authn=True)
        ```

        ## Import

        Identity providers can be imported using the format `{{realm_id}}/{{idp_alias}}`, where `idp_alias` is the identity provider alias. Examplebash

        ```sh
         $ pulumi import keycloak:saml/identityProvider:IdentityProvider realm_saml_identity_provider my-realm/my-saml-idp
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] add_read_token_role_on_create: When `true`, new users will be able to read stored tokens. This will automatically assign the `broker.read-token` role. Defaults to `false`.
        :param pulumi.Input[str] alias: The unique name of identity provider.
        :param pulumi.Input[bool] authenticate_by_default: Authenticate users by default. Defaults to `false`.
        :param pulumi.Input[bool] backchannel_supported: Does the external IDP support back-channel logout ?.
        :param pulumi.Input[str] display_name: The display name for the realm that is shown when logging in to the admin console.
        :param pulumi.Input[bool] enabled: When `false`, users and clients will not be able to access this realm. Defaults to `true`.
        :param pulumi.Input[str] first_broker_login_flow_alias: Alias of authentication flow, which is triggered after first login with this identity provider. Term 'First Login' means that there is not yet existing Keycloak account linked with the authenticated identity provider account. Defaults to `first broker login`.
        :param pulumi.Input[bool] force_authn: Indicates whether the identity provider must authenticate the presenter directly rather than rely on a previous security context.
        :param pulumi.Input[bool] hide_on_login_page: If hidden, then login with this provider is possible only if requested explicitly, e.g. using the 'kc_idp_hint' parameter.
        :param pulumi.Input[bool] link_only: When `true`, users cannot login using this provider, but their existing accounts will be linked when possible. Defaults to `false`.
        :param pulumi.Input[str] name_id_policy_format: Specifies the URI reference corresponding to a name identifier format. Defaults to empty.
        :param pulumi.Input[bool] post_binding_authn_request: Indicates whether the AuthnRequest must be sent using HTTP-POST binding. If false, HTTP-REDIRECT binding will be used.
        :param pulumi.Input[bool] post_binding_logout: Indicates whether to respond to requests using HTTP-POST binding. If false, HTTP-REDIRECT binding will be used.
        :param pulumi.Input[bool] post_binding_response: Indicates whether to respond to requests using HTTP-POST binding. If false, HTTP-REDIRECT binding will be used..
        :param pulumi.Input[str] post_broker_login_flow_alias: Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that authenticator implementations must assume that user is already set in ClientSession as identity provider already set it. Defaults to empty.
        :param pulumi.Input[str] realm: The name of the realm. This is unique across Keycloak.
        :param pulumi.Input[str] signature_algorithm: Signing Algorithm. Defaults to empty.
        :param pulumi.Input[str] signing_certificate: Signing Certificate.
        :param pulumi.Input[str] single_logout_service_url: The Url that must be used to send logout requests.
        :param pulumi.Input[str] single_sign_on_service_url: The Url that must be used to send authentication requests (SAML AuthnRequest).
        :param pulumi.Input[bool] store_token: When `true`, tokens will be stored after authenticating users. Defaults to `true`.
        :param pulumi.Input[bool] trust_email: When `true`, email addresses for users in this provider will automatically be verified regardless of the realm's email verification policy. Defaults to `false`.
        :param pulumi.Input[bool] validate_signature: Enable/disable signature validation of SAML responses.
        :param pulumi.Input[bool] want_assertions_encrypted: Indicates whether this service provider expects an encrypted Assertion.
        :param pulumi.Input[bool] want_assertions_signed: Indicates whether this service provider expects a signed Assertion.
        :param pulumi.Input[str] xml_sign_key_info_key_name_transformer: Sign Key Transformer. Defaults to empty.
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

            __props__['add_read_token_role_on_create'] = add_read_token_role_on_create
            if alias is None and not opts.urn:
                raise TypeError("Missing required property 'alias'")
            __props__['alias'] = alias
            __props__['authenticate_by_default'] = authenticate_by_default
            __props__['backchannel_supported'] = backchannel_supported
            __props__['display_name'] = display_name
            __props__['enabled'] = enabled
            __props__['first_broker_login_flow_alias'] = first_broker_login_flow_alias
            __props__['force_authn'] = force_authn
            __props__['hide_on_login_page'] = hide_on_login_page
            __props__['link_only'] = link_only
            __props__['name_id_policy_format'] = name_id_policy_format
            __props__['post_binding_authn_request'] = post_binding_authn_request
            __props__['post_binding_logout'] = post_binding_logout
            __props__['post_binding_response'] = post_binding_response
            __props__['post_broker_login_flow_alias'] = post_broker_login_flow_alias
            if realm is None and not opts.urn:
                raise TypeError("Missing required property 'realm'")
            __props__['realm'] = realm
            __props__['signature_algorithm'] = signature_algorithm
            __props__['signing_certificate'] = signing_certificate
            __props__['single_logout_service_url'] = single_logout_service_url
            if single_sign_on_service_url is None and not opts.urn:
                raise TypeError("Missing required property 'single_sign_on_service_url'")
            __props__['single_sign_on_service_url'] = single_sign_on_service_url
            __props__['store_token'] = store_token
            __props__['trust_email'] = trust_email
            __props__['validate_signature'] = validate_signature
            __props__['want_assertions_encrypted'] = want_assertions_encrypted
            __props__['want_assertions_signed'] = want_assertions_signed
            __props__['xml_sign_key_info_key_name_transformer'] = xml_sign_key_info_key_name_transformer
            __props__['internal_id'] = None
        super(IdentityProvider, __self__).__init__(
            'keycloak:saml/identityProvider:IdentityProvider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            add_read_token_role_on_create: Optional[pulumi.Input[bool]] = None,
            alias: Optional[pulumi.Input[str]] = None,
            authenticate_by_default: Optional[pulumi.Input[bool]] = None,
            backchannel_supported: Optional[pulumi.Input[bool]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            first_broker_login_flow_alias: Optional[pulumi.Input[str]] = None,
            force_authn: Optional[pulumi.Input[bool]] = None,
            hide_on_login_page: Optional[pulumi.Input[bool]] = None,
            internal_id: Optional[pulumi.Input[str]] = None,
            link_only: Optional[pulumi.Input[bool]] = None,
            name_id_policy_format: Optional[pulumi.Input[str]] = None,
            post_binding_authn_request: Optional[pulumi.Input[bool]] = None,
            post_binding_logout: Optional[pulumi.Input[bool]] = None,
            post_binding_response: Optional[pulumi.Input[bool]] = None,
            post_broker_login_flow_alias: Optional[pulumi.Input[str]] = None,
            realm: Optional[pulumi.Input[str]] = None,
            signature_algorithm: Optional[pulumi.Input[str]] = None,
            signing_certificate: Optional[pulumi.Input[str]] = None,
            single_logout_service_url: Optional[pulumi.Input[str]] = None,
            single_sign_on_service_url: Optional[pulumi.Input[str]] = None,
            store_token: Optional[pulumi.Input[bool]] = None,
            trust_email: Optional[pulumi.Input[bool]] = None,
            validate_signature: Optional[pulumi.Input[bool]] = None,
            want_assertions_encrypted: Optional[pulumi.Input[bool]] = None,
            want_assertions_signed: Optional[pulumi.Input[bool]] = None,
            xml_sign_key_info_key_name_transformer: Optional[pulumi.Input[str]] = None) -> 'IdentityProvider':
        """
        Get an existing IdentityProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] add_read_token_role_on_create: When `true`, new users will be able to read stored tokens. This will automatically assign the `broker.read-token` role. Defaults to `false`.
        :param pulumi.Input[str] alias: The unique name of identity provider.
        :param pulumi.Input[bool] authenticate_by_default: Authenticate users by default. Defaults to `false`.
        :param pulumi.Input[bool] backchannel_supported: Does the external IDP support back-channel logout ?.
        :param pulumi.Input[str] display_name: The display name for the realm that is shown when logging in to the admin console.
        :param pulumi.Input[bool] enabled: When `false`, users and clients will not be able to access this realm. Defaults to `true`.
        :param pulumi.Input[str] first_broker_login_flow_alias: Alias of authentication flow, which is triggered after first login with this identity provider. Term 'First Login' means that there is not yet existing Keycloak account linked with the authenticated identity provider account. Defaults to `first broker login`.
        :param pulumi.Input[bool] force_authn: Indicates whether the identity provider must authenticate the presenter directly rather than rely on a previous security context.
        :param pulumi.Input[bool] hide_on_login_page: If hidden, then login with this provider is possible only if requested explicitly, e.g. using the 'kc_idp_hint' parameter.
        :param pulumi.Input[str] internal_id: Internal Identity Provider Id
        :param pulumi.Input[bool] link_only: When `true`, users cannot login using this provider, but their existing accounts will be linked when possible. Defaults to `false`.
        :param pulumi.Input[str] name_id_policy_format: Specifies the URI reference corresponding to a name identifier format. Defaults to empty.
        :param pulumi.Input[bool] post_binding_authn_request: Indicates whether the AuthnRequest must be sent using HTTP-POST binding. If false, HTTP-REDIRECT binding will be used.
        :param pulumi.Input[bool] post_binding_logout: Indicates whether to respond to requests using HTTP-POST binding. If false, HTTP-REDIRECT binding will be used.
        :param pulumi.Input[bool] post_binding_response: Indicates whether to respond to requests using HTTP-POST binding. If false, HTTP-REDIRECT binding will be used..
        :param pulumi.Input[str] post_broker_login_flow_alias: Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that authenticator implementations must assume that user is already set in ClientSession as identity provider already set it. Defaults to empty.
        :param pulumi.Input[str] realm: The name of the realm. This is unique across Keycloak.
        :param pulumi.Input[str] signature_algorithm: Signing Algorithm. Defaults to empty.
        :param pulumi.Input[str] signing_certificate: Signing Certificate.
        :param pulumi.Input[str] single_logout_service_url: The Url that must be used to send logout requests.
        :param pulumi.Input[str] single_sign_on_service_url: The Url that must be used to send authentication requests (SAML AuthnRequest).
        :param pulumi.Input[bool] store_token: When `true`, tokens will be stored after authenticating users. Defaults to `true`.
        :param pulumi.Input[bool] trust_email: When `true`, email addresses for users in this provider will automatically be verified regardless of the realm's email verification policy. Defaults to `false`.
        :param pulumi.Input[bool] validate_signature: Enable/disable signature validation of SAML responses.
        :param pulumi.Input[bool] want_assertions_encrypted: Indicates whether this service provider expects an encrypted Assertion.
        :param pulumi.Input[bool] want_assertions_signed: Indicates whether this service provider expects a signed Assertion.
        :param pulumi.Input[str] xml_sign_key_info_key_name_transformer: Sign Key Transformer. Defaults to empty.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["add_read_token_role_on_create"] = add_read_token_role_on_create
        __props__["alias"] = alias
        __props__["authenticate_by_default"] = authenticate_by_default
        __props__["backchannel_supported"] = backchannel_supported
        __props__["display_name"] = display_name
        __props__["enabled"] = enabled
        __props__["first_broker_login_flow_alias"] = first_broker_login_flow_alias
        __props__["force_authn"] = force_authn
        __props__["hide_on_login_page"] = hide_on_login_page
        __props__["internal_id"] = internal_id
        __props__["link_only"] = link_only
        __props__["name_id_policy_format"] = name_id_policy_format
        __props__["post_binding_authn_request"] = post_binding_authn_request
        __props__["post_binding_logout"] = post_binding_logout
        __props__["post_binding_response"] = post_binding_response
        __props__["post_broker_login_flow_alias"] = post_broker_login_flow_alias
        __props__["realm"] = realm
        __props__["signature_algorithm"] = signature_algorithm
        __props__["signing_certificate"] = signing_certificate
        __props__["single_logout_service_url"] = single_logout_service_url
        __props__["single_sign_on_service_url"] = single_sign_on_service_url
        __props__["store_token"] = store_token
        __props__["trust_email"] = trust_email
        __props__["validate_signature"] = validate_signature
        __props__["want_assertions_encrypted"] = want_assertions_encrypted
        __props__["want_assertions_signed"] = want_assertions_signed
        __props__["xml_sign_key_info_key_name_transformer"] = xml_sign_key_info_key_name_transformer
        return IdentityProvider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addReadTokenRoleOnCreate")
    def add_read_token_role_on_create(self) -> pulumi.Output[Optional[bool]]:
        """
        When `true`, new users will be able to read stored tokens. This will automatically assign the `broker.read-token` role. Defaults to `false`.
        """
        return pulumi.get(self, "add_read_token_role_on_create")

    @property
    @pulumi.getter
    def alias(self) -> pulumi.Output[str]:
        """
        The unique name of identity provider.
        """
        return pulumi.get(self, "alias")

    @property
    @pulumi.getter(name="authenticateByDefault")
    def authenticate_by_default(self) -> pulumi.Output[Optional[bool]]:
        """
        Authenticate users by default. Defaults to `false`.
        """
        return pulumi.get(self, "authenticate_by_default")

    @property
    @pulumi.getter(name="backchannelSupported")
    def backchannel_supported(self) -> pulumi.Output[Optional[bool]]:
        """
        Does the external IDP support back-channel logout ?.
        """
        return pulumi.get(self, "backchannel_supported")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name for the realm that is shown when logging in to the admin console.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        When `false`, users and clients will not be able to access this realm. Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="firstBrokerLoginFlowAlias")
    def first_broker_login_flow_alias(self) -> pulumi.Output[Optional[str]]:
        """
        Alias of authentication flow, which is triggered after first login with this identity provider. Term 'First Login' means that there is not yet existing Keycloak account linked with the authenticated identity provider account. Defaults to `first broker login`.
        """
        return pulumi.get(self, "first_broker_login_flow_alias")

    @property
    @pulumi.getter(name="forceAuthn")
    def force_authn(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the identity provider must authenticate the presenter directly rather than rely on a previous security context.
        """
        return pulumi.get(self, "force_authn")

    @property
    @pulumi.getter(name="hideOnLoginPage")
    def hide_on_login_page(self) -> pulumi.Output[Optional[bool]]:
        """
        If hidden, then login with this provider is possible only if requested explicitly, e.g. using the 'kc_idp_hint' parameter.
        """
        return pulumi.get(self, "hide_on_login_page")

    @property
    @pulumi.getter(name="internalId")
    def internal_id(self) -> pulumi.Output[str]:
        """
        Internal Identity Provider Id
        """
        return pulumi.get(self, "internal_id")

    @property
    @pulumi.getter(name="linkOnly")
    def link_only(self) -> pulumi.Output[Optional[bool]]:
        """
        When `true`, users cannot login using this provider, but their existing accounts will be linked when possible. Defaults to `false`.
        """
        return pulumi.get(self, "link_only")

    @property
    @pulumi.getter(name="nameIdPolicyFormat")
    def name_id_policy_format(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the URI reference corresponding to a name identifier format. Defaults to empty.
        """
        return pulumi.get(self, "name_id_policy_format")

    @property
    @pulumi.getter(name="postBindingAuthnRequest")
    def post_binding_authn_request(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the AuthnRequest must be sent using HTTP-POST binding. If false, HTTP-REDIRECT binding will be used.
        """
        return pulumi.get(self, "post_binding_authn_request")

    @property
    @pulumi.getter(name="postBindingLogout")
    def post_binding_logout(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether to respond to requests using HTTP-POST binding. If false, HTTP-REDIRECT binding will be used.
        """
        return pulumi.get(self, "post_binding_logout")

    @property
    @pulumi.getter(name="postBindingResponse")
    def post_binding_response(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether to respond to requests using HTTP-POST binding. If false, HTTP-REDIRECT binding will be used..
        """
        return pulumi.get(self, "post_binding_response")

    @property
    @pulumi.getter(name="postBrokerLoginFlowAlias")
    def post_broker_login_flow_alias(self) -> pulumi.Output[Optional[str]]:
        """
        Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that authenticator implementations must assume that user is already set in ClientSession as identity provider already set it. Defaults to empty.
        """
        return pulumi.get(self, "post_broker_login_flow_alias")

    @property
    @pulumi.getter
    def realm(self) -> pulumi.Output[str]:
        """
        The name of the realm. This is unique across Keycloak.
        """
        return pulumi.get(self, "realm")

    @property
    @pulumi.getter(name="signatureAlgorithm")
    def signature_algorithm(self) -> pulumi.Output[Optional[str]]:
        """
        Signing Algorithm. Defaults to empty.
        """
        return pulumi.get(self, "signature_algorithm")

    @property
    @pulumi.getter(name="signingCertificate")
    def signing_certificate(self) -> pulumi.Output[Optional[str]]:
        """
        Signing Certificate.
        """
        return pulumi.get(self, "signing_certificate")

    @property
    @pulumi.getter(name="singleLogoutServiceUrl")
    def single_logout_service_url(self) -> pulumi.Output[Optional[str]]:
        """
        The Url that must be used to send logout requests.
        """
        return pulumi.get(self, "single_logout_service_url")

    @property
    @pulumi.getter(name="singleSignOnServiceUrl")
    def single_sign_on_service_url(self) -> pulumi.Output[str]:
        """
        The Url that must be used to send authentication requests (SAML AuthnRequest).
        """
        return pulumi.get(self, "single_sign_on_service_url")

    @property
    @pulumi.getter(name="storeToken")
    def store_token(self) -> pulumi.Output[Optional[bool]]:
        """
        When `true`, tokens will be stored after authenticating users. Defaults to `true`.
        """
        return pulumi.get(self, "store_token")

    @property
    @pulumi.getter(name="trustEmail")
    def trust_email(self) -> pulumi.Output[Optional[bool]]:
        """
        When `true`, email addresses for users in this provider will automatically be verified regardless of the realm's email verification policy. Defaults to `false`.
        """
        return pulumi.get(self, "trust_email")

    @property
    @pulumi.getter(name="validateSignature")
    def validate_signature(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable/disable signature validation of SAML responses.
        """
        return pulumi.get(self, "validate_signature")

    @property
    @pulumi.getter(name="wantAssertionsEncrypted")
    def want_assertions_encrypted(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether this service provider expects an encrypted Assertion.
        """
        return pulumi.get(self, "want_assertions_encrypted")

    @property
    @pulumi.getter(name="wantAssertionsSigned")
    def want_assertions_signed(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether this service provider expects a signed Assertion.
        """
        return pulumi.get(self, "want_assertions_signed")

    @property
    @pulumi.getter(name="xmlSignKeyInfoKeyNameTransformer")
    def xml_sign_key_info_key_name_transformer(self) -> pulumi.Output[Optional[str]]:
        """
        Sign Key Transformer. Defaults to empty.
        """
        return pulumi.get(self, "xml_sign_key_info_key_name_transformer")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

