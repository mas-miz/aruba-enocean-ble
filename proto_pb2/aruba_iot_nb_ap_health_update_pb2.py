# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruba-iot-nb-ap-health-update.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='aruba-iot-nb-ap-health-update.proto',
  package='aruba_telemetry',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#aruba-iot-nb-ap-health-update.proto\x12\x0f\x61ruba_telemetry\"\xbe\x01\n\x08IotRadio\x12\x0b\n\x03mac\x18\x01 \x01(\x0c\x12/\n\x08hardware\x18\x02 \x01(\x0e\x32\x1d.aruba_telemetry.IotRadioType\x12\x33\n\x08\x66irmware\x18\x03 \x01(\x0e\x32!.aruba_telemetry.IotRadioFirmware\x12-\n\x06health\x18\x04 \x01(\x0e\x32\x1d.aruba_telemetry.HealthStatus\x12\x10\n\x08\x65xternal\x18\x05 \x01(\x08\"N\n\tUsbDevice\x12\x12\n\nidentifier\x18\x01 \x01(\t\x12-\n\x06health\x18\x02 \x01(\x0e\x32\x1d.aruba_telemetry.HealthStatus\"\x94\x01\n\x0e\x41pHealthUpdate\x12/\n\x08\x61pStatus\x18\x01 \x01(\x0e\x32\x1d.aruba_telemetry.HealthStatus\x12(\n\x05radio\x18\x02 \x03(\x0b\x32\x19.aruba_telemetry.IotRadio\x12\'\n\x03usb\x18\x03 \x03(\x0b\x32\x1a.aruba_telemetry.UsbDevice*:\n\x0cHealthStatus\x12\x0b\n\x07healthy\x10\x00\x12\x0c\n\x08\x64\x65graded\x10\x01\x12\x0f\n\x0bunavailable\x10\x02*$\n\x10IotRadioFirmware\x12\x10\n\x0c\x61rubaDefault\x10\x00*\"\n\x0cIotRadioType\x12\x08\n\x04gen1\x10\x00\x12\x08\n\x04gen2\x10\x01'
)

_HEALTHSTATUS = _descriptor.EnumDescriptor(
  name='HealthStatus',
  full_name='aruba_telemetry.HealthStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='healthy', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='degraded', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='unavailable', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=480,
  serialized_end=538,
)
_sym_db.RegisterEnumDescriptor(_HEALTHSTATUS)

HealthStatus = enum_type_wrapper.EnumTypeWrapper(_HEALTHSTATUS)
_IOTRADIOFIRMWARE = _descriptor.EnumDescriptor(
  name='IotRadioFirmware',
  full_name='aruba_telemetry.IotRadioFirmware',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='arubaDefault', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=540,
  serialized_end=576,
)
_sym_db.RegisterEnumDescriptor(_IOTRADIOFIRMWARE)

IotRadioFirmware = enum_type_wrapper.EnumTypeWrapper(_IOTRADIOFIRMWARE)
_IOTRADIOTYPE = _descriptor.EnumDescriptor(
  name='IotRadioType',
  full_name='aruba_telemetry.IotRadioType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='gen1', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='gen2', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=578,
  serialized_end=612,
)
_sym_db.RegisterEnumDescriptor(_IOTRADIOTYPE)

IotRadioType = enum_type_wrapper.EnumTypeWrapper(_IOTRADIOTYPE)
healthy = 0
degraded = 1
unavailable = 2
arubaDefault = 0
gen1 = 0
gen2 = 1



_IOTRADIO = _descriptor.Descriptor(
  name='IotRadio',
  full_name='aruba_telemetry.IotRadio',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mac', full_name='aruba_telemetry.IotRadio.mac', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hardware', full_name='aruba_telemetry.IotRadio.hardware', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='firmware', full_name='aruba_telemetry.IotRadio.firmware', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='health', full_name='aruba_telemetry.IotRadio.health', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='external', full_name='aruba_telemetry.IotRadio.external', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=57,
  serialized_end=247,
)


_USBDEVICE = _descriptor.Descriptor(
  name='UsbDevice',
  full_name='aruba_telemetry.UsbDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='aruba_telemetry.UsbDevice.identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='health', full_name='aruba_telemetry.UsbDevice.health', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=249,
  serialized_end=327,
)


_APHEALTHUPDATE = _descriptor.Descriptor(
  name='ApHealthUpdate',
  full_name='aruba_telemetry.ApHealthUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='apStatus', full_name='aruba_telemetry.ApHealthUpdate.apStatus', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='radio', full_name='aruba_telemetry.ApHealthUpdate.radio', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='usb', full_name='aruba_telemetry.ApHealthUpdate.usb', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=330,
  serialized_end=478,
)

_IOTRADIO.fields_by_name['hardware'].enum_type = _IOTRADIOTYPE
_IOTRADIO.fields_by_name['firmware'].enum_type = _IOTRADIOFIRMWARE
_IOTRADIO.fields_by_name['health'].enum_type = _HEALTHSTATUS
_USBDEVICE.fields_by_name['health'].enum_type = _HEALTHSTATUS
_APHEALTHUPDATE.fields_by_name['apStatus'].enum_type = _HEALTHSTATUS
_APHEALTHUPDATE.fields_by_name['radio'].message_type = _IOTRADIO
_APHEALTHUPDATE.fields_by_name['usb'].message_type = _USBDEVICE
DESCRIPTOR.message_types_by_name['IotRadio'] = _IOTRADIO
DESCRIPTOR.message_types_by_name['UsbDevice'] = _USBDEVICE
DESCRIPTOR.message_types_by_name['ApHealthUpdate'] = _APHEALTHUPDATE
DESCRIPTOR.enum_types_by_name['HealthStatus'] = _HEALTHSTATUS
DESCRIPTOR.enum_types_by_name['IotRadioFirmware'] = _IOTRADIOFIRMWARE
DESCRIPTOR.enum_types_by_name['IotRadioType'] = _IOTRADIOTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IotRadio = _reflection.GeneratedProtocolMessageType('IotRadio', (_message.Message,), {
  'DESCRIPTOR' : _IOTRADIO,
  '__module__' : 'aruba_iot_nb_ap_health_update_pb2'
  # @@protoc_insertion_point(class_scope:aruba_telemetry.IotRadio)
  })
_sym_db.RegisterMessage(IotRadio)

UsbDevice = _reflection.GeneratedProtocolMessageType('UsbDevice', (_message.Message,), {
  'DESCRIPTOR' : _USBDEVICE,
  '__module__' : 'aruba_iot_nb_ap_health_update_pb2'
  # @@protoc_insertion_point(class_scope:aruba_telemetry.UsbDevice)
  })
_sym_db.RegisterMessage(UsbDevice)

ApHealthUpdate = _reflection.GeneratedProtocolMessageType('ApHealthUpdate', (_message.Message,), {
  'DESCRIPTOR' : _APHEALTHUPDATE,
  '__module__' : 'aruba_iot_nb_ap_health_update_pb2'
  # @@protoc_insertion_point(class_scope:aruba_telemetry.ApHealthUpdate)
  })
_sym_db.RegisterMessage(ApHealthUpdate)


# @@protoc_insertion_point(module_scope)
