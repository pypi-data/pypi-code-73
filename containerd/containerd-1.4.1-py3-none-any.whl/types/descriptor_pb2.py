# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containerd/types/descriptor.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from containerd.vendor.gogoproto import gogo_pb2 as containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='containerd/types/descriptor.proto',
  package='containerd.types',
  syntax='proto3',
  serialized_options=b'Z0github.com/containerd/containerd/api/types;types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!containerd/types/descriptor.proto\x12\x10\x63ontainerd.types\x1a&containerd/vendor/gogoproto/gogo.proto\"\xea\x01\n\nDescriptor\x12\x12\n\nmedia_type\x18\x01 \x01(\t\x12\x42\n\x06\x64igest\x18\x02 \x01(\tB2\xda\xde\x1f*github.com/opencontainers/go-digest.Digest\xc8\xde\x1f\x00\x12\x0c\n\x04size\x18\x03 \x01(\x03\x12\x42\n\x0b\x61nnotations\x18\x05 \x03(\x0b\x32-.containerd.types.Descriptor.AnnotationsEntry\x1a\x32\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x32Z0github.com/containerd/containerd/api/types;typesX\x00\x62\x06proto3'
  ,
  dependencies=[containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_DESCRIPTOR_ANNOTATIONSENTRY = _descriptor.Descriptor(
  name='AnnotationsEntry',
  full_name='containerd.types.Descriptor.AnnotationsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='containerd.types.Descriptor.AnnotationsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='containerd.types.Descriptor.AnnotationsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=280,
  serialized_end=330,
)

_DESCRIPTOR = _descriptor.Descriptor(
  name='Descriptor',
  full_name='containerd.types.Descriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='media_type', full_name='containerd.types.Descriptor.media_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='digest', full_name='containerd.types.Descriptor.digest', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037*github.com/opencontainers/go-digest.Digest\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='containerd.types.Descriptor.size', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='containerd.types.Descriptor.annotations', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DESCRIPTOR_ANNOTATIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=330,
)

_DESCRIPTOR_ANNOTATIONSENTRY.containing_type = _DESCRIPTOR
_DESCRIPTOR.fields_by_name['annotations'].message_type = _DESCRIPTOR_ANNOTATIONSENTRY
DESCRIPTOR.message_types_by_name['Descriptor'] = _DESCRIPTOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Descriptor = _reflection.GeneratedProtocolMessageType('Descriptor', (_message.Message,), {

  'AnnotationsEntry' : _reflection.GeneratedProtocolMessageType('AnnotationsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DESCRIPTOR_ANNOTATIONSENTRY,
    '__module__' : 'containerd.types.descriptor_pb2'
    # @@protoc_insertion_point(class_scope:containerd.types.Descriptor.AnnotationsEntry)
    })
  ,
  'DESCRIPTOR' : _DESCRIPTOR,
  '__module__' : 'containerd.types.descriptor_pb2'
  # @@protoc_insertion_point(class_scope:containerd.types.Descriptor)
  })
_sym_db.RegisterMessage(Descriptor)
_sym_db.RegisterMessage(Descriptor.AnnotationsEntry)


DESCRIPTOR._options = None
_DESCRIPTOR_ANNOTATIONSENTRY._options = None
_DESCRIPTOR.fields_by_name['digest']._options = None
# @@protoc_insertion_point(module_scope)
