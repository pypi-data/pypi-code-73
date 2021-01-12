# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admobilize/query/v1alpha1/resources.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='admobilize/query/v1alpha1/resources.proto',
  package='admobilize.query.v1alpha1',
  syntax='proto3',
  serialized_options=b'\n\035com.admobilize.query.v1alpha1B\nQueryProtoP\001Z@bitbucket.org/admobilize/admobilizeapis-go/pkg/queryapi/v1alpha1\242\002\005ADMQY\252\002\031AdMobilize.Query.V1Alpha1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)admobilize/query/v1alpha1/resources.proto\x12\x19\x61\x64mobilize.query.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto\"B\n\x07Project\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x12\n\ncreated_at\x18\x02 \x01(\t\x12\x12\n\nupdated_at\x18\x03 \x01(\t\"r\n\x06Metric\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x66ield\x18\x02 \x01(\t\x12\x11\n\toperation\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x03(\t\x12\r\n\x05order\x18\x05 \x01(\t\x12\x19\n\x11\x63onversion_factor\x18\x06 \x01(\x01\"4\n\x0f\x41ggregateResult\x12\x0e\n\x06metric\x18\x01 \x01(\t\x12\x11\n\toperation\x18\x02 \x01(\t\"?\n\x07\x44\x61taset\x12\r\n\x05label\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\")\n\x0bSchemaField\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"\x80\x01\n\nClassifier\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\toperation\x18\x02 \x01(\t\x12\r\n\x05\x66ield\x18\x03 \x01(\t\x12\x42\n\nconditions\x18\x04 \x03(\x0b\x32..admobilize.query.v1alpha1.ClassifierCondition\"+\n\nOrderField\x12\x0e\n\x06\x63olumn\x18\x01 \x01(\t\x12\r\n\x05order\x18\x02 \x01(\t\"M\n\x13\x43lassifierCondition\x12\x0c\n\x04when\x18\x01 \x01(\t\x12\r\n\x05start\x18\x02 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x03\x12\x0c\n\x04then\x18\x04 \x01(\t\"5\n\x06Status\x12\x13\n\x0bstatus_code\x18\x01 \x01(\t\x12\x16\n\x0estatus_message\x18\x02 \x01(\t\"3\n\tDeviceMap\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x02 \x01(\t\"\xc0\x01\n\x03Job\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x35\n\x06status\x18\x02 \x01(\x0e\x32%.admobilize.query.v1alpha1.Job.Status\x12\x0e\n\x06\x64\x65tail\x18\x03 \x01(\t\x12\x16\n\x0estatus_message\x18\x04 \x01(\t\x12\x11\n\tself_link\x18\x05 \x01(\t\"7\n\x06Status\x12\x0b\n\x07PENDING\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\x08\n\x04\x44ONE\x10\x03\x12\t\n\x05\x45RROR\x10\x04\"\xed\x03\n\x06Report\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x61\x64vertisers\x18\x02 \x03(\t\x12.\n\ncreated_on\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0c\x64\x61ys_to_send\x18\x04 \x03(\t\x12\x12\n\ndevice_ids\x18\x05 \x03(\t\x12\r\n\x05\x65mail\x18\x06 \x03(\t\x12\x0e\n\x06\x66ields\x18\x07 \x03(\t\x12\x0e\n\x06\x66ormat\x18\x08 \x01(\t\x12\x11\n\tfrequency\x18\t \x01(\t\x12\x10\n\x08interval\x18\n \x01(\t\x12-\n\tlast_sent\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\x0flast_report_url\x18\x0c \x01(\t\x12\r\n\x05media\x18\r \x03(\t\x12\x0c\n\x04name\x18\x0e \x01(\t\x12\x12\n\nproject_id\x18\x0f \x01(\t\x12.\n\nstart_date\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_date\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06status\x18\x11 \x01(\t\x12\r\n\x05table\x18\x12 \x01(\t\x12\x10\n\x08timezone\x18\x13 \x01(\t\x12\x0c\n\x04type\x18\x14 \x01(\tB\x93\x01\n\x1d\x63om.admobilize.query.v1alpha1B\nQueryProtoP\x01Z@bitbucket.org/admobilize/admobilizeapis-go/pkg/queryapi/v1alpha1\xa2\x02\x05\x41\x44MQY\xaa\x02\x19\x41\x64Mobilize.Query.V1Alpha1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])



_JOB_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='admobilize.query.v1alpha1.Job.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DONE', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1046,
  serialized_end=1101,
)
_sym_db.RegisterEnumDescriptor(_JOB_STATUS)


_PROJECT = _descriptor.Descriptor(
  name='Project',
  full_name='admobilize.query.v1alpha1.Project',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='admobilize.query.v1alpha1.Project.project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='admobilize.query.v1alpha1.Project.created_at', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='admobilize.query.v1alpha1.Project.updated_at', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=199,
  serialized_end=265,
)


