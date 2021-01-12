import datetime
import typing
import os
import tempfile

from dataclasses import dataclass

from dominus.dominus_pb2 import (
    EntityEntry,
    Descriptor as PDescriptor,
    IdentityEntry,
    TimestampRange,
    RelationshipEntry,
)

from bakplane.utils import to_proto_timestamp, to_timestamp, hash_string
from bakplane.bakplane_pb2 import ErrorEntry


@dataclass
class IngestionSessionContext:
    ingestion_session_id: int
    entities_output_location: str
    assets_output_location: str
    errors_output_location: str
    relationships_output_location: str

    @staticmethod
    def from_env():
        return IngestionSessionContext(
            ingestion_session_id=int(os.getenv("INGESTION_SESSION_ID", 0)),
            entities_output_location=os.getenv(
                "ENTITIES_OUTPUT_LOCATION", f'file://{tempfile.mkdtemp()}/'
            ),
            assets_output_location=os.getenv(
                "ASSETS_OUTPUT_LOCATION", f'file://{tempfile.mkdtemp()}/'
            ),
            errors_output_location=os.getenv(
                "ERRORS_OUTPUT_LOCATION", f'file://{tempfile.mkdtemp()}/'
            ),
            relationships_output_location=os.getenv(
                "RELATIONSHIPS_OUTPUT_LOCATION",
                f'file://{tempfile.mkdtemp()}/'
            ),
        )


@dataclass
class Asset:
    resource_code: str
    retrieved_by: typing.Dict[str, int]
    fields: typing.Dict[str, str]

    key_hash_fields: typing.List[str]
    payload_hash_fields: typing.List[str]

    effective_start_dt: datetime.datetime
    effective_end_dt: datetime.datetime
    valid_start_dt: datetime.datetime = None
    valid_end_dt: datetime.datetime = None
    knowledge_start_dt: datetime.datetime = None
    knowledge_end_dt: datetime.datetime = None

    def calculate_hash(self, f: typing.List[str]):
        parts = set()

        for k in f:
            if k in self.fields:
                parts.add(str(self.fields[k]))
            elif k in self.retrieved_by:
                parts.add(str(self.retrieved_by[k]))
            elif k == "effective_start_dt":
                parts.add(str(to_timestamp(self.effective_start_dt)))
            elif k == "effective_end_dt":
                parts.add(str(to_timestamp(self.effective_end_dt)))
            elif k == "valid_start_dt":
                if self.valid_start_dt:
                    parts.add(str(to_timestamp(self.valid_start_dt)))
            elif k == "valid_end_dt":
                if self.valid_end_dt:
                    parts.add(str(to_timestamp(self.valid_end_dt)))
            elif k == "knowledge_start_dt":
                if self.knowledge_start_dt:
                    parts.add(str(to_timestamp(self.knowledge_start_dt)))
            elif k == "knowledge_end_dt":
                if self.knowledge_end_dt:
                    parts.add(str(to_timestamp(self.knowledge_end_dt)))

        return hash_string("".join(sorted(list(parts))))

    @property
    def key_hash(self):
        return self.calculate_hash(self.key_hash_fields)

    @property
    def payload_hash(self):
        return self.calculate_hash(self.payload_hash_fields)

    def to_csv_entry(self, ctx: IngestionSessionContext):
        parts = []

        sorted_retrieved_by = sorted(self.retrieved_by.keys())
        sorted_fields = sorted(self.fields.keys())

        for k in sorted_retrieved_by:
            parts.append(str(self.retrieved_by[k]))

        for k in sorted_fields:
            parts.append(str(self.fields[k]))

        parts.append(
            self.effective_start_dt.strftime("%Y-%m-%d") + " 00:00:00.00000"
        )
        parts.append(
            self.effective_end_dt.strftime("%Y-%m-%d") + " 00:00:00.00000"
        )

        if self.valid_start_dt is None:
            self.valid_start_dt = self.effective_end_dt

        if self.valid_end_dt is None:
            self.valid_end_dt = datetime.datetime(year=3000, month=12, day=31)

        if self.knowledge_start_dt is None:
            self.knowledge_start_dt = datetime.datetime.utcnow()

        if self.knowledge_end_dt is None:
            self.knowledge_end_dt = datetime.datetime(
                year=3000, month=12, day=31
            )

        parts.append(
            self.valid_start_dt.strftime("%Y-%m-%d") + " 00:00:00.00000"
        )
        parts.append(
            self.valid_end_dt.strftime("%Y-%m-%d") + " 00:00:00.00000"
        )

        parts.append(
            self.knowledge_start_dt.strftime("%Y-%m-%d") + " 00:00:00.00000"
        )
        parts.append(
            self.knowledge_end_dt.strftime("%Y-%m-%d") + " 00:00:00.00000"
        )

        parts.append(self.resource_code)
        parts.append(str(ctx.ingestion_session_id))

        parts.append(str(self.key_hash))
        parts.append(str(self.payload_hash))

        return "|".join(parts)


