# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exabel/api/data/v1/entity_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2

from exabel_data_sdk.stubs.exabel.api.data.v1 import (
    entity_messages_pb2 as exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2,
)
from exabel_data_sdk.stubs.exabel.api.data.v1 import (
    search_messages_pb2 as exabel_dot_api_dot_data_dot_v1_dot_search__messages__pb2,
)
from exabel_data_sdk.stubs.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="exabel/api/data/v1/entity_service.proto",
    package="exabel.api.data.v1",
    syntax="proto3",
    serialized_options=b"\n\026com.exabel.api.data.v1B\022EntityServiceProtoP\001",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\'exabel/api/data/v1/entity_service.proto\x12\x12\x65xabel.api.data.v1\x1a(exabel/api/data/v1/entity_messages.proto\x1a(exabel/api/data/v1/search_messages.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"?\n\x16ListEntityTypesRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t"|\n\x17ListEntityTypesResponse\x12\x34\n\x0c\x65ntity_types\x18\x01 \x03(\x0b\x32\x1e.exabel.api.data.v1.EntityType\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"$\n\x14GetEntityTypeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"L\n\x13ListEntitiesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"q\n\x14ListEntitiesResponse\x12,\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\x1a.exabel.api.data.v1.Entity\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05" \n\x10GetEntityRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"Q\n\x13\x43reateEntityRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12*\n\x06\x65ntity\x18\x02 \x01(\x0b\x32\x1a.exabel.api.data.v1.Entity"r\n\x13UpdateEntityRequest\x12*\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x1a.exabel.api.data.v1.Entity\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask"#\n\x13\x44\x65leteEntityRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"}\n\x15SearchEntitiesRequest\x12\x0e\n\x06parent\x18\x04 \x01(\t\x12-\n\x05terms\x18\x01 \x03(\x0b\x32\x1e.exabel.api.data.v1.SearchTerm\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"_\n\x16SearchEntitiesResponse\x12,\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\x1a.exabel.api.data.v1.Entity\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xdb\x08\n\rEntityService\x12\x83\x01\n\x0fListEntityTypes\x12*.exabel.api.data.v1.ListEntityTypesRequest\x1a+.exabel.api.data.v1.ListEntityTypesResponse"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1/entityTypes\x12{\n\rGetEntityType\x12(.exabel.api.data.v1.GetEntityTypeRequest\x1a\x1e.exabel.api.data.v1.EntityType" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/{name=entityTypes/*}\x12\x8e\x01\n\x0cListEntities\x12\'.exabel.api.data.v1.ListEntitiesRequest\x1a(.exabel.api.data.v1.ListEntitiesResponse"+\x82\xd3\xe4\x93\x02%\x12#/v1/{parent=entityTypes/*}/entities\x12z\n\tGetEntity\x12$.exabel.api.data.v1.GetEntityRequest\x1a\x1a.exabel.api.data.v1.Entity"+\x82\xd3\xe4\x93\x02%\x12#/v1/{name=entityTypes/*/entities/*}\x12\x88\x01\n\x0c\x43reateEntity\x12\'.exabel.api.data.v1.CreateEntityRequest\x1a\x1a.exabel.api.data.v1.Entity"3\x82\xd3\xe4\x93\x02-"#/v1/{parent=entityTypes/*}/entities:\x06\x65ntity\x12\x8f\x01\n\x0cUpdateEntity\x12\'.exabel.api.data.v1.UpdateEntityRequest\x1a\x1a.exabel.api.data.v1.Entity":\x82\xd3\xe4\x93\x02\x34\x32*/v1/{entity.name=entityTypes/*/entities/*}:\x06\x65ntity\x12|\n\x0c\x44\x65leteEntity\x12\'.exabel.api.data.v1.DeleteEntityRequest\x1a\x16.google.protobuf.Empty"+\x82\xd3\xe4\x93\x02%*#/v1/{name=entityTypes/*/entities/*}\x12\x9e\x01\n\x0eSearchEntities\x12).exabel.api.data.v1.SearchEntitiesRequest\x1a*.exabel.api.data.v1.SearchEntitiesResponse"5\x82\xd3\xe4\x93\x02/"*/v1/{parent=entityTypes/*}/entities:search:\x01*B.\n\x16\x63om.exabel.api.data.v1B\x12\x45ntityServiceProtoP\x01\x62\x06proto3',
    dependencies=[
        exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2.DESCRIPTOR,
        exabel_dot_api_dot_data_dot_v1_dot_search__messages__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,
    ],
)


