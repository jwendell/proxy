# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mixer/v1/config/client/quota.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from mixer.v1.config.client import service_pb2 as mixer_dot_v1_dot_config_dot_client_dot_service__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mixer/v1/config/client/quota.proto',
  package='istio.mixer.v1.config.client',
  syntax='proto3',
  serialized_options=_b('Z#istio.io/api/mixer/v1/config/client\310\341\036\000\250\342\036\000\360\341\036\000\330\342\036\001'),
  serialized_pb=_b('\n\"mixer/v1/config/client/quota.proto\x12\x1cistio.mixer.v1.config.client\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a$mixer/v1/config/client/service.proto\"C\n\tQuotaSpec\x12\x36\n\x05rules\x18\x01 \x03(\x0b\x32\'.istio.mixer.v1.config.client.QuotaRule\"}\n\tQuotaRule\x12;\n\x05match\x18\x01 \x03(\x0b\x32,.istio.mixer.v1.config.client.AttributeMatch\x12\x33\n\x06quotas\x18\x02 \x03(\x0b\x32#.istio.mixer.v1.config.client.Quota\"O\n\x0bStringMatch\x12\x0f\n\x05\x65xact\x18\x01 \x01(\tH\x00\x12\x10\n\x06prefix\x18\x02 \x01(\tH\x00\x12\x0f\n\x05regex\x18\x03 \x01(\tH\x00\x42\x0c\n\nmatch_type\"\xb4\x01\n\x0e\x41ttributeMatch\x12H\n\x06\x63lause\x18\x01 \x03(\x0b\x32\x38.istio.mixer.v1.config.client.AttributeMatch.ClauseEntry\x1aX\n\x0b\x43lauseEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32).istio.mixer.v1.config.client.StringMatch:\x02\x38\x01\"&\n\x05Quota\x12\r\n\x05quota\x18\x01 \x01(\t\x12\x0e\n\x06\x63harge\x18\x02 \x01(\x05\"\xee\x01\n\x10QuotaSpecBinding\x12\x41\n\x08services\x18\x01 \x03(\x0b\x32*.istio.mixer.v1.config.client.IstioServiceB\x03\xe0\x41\x02\x12[\n\x0bquota_specs\x18\x02 \x03(\x0b\x32\x41.istio.mixer.v1.config.client.QuotaSpecBinding.QuotaSpecReferenceB\x03\xe0\x41\x02\x1a:\n\x12QuotaSpecReference\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x11\n\tnamespace\x18\x02 \x01(\tB5Z#istio.io/api/mixer/v1/config/client\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00\xf0\xe1\x1e\x00\xd8\xe2\x1e\x01\x62\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,mixer_dot_v1_dot_config_dot_client_dot_service__pb2.DESCRIPTOR,])




_QUOTASPEC = _descriptor.Descriptor(
  name='QuotaSpec',
  full_name='istio.mixer.v1.config.client.QuotaSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rules', full_name='istio.mixer.v1.config.client.QuotaSpec.rules', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=228,
)


_QUOTARULE = _descriptor.Descriptor(
  name='QuotaRule',
  full_name='istio.mixer.v1.config.client.QuotaRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='match', full_name='istio.mixer.v1.config.client.QuotaRule.match', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quotas', full_name='istio.mixer.v1.config.client.QuotaRule.quotas', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=355,
)


_STRINGMATCH = _descriptor.Descriptor(
  name='StringMatch',
  full_name='istio.mixer.v1.config.client.StringMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exact', full_name='istio.mixer.v1.config.client.StringMatch.exact', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='istio.mixer.v1.config.client.StringMatch.prefix', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regex', full_name='istio.mixer.v1.config.client.StringMatch.regex', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='match_type', full_name='istio.mixer.v1.config.client.StringMatch.match_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=357,
  serialized_end=436,
)


_ATTRIBUTEMATCH_CLAUSEENTRY = _descriptor.Descriptor(
  name='ClauseEntry',
  full_name='istio.mixer.v1.config.client.AttributeMatch.ClauseEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='istio.mixer.v1.config.client.AttributeMatch.ClauseEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='istio.mixer.v1.config.client.AttributeMatch.ClauseEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=531,
  serialized_end=619,
)

_ATTRIBUTEMATCH = _descriptor.Descriptor(
  name='AttributeMatch',
  full_name='istio.mixer.v1.config.client.AttributeMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clause', full_name='istio.mixer.v1.config.client.AttributeMatch.clause', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ATTRIBUTEMATCH_CLAUSEENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=439,
  serialized_end=619,
)


_QUOTA = _descriptor.Descriptor(
  name='Quota',
  full_name='istio.mixer.v1.config.client.Quota',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quota', full_name='istio.mixer.v1.config.client.Quota.quota', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='charge', full_name='istio.mixer.v1.config.client.Quota.charge', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=621,
  serialized_end=659,
)


_QUOTASPECBINDING_QUOTASPECREFERENCE = _descriptor.Descriptor(
  name='QuotaSpecReference',
  full_name='istio.mixer.v1.config.client.QuotaSpecBinding.QuotaSpecReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='istio.mixer.v1.config.client.QuotaSpecBinding.QuotaSpecReference.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='istio.mixer.v1.config.client.QuotaSpecBinding.QuotaSpecReference.namespace', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=842,
  serialized_end=900,
)

_QUOTASPECBINDING = _descriptor.Descriptor(
  name='QuotaSpecBinding',
  full_name='istio.mixer.v1.config.client.QuotaSpecBinding',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='services', full_name='istio.mixer.v1.config.client.QuotaSpecBinding.services', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quota_specs', full_name='istio.mixer.v1.config.client.QuotaSpecBinding.quota_specs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_QUOTASPECBINDING_QUOTASPECREFERENCE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=662,
  serialized_end=900,
)

_QUOTASPEC.fields_by_name['rules'].message_type = _QUOTARULE
_QUOTARULE.fields_by_name['match'].message_type = _ATTRIBUTEMATCH
_QUOTARULE.fields_by_name['quotas'].message_type = _QUOTA
_STRINGMATCH.oneofs_by_name['match_type'].fields.append(
  _STRINGMATCH.fields_by_name['exact'])
_STRINGMATCH.fields_by_name['exact'].containing_oneof = _STRINGMATCH.oneofs_by_name['match_type']
_STRINGMATCH.oneofs_by_name['match_type'].fields.append(
  _STRINGMATCH.fields_by_name['prefix'])
_STRINGMATCH.fields_by_name['prefix'].containing_oneof = _STRINGMATCH.oneofs_by_name['match_type']
_STRINGMATCH.oneofs_by_name['match_type'].fields.append(
  _STRINGMATCH.fields_by_name['regex'])
_STRINGMATCH.fields_by_name['regex'].containing_oneof = _STRINGMATCH.oneofs_by_name['match_type']
_ATTRIBUTEMATCH_CLAUSEENTRY.fields_by_name['value'].message_type = _STRINGMATCH
_ATTRIBUTEMATCH_CLAUSEENTRY.containing_type = _ATTRIBUTEMATCH
_ATTRIBUTEMATCH.fields_by_name['clause'].message_type = _ATTRIBUTEMATCH_CLAUSEENTRY
_QUOTASPECBINDING_QUOTASPECREFERENCE.containing_type = _QUOTASPECBINDING
_QUOTASPECBINDING.fields_by_name['services'].message_type = mixer_dot_v1_dot_config_dot_client_dot_service__pb2._ISTIOSERVICE
_QUOTASPECBINDING.fields_by_name['quota_specs'].message_type = _QUOTASPECBINDING_QUOTASPECREFERENCE
DESCRIPTOR.message_types_by_name['QuotaSpec'] = _QUOTASPEC
DESCRIPTOR.message_types_by_name['QuotaRule'] = _QUOTARULE
DESCRIPTOR.message_types_by_name['StringMatch'] = _STRINGMATCH
DESCRIPTOR.message_types_by_name['AttributeMatch'] = _ATTRIBUTEMATCH
DESCRIPTOR.message_types_by_name['Quota'] = _QUOTA
DESCRIPTOR.message_types_by_name['QuotaSpecBinding'] = _QUOTASPECBINDING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QuotaSpec = _reflection.GeneratedProtocolMessageType('QuotaSpec', (_message.Message,), {
  'DESCRIPTOR' : _QUOTASPEC,
  '__module__' : 'mixer.v1.config.client.quota_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.v1.config.client.QuotaSpec)
  })
_sym_db.RegisterMessage(QuotaSpec)

QuotaRule = _reflection.GeneratedProtocolMessageType('QuotaRule', (_message.Message,), {
  'DESCRIPTOR' : _QUOTARULE,
  '__module__' : 'mixer.v1.config.client.quota_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.v1.config.client.QuotaRule)
  })
_sym_db.RegisterMessage(QuotaRule)

StringMatch = _reflection.GeneratedProtocolMessageType('StringMatch', (_message.Message,), {
  'DESCRIPTOR' : _STRINGMATCH,
  '__module__' : 'mixer.v1.config.client.quota_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.v1.config.client.StringMatch)
  })
_sym_db.RegisterMessage(StringMatch)

AttributeMatch = _reflection.GeneratedProtocolMessageType('AttributeMatch', (_message.Message,), {

  'ClauseEntry' : _reflection.GeneratedProtocolMessageType('ClauseEntry', (_message.Message,), {
    'DESCRIPTOR' : _ATTRIBUTEMATCH_CLAUSEENTRY,
    '__module__' : 'mixer.v1.config.client.quota_pb2'
    # @@protoc_insertion_point(class_scope:istio.mixer.v1.config.client.AttributeMatch.ClauseEntry)
    })
  ,
  'DESCRIPTOR' : _ATTRIBUTEMATCH,
  '__module__' : 'mixer.v1.config.client.quota_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.v1.config.client.AttributeMatch)
  })
_sym_db.RegisterMessage(AttributeMatch)
_sym_db.RegisterMessage(AttributeMatch.ClauseEntry)

Quota = _reflection.GeneratedProtocolMessageType('Quota', (_message.Message,), {
  'DESCRIPTOR' : _QUOTA,
  '__module__' : 'mixer.v1.config.client.quota_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.v1.config.client.Quota)
  })
_sym_db.RegisterMessage(Quota)

QuotaSpecBinding = _reflection.GeneratedProtocolMessageType('QuotaSpecBinding', (_message.Message,), {

  'QuotaSpecReference' : _reflection.GeneratedProtocolMessageType('QuotaSpecReference', (_message.Message,), {
    'DESCRIPTOR' : _QUOTASPECBINDING_QUOTASPECREFERENCE,
    '__module__' : 'mixer.v1.config.client.quota_pb2'
    # @@protoc_insertion_point(class_scope:istio.mixer.v1.config.client.QuotaSpecBinding.QuotaSpecReference)
    })
  ,
  'DESCRIPTOR' : _QUOTASPECBINDING,
  '__module__' : 'mixer.v1.config.client.quota_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.v1.config.client.QuotaSpecBinding)
  })
_sym_db.RegisterMessage(QuotaSpecBinding)
_sym_db.RegisterMessage(QuotaSpecBinding.QuotaSpecReference)


DESCRIPTOR._options = None
_ATTRIBUTEMATCH_CLAUSEENTRY._options = None
_QUOTASPECBINDING_QUOTASPECREFERENCE.fields_by_name['name']._options = None
_QUOTASPECBINDING.fields_by_name['services']._options = None
_QUOTASPECBINDING.fields_by_name['quota_specs']._options = None
# @@protoc_insertion_point(module_scope)
