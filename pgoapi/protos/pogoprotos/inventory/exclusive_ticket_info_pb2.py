# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/exclusive_ticket_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2
from pogoprotos.data.raid import shared_exclusive_ticket_trainer_info_pb2 as pogoprotos_dot_data_dot_raid_dot_shared__exclusive__ticket__trainer__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/inventory/exclusive_ticket_info.proto',
  package='pogoprotos.inventory',
  syntax='proto3',
  serialized_pb=_b('\n0pogoprotos/inventory/exclusive_ticket_info.proto\x12\x14pogoprotos.inventory\x1a\"pogoprotos/data/pokemon_data.proto\x1a?pogoprotos/data/raid/shared_exclusive_ticket_trainer_info.proto\"\xa2\x03\n\x13\x45xclusiveTicketInfo\x12\x11\n\traid_seed\x18\x01 \x01(\x03\x12\x0f\n\x07\x66ort_id\x18\x02 \x01(\t\x12\x15\n\rstart_time_ms\x18\x04 \x01(\x03\x12\x13\n\x0b\x65nd_time_ms\x18\x05 \x01(\x03\x12\x11\n\timage_url\x18\x06 \x01(\t\x12\x10\n\x08latitude\x18\x07 \x01(\x01\x12\x11\n\tlongitude\x18\x08 \x01(\x01\x12\x10\n\x08gym_name\x18\t \x01(\t\x12\x15\n\rspawn_time_ms\x18\n \x01(\x03\x12\x14\n\x0cis_cancelled\x18\x0b \x01(\x08\x12\x32\n\x0craid_pokemon\x18\x0c \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12G\n\x07inviter\x18\r \x01(\x0b\x32\x36.pogoprotos.data.raid.SharedExclusiveTicketTrainerInfo\x12G\n\x07invitee\x18\x0e \x01(\x0b\x32\x36.pogoprotos.data.raid.SharedExclusiveTicketTrainerInfob\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_raid_dot_shared__exclusive__ticket__trainer__info__pb2.DESCRIPTOR,])




_EXCLUSIVETICKETINFO = _descriptor.Descriptor(
  name='ExclusiveTicketInfo',
  full_name='pogoprotos.inventory.ExclusiveTicketInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raid_seed', full_name='pogoprotos.inventory.ExclusiveTicketInfo.raid_seed', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='pogoprotos.inventory.ExclusiveTicketInfo.fort_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time_ms', full_name='pogoprotos.inventory.ExclusiveTicketInfo.start_time_ms', index=2,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time_ms', full_name='pogoprotos.inventory.ExclusiveTicketInfo.end_time_ms', index=3,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_url', full_name='pogoprotos.inventory.ExclusiveTicketInfo.image_url', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='pogoprotos.inventory.ExclusiveTicketInfo.latitude', index=5,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='pogoprotos.inventory.ExclusiveTicketInfo.longitude', index=6,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gym_name', full_name='pogoprotos.inventory.ExclusiveTicketInfo.gym_name', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spawn_time_ms', full_name='pogoprotos.inventory.ExclusiveTicketInfo.spawn_time_ms', index=8,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_cancelled', full_name='pogoprotos.inventory.ExclusiveTicketInfo.is_cancelled', index=9,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raid_pokemon', full_name='pogoprotos.inventory.ExclusiveTicketInfo.raid_pokemon', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inviter', full_name='pogoprotos.inventory.ExclusiveTicketInfo.inviter', index=11,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='invitee', full_name='pogoprotos.inventory.ExclusiveTicketInfo.invitee', index=12,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=176,
  serialized_end=594,
)

_EXCLUSIVETICKETINFO.fields_by_name['raid_pokemon'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_EXCLUSIVETICKETINFO.fields_by_name['inviter'].message_type = pogoprotos_dot_data_dot_raid_dot_shared__exclusive__ticket__trainer__info__pb2._SHAREDEXCLUSIVETICKETTRAINERINFO
_EXCLUSIVETICKETINFO.fields_by_name['invitee'].message_type = pogoprotos_dot_data_dot_raid_dot_shared__exclusive__ticket__trainer__info__pb2._SHAREDEXCLUSIVETICKETTRAINERINFO
DESCRIPTOR.message_types_by_name['ExclusiveTicketInfo'] = _EXCLUSIVETICKETINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExclusiveTicketInfo = _reflection.GeneratedProtocolMessageType('ExclusiveTicketInfo', (_message.Message,), dict(
  DESCRIPTOR = _EXCLUSIVETICKETINFO,
  __module__ = 'pogoprotos.inventory.exclusive_ticket_info_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.inventory.ExclusiveTicketInfo)
  ))
_sym_db.RegisterMessage(ExclusiveTicketInfo)


# @@protoc_insertion_point(module_scope)
