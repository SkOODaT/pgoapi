# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/social/gift_details_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.gift import gift_box_details_pb2 as pogoprotos_dot_data_dot_gift_dot_gift__box__details__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/social/gift_details_response.proto',
  package='pogoprotos.networking.responses.social',
  syntax='proto3',
  serialized_pb=_b('\nBpogoprotos/networking/responses/social/gift_details_response.proto\x12&pogoprotos.networking.responses.social\x1a+pogoprotos/data/gift/gift_box_details.proto\"\xc8\x02\n\x13GiftDetailsResponse\x12R\n\x06result\x18\x01 \x01(\x0e\x32\x42.pogoprotos.networking.responses.social.GiftDetailsResponse.Result\x12\x38\n\ngift_boxes\x18\x02 \x03(\x0b\x32$.pogoprotos.data.gift.GiftBoxDetails\"\xa2\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x12\x1d\n\x19\x45RROR_GIFT_DOES_NOT_EXIST\x10\x03\x12\x1b\n\x17\x45RROR_INVALID_PLAYER_ID\x10\x04\x12\x1a\n\x16\x45RROR_FRIEND_NOT_FOUND\x10\x05\x12\x15\n\x11\x45RROR_FORT_SEARCH\x10\x06\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_gift_dot_gift__box__details__pb2.DESCRIPTOR,])



_GIFTDETAILSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.social.GiftDetailsResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_GIFT_DOES_NOT_EXIST', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_PLAYER_ID', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_FRIEND_NOT_FOUND', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_FORT_SEARCH', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=322,
  serialized_end=484,
)
_sym_db.RegisterEnumDescriptor(_GIFTDETAILSRESPONSE_RESULT)


_GIFTDETAILSRESPONSE = _descriptor.Descriptor(
  name='GiftDetailsResponse',
  full_name='pogoprotos.networking.responses.social.GiftDetailsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.social.GiftDetailsResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gift_boxes', full_name='pogoprotos.networking.responses.social.GiftDetailsResponse.gift_boxes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GIFTDETAILSRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=156,
  serialized_end=484,
)

_GIFTDETAILSRESPONSE.fields_by_name['result'].enum_type = _GIFTDETAILSRESPONSE_RESULT
_GIFTDETAILSRESPONSE.fields_by_name['gift_boxes'].message_type = pogoprotos_dot_data_dot_gift_dot_gift__box__details__pb2._GIFTBOXDETAILS
_GIFTDETAILSRESPONSE_RESULT.containing_type = _GIFTDETAILSRESPONSE
DESCRIPTOR.message_types_by_name['GiftDetailsResponse'] = _GIFTDETAILSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GiftDetailsResponse = _reflection.GeneratedProtocolMessageType('GiftDetailsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GIFTDETAILSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.social.gift_details_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.social.GiftDetailsResponse)
  ))
_sym_db.RegisterMessage(GiftDetailsResponse)


# @@protoc_insertion_point(module_scope)
