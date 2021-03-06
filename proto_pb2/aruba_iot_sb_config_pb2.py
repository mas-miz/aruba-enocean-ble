# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruba-iot-sb-config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='aruba-iot-sb-config.proto',
  package='aruba_telemetry',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19\x61ruba-iot-sb-config.proto\x12\x0f\x61ruba_telemetry\"<\n\x0fTransportConfig\x12\x17\n\x0freportingPeriod\x18\x01 \x01(\r\x12\x10\n\x08\x63\x65llSize\x18\x02 \x01(\r'
)




_TRANSPORTCONFIG = _descriptor.Descriptor(
  name='TransportConfig',
  full_name='aruba_telemetry.TransportConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reportingPeriod', full_name='aruba_telemetry.TransportConfig.reportingPeriod', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cellSize', full_name='aruba_telemetry.TransportConfig.cellSize', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_end=106,
)

DESCRIPTOR.message_types_by_name['TransportConfig'] = _TRANSPORTCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransportConfig = _reflection.GeneratedProtocolMessageType('TransportConfig', (_message.Message,), {
  'DESCRIPTOR' : _TRANSPORTCONFIG,
  '__module__' : 'aruba_iot_sb_config_pb2'
  # @@protoc_insertion_point(class_scope:aruba_telemetry.TransportConfig)
  })
_sym_db.RegisterMessage(TransportConfig)


# @@protoc_insertion_point(module_scope)