_METRIC = _descriptor.Descriptor(
  name='Metric',
  full_name='admobilize.query.v1alpha1.Metric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='admobilize.query.v1alpha1.Metric.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='field', full_name='admobilize.query.v1alpha1.Metric.field', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operation', full_name='admobilize.query.v1alpha1.Metric.operation', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='admobilize.query.v1alpha1.Metric.filter', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='admobilize.query.v1alpha1.Metric.order', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='conversion_factor', full_name='admobilize.query.v1alpha1.Metric.conversion_factor', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=267,
  serialized_end=381,
)


_AGGREGATERESULT = _descriptor.Descriptor(
  name='AggregateResult',
  full_name='admobilize.query.v1alpha1.AggregateResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metric', full_name='admobilize.query.v1alpha1.AggregateResult.metric', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operation', full_name='admobilize.query.v1alpha1.AggregateResult.operation', index=1,
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
  serialized_start=383,
  serialized_end=435,
)


_DATASET = _descriptor.Descriptor(
  name='Dataset',
  full_name='admobilize.query.v1alpha1.Dataset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='admobilize.query.v1alpha1.Dataset.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='admobilize.query.v1alpha1.Dataset.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=437,
  serialized_end=500,
)


_SCHEMAFIELD = _descriptor.Descriptor(
  name='SchemaField',
  full_name='admobilize.query.v1alpha1.SchemaField',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='admobilize.query.v1alpha1.SchemaField.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='admobilize.query.v1alpha1.SchemaField.type', index=1,
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
  serialized_start=502,
  serialized_end=543,
)


_CLASSIFIER = _descriptor.Descriptor(
  name='Classifier',
  full_name='admobilize.query.v1alpha1.Classifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='admobilize.query.v1alpha1.Classifier.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operation', full_name='admobilize.query.v1alpha1.Classifier.operation', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='field', full_name='admobilize.query.v1alpha1.Classifier.field', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='conditions', full_name='admobilize.query.v1alpha1.Classifier.conditions', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=546,
  serialized_end=674,
)


_ORDERFIELD = _descriptor.Descriptor(
  name='OrderField',
  full_name='admobilize.query.v1alpha1.OrderField',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='column', full_name='admobilize.query.v1alpha1.OrderField.column', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='admobilize.query.v1alpha1.OrderField.order', index=1,
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
  serialized_start=676,
  serialized_end=719,
)


_CLASSIFIERCONDITION = _descriptor.Descriptor(
  name='ClassifierCondition',
  full_name='admobilize.query.v1alpha1.ClassifierCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='when', full_name='admobilize.query.v1alpha1.ClassifierCondition.when', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start', full_name='admobilize.query.v1alpha1.ClassifierCondition.start', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='admobilize.query.v1alpha1.ClassifierCondition.end', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='then', full_name='admobilize.query.v1alpha1.ClassifierCondition.then', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=721,
  serialized_end=798,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='admobilize.query.v1alpha1.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status_code', full_name='admobilize.query.v1alpha1.Status.status_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status_message', full_name='admobilize.query.v1alpha1.Status.status_message', index=1,
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
  serialized_start=800,
  serialized_end=853,
)


_DEVICEMAP = _descriptor.Descriptor(
  name='DeviceMap',
  full_name='admobilize.query.v1alpha1.DeviceMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='admobilize.query.v1alpha1.DeviceMap.device_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_name', full_name='admobilize.query.v1alpha1.DeviceMap.device_name', index=1,
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
  serialized_start=855,
  serialized_end=906,
)


_JOB = _descriptor.Descriptor(
  name='Job',
  full_name='admobilize.query.v1alpha1.Job',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='admobilize.query.v1alpha1.Job.job_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='admobilize.query.v1alpha1.Job.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='detail', full_name='admobilize.query.v1alpha1.Job.detail', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status_message', full_name='admobilize.query.v1alpha1.Job.status_message', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='self_link', full_name='admobilize.query.v1alpha1.Job.self_link', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _JOB_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=909,
  serialized_end=1101,
)


_REPORT = _descriptor.Descriptor(
  name='Report',
  full_name='admobilize.query.v1alpha1.Report',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='admobilize.query.v1alpha1.Report.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='advertisers', full_name='admobilize.query.v1alpha1.Report.advertisers', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_on', full_name='admobilize.query.v1alpha1.Report.created_on', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='days_to_send', full_name='admobilize.query.v1alpha1.Report.days_to_send', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_ids', full_name='admobilize.query.v1alpha1.Report.device_ids', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='admobilize.query.v1alpha1.Report.email', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fields', full_name='admobilize.query.v1alpha1.Report.fields', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='format', full_name='admobilize.query.v1alpha1.Report.format', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frequency', full_name='admobilize.query.v1alpha1.Report.frequency', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='interval', full_name='admobilize.query.v1alpha1.Report.interval', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_sent', full_name='admobilize.query.v1alpha1.Report.last_sent', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_report_url', full_name='admobilize.query.v1alpha1.Report.last_report_url', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='media', full_name='admobilize.query.v1alpha1.Report.media', index=12,
      number=13, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='admobilize.query.v1alpha1.Report.name', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='admobilize.query.v1alpha1.Report.project_id', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='admobilize.query.v1alpha1.Report.start_date', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='admobilize.query.v1alpha1.Report.end_date', index=16,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='admobilize.query.v1alpha1.Report.status', index=17,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='table', full_name='admobilize.query.v1alpha1.Report.table', index=18,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timezone', full_name='admobilize.query.v1alpha1.Report.timezone', index=19,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='admobilize.query.v1alpha1.Report.type', index=20,
      number=20, type=9, cpp_type=9, label=1,
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
  serialized_start=1104,
  serialized_end=1597,
)

