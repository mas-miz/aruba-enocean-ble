# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruba-iot-sb-status.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='aruba-iot-sb-status.proto',
  package='aruba_telemetry',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19\x61ruba-iot-sb-status.proto\x12\x0f\x61ruba_telemetry\"^\n\rConnectStatus\x12\x31\n\x0b\x63onnectCode\x18\x01 \x01(\x0e\x32\x1c.aruba_telemetry.ConnectCode\x12\x1a\n\x12\x63onnectDescription\x18\x02 \x01(\t*,\n\x0b\x43onnectCode\x12\x0c\n\x08statusOK\x10\x00\x12\x0f\n\x0btokenExpire\x10\x01'
)

_CONNECTCODE = _descriptor.EnumDescriptor(
  name='ConnectCode',
  full_name='aruba_telemetry.ConnectCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='statusOK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='tokenExpire', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=142,
  serialized_end=186,
)
_sym_db.RegisterEnumDescriptor(_CONNECTCODE)

ConnectCode = enum_type_wrapper.EnumTypeWrapper(_CONNECTCODE)
statusOK = 0
tokenExpire = 1



_CONNECTSTATUS = _descriptor.Descriptor(
  name='ConnectStatus',
  full_name='aruba_telemetry.ConnectStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connectCode', full_name='aruba_telemetry.ConnectStatus.connectCode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connectDescription', full_name='aruba_telemetry.ConnectStatus.connectDescription', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=140,
)

_CONNECTSTATUS.fields_by_name['connectCode'].enum_type = _CONNECTCODE
DESCRIPTOR.message_types_by_name['ConnectStatus'] = _CONNECTSTATUS
DESCRIPTOR.enum_types_by_name['ConnectCode'] = _CONNECTCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConnectStatus = _reflection.GeneratedProtocolMessageType('ConnectStatus', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTSTATUS,
  '__module__' : 'aruba_iot_sb_status_pb2'
  # @@protoc_insertion_point(class_scope:aruba_telemetry.ConnectStatus)
  })
_sym_db.RegisterMessage(ConnectStatus)


# @@protoc_insertion_point(module_scope)