_LISTENTITYTYPESREQUEST = _descriptor.Descriptor(
    name="ListEntityTypesRequest",
    full_name="exabel.api.data.v1.ListEntityTypesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="page_size",
            full_name="exabel.api.data.v1.ListEntityTypesRequest.page_size",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="page_token",
            full_name="exabel.api.data.v1.ListEntityTypesRequest.page_token",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=240,
    serialized_end=303,
)


_LISTENTITYTYPESRESPONSE = _descriptor.Descriptor(
    name="ListEntityTypesResponse",
    full_name="exabel.api.data.v1.ListEntityTypesResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="entity_types",
            full_name="exabel.api.data.v1.ListEntityTypesResponse.entity_types",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="next_page_token",
            full_name="exabel.api.data.v1.ListEntityTypesResponse.next_page_token",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="total_size",
            full_name="exabel.api.data.v1.ListEntityTypesResponse.total_size",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=305,
    serialized_end=429,
)


_GETENTITYTYPEREQUEST = _descriptor.Descriptor(
    name="GetEntityTypeRequest",
    full_name="exabel.api.data.v1.GetEntityTypeRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="exabel.api.data.v1.GetEntityTypeRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=431,
    serialized_end=467,
)


_LISTENTITIESREQUEST = _descriptor.Descriptor(
    name="ListEntitiesRequest",
    full_name="exabel.api.data.v1.ListEntitiesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="exabel.api.data.v1.ListEntitiesRequest.parent",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="page_size",
            full_name="exabel.api.data.v1.ListEntitiesRequest.page_size",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="page_token",
            full_name="exabel.api.data.v1.ListEntitiesRequest.page_token",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=469,
    serialized_end=545,
)


_LISTENTITIESRESPONSE = _descriptor.Descriptor(
    name="ListEntitiesResponse",
    full_name="exabel.api.data.v1.ListEntitiesResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="entities",
            full_name="exabel.api.data.v1.ListEntitiesResponse.entities",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="next_page_token",
            full_name="exabel.api.data.v1.ListEntitiesResponse.next_page_token",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="total_size",
            full_name="exabel.api.data.v1.ListEntitiesResponse.total_size",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=547,
    serialized_end=660,
)


_GETENTITYREQUEST = _descriptor.Descriptor(
    name="GetEntityRequest",
    full_name="exabel.api.data.v1.GetEntityRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="exabel.api.data.v1.GetEntityRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=662,
    serialized_end=694,
)


_CREATEENTITYREQUEST = _descriptor.Descriptor(
    name="CreateEntityRequest",
    full_name="exabel.api.data.v1.CreateEntityRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="exabel.api.data.v1.CreateEntityRequest.parent",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="entity",
            full_name="exabel.api.data.v1.CreateEntityRequest.entity",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=696,
    serialized_end=777,
)


_UPDATEENTITYREQUEST = _descriptor.Descriptor(
    name="UpdateEntityRequest",
    full_name="exabel.api.data.v1.UpdateEntityRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="entity",
            full_name="exabel.api.data.v1.UpdateEntityRequest.entity",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="update_mask",
            full_name="exabel.api.data.v1.UpdateEntityRequest.update_mask",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=779,
    serialized_end=893,
)


_DELETEENTITYREQUEST = _descriptor.Descriptor(
    name="DeleteEntityRequest",
    full_name="exabel.api.data.v1.DeleteEntityRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="exabel.api.data.v1.DeleteEntityRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=895,
    serialized_end=930,
)


_SEARCHENTITIESREQUEST = _descriptor.Descriptor(
    name="SearchEntitiesRequest",
    full_name="exabel.api.data.v1.SearchEntitiesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="exabel.api.data.v1.SearchEntitiesRequest.parent",
            index=0,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="terms",
            full_name="exabel.api.data.v1.SearchEntitiesRequest.terms",
            index=1,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="page_size",
            full_name="exabel.api.data.v1.SearchEntitiesRequest.page_size",
            index=2,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="page_token",
            full_name="exabel.api.data.v1.SearchEntitiesRequest.page_token",
            index=3,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=932,
    serialized_end=1057,
)


_SEARCHENTITIESRESPONSE = _descriptor.Descriptor(
    name="SearchEntitiesResponse",
    full_name="exabel.api.data.v1.SearchEntitiesResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="entities",
            full_name="exabel.api.data.v1.SearchEntitiesResponse.entities",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="next_page_token",
            full_name="exabel.api.data.v1.SearchEntitiesResponse.next_page_token",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1059,
    serialized_end=1154,
)