_DATASET.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_CLASSIFIER.fields_by_name['conditions'].message_type = _CLASSIFIERCONDITION
_JOB.fields_by_name['status'].enum_type = _JOB_STATUS
_JOB_STATUS.containing_type = _JOB
_REPORT.fields_by_name['created_on'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_REPORT.fields_by_name['last_sent'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_REPORT.fields_by_name['start_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_REPORT.fields_by_name['end_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Project'] = _PROJECT
DESCRIPTOR.message_types_by_name['Metric'] = _METRIC
DESCRIPTOR.message_types_by_name['AggregateResult'] = _AGGREGATERESULT
DESCRIPTOR.message_types_by_name['Dataset'] = _DATASET
DESCRIPTOR.message_types_by_name['SchemaField'] = _SCHEMAFIELD
DESCRIPTOR.message_types_by_name['Classifier'] = _CLASSIFIER
DESCRIPTOR.message_types_by_name['OrderField'] = _ORDERFIELD
DESCRIPTOR.message_types_by_name['ClassifierCondition'] = _CLASSIFIERCONDITION
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['DeviceMap'] = _DEVICEMAP
DESCRIPTOR.message_types_by_name['Job'] = _JOB
DESCRIPTOR.message_types_by_name['Report'] = _REPORT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Project = _reflection.GeneratedProtocolMessageType('Project', (_message.Message,), {
  'DESCRIPTOR' : _PROJECT,
  '__module__' : 'admobilize.query.v1alpha1.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.Project)
  })
_sym_db.RegisterMessage(Project)

Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), {
  'DESCRIPTOR' : _METRIC,
  '__module__' : 'admobilize.query.v1alpha1.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.Metric)
  })
_sym_db.RegisterMessage(Metric)

AggregateResult = _reflection.GeneratedProtocolMessageType('AggregateResult', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATERESULT,
  '__module__' : 'admobilize.query.v1alpha1.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.AggregateResult)
  })
_sym_db.RegisterMessage(AggregateResult)

Dataset = _reflection.GeneratedProtocolMessageType('Dataset', (_message.Message,), {
  'DESCRIPTOR' : _DATASET,
  '__module__' : 'admobilize.query.v1alpha1.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.Dataset)
  })
_sym_db.RegisterMessage(Dataset)

SchemaField = _reflection.GeneratedProtocolMessageType('SchemaField', (_message.Message,), {
  'DESCRIPTOR' : _SCHEMAFIELD,
  '__module__' : 'admobilize.query.v1alpha1.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.SchemaField)
  })
_sym_db.RegisterMessage(SchemaField)

Classifier = _reflection.GeneratedProtocolMessageType('Classifier', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFIER,
  '__module__' : 'admobilize.query.v1alpha1.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.Classifier)
  })
_sym_db.RegisterMessage(Classifier)

OrderField = _reflection.GeneratedProtocolMessageType('OrderField', (_message.Message,), {
  'DESCRIPTOR' : _ORDERFIELD,
  '__module__' : 'admobilize.query.v1alpha1.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.OrderField)
  })
_sym_db.RegisterMessage(OrderField)

ClassifierCondition = _reflection.GeneratedProtocolMessageType('ClassifierCondition', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFIERCONDITION,
  '__module__' : 'admobilize.query.v1alpha1.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.ClassifierCondition)
  })
_sym_db.RegisterMessage(ClassifierCondition)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'admobilize.query.v1alpha1.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.Status)
  })
_sym_db.RegisterMessage(Status)

DeviceMap = _reflection.GeneratedProtocolMessageType('DeviceMap', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEMAP,
  '__module__' : 'admobilize.query.v1alpha1.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.DeviceMap)
  })
_sym_db.RegisterMessage(DeviceMap)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), {
  'DESCRIPTOR' : _JOB,
  '__module__' : 'admobilize.query.v1alpha1.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.Job)
  })
_sym_db.RegisterMessage(Job)

Report = _reflection.GeneratedProtocolMessageType('Report', (_message.Message,), {
  'DESCRIPTOR' : _REPORT,
  '__module__' : 'admobilize.query.v1alpha1.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.Report)
  })
_sym_db.RegisterMessage(Report)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