@dataclass
class Identity:
    entity_type: str
    perspective: str
    attributes: typing.Dict[str, str]

    @property
    def uid(self):
        c = []
        for i in sorted(self.attributes.keys()):
            c.append(i + self.attributes[i])

        return hash_string(
            "".join([self.perspective, self.entity_type, "".join(c)])
        )

    def to_proto(self) -> IdentityEntry:
        return IdentityEntry(
            uid=self.uid,
            entity_type_code=self.entity_type,
            perspective_code=self.perspective,
        )


@dataclass
class Descriptor:
    attribute: str
    value: str
    effective_start_dt: datetime.datetime
    effective_end_dt: datetime.datetime
    valid_start_dt: datetime.datetime = None
    valid_end_dt: datetime.datetime = None
    knowledge_start_dt: datetime.datetime = None
    knowledge_end_dt: datetime.datetime = None

    @property
    def payload_hash(self) -> int:
        components = [
            hash(self.attribute),
            hash(self.value),
            hash(self.effective_start_dt),
            hash(self.effective_end_dt),
            hash(self.valid_start_dt),
            hash(self.valid_end_dt),
            hash(self.knowledge_start_dt),
            hash(self.knowledge_end_dt),
        ]

        return hash(frozenset(sorted(components)))

    def to_proto(self) -> PDescriptor:
        return PDescriptor(
            attribute_code=self.attribute,
            value=self.value,
            effective_dating=[
                TimestampRange(
                    start_dt=to_proto_timestamp(self.effective_start_dt),
                    end_dt=to_proto_timestamp(self.effective_end_dt),
                )
            ],
        )


@dataclass
class Entity:
    identity: Identity
    descriptors: typing.List[Descriptor]

    @property
    def payload_hash(self) -> int:
        components = [self.identity.uid]

        for d in self.descriptors:
            components.append(d.payload_hash)

        return hash(frozenset(sorted(components)))

    def to_proto(self) -> EntityEntry:
        return EntityEntry(
            identity=self.identity.to_proto(),
            descriptors=[x.to_proto() for x in self.descriptors],
        )


@dataclass
class Relationship:
    source_identity_uid: int
    target_identity_uid: int
    relationship_type: str
    effective_start_dt: datetime.datetime
    effective_end_dt: datetime.datetime

    @property
    def payload_hash(self) -> int:

        components = [
            hash(self.source_identity_uid),
            hash(self.target_identity_uid),
            hash(self.relationship_type),
            hash(self.effective_start_dt),
            hash(self.effective_end_dt),
        ]

        return hash(frozenset(sorted(components)))

    def to_proto(self) -> RelationshipEntry:
        return RelationshipEntry(
            source_identity_uid=self.source_identity_uid,
            target_identity_uid=self.target_identity_uid,
            relationship_type_code=self.relationship_type,
            effective_dating=[
                TimestampRange(
                    start_dt=to_proto_timestamp(self.effective_start_dt),
                    end_dt=to_proto_timestamp(self.effective_end_dt),
                )
            ],
        )


@dataclass
class Error:
    message: str
    stacktrace: str = None
    context: typing.Dict[str, str] = None

    def to_proto(self) -> ErrorEntry:
        return ErrorEntry(
            message=self.message,
            stacktrace=self.stacktrace,
            context=self.context,
        )