_LISTENTITYTYPESRESPONSE.fields_by_name[
    "entity_types"
].message_type = exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2._ENTITYTYPE
_LISTENTITIESRESPONSE.fields_by_name[
    "entities"
].message_type = exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2._ENTITY
_CREATEENTITYREQUEST.fields_by_name[
    "entity"
].message_type = exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2._ENTITY
_UPDATEENTITYREQUEST.fields_by_name[
    "entity"
].message_type = exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2._ENTITY
_UPDATEENTITYREQUEST.fields_by_name[
    "update_mask"
].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_SEARCHENTITIESREQUEST.fields_by_name[
    "terms"
].message_type = exabel_dot_api_dot_data_dot_v1_dot_search__messages__pb2._SEARCHTERM
_SEARCHENTITIESRESPONSE.fields_by_name[
    "entities"
].message_type = exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2._ENTITY
DESCRIPTOR.message_types_by_name["ListEntityTypesRequest"] = _LISTENTITYTYPESREQUEST
DESCRIPTOR.message_types_by_name["ListEntityTypesResponse"] = _LISTENTITYTYPESRESPONSE
DESCRIPTOR.message_types_by_name["GetEntityTypeRequest"] = _GETENTITYTYPEREQUEST
DESCRIPTOR.message_types_by_name["ListEntitiesRequest"] = _LISTENTITIESREQUEST
DESCRIPTOR.message_types_by_name["ListEntitiesResponse"] = _LISTENTITIESRESPONSE
DESCRIPTOR.message_types_by_name["GetEntityRequest"] = _GETENTITYREQUEST
DESCRIPTOR.message_types_by_name["CreateEntityRequest"] = _CREATEENTITYREQUEST
DESCRIPTOR.message_types_by_name["UpdateEntityRequest"] = _UPDATEENTITYREQUEST
DESCRIPTOR.message_types_by_name["DeleteEntityRequest"] = _DELETEENTITYREQUEST
DESCRIPTOR.message_types_by_name["SearchEntitiesRequest"] = _SEARCHENTITIESREQUEST
DESCRIPTOR.message_types_by_name["SearchEntitiesResponse"] = _SEARCHENTITIESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListEntityTypesRequest = _reflection.GeneratedProtocolMessageType(
    "ListEntityTypesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTENTITYTYPESREQUEST,
        "__module__": "exabel.api.data.v1.entity_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.ListEntityTypesRequest)
    },
)
_sym_db.RegisterMessage(ListEntityTypesRequest)

ListEntityTypesResponse = _reflection.GeneratedProtocolMessageType(
    "ListEntityTypesResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTENTITYTYPESRESPONSE,
        "__module__": "exabel.api.data.v1.entity_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.ListEntityTypesResponse)
    },
)
_sym_db.RegisterMessage(ListEntityTypesResponse)

GetEntityTypeRequest = _reflection.GeneratedProtocolMessageType(
    "GetEntityTypeRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETENTITYTYPEREQUEST,
        "__module__": "exabel.api.data.v1.entity_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.GetEntityTypeRequest)
    },
)
_sym_db.RegisterMessage(GetEntityTypeRequest)

ListEntitiesRequest = _reflection.GeneratedProtocolMessageType(
    "ListEntitiesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTENTITIESREQUEST,
        "__module__": "exabel.api.data.v1.entity_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.ListEntitiesRequest)
    },
)
_sym_db.RegisterMessage(ListEntitiesRequest)

ListEntitiesResponse = _reflection.GeneratedProtocolMessageType(
    "ListEntitiesResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTENTITIESRESPONSE,
        "__module__": "exabel.api.data.v1.entity_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.ListEntitiesResponse)
    },
)
_sym_db.RegisterMessage(ListEntitiesResponse)

GetEntityRequest = _reflection.GeneratedProtocolMessageType(
    "GetEntityRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETENTITYREQUEST,
        "__module__": "exabel.api.data.v1.entity_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.GetEntityRequest)
    },
)
_sym_db.RegisterMessage(GetEntityRequest)

CreateEntityRequest = _reflection.GeneratedProtocolMessageType(
    "CreateEntityRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEENTITYREQUEST,
        "__module__": "exabel.api.data.v1.entity_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.CreateEntityRequest)
    },
)
_sym_db.RegisterMessage(CreateEntityRequest)

