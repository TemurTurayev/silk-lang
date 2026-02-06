"""
Silk Interpreter - Member Dispatch Mixin

Handles member access and method calls on built-in types
(dict, list, string) and user-defined types (struct, enum).
"""

import math
import random
import json
from typing import Any

from .errors import RuntimeError_
from .builtins.core import silk_repr
from .types import (
    Environment, SilkStruct, SilkEnumValue,
)


class MemberMixin:
    """Mixin providing _eval_member, _eval_method, and _typeof for Interpreter."""

    def _typeof(self, val: Any) -> str:
        """Return the type name of a value."""
        if val is None:
            return "null"
        if isinstance(val, bool):
            return "bool"
        if isinstance(val, int):
            return "int"
        if isinstance(val, float):
            return "float"
        if isinstance(val, str):
            return "string"
        if isinstance(val, list):
            return "array"
        if isinstance(val, dict):
            return "map"
        if isinstance(val, SilkStruct):
            return val.struct_name
        if isinstance(val, tuple) and val[0] in ('function', 'builtin'):
            return "function"
        return "unknown"

    def _eval_member(self, obj: Any, member: str, env: 'Environment | None' = None) -> Any:
        """Evaluate member access."""
        if isinstance(obj, Environment):
            return obj.get(member)

        if isinstance(obj, SilkStruct):
            return self._eval_struct_member(obj, member, env)

        if isinstance(obj, tuple) and len(obj) >= 3 and obj[0] == 'enum_def':
            _, enum_name, variants = obj
            if member in variants:
                return SilkEnumValue(enum_name, member)
            raise RuntimeError_(f"Enum '{enum_name}' has no variant '{member}'")

        if isinstance(obj, dict):
            return self._eval_dict_member(obj, member)

        if isinstance(obj, list):
            return self._eval_list_member(obj, member)

        if isinstance(obj, str):
            return self._eval_string_member(obj, member)

        if isinstance(obj, (int, float)):
            return self._eval_number_member(obj, member)

        raise RuntimeError_(f"'{type(obj).__name__}' has no member '{member}'")

    def _eval_struct_member(self, obj: SilkStruct, member: str, env: Any) -> Any:
        """Evaluate member access on a struct."""
        if member in obj.fields:
            return obj.fields[member]
        if env is not None:
            struct_info = env.get(obj.struct_name)
            if (isinstance(struct_info, tuple)
                    and struct_info[0] == 'struct_def'):
                _, _, _, methods = struct_info
                if member in methods:
                    return ('bound_method', methods[member], obj)
        raise RuntimeError_(
            f"Struct '{obj.struct_name}' has no field or method '{member}'"
        )

    def _eval_dict_member(self, obj: dict, member: str) -> Any:
        """Evaluate member access on a dict."""
        if member == 'length':
            return len(obj)
        if member == 'keys':
            return ('builtin', lambda args, ctx: list(obj.keys()))
        if member == 'values':
            return ('builtin', lambda args, ctx: list(obj.values()))
        if member == 'has':
            return ('builtin', lambda args, ctx: args[0] in obj)
        if member == 'delete':
            return ('builtin', lambda args, ctx: obj.pop(args[0], None))
        if member in ('entries', 'toArray'):
            return ('builtin', lambda args, ctx: [[k, v] for k, v in obj.items()])
        if member in ('merge', 'update'):
            return ('builtin', lambda args, ctx: {**obj, **args[0]})
        if member == 'forEach':
            def _map_foreach(args, ctx):
                for k, v in obj.items():
                    self._call_function(args[0], [k, v])
                return None
            return ('builtin', _map_foreach)
        if member == 'get':
            return ('builtin', lambda args, ctx: obj.get(
                args[0], args[1] if len(args) > 1 else None
            ))
        if member == 'filter':
            def _map_filter(args, ctx):
                return {k: v for k, v in obj.items()
                        if self._call_function(args[0], [k, v])}
            return ('builtin', _map_filter)
        if member == 'map':
            def _map_map(args, ctx):
                return {k: self._call_function(args[0], [k, v])
                        for k, v in obj.items()}
            return ('builtin', _map_map)
        if member == 'isEmpty':
            return ('builtin', lambda args, ctx: len(obj) == 0)
        if member == 'count':
            def _map_count(args, ctx):
                return sum(1 for k, v in obj.items()
                           if self._call_function(args[0], [k, v]))
            return ('builtin', _map_count)
        if member == 'mapValues':
            def _map_values(args, ctx):
                return {k: self._call_function(args[0], [v]) for k, v in obj.items()}
            return ('builtin', _map_values)
        if member == 'pick':
            return ('builtin', lambda args, ctx: {k: obj[k] for k in args[0] if k in obj})
        if member == 'omit':
            return ('builtin', lambda args, ctx: {k: v for k, v in obj.items() if k not in args[0]})
        if member == 'invert':
            return ('builtin', lambda args, ctx: {v: k for k, v in obj.items()})
        if member == 'findKey':
            def _map_find_key(args, ctx):
                for k, v in obj.items():
                    if self._call_function(args[0], [k, v]):
                        return k
                return None
            return ('builtin', _map_find_key)
        if member == 'findValue':
            def _map_find_value(args, ctx):
                for k, v in obj.items():
                    if self._call_function(args[0], [k, v]):
                        return v
                return None
            return ('builtin', _map_find_value)
        if member == 'defaults':
            return ('builtin', lambda args, ctx: {**args[0], **obj})
        if member == 'every':
            def _map_every(args, ctx):
                return all(self._call_function(args[0], [k, v]) for k, v in obj.items())
            return ('builtin', _map_every)
        if member == 'some':
            def _map_some(args, ctx):
                return any(self._call_function(args[0], [k, v]) for k, v in obj.items())
            return ('builtin', _map_some)
        if member == 'mapKeys':
            def _map_keys(args, ctx):
                return {self._call_function(args[0], [k]): v for k, v in obj.items()}
            return ('builtin', _map_keys)
        if member == 'toJson':
            def _to_json(args, ctx):
                def _convert(v):
                    if v is None:
                        return None
                    if isinstance(v, bool):
                        return v
                    if isinstance(v, (int, float, str)):
                        return v
                    if isinstance(v, list):
                        return [_convert(i) for i in v]
                    if isinstance(v, dict):
                        return {str(k): _convert(val) for k, val in v.items()}
                    return str(v)
                return json.dumps(_convert(obj))
            return ('builtin', _to_json)
        if member == 'size':
            return ('builtin', lambda args, ctx: len(obj))
        if member == 'clear':
            return ('builtin', lambda args, ctx: {})
        if member == 'invert':
            return ('builtin', lambda args, ctx: {v: k for k, v in obj.items()})
        raise RuntimeError_(f"'dict' has no member '{member}'")

    def _eval_list_member(self, obj: list, member: str) -> Any:
        """Evaluate member access on a list."""
        if member == 'length':
            return len(obj)
        if member == 'push':
            return ('builtin', lambda args, ctx: obj.append(args[0]) or obj)
        if member == 'pop':
            return ('builtin', lambda args, ctx: obj.pop())
        if member == 'slice':
            return ('builtin', lambda args, ctx: obj[int(args[0]):int(args[1])])
        if member == 'reverse':
            return ('builtin', lambda args, ctx: obj[::-1])
        if member == 'contains':
            return ('builtin', lambda args, ctx: args[0] in obj)
        if member == 'join':
            return ('builtin', lambda args, ctx: args[0].join(
                silk_repr(item) for item in obj
            ))
        if member == 'indexOf':
            def _index_of(args, ctx):
                try:
                    return obj.index(args[0])
                except ValueError:
                    return -1
            return ('builtin', _index_of)
        if member == 'map':
            def _arr_map(args, ctx):
                return [self._call_function(args[0], [item]) for item in obj]
            return ('builtin', _arr_map)
        if member == 'filter':
            def _arr_filter(args, ctx):
                return [item for item in obj if self._call_function(args[0], [item])]
            return ('builtin', _arr_filter)
        if member == 'forEach':
            def _arr_foreach(args, ctx):
                for item in obj:
                    self._call_function(args[0], [item])
                return None
            return ('builtin', _arr_foreach)
        if member == 'reduce':
            def _arr_reduce(args, ctx):
                acc = args[1]
                for item in obj:
                    acc = self._call_function(args[0], [acc, item])
                return acc
            return ('builtin', _arr_reduce)
        if member == 'find':
            def _arr_find(args, ctx):
                for item in obj:
                    if self._call_function(args[0], [item]):
                        return item
                return None
            return ('builtin', _arr_find)
        if member == 'findIndex':
            def _arr_find_index(args, ctx):
                for i, item in enumerate(obj):
                    if self._call_function(args[0], [item]):
                        return i
                return -1
            return ('builtin', _arr_find_index)
        if member == 'sort':
            return ('builtin', lambda args, ctx: sorted(obj))
        if member in ('every', 'all'):
            def _arr_every(args, ctx):
                return all(self._call_function(args[0], [item]) for item in obj)
            return ('builtin', _arr_every)
        if member in ('some', 'any'):
            def _arr_some(args, ctx):
                return any(self._call_function(args[0], [item]) for item in obj)
            return ('builtin', _arr_some)
        if member == 'flat':
            def _arr_flat(args, ctx):
                result = []
                for item in obj:
                    if isinstance(item, list):
                        result.extend(item)
                    else:
                        result.append(item)
                return result
            return ('builtin', _arr_flat)
        if member == 'flatMap':
            def _arr_flat_map(args, ctx):
                result = []
                for item in obj:
                    mapped = self._call_function(args[0], [item])
                    if isinstance(mapped, list):
                        result.extend(mapped)
                    else:
                        result.append(mapped)
                return result
            return ('builtin', _arr_flat_map)
        if member == 'enumerate':
            return ('builtin', lambda args, ctx: [[i, v] for i, v in enumerate(obj)])
        if member == 'take':
            return ('builtin', lambda args, ctx: obj[:int(args[0])])
        if member == 'skip':
            return ('builtin', lambda args, ctx: obj[int(args[0]):])
        if member == 'unique':
            def _arr_unique(args, ctx):
                seen = []
                for item in obj:
                    if item not in seen:
                        seen.append(item)
                return seen
            return ('builtin', _arr_unique)
        if member == 'count':
            def _arr_count(args, ctx):
                return sum(1 for item in obj if self._call_function(args[0], [item]))
            return ('builtin', _arr_count)
        if member == 'sortBy':
            def _arr_sort_by(args, ctx):
                return sorted(obj, key=lambda item: self._call_function(args[0], [item]))
            return ('builtin', _arr_sort_by)
        if member == 'groupBy':
            def _arr_group_by(args, ctx):
                groups = {}
                for item in obj:
                    key = self._call_function(args[0], [item])
                    if key not in groups:
                        groups[key] = []
                    groups[key].append(item)
                return groups
            return ('builtin', _arr_group_by)
        if member == 'min':
            return ('builtin', lambda args, ctx: min(obj))
        if member == 'max':
            return ('builtin', lambda args, ctx: max(obj))
        if member == 'sum':
            return ('builtin', lambda args, ctx: sum(obj))
        if member == 'first':
            return ('builtin', lambda args, ctx: obj[0] if obj else None)
        if member == 'last':
            return ('builtin', lambda args, ctx: obj[-1] if obj else None)
        if member == 'isEmpty':
            return ('builtin', lambda args, ctx: len(obj) == 0)
        if member == 'zip':
            return ('builtin', lambda args, ctx: [
                [a, b] for a, b in zip(obj, args[0])
            ])
        if member == 'compact':
            return ('builtin', lambda args, ctx: [x for x in obj if x is not None])
        if member == 'chunked':
            def _arr_chunked(args, ctx):
                n = int(args[0])
                return [obj[i:i + n] for i in range(0, len(obj), n)]
            return ('builtin', _arr_chunked)
        if member == 'rotate':
            def _arr_rotate(args, ctx):
                n = int(args[0])
                if not obj:
                    return []
                n = n % len(obj)
                return obj[-n:] + obj[:-n] if n else list(obj)
            return ('builtin', _arr_rotate)
        if member == 'window':
            def _arr_window(args, ctx):
                size = int(args[0])
                return [obj[i:i + size] for i in range(len(obj) - size + 1)]
            return ('builtin', _arr_window)
        if member == 'partition':
            def _arr_partition(args, ctx):
                yes, no = [], []
                for item in obj:
                    (yes if self._call_function(args[0], [item]) else no).append(item)
                return [yes, no]
            return ('builtin', _arr_partition)
        if member == 'findLast':
            def _arr_find_last(args, ctx):
                for item in reversed(obj):
                    if self._call_function(args[0], [item]):
                        return item
                return None
            return ('builtin', _arr_find_last)
        if member == 'findLastIndex':
            def _arr_find_last_index(args, ctx):
                for i in range(len(obj) - 1, -1, -1):
                    if self._call_function(args[0], [obj[i]]):
                        return i
                return -1
            return ('builtin', _arr_find_last_index)
        if member == 'tally':
            def _arr_tally(args, ctx):
                counts = {}
                for item in obj:
                    counts[item] = counts.get(item, 0) + 1
                return counts
            return ('builtin', _arr_tally)
        if member == 'pairwise':
            return ('builtin', lambda args, ctx: [[obj[i], obj[i + 1]] for i in range(len(obj) - 1)])
        if member == 'interleave':
            def _arr_interleave(args, ctx):
                other = args[0]
                result = []
                i = j = 0
                while i < len(obj) or j < len(other):
                    if i < len(obj):
                        result.append(obj[i])
                        i += 1
                    if j < len(other):
                        result.append(other[j])
                        j += 1
                return result
            return ('builtin', _arr_interleave)
        if member == 'flatten':
            def _arr_flatten(args, ctx):
                depth = int(args[0]) if args else 1
                def _flat(arr, d):
                    result = []
                    for item in arr:
                        if isinstance(item, list) and d > 0:
                            result.extend(_flat(item, d - 1))
                        else:
                            result.append(item)
                    return result
                return _flat(obj, depth)
            return ('builtin', _arr_flatten)
        if member == 'takeWhile':
            def _arr_take_while(args, ctx):
                result = []
                for item in obj:
                    if not self._call_function(args[0], [item]):
                        break
                    result.append(item)
                return result
            return ('builtin', _arr_take_while)
        if member == 'skipWhile':
            def _arr_skip_while(args, ctx):
                i = 0
                while i < len(obj) and self._call_function(args[0], [obj[i]]):
                    i += 1
                return obj[i:]
            return ('builtin', _arr_skip_while)
        if member == 'scan':
            def _arr_scan(args, ctx):
                result = []
                acc = args[1]
                for item in obj:
                    acc = self._call_function(args[0], [acc, item])
                    result.append(acc)
                return result
            return ('builtin', _arr_scan)
        if member == 'product':
            def _arr_product(args, ctx):
                result = 1
                for item in obj:
                    result = result * item
                return result
            return ('builtin', _arr_product)
        if member == 'mapIndexed':
            def _arr_map_indexed(args, ctx):
                return [self._call_function(args[0], [i, item]) for i, item in enumerate(obj)]
            return ('builtin', _arr_map_indexed)
        if member == 'average':
            def _arr_average(args, ctx):
                total = sum(obj)
                result = total / len(obj)
                return int(result) if result == int(result) else result
            return ('builtin', _arr_average)
        if member == 'none':
            def _arr_none(args, ctx):
                return not any(self._call_function(args[0], [item]) for item in obj)
            return ('builtin', _arr_none)
        if member == 'without':
            return ('builtin', lambda args, ctx: [x for x in obj if x not in args[0]])
        if member == 'head':
            return ('builtin', lambda args, ctx: obj[:int(args[0])])
        if member == 'tail':
            return ('builtin', lambda args, ctx: obj[-int(args[0]):] if int(args[0]) <= len(obj) else list(obj))
        if member == 'reject':
            def _arr_reject(args, ctx):
                return [item for item in obj if not self._call_function(args[0], [item])]
            return ('builtin', _arr_reject)
        if member == 'intersection':
            return ('builtin', lambda args, ctx: [x for x in obj if x in args[0]])
        if member == 'union':
            def _arr_union(args, ctx):
                seen = []
                for item in obj + args[0]:
                    if item not in seen:
                        seen.append(item)
                return seen
            return ('builtin', _arr_union)
        if member == 'sample':
            return ('builtin', lambda args, ctx: random.sample(list(obj), min(int(args[0]), len(obj))))
        if member == 'shuffle':
            def _arr_shuffle(args, ctx):
                copy = list(obj)
                random.shuffle(copy)
                return copy
            return ('builtin', _arr_shuffle)
        if member == 'difference':
            return ('builtin', lambda args, ctx: [x for x in obj if x not in args[0]])
        if member == 'sortDescending':
            return ('builtin', lambda args, ctx: sorted(obj, reverse=True))
        if member == 'forEachIndexed':
            def _arr_foreach_indexed(args, ctx):
                for i, item in enumerate(obj):
                    self._call_function(args[0], [i, item])
                return None
            return ('builtin', _arr_foreach_indexed)
        if member == 'symmetricDifference':
            def _arr_sym_diff(args, ctx):
                other = args[0]
                return [x for x in obj if x not in other] + [x for x in other if x not in obj]
            return ('builtin', _arr_sym_diff)
        if member == 'at':
            def _arr_at(args, ctx):
                idx = int(args[0])
                return obj[idx] if -len(obj) <= idx < len(obj) else None
            return ('builtin', _arr_at)
        if member == 'associate':
            def _arr_associate(args, ctx):
                result = {}
                for item in obj:
                    pair = self._call_function(args[0], [item])
                    result[pair[0]] = pair[1]
                return result
            return ('builtin', _arr_associate)
        if member == 'toString':
            return ('builtin', lambda args, ctx: silk_repr(obj))
        if member == 'frequencies':
            def _frequencies(args, ctx):
                result = {}
                for item in obj:
                    key = item
                    result[key] = result.get(key, 0) + 1
                return result
            return ('builtin', _frequencies)
        if member == 'chunk':
            def _chunk(args, ctx):
                size = int(args[0])
                return [obj[i:i + size] for i in range(0, len(obj), size)]
            return ('builtin', _chunk)
        raise RuntimeError_(f"'list' has no member '{member}'")

    def _eval_string_member(self, obj: str, member: str) -> Any:
        """Evaluate member access on a string."""
        if member == 'length':
            return len(obj)
        if member in ('upper', 'toUpper'):
            return ('builtin', lambda args, ctx: obj.upper())
        if member in ('lower', 'toLower'):
            return ('builtin', lambda args, ctx: obj.lower())
        if member in ('strip', 'trim'):
            return ('builtin', lambda args, ctx: obj.strip())
        if member == 'trim_start':
            return ('builtin', lambda args, ctx: obj.lstrip())
        if member == 'trim_end':
            return ('builtin', lambda args, ctx: obj.rstrip())
        if member == 'replace':
            return ('builtin', lambda args, ctx: obj.replace(args[0], args[1]))
        if member == 'starts_with':
            return ('builtin', lambda args, ctx: obj.startswith(args[0]))
        if member == 'ends_with':
            return ('builtin', lambda args, ctx: obj.endswith(args[0]))
        if member == 'contains':
            return ('builtin', lambda args, ctx: args[0] in obj)
        if member == 'split':
            return ('builtin', lambda args, ctx: obj.split(args[0] if args else " "))
        if member == 'chars':
            return ('builtin', lambda args, ctx: list(obj))
        if member == 'indexOf':
            return ('builtin', lambda args, ctx: obj.find(args[0]))
        if member in ('substring', 'slice'):
            def _substring(args, ctx):
                start = int(args[0])
                if len(args) > 1:
                    return obj[start:int(args[1])]
                return obj[start:]
            return ('builtin', _substring)
        if member == 'repeat':
            return ('builtin', lambda args, ctx: obj * int(args[0]))
        if member == 'padStart':
            return ('builtin', lambda args, ctx: obj.rjust(int(args[0]), args[1]))
        if member == 'padEnd':
            return ('builtin', lambda args, ctx: obj.ljust(int(args[0]), args[1]))
        if member == 'toInt':
            def _to_int(args, ctx):
                try:
                    return int(obj)
                except ValueError:
                    raise RuntimeError_(f"Cannot convert '{obj}' to int")
            return ('builtin', _to_int)
        if member == 'toFloat':
            def _to_float(args, ctx):
                try:
                    val = float(obj)
                    return int(val) if val == int(val) else val
                except ValueError:
                    raise RuntimeError_(f"Cannot convert '{obj}' to float")
            return ('builtin', _to_float)
        if member == 'reverse':
            return ('builtin', lambda args, ctx: obj[::-1])
        if member == 'isEmpty':
            return ('builtin', lambda args, ctx: len(obj) == 0)
        if member == 'replaceAll':
            return ('builtin', lambda args, ctx: obj.replace(args[0], args[1]))
        if member == 'includes':
            return ('builtin', lambda args, ctx: args[0] in obj)
        if member == 'charAt':
            return ('builtin', lambda args, ctx: obj[int(args[0])])
        if member == 'charCodeAt':
            return ('builtin', lambda args, ctx: ord(obj[int(args[0])]))
        if member == 'count':
            return ('builtin', lambda args, ctx: obj.count(args[0]))
        if member == 'isDigit':
            return ('builtin', lambda args, ctx: len(obj) > 0 and obj.isdigit())
        if member == 'isAlpha':
            return ('builtin', lambda args, ctx: len(obj) > 0 and obj.isalpha())
        if member == 'title':
            return ('builtin', lambda args, ctx: obj.title())
        if member == 'capitalize':
            return ('builtin', lambda args, ctx: obj.capitalize())
        if member == 'words':
            return ('builtin', lambda args, ctx: obj.split())
        if member == 'center':
            return ('builtin', lambda args, ctx: obj.center(int(args[0]), args[1]))
        if member == 'lines':
            return ('builtin', lambda args, ctx: obj.split('\n'))
        if member == 'format':
            def _format(args, ctx):
                result = obj
                for arg in args:
                    result = result.replace('{}', silk_repr(arg), 1)
                return result
            return ('builtin', _format)
        if member == 'removePrefix':
            def _remove_prefix(args, ctx):
                return obj[len(args[0]):] if obj.startswith(args[0]) else obj
            return ('builtin', _remove_prefix)
        if member == 'removeSuffix':
            def _remove_suffix(args, ctx):
                return obj[:-len(args[0])] if obj.endswith(args[0]) else obj
            return ('builtin', _remove_suffix)
        if member == 'truncate':
            def _truncate(args, ctx):
                max_len = int(args[0])
                suffix = args[1] if len(args) > 1 else ""
                if len(obj) <= max_len:
                    return obj
                return obj[:max_len - len(suffix)] + suffix
            return ('builtin', _truncate)
        if member == 'isUpper':
            return ('builtin', lambda args, ctx: len(obj) > 0 and obj.isupper())
        if member == 'isLower':
            return ('builtin', lambda args, ctx: len(obj) > 0 and obj.islower())
        if member == 'isNumeric':
            def _is_numeric(args, ctx):
                if not obj:
                    return False
                try:
                    float(obj)
                    return True
                except ValueError:
                    return False
            return ('builtin', _is_numeric)
        if member == 'wrap':
            return ('builtin', lambda args, ctx: args[0] + obj + args[1])
        if member == 'lastIndexOf':
            return ('builtin', lambda args, ctx: obj.rfind(args[0]))
        if member == 'squeeze':
            def _squeeze(args, ctx):
                import re
                return re.sub(r' {2,}', ' ', obj)
            return ('builtin', _squeeze)
        if member == 'mask':
            def _mask(args, ctx):
                char, keep = args[0], int(args[1])
                if len(obj) <= keep:
                    return obj
                return char * (len(obj) - keep) + obj[-keep:]
            return ('builtin', _mask)
        if member == 'at':
            def _str_at(args, ctx):
                idx = int(args[0])
                return obj[idx] if -len(obj) <= idx < len(obj) else None
            return ('builtin', _str_at)
        if member == 'replaceFirst':
            return ('builtin', lambda args, ctx: obj.replace(args[0], args[1], 1))
        if member == 'isBlank':
            return ('builtin', lambda args, ctx: len(obj.strip()) == 0)
        if member == 'swapCase':
            return ('builtin', lambda args, ctx: obj.swapcase())
        if member == 'zfill':
            return ('builtin', lambda args, ctx: obj.zfill(int(args[0])))
        if member == 'camelCase':
            def _camel(args, ctx):
                import re
                parts = re.split(r'[-_\s]+', obj)
                return parts[0].lower() + ''.join(w.capitalize() for w in parts[1:])
            return ('builtin', _camel)
        if member == 'snakeCase':
            def _snake(args, ctx):
                import re
                s = re.sub(r'[-\s]+', '_', obj)
                s = re.sub(r'([a-z])([A-Z])', r'\1_\2', s)
                return s.lower()
            return ('builtin', _snake)
        raise RuntimeError_(f"'str' has no member '{member}'")

    def _eval_number_member(self, obj: int | float, member: str) -> Any:
        """Evaluate member access on a number."""
        _simple = {
            'abs': lambda: abs(obj), 'floor': lambda: math.floor(obj),
            'ceil': lambda: math.ceil(obj), 'round': lambda: round(obj),
            'toString': lambda: str(obj), 'sqrt': lambda: math.sqrt(obj),
            'isEven': lambda: int(obj) % 2 == 0, 'isOdd': lambda: int(obj) % 2 != 0,
            'isPositive': lambda: obj > 0, 'isNegative': lambda: obj < 0,
            'isZero': lambda: obj == 0, 'isInteger': lambda: isinstance(obj, int),
            'isFloat': lambda: isinstance(obj, float),
            'sign': lambda: (1 if obj > 0 else (-1 if obj < 0 else 0)),
            'toRadians': lambda: obj * math.pi / 180,
            'toDegrees': lambda: obj * 180 / math.pi,
            'factorial': lambda: math.factorial(int(obj)),
        }
        if member in _simple:
            fn = _simple[member]
            return ('builtin', lambda args, ctx: fn())
        if member == 'clamp':
            return ('builtin', lambda args, ctx: max(args[0], min(obj, args[1])))
        if member == 'clampMin':
            return ('builtin', lambda args, ctx: max(obj, args[0]))
        if member == 'clampMax':
            return ('builtin', lambda args, ctx: min(obj, args[0]))
        if member == 'toFixed':
            return ('builtin', lambda args, ctx: f"{obj:.{int(args[0])}f}")
        if member == 'pow':
            return ('builtin', lambda args, ctx: obj ** int(args[0]))
        if member == 'isBetween':
            return ('builtin', lambda args, ctx: args[0] <= obj <= args[1])
        if member == 'lerp':
            def _lerp(args, ctx):
                result = obj + (args[0] - obj) * args[1]
                return int(result) if result == int(result) else result
            return ('builtin', _lerp)
        if member == 'map':
            return ('builtin', lambda args, ctx: self._call_function(args[0], [obj]))
        if member in ('percent', 'percentOf'):
            def _pct(args, ctx):
                result = (obj / 100) if member == 'percent' else (obj * args[0] / 100)
                return int(result) if result == int(result) else result
            return ('builtin', _pct)
        if member == 'toPercent':
            def _to_percent(args, ctx):
                val = round(obj * 100, 10)
                return f"{int(val) if val == int(val) else val}%"
            return ('builtin', _to_percent)
        raise RuntimeError_(f"'number' has no member '{member}'")

    def _eval_method(self, obj: Any, method: str, args: list, env: 'Environment | None' = None) -> Any:
        """Evaluate method call."""
        member = self._eval_member(obj, method, env)
        if isinstance(member, tuple) and member[0] == 'builtin':
            context = {'output_lines': self.output_lines}
            return member[1](args, context)
        if isinstance(member, tuple) and member[0] == 'bound_method':
            _, func, self_obj = member
            return self._call_function(func, [self_obj] + args)
        if isinstance(member, tuple) and member[0] == 'function':
            return self._call_function(member, args)
        return member
