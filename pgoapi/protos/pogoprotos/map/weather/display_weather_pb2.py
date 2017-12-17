# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/map/weather/display_weather.proto

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
  name='pogoprotos/map/weather/display_weather.proto',
  package='pogoprotos.map.weather',
  syntax='proto3',
  serialized_pb=_b('\n,pogoprotos/map/weather/display_weather.proto\x12\x16pogoprotos.map.weather\"\xd9\x03\n\x0e\x44isplayWeather\x12H\n\x0b\x63loud_level\x18\x01 \x01(\x0e\x32\x33.pogoprotos.map.weather.DisplayWeather.DisplayLevel\x12G\n\nrain_level\x18\x02 \x01(\x0e\x32\x33.pogoprotos.map.weather.DisplayWeather.DisplayLevel\x12G\n\nwind_level\x18\x03 \x01(\x0e\x32\x33.pogoprotos.map.weather.DisplayWeather.DisplayLevel\x12G\n\nsnow_level\x18\x04 \x01(\x0e\x32\x33.pogoprotos.map.weather.DisplayWeather.DisplayLevel\x12\x46\n\tfog_level\x18\x05 \x01(\x0e\x32\x33.pogoprotos.map.weather.DisplayWeather.DisplayLevel\x12\x16\n\x0ewind_direction\x18\x06 \x01(\x05\"B\n\x0c\x44isplayLevel\x12\x0b\n\x07LEVEL_0\x10\x00\x12\x0b\n\x07LEVEL_1\x10\x01\x12\x0b\n\x07LEVEL_2\x10\x02\x12\x0b\n\x07LEVEL_3\x10\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_DISPLAYWEATHER_DISPLAYLEVEL = _descriptor.EnumDescriptor(
  name='DisplayLevel',
  full_name='pogoprotos.map.weather.DisplayWeather.DisplayLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LEVEL_0', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEVEL_1', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEVEL_2', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEVEL_3', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=480,
  serialized_end=546,
)
_sym_db.RegisterEnumDescriptor(_DISPLAYWEATHER_DISPLAYLEVEL)


_DISPLAYWEATHER = _descriptor.Descriptor(
  name='DisplayWeather',
  full_name='pogoprotos.map.weather.DisplayWeather',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cloud_level', full_name='pogoprotos.map.weather.DisplayWeather.cloud_level', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rain_level', full_name='pogoprotos.map.weather.DisplayWeather.rain_level', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wind_level', full_name='pogoprotos.map.weather.DisplayWeather.wind_level', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='snow_level', full_name='pogoprotos.map.weather.DisplayWeather.snow_level', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fog_level', full_name='pogoprotos.map.weather.DisplayWeather.fog_level', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wind_direction', full_name='pogoprotos.map.weather.DisplayWeather.wind_direction', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DISPLAYWEATHER_DISPLAYLEVEL,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=546,
)

_DISPLAYWEATHER.fields_by_name['cloud_level'].enum_type = _DISPLAYWEATHER_DISPLAYLEVEL
_DISPLAYWEATHER.fields_by_name['rain_level'].enum_type = _DISPLAYWEATHER_DISPLAYLEVEL
_DISPLAYWEATHER.fields_by_name['wind_level'].enum_type = _DISPLAYWEATHER_DISPLAYLEVEL
_DISPLAYWEATHER.fields_by_name['snow_level'].enum_type = _DISPLAYWEATHER_DISPLAYLEVEL
_DISPLAYWEATHER.fields_by_name['fog_level'].enum_type = _DISPLAYWEATHER_DISPLAYLEVEL
_DISPLAYWEATHER_DISPLAYLEVEL.containing_type = _DISPLAYWEATHER
DESCRIPTOR.message_types_by_name['DisplayWeather'] = _DISPLAYWEATHER

DisplayWeather = _reflection.GeneratedProtocolMessageType('DisplayWeather', (_message.Message,), dict(
  DESCRIPTOR = _DISPLAYWEATHER,
  __module__ = 'pogoprotos.map.weather.display_weather_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.map.weather.DisplayWeather)
  ))
_sym_db.RegisterMessage(DisplayWeather)


# @@protoc_insertion_point(module_scope)
