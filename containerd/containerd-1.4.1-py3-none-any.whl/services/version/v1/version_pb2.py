# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containerd/services/version/v1/version.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from containerd.vendor.gogoproto import gogo_pb2 as containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='containerd/services/version/v1/version.proto',
  package='containerd.services.version.v1',
  syntax='proto3',
  serialized_options=b'Z@github.com/containerd/containerd/api/services/version/v1;version',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,containerd/services/version/v1/version.proto\x12\x1e\x63ontainerd.services.version.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a&containerd/vendor/gogoproto/gogo.proto\"4\n\x0fVersionResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x10\n\x08revision\x18\x02 \x01(\t2]\n\x07Version\x12R\n\x07Version\x12\x16.google.protobuf.Empty\x1a/.containerd.services.version.v1.VersionResponseBBZ@github.com/containerd/containerd/api/services/version/v1;versionX\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_VERSIONRESPONSE = _descriptor.Descriptor(
  name='VersionResponse',
  full_name='containerd.services.version.v1.VersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='containerd.services.version.v1.VersionResponse.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='revision', full_name='containerd.services.version.v1.VersionResponse.revision', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=201,
)

DESCRIPTOR.message_types_by_name['VersionResponse'] = _VERSIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VersionResponse = _reflection.GeneratedProtocolMessageType('VersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _VERSIONRESPONSE,
  '__module__' : 'containerd.services.version.v1.version_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.version.v1.VersionResponse)
  })
_sym_db.RegisterMessage(VersionResponse)


DESCRIPTOR._options = None

_VERSION = _descriptor.ServiceDescriptor(
  name='Version',
  full_name='containerd.services.version.v1.Version',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=203,
  serialized_end=296,
  methods=[
  _descriptor.MethodDescriptor(
    name='Version',
    full_name='containerd.services.version.v1.Version.Version',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_VERSIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_VERSION)

DESCRIPTOR.services_by_name['Version'] = _VERSION

# @@protoc_insertion_point(module_scope)
