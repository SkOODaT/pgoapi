# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/social/get_gift_box_details_message.proto

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
  name='pogoprotos/networking/requests/social/get_gift_box_details_message.proto',
  package='pogoprotos.networking.requests.social',
  syntax='proto3',
  serialized_pb=_b('\nHpogoprotos/networking/requests/social/get_gift_box_details_message.proto\x12%pogoprotos.networking.requests.social\"A\n\x18GetGiftBoxDetailsMessage\x12\x12\n\ngiftbox_id\x18\x01 \x03(\x04\x12\x11\n\tplayer_id\x18\x02 \x01(\tb\x06proto3')
)




_GETGIFTBOXDETAILSMESSAGE = _descriptor.Descriptor(
  name='GetGiftBoxDetailsMessage',
  full_name='pogoprotos.networking.requests.social.GetGiftBoxDetailsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='giftbox_id', full_name='pogoprotos.networking.requests.social.GetGiftBoxDetailsMessage.giftbox_id', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='pogoprotos.networking.requests.social.GetGiftBoxDetailsMessage.player_id', index=1,
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
  serialized_start=115,
  serialized_end=180,
)

DESCRIPTOR.message_types_by_name['GetGiftBoxDetailsMessage'] = _GETGIFTBOXDETAILSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetGiftBoxDetailsMessage = _reflection.GeneratedProtocolMessageType('GetGiftBoxDetailsMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETGIFTBOXDETAILSMESSAGE,
  __module__ = 'pogoprotos.networking.requests.social.get_gift_box_details_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.social.GetGiftBoxDetailsMessage)
  ))
_sym_db.RegisterMessage(GetGiftBoxDetailsMessage)


# @@protoc_insertion_point(module_scope)