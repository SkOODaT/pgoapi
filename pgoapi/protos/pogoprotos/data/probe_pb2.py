# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/probe.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/probe.proto',
  package='pogoprotos.data',
  syntax='proto3',
  serialized_pb=_b('\n\x1bpogoprotos/data/probe.proto\x12\x0fpogoprotos.data\"$\n\x05Probe\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\tb\x06proto3')
)




_PROBE = _descriptor.Descriptor(
  name='Probe',
  full_name='pogoprotos.data.Probe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pogoprotos.data.Probe.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='pogoprotos.data.Probe.payload', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=84,
)

DESCRIPTOR.message_types_by_name['Probe'] = _PROBE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Probe = _reflection.GeneratedProtocolMessageType('Probe', (_message.Message,), dict(
  DESCRIPTOR = _PROBE,
  __module__ = 'pogoprotos.data.probe_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.Probe)
  ))
_sym_db.RegisterMessage(Probe)


# @@protoc_insertion_point(module_scope)