# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/telemetry/telemetry_domain_id.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/telemetry/telemetry_domain_id.proto',
  package='pogoprotos.networking.platform.telemetry',
  syntax='proto3',
  serialized_pb=_b('\nBpogoprotos/networking/platform/telemetry/telemetry_domain_id.proto\x12(pogoprotos.networking.platform.telemetry*X\n\x11TelemetryDomainId\x12\x1a\n\x16TELEMETRY_NO_DOMAIN_ID\x10\x00\x12\x13\n\x0fTELEMETRY_DITTO\x10\x01\x12\x12\n\x0eTELEMETRY_GAME\x10\x02\x62\x06proto3')
)

_TELEMETRYDOMAINID = _descriptor.EnumDescriptor(
  name='TelemetryDomainId',
  full_name='pogoprotos.networking.platform.telemetry.TelemetryDomainId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TELEMETRY_NO_DOMAIN_ID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TELEMETRY_DITTO', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TELEMETRY_GAME', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=112,
  serialized_end=200,
)
_sym_db.RegisterEnumDescriptor(_TELEMETRYDOMAINID)

TelemetryDomainId = enum_type_wrapper.EnumTypeWrapper(_TELEMETRYDOMAINID)
TELEMETRY_NO_DOMAIN_ID = 0
TELEMETRY_DITTO = 1
TELEMETRY_GAME = 2


DESCRIPTOR.enum_types_by_name['TelemetryDomainId'] = _TELEMETRYDOMAINID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
