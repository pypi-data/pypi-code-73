# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .crypto_key import *
from .crypto_key_iam_binding import *
from .crypto_key_iam_member import *
from .crypto_key_iam_policy import *
from .get_kms_crypto_key import *
from .get_kms_crypto_key_version import *
from .get_kms_key_ring import *
from .get_kms_secret import *
from .get_kms_secret_ciphertext import *
from .key_ring import *
from .key_ring_iam_binding import *
from .key_ring_iam_member import *
from .key_ring_iam_policy import *
from .key_ring_import_job import *
from .registry import *
from .secret_ciphertext import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "gcp:kms/cryptoKey:CryptoKey":
                return CryptoKey(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:kms/cryptoKeyIAMBinding:CryptoKeyIAMBinding":
                return CryptoKeyIAMBinding(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:kms/cryptoKeyIAMMember:CryptoKeyIAMMember":
                return CryptoKeyIAMMember(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:kms/cryptoKeyIAMPolicy:CryptoKeyIAMPolicy":
                return CryptoKeyIAMPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:kms/keyRing:KeyRing":
                return KeyRing(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:kms/keyRingIAMBinding:KeyRingIAMBinding":
                return KeyRingIAMBinding(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:kms/keyRingIAMMember:KeyRingIAMMember":
                return KeyRingIAMMember(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:kms/keyRingIAMPolicy:KeyRingIAMPolicy":
                return KeyRingIAMPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:kms/keyRingImportJob:KeyRingImportJob":
                return KeyRingImportJob(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:kms/registry:Registry":
                return Registry(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:kms/secretCiphertext:SecretCiphertext":
                return SecretCiphertext(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("gcp", "kms/cryptoKey", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "kms/cryptoKeyIAMBinding", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "kms/cryptoKeyIAMMember", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "kms/cryptoKeyIAMPolicy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "kms/keyRing", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "kms/keyRingIAMBinding", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "kms/keyRingIAMMember", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "kms/keyRingIAMPolicy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "kms/keyRingImportJob", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "kms/registry", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "kms/secretCiphertext", _module_instance)

_register_module()