UpdateEntityRequest = _reflection.GeneratedProtocolMessageType(
    "UpdateEntityRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATEENTITYREQUEST,
        "__module__": "exabel.api.data.v1.entity_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.UpdateEntityRequest)
    },
)
_sym_db.RegisterMessage(UpdateEntityRequest)

DeleteEntityRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteEntityRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETEENTITYREQUEST,
        "__module__": "exabel.api.data.v1.entity_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.DeleteEntityRequest)
    },
)
_sym_db.RegisterMessage(DeleteEntityRequest)

SearchEntitiesRequest = _reflection.GeneratedProtocolMessageType(
    "SearchEntitiesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SEARCHENTITIESREQUEST,
        "__module__": "exabel.api.data.v1.entity_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.SearchEntitiesRequest)
    },
)
_sym_db.RegisterMessage(SearchEntitiesRequest)

SearchEntitiesResponse = _reflection.GeneratedProtocolMessageType(
    "SearchEntitiesResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SEARCHENTITIESRESPONSE,
        "__module__": "exabel.api.data.v1.entity_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.SearchEntitiesResponse)
    },
)
_sym_db.RegisterMessage(SearchEntitiesResponse)


DESCRIPTOR._options = None

_ENTITYSERVICE = _descriptor.ServiceDescriptor(
    name="EntityService",
    full_name="exabel.api.data.v1.EntityService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=1157,
    serialized_end=2272,
    methods=[
        _descriptor.MethodDescriptor(
            name="ListEntityTypes",
            full_name="exabel.api.data.v1.EntityService.ListEntityTypes",
            index=0,
            containing_service=None,
            input_type=_LISTENTITYTYPESREQUEST,
            output_type=_LISTENTITYTYPESRESPONSE,
            serialized_options=b"\202\323\344\223\002\021\022\017/v1/entityTypes",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="GetEntityType",
            full_name="exabel.api.data.v1.EntityService.GetEntityType",
            index=1,
            containing_service=None,
            input_type=_GETENTITYTYPEREQUEST,
            output_type=exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2._ENTITYTYPE,
            serialized_options=b"\202\323\344\223\002\032\022\030/v1/{name=entityTypes/*}",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="ListEntities",
            full_name="exabel.api.data.v1.EntityService.ListEntities",
            index=2,
            containing_service=None,
            input_type=_LISTENTITIESREQUEST,
            output_type=_LISTENTITIESRESPONSE,
            serialized_options=b"\202\323\344\223\002%\022#/v1/{parent=entityTypes/*}/entities",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="GetEntity",
            full_name="exabel.api.data.v1.EntityService.GetEntity",
            index=3,
            containing_service=None,
            input_type=_GETENTITYREQUEST,
            output_type=exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2._ENTITY,
            serialized_options=b"\202\323\344\223\002%\022#/v1/{name=entityTypes/*/entities/*}",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="CreateEntity",
            full_name="exabel.api.data.v1.EntityService.CreateEntity",
            index=4,
            containing_service=None,
            input_type=_CREATEENTITYREQUEST,
            output_type=exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2._ENTITY,
            serialized_options=b'\202\323\344\223\002-"#/v1/{parent=entityTypes/*}/entities:\006entity',
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="UpdateEntity",
            full_name="exabel.api.data.v1.EntityService.UpdateEntity",
            index=5,
            containing_service=None,
            input_type=_UPDATEENTITYREQUEST,
            output_type=exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2._ENTITY,
            serialized_options=b"\202\323\344\223\00242*/v1/{entity.name=entityTypes/*/entities/*}:\006entity",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="DeleteEntity",
            full_name="exabel.api.data.v1.EntityService.DeleteEntity",
            index=6,
            containing_service=None,
            input_type=_DELETEENTITYREQUEST,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=b"\202\323\344\223\002%*#/v1/{name=entityTypes/*/entities/*}",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="SearchEntities",
            full_name="exabel.api.data.v1.EntityService.SearchEntities",
            index=7,
            containing_service=None,
            input_type=_SEARCHENTITIESREQUEST,
            output_type=_SEARCHENTITIESRESPONSE,
            serialized_options=b'\202\323\344\223\002/"*/v1/{parent=entityTypes/*}/entities:search:\001*',
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_ENTITYSERVICE)

DESCRIPTOR.services_by_name["EntityService"] = _ENTITYSERVICE

# @@protoc_insertion_point(module_scope)
