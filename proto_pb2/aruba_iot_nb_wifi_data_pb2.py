# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruba-iot-nb-wifi-data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import aruba_iot_types_pb2 as aruba__iot__types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='aruba-iot-nb-wifi-data.proto',
  package='aruba_telemetry',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1c\x61ruba-iot-nb-wifi-data.proto\x12\x0f\x61ruba_telemetry\x1a\x15\x61ruba-iot-types.proto\"r\n\x08WiFiData\x12\x0b\n\x03mac\x18\x01 \x01(\x0c\x12\x35\n\x0b\x64\x65viceClass\x18\x02 \x03(\x0e\x32 .aruba_telemetry.deviceClassEnum\x12\x0c\n\x04rssi\x18\x03 \x01(\x11\x12\x14\n\x0crtls_payload\x18\x04 \x01(\x0c'
  ,
  dependencies=[aruba__iot__types__pb2.DESCRIPTOR,])




_WIFIDATA = _descriptor.Descriptor(
  name='WiFiData',
  full_name='aruba_telemetry.WiFiData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mac', full_name='aruba_telemetry.WiFiData.mac', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deviceClass', full_name='aruba_telemetry.WiFiData.deviceClass', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rssi', full_name='aruba_telemetry.WiFiData.rssi', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rtls_payload', full_name='aruba_telemetry.WiFiData.rtls_payload', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=186,
)

_WIFIDATA.fields_by_name['deviceClass'].enum_type = aruba__iot__types__pb2._DEVICECLASSENUM
DESCRIPTOR.message_types_by_name['WiFiData'] = _WIFIDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WiFiData = _reflection.GeneratedProtocolMessageType('WiFiData', (_message.Message,), {
  'DESCRIPTOR' : _WIFIDATA,
  '__module__' : 'aruba_iot_nb_wifi_data_pb2'
  # @@protoc_insertion_point(class_scope:aruba_telemetry.WiFiData)
  })
_sym_db.RegisterMessage(WiFiData)


# @@protoc_insertion_point(module_scope)