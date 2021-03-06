TYPE_REGEX = r'(\(type \(;)([0-9]+)(.*)'
FUNC_REGEX = r'(\(func \(;)([0-9]+)(;\) \(type )([0-9]+)(.*)'
CALL_REGEX = r'(call )([0-9]+)(.*)'
CALL_INDIRECT_REGEX = r'(call_indirect \(type )([0-9]+)(.*)'
EXPORT_REGEX = r'(\(export ")([\w\-\.]+)(" \(func )([0-9]+)(.*)'
ELEM_REGEX = r'(\(elem \(i32.const 0\) )([0-9\s]+)(.*)'
IMPORT_REGEX = r'(\(import ")([\w]+)(" ")([\w]+)(" \(func \(;)([0-9]+)(;\) \(type )([0-9]+)(.*)'
GLOBAL_REGEX = r'(\(global \(;)([0-9]+)(.*)'
GET_SET_GLOBAL_REGEX = r'(\w+_global )([0-9]+)(.*)'
START_REGEX = r'(start )([0-9]+)(.*)'
DATA_REGEX = r'(\(data \(i32.const )([0-9]+)(.*)'
