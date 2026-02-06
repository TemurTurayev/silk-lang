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
        if member in ('length', 'size'):
            return len(obj)
        _noarg = {
            'keys': lambda: list(obj.keys()), 'values': lambda: list(obj.values()),
            'isEmpty': lambda: len(obj) == 0, 'clear': lambda: {},
            'invert': lambda: {v: k for k, v in obj.items()},
            'toSortedArray': lambda: [[k, obj[k]] for k in sorted(obj.keys())],
            'sortByValue': lambda: [[k, v] for k, v in sorted(obj.items(), key=lambda x: x[1])],
            'toQueryString': lambda: '&'.join(f"{k}={v}" for k, v in obj.items()),
            'toFormattedString': lambda: ', '.join(f"{k}: {silk_repr(v)}" for k, v in obj.items()),
        }
        if member in _noarg:
            fn = _noarg[member]
            return ('builtin', lambda args, ctx: fn())
        _onearg = {
            'has': lambda a: a[0] in obj, 'delete': lambda a: obj.pop(a[0], None),
            'pick': lambda a: {k: obj[k] for k in a[0] if k in obj},
            'omit': lambda a: {k: v for k, v in obj.items() if k not in a[0]},
            'defaults': lambda a: {**a[0], **obj},
        }
        if member in ('entries', 'toArray'):
            return ('builtin', lambda args, ctx: [[k, v] for k, v in obj.items()])
        if member in ('merge', 'update'):
            return ('builtin', lambda args, ctx: {**obj, **args[0]})
        if member in _onearg:
            fn = _onearg[member]
            return ('builtin', lambda args, ctx: fn(args))
        if member == 'get':
            return ('builtin', lambda args, ctx: obj.get(args[0], args[1] if len(args) > 1 else None))
        if member == 'forEach':
            def _fe(args, ctx):
                for k, v in obj.items():
                    self._call_function(args[0], [k, v])
            return ('builtin', _fe)
        if member == 'filter':
            return ('builtin', lambda args, ctx: {k: v for k, v in obj.items() if self._call_function(args[0], [k, v])})
        if member == 'map':
            return ('builtin', lambda args, ctx: {k: self._call_function(args[0], [k, v]) for k, v in obj.items()})
        if member == 'count':
            return ('builtin', lambda args, ctx: sum(1 for k, v in obj.items() if self._call_function(args[0], [k, v])))
        if member == 'mapValues':
            return ('builtin', lambda args, ctx: {k: self._call_function(args[0], [v]) for k, v in obj.items()})
        if member == 'mapKeys':
            return ('builtin', lambda args, ctx: {self._call_function(args[0], [k]): v for k, v in obj.items()})
        if member == 'filterValues':
            return ('builtin', lambda args, ctx: {k: v for k, v in obj.items() if self._call_function(args[0], [v])})
        if member == 'filterKeys':
            return ('builtin', lambda args, ctx: {k: v for k, v in obj.items() if self._call_function(args[0], [k])})
        if member == 'every':
            return ('builtin', lambda args, ctx: all(self._call_function(args[0], [k, v]) for k, v in obj.items()))
        if member == 'some':
            return ('builtin', lambda args, ctx: any(self._call_function(args[0], [k, v]) for k, v in obj.items()))
        if member in ('findKey', 'findValue'):
            def _find(args, ctx):
                for k, v in obj.items():
                    if self._call_function(args[0], [k, v]):
                        return k if member == 'findKey' else v
            return ('builtin', _find)
        if member == 'toJson':
            def _to_json(args, ctx):
                def _c(v):
                    if isinstance(v, (type(None), bool, int, float, str)):
                        return v
                    if isinstance(v, list):
                        return [_c(i) for i in v]
                    if isinstance(v, dict):
                        return {str(k): _c(val) for k, val in v.items()}
                    return str(v)
                return json.dumps(_c(obj))
            return ('builtin', _to_json)
        if member == 'mapEntries':
            def _me(args, ctx):
                return {(p := self._call_function(args[0], [k, v]))[0]: p[1] for k, v in obj.items()}
            return ('builtin', _me)
        if member == 'flatMap':
            def _fm(args, ctx):
                return [x for k, v in obj.items() for x in self._call_function(args[0], [k, v])]
            return ('builtin', _fm)
        if member == 'groupByValue':
            def _gbv(args, ctx):
                groups = {}
                for k, v in obj.items():
                    groups.setdefault(v, []).append(k)
                return groups
            return ('builtin', _gbv)
        raise RuntimeError_(f"'dict' has no member '{member}'")

    def _eval_list_member(self, obj: list, member: str) -> Any:
        """Evaluate member access on a list."""
        if member == 'length':
            return len(obj)
        # No-arg methods
        _noarg = {
            'pop': lambda: obj.pop(), 'reverse': lambda: obj[::-1],
            'sort': lambda: sorted(obj), 'sortDescending': lambda: sorted(obj, reverse=True),
            'min': lambda: min(obj), 'max': lambda: max(obj), 'sum': lambda: sum(obj),
            'first': lambda: obj[0] if obj else None, 'last': lambda: obj[-1] if obj else None,
            'isEmpty': lambda: len(obj) == 0, 'compact': lambda: [x for x in obj if x is not None],
            'enumerate': lambda: [[i, v] for i, v in enumerate(obj)],
            'pairwise': lambda: [[obj[i], obj[i + 1]] for i in range(len(obj) - 1)],
            'toString': lambda: silk_repr(obj),
            'zipWithIndex': lambda: [[v, i] for i, v in enumerate(obj)],
        }
        if member in _noarg:
            fn = _noarg[member]
            return ('builtin', lambda args, ctx: fn())
        # Simple one-arg methods
        _onearg = {
            'push': lambda a: obj.append(a[0]) or obj,
            'contains': lambda a: a[0] in obj,
            'join': lambda a: a[0].join(silk_repr(item) for item in obj),
            'take': lambda a: obj[:int(a[0])], 'head': lambda a: obj[:int(a[0])],
            'skip': lambda a: obj[int(a[0]):],
            'tail': lambda a: obj[-int(a[0]):] if int(a[0]) <= len(obj) else list(obj),
            'without': lambda a: [x for x in obj if x not in a[0]],
            'difference': lambda a: [x for x in obj if x not in a[0]],
            'intersection': lambda a: [x for x in obj if x in a[0]],
            'zip': lambda a: [[x, y] for x, y in zip(obj, a[0])],
            'sample': lambda a: random.sample(list(obj), min(int(a[0]), len(obj))),
        }
        if member in _onearg:
            fn = _onearg[member]
            return ('builtin', lambda args, ctx: fn(args))
        if member == 'slice':
            return ('builtin', lambda args, ctx: obj[int(args[0]):int(args[1])])
        if member == 'indexOf':
            def _index_of(args, ctx):
                try:
                    return obj.index(args[0])
                except ValueError:
                    return -1
            return ('builtin', _index_of)
        if member == 'map':
            return ('builtin', lambda args, ctx: [self._call_function(args[0], [item]) for item in obj])
        if member == 'filter':
            return ('builtin', lambda args, ctx: [item for item in obj if self._call_function(args[0], [item])])
        if member == 'forEach':
            def _fe(args, ctx):
                for item in obj:
                    self._call_function(args[0], [item])
            return ('builtin', _fe)
        if member == 'reduce':
            def _reduce(args, ctx):
                acc = args[1]
                for item in obj:
                    acc = self._call_function(args[0], [acc, item])
                return acc
            return ('builtin', _reduce)
        if member == 'find':
            def _find(args, ctx):
                for item in obj:
                    if self._call_function(args[0], [item]):
                        return item
            return ('builtin', _find)
        if member == 'findIndex':
            def _fi(args, ctx):
                for i, item in enumerate(obj):
                    if self._call_function(args[0], [item]):
                        return i
                return -1
            return ('builtin', _fi)
        if member in ('every', 'all'):
            return ('builtin', lambda args, ctx: all(self._call_function(args[0], [item]) for item in obj))
        if member in ('some', 'any'):
            return ('builtin', lambda args, ctx: any(self._call_function(args[0], [item]) for item in obj))
        if member == 'flat':
            def _flat(args, ctx):
                result = []
                for item in obj:
                    (result.extend if isinstance(item, list) else result.append)(item)
                return result
            return ('builtin', _flat)
        if member == 'flatMap':
            def _flat_map(args, ctx):
                result = []
                for item in obj:
                    mapped = self._call_function(args[0], [item])
                    (result.extend if isinstance(mapped, list) else result.append)(mapped)
                return result
            return ('builtin', _flat_map)
        if member == 'unique':
            def _unique(args, ctx):
                seen = []
                for item in obj:
                    if item not in seen:
                        seen.append(item)
                return seen
            return ('builtin', _unique)
        if member == 'count':
            return ('builtin', lambda args, ctx: sum(1 for item in obj if self._call_function(args[0], [item])))
        if member == 'sortBy':
            return ('builtin', lambda args, ctx: sorted(obj, key=lambda item: self._call_function(args[0], [item])))
        if member == 'groupBy':
            def _group_by(args, ctx):
                groups = {}
                for item in obj:
                    key = self._call_function(args[0], [item])
                    groups.setdefault(key, []).append(item)
                return groups
            return ('builtin', _group_by)
        if member in ('chunked', 'chunk'):
            return ('builtin', lambda args, ctx: [obj[i:i+int(args[0])] for i in range(0, len(obj), int(args[0]))])
        if member in ('window', 'windowed'):
            return ('builtin', lambda args, ctx: [obj[i:i+int(args[0])] for i in range(len(obj) - int(args[0]) + 1)])
        if member == 'rotate':
            def _rotate(args, ctx):
                n = int(args[0])
                if not obj:
                    return []
                n = n % len(obj)
                return obj[-n:] + obj[:-n] if n else list(obj)
            return ('builtin', _rotate)
        if member == 'partition':
            def _partition(args, ctx):
                yes, no = [], []
                for item in obj:
                    (yes if self._call_function(args[0], [item]) else no).append(item)
                return [yes, no]
            return ('builtin', _partition)
        if member == 'findLast':
            def _find_last(args, ctx):
                for item in reversed(obj):
                    if self._call_function(args[0], [item]):
                        return item
            return ('builtin', _find_last)
        if member == 'findLastIndex':
            def _fli(args, ctx):
                for i in range(len(obj) - 1, -1, -1):
                    if self._call_function(args[0], [obj[i]]):
                        return i
                return -1
            return ('builtin', _fli)
        if member in ('tally', 'frequencies'):
            def _tally(args, ctx):
                counts = {}
                for item in obj:
                    counts[item] = counts.get(item, 0) + 1
                return counts
            return ('builtin', _tally)
        if member == 'interleave':
            def _interleave(args, ctx):
                other, result, i, j = args[0], [], 0, 0
                while i < len(obj) or j < len(other):
                    if i < len(obj):
                        result.append(obj[i]); i += 1
                    if j < len(other):
                        result.append(other[j]); j += 1
                return result
            return ('builtin', _interleave)
        if member == 'flatten':
            def _flatten(args, ctx):
                depth = int(args[0]) if args else 1
                def _f(arr, d):
                    result = []
                    for item in arr:
                        if isinstance(item, list) and d > 0:
                            result.extend(_f(item, d - 1))
                        else:
                            result.append(item)
                    return result
                return _f(obj, depth)
            return ('builtin', _flatten)
        if member == 'takeWhile':
            def _tw(args, ctx):
                result = []
                for item in obj:
                    if not self._call_function(args[0], [item]):
                        break
                    result.append(item)
                return result
            return ('builtin', _tw)
        if member == 'skipWhile':
            def _sw(args, ctx):
                i = 0
                while i < len(obj) and self._call_function(args[0], [obj[i]]):
                    i += 1
                return obj[i:]
            return ('builtin', _sw)
        if member == 'scan':
            def _scan(args, ctx):
                result, acc = [], args[1]
                for item in obj:
                    acc = self._call_function(args[0], [acc, item])
                    result.append(acc)
                return result
            return ('builtin', _scan)
        if member == 'product':
            def _product(args, ctx):
                r = 1
                for item in obj:
                    r *= item
                return r
            return ('builtin', _product)
        if member == 'mapIndexed':
            return ('builtin', lambda args, ctx: [self._call_function(args[0], [i, item]) for i, item in enumerate(obj)])
        if member == 'average':
            def _avg(args, ctx):
                result = sum(obj) / len(obj)
                return int(result) if result == int(result) else result
            return ('builtin', _avg)
        if member == 'none':
            return ('builtin', lambda args, ctx: not any(self._call_function(args[0], [item]) for item in obj))
        if member == 'reject':
            return ('builtin', lambda args, ctx: [item for item in obj if not self._call_function(args[0], [item])])
        if member == 'union':
            def _union(args, ctx):
                seen = []
                for item in obj + args[0]:
                    if item not in seen:
                        seen.append(item)
                return seen
            return ('builtin', _union)
        if member == 'shuffle':
            def _shuffle(args, ctx):
                copy = list(obj)
                random.shuffle(copy)
                return copy
            return ('builtin', _shuffle)
        if member == 'forEachIndexed':
            def _fei(args, ctx):
                for i, item in enumerate(obj):
                    self._call_function(args[0], [i, item])
            return ('builtin', _fei)
        if member == 'symmetricDifference':
            def _sd(args, ctx):
                other = args[0]
                return [x for x in obj if x not in other] + [x for x in other if x not in obj]
            return ('builtin', _sd)
        if member == 'at':
            return ('builtin', lambda args, ctx: obj[int(args[0])] if -len(obj) <= int(args[0]) < len(obj) else None)
        if member == 'associate':
            def _assoc(args, ctx):
                result = {}
                for item in obj:
                    pair = self._call_function(args[0], [item])
                    result[pair[0]] = pair[1]
                return result
            return ('builtin', _assoc)
        if member == 'interpose':
            def _interpose(args, ctx):
                if len(obj) <= 1:
                    return list(obj)
                result = [obj[0]]
                for item in obj[1:]:
                    result.append(args[0]); result.append(item)
                return result
            return ('builtin', _interpose)
        if member == 'transpose':
            return ('builtin', lambda args, ctx: [list(row) for row in zip(*obj)])
        if member == 'combinations':
            def _combinations(args, ctx):
                from itertools import combinations as _c
                return [list(c) for c in _c(obj, int(args[0]))]
            return ('builtin', _combinations)
        if member == 'permutations':
            def _permutations(args, ctx):
                from itertools import permutations as _p
                return [list(p) for p in _p(obj)]
            return ('builtin', _permutations)
        if member == 'median':
            def _median(args, ctx):
                s = sorted(obj)
                n = len(s)
                if n % 2 == 1:
                    return s[n // 2]
                mid = s[n // 2 - 1] + s[n // 2]
                return mid / 2 if mid % 2 else mid // 2
            return ('builtin', _median)
        if member == 'mode':
            def _mode(args, ctx):
                counts = {}
                for item in obj:
                    counts[item] = counts.get(item, 0) + 1
                max_count = max(counts.values())
                return [k for k, v in counts.items() if v == max_count]
            return ('builtin', _mode)
        if member == 'stddev':
            def _stddev(args, ctx):
                mean = sum(obj) / len(obj)
                variance = sum((x - mean) ** 2 for x in obj) / len(obj)
                result = variance ** 0.5
                return int(result) if result == int(result) else result
            return ('builtin', _stddev)
        raise RuntimeError_(f"'list' has no member '{member}'")

    def _eval_string_member(self, obj: str, member: str) -> Any:
        """Evaluate member access on a string."""
        if member == 'length':
            return len(obj)
        # No-arg methods (return lambdas that ignore args)
        _noarg = {
            'upper': lambda: obj.upper(), 'toUpper': lambda: obj.upper(),
            'lower': lambda: obj.lower(), 'toLower': lambda: obj.lower(),
            'strip': lambda: obj.strip(), 'trim': lambda: obj.strip(),
            'trim_start': lambda: obj.lstrip(), 'trim_end': lambda: obj.rstrip(),
            'chars': lambda: list(obj), 'reverse': lambda: obj[::-1],
            'isEmpty': lambda: len(obj) == 0, 'words': lambda: obj.split(),
            'lines': lambda: obj.split('\n'), 'title': lambda: obj.title(),
            'capitalize': lambda: obj.capitalize(), 'swapCase': lambda: obj.swapcase(),
            'isDigit': lambda: len(obj) > 0 and obj.isdigit(),
            'isAlpha': lambda: len(obj) > 0 and obj.isalpha(),
            'isUpper': lambda: len(obj) > 0 and obj.isupper(),
            'isLower': lambda: len(obj) > 0 and obj.islower(),
            'isBlank': lambda: len(obj.strip()) == 0,
            'isAlphanumeric': lambda: len(obj) > 0 and obj.isalnum(),
            'rot13': lambda: ''.join(chr((ord(c) - (65 if c.isupper() else 97) + 13) % 26 + (65 if c.isupper() else 97)) if c.isalpha() else c for c in obj),
            'isPalindrome': lambda: obj == obj[::-1],
        }
        if member in _noarg:
            fn = _noarg[member]
            return ('builtin', lambda args, ctx: fn())
        # Single-arg methods
        _onearg = {
            'contains': lambda a: a[0] in obj, 'includes': lambda a: a[0] in obj,
            'starts_with': lambda a: obj.startswith(a[0]),
            'ends_with': lambda a: obj.endswith(a[0]),
            'indexOf': lambda a: obj.find(a[0]),
            'lastIndexOf': lambda a: obj.rfind(a[0]),
            'count': lambda a: obj.count(a[0]),
            'split': lambda a: obj.split(a[0] if a else " "),
            'repeat': lambda a: obj * int(a[0]),
            'charAt': lambda a: obj[int(a[0])],
            'charCodeAt': lambda a: ord(obj[int(a[0])]),
            'zfill': lambda a: obj.zfill(int(a[0])),
        }
        if member in _onearg:
            fn = _onearg[member]
            return ('builtin', lambda args, ctx: fn(args))
        # Two-arg methods
        _twoarg = {
            'replace': lambda a: obj.replace(a[0], a[1]),
            'replaceAll': lambda a: obj.replace(a[0], a[1]),
            'replaceFirst': lambda a: obj.replace(a[0], a[1], 1),
            'padStart': lambda a: obj.rjust(int(a[0]), a[1]),
            'padEnd': lambda a: obj.ljust(int(a[0]), a[1]),
            'center': lambda a: obj.center(int(a[0]), a[1]),
            'wrap': lambda a: a[0] + obj + a[1],
            'mask': lambda a: a[0] * (len(obj) - int(a[1])) + obj[-int(a[1]):] if len(obj) > int(a[1]) else obj,
            'padCenter': lambda a: obj.center(int(a[0]), a[1]),
        }
        if member in _twoarg:
            fn = _twoarg[member]
            return ('builtin', lambda args, ctx: fn(args))
        if member in ('substring', 'slice'):
            return ('builtin', lambda args, ctx: obj[int(args[0]):int(args[1])] if len(args) > 1 else obj[int(args[0]):])
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
        if member == 'format':
            def _format(args, ctx):
                result = obj
                for arg in args:
                    result = result.replace('{}', silk_repr(arg), 1)
                return result
            return ('builtin', _format)
        if member == 'removePrefix':
            return ('builtin', lambda args, ctx: obj[len(args[0]):] if obj.startswith(args[0]) else obj)
        if member == 'removeSuffix':
            return ('builtin', lambda args, ctx: obj[:-len(args[0])] if obj.endswith(args[0]) else obj)
        if member == 'truncate':
            def _truncate(args, ctx):
                max_len, suffix = int(args[0]), args[1] if len(args) > 1 else ""
                return obj if len(obj) <= max_len else obj[:max_len - len(suffix)] + suffix
            return ('builtin', _truncate)
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
        if member == 'squeeze':
            import re as _re
            return ('builtin', lambda args, ctx: _re.sub(r' {2,}', ' ', obj))
        if member == 'at':
            return ('builtin', lambda args, ctx: obj[int(args[0])] if -len(obj) <= int(args[0]) < len(obj) else None)
        if member in ('camelCase', 'snakeCase', 'kebabCase', 'titleCase'):
            import re as _re
            def _case_convert(args, ctx):
                parts = _re.split(r'[-_\s]+', obj)
                if member == 'camelCase':
                    return parts[0].lower() + ''.join(w.capitalize() for w in parts[1:])
                if member == 'titleCase':
                    return ' '.join(w.capitalize() for w in parts)
                s = _re.sub(r'[-_\s]+', '_' if member == 'snakeCase' else '-', obj)
                s = _re.sub(r'([a-z])([A-Z])', r'\1_\2' if member == 'snakeCase' else r'\1-\2', s)
                return s.lower()
            return ('builtin', _case_convert)
        if member == 'truncateWords':
            return ('builtin', lambda args, ctx: obj if len(w := obj.split()) <= int(args[0]) else ' '.join(w[:int(args[0])]) + '...')
        if member == 'isEmail':
            return ('builtin', lambda args, ctx: len(p := obj.split('@')) == 2 and len(p[0]) > 0 and '.' in p[1])
        if member == 'partition':
            return ('builtin', lambda args, ctx: list(obj.partition(args[0])))
        if member == 'commonPrefix':
            def _common_prefix(args, ctx):
                other = args[0]
                i = 0
                while i < len(obj) and i < len(other) and obj[i] == other[i]:
                    i += 1
                return obj[:i]
            return ('builtin', _common_prefix)
        if member == 'commonSuffix':
            def _common_suffix(args, ctx):
                other = args[0]
                i = 0
                while i < len(obj) and i < len(other) and obj[-(i+1)] == other[-(i+1)]:
                    i += 1
                return obj[len(obj)-i:] if i else ''
            return ('builtin', _common_suffix)
        if member == 'levenshtein':
            def _levenshtein(args, ctx):
                other = args[0]
                m, n = len(obj), len(other)
                if m == 0:
                    return n
                if n == 0:
                    return m
                prev = list(range(n + 1))
                for i in range(1, m + 1):
                    curr = [i] + [0] * n
                    for j in range(1, n + 1):
                        cost = 0 if obj[i-1] == other[j-1] else 1
                        curr[j] = min(curr[j-1] + 1, prev[j] + 1, prev[j-1] + cost)
                    prev = curr
                return prev[n]
            return ('builtin', _levenshtein)
        if member == 'hamming':
            return ('builtin', lambda args, ctx: sum(a != b for a, b in zip(obj, args[0])))
        if member == 'soundex':
            def _soundex(args, ctx):
                if not obj:
                    return ''
                codes = {'B':'1','F':'1','P':'1','V':'1','C':'2','G':'2','J':'2','K':'2',
                    'Q':'2','S':'2','X':'2','Z':'2','D':'3','T':'3','L':'4','M':'5',
                    'N':'5','R':'6'}
                result = obj[0].upper()
                prev = codes.get(obj[0].upper(), '0')
                for ch in obj[1:]:
                    code = codes.get(ch.upper(), '0')
                    if code != '0' and code != prev:
                        result += code
                    prev = code if code != '0' else prev
                return (result + '000')[:4]
            return ('builtin', _soundex)
        if member == 'isUrl':
            return ('builtin', lambda args, ctx: obj.startswith(('http://', 'https://')) and '.' in obj.split('//')[1])
        if member == 'caesar':
            def _caesar(args, ctx):
                shift = int(args[0])
                result = []
                for ch in obj:
                    if ch.isalpha():
                        base = ord('A') if ch.isupper() else ord('a')
                        result.append(chr((ord(ch) - base + shift) % 26 + base))
                    else:
                        result.append(ch)
                return ''.join(result)
            return ('builtin', _caesar)
        if member == 'charFrequency':
            def _char_freq(args, ctx):
                freq = {}
                for ch in obj:
                    freq[ch] = freq.get(ch, 0) + 1
                return freq
            return ('builtin', _char_freq)
        raise RuntimeError_(f"'str' has no member '{member}'")

    def _eval_number_member(self, obj: int | float, member: str) -> Any:
        """Evaluate member access on a number."""
        def _to_base(n, base):
            if n == 0:
                return '0'
            digits, neg = '0123456789abcdefghijklmnopqrstuvwxyz', n < 0
            n, result = abs(n), []
            while n:
                result.append(digits[n % base])
                n //= base
            return ('-' if neg else '') + ''.join(reversed(result))
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
            'toBinary': lambda: bin(int(obj))[2:],
            'toHex': lambda: hex(int(obj))[2:],
            'toChar': lambda: chr(int(obj)),
            'digitSum': lambda: sum(int(d) for d in str(abs(int(obj)))),
            'digitCount': lambda: len(str(abs(int(obj)))),
        }
        if member in _simple:
            fn = _simple[member]
            return ('builtin', lambda args, ctx: fn())
        _onearg = {
            'clampMin': lambda a: max(obj, a[0]), 'clampMax': lambda a: min(obj, a[0]),
            'toFixed': lambda a: f"{obj:.{int(a[0])}f}", 'pow': lambda a: obj ** int(a[0]),
            'gcd': lambda a: math.gcd(int(obj), int(a[0])),
            'lcm': lambda a: abs(int(obj) * int(a[0])) // math.gcd(int(obj), int(a[0])),
            'clamp': lambda a: max(a[0], min(obj, a[1])),
            'isBetween': lambda a: a[0] <= obj <= a[1],
            'toBase': lambda a: _to_base(int(obj), int(a[0])),
        }
        if member in _onearg:
            fn = _onearg[member]
            return ('builtin', lambda args, ctx: fn(args))
        if member == 'lerp':
            return ('builtin', lambda args, ctx: (lambda r: int(r) if r == int(r) else r)(obj + (args[0] - obj) * args[1]))
        if member == 'map':
            return ('builtin', lambda args, ctx: self._call_function(args[0], [obj]))
        if member in ('percent', 'percentOf'):
            def _pct(args, ctx):
                r = (obj / 100) if member == 'percent' else (obj * args[0] / 100)
                return int(r) if r == int(r) else r
            return ('builtin', _pct)
        if member == 'toPercent':
            return ('builtin', lambda args, ctx: f"{int(v) if (v := round(obj * 100, 10)) == int(v) else v}%")
        if member == 'toOrdinal':
            def _ordinal(args, ctx):
                n = int(obj)
                s = 'th' if 11 <= n % 100 <= 13 else ['th','st','nd','rd'][n % 10] if n % 10 < 4 else 'th'
                return f"{n}{s}"
            return ('builtin', _ordinal)
        if member == 'isPrime':
            def _is_prime(args, ctx):
                n = int(obj)
                if n < 2:
                    return False
                for i in range(2, int(n**0.5) + 1):
                    if n % i == 0:
                        return False
                return True
            return ('builtin', _is_prime)
        if member == 'toRoman':
            def _roman(args, ctx):
                n, result = int(obj), ''
                for val, sym in [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),
                    (90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]:
                    while n >= val:
                        result += sym
                        n -= val
                return result
            return ('builtin', _roman)
        if member == 'fibonacci':
            def _fibonacci(args, ctx):
                n = int(obj)
                if n <= 0:
                    return 0
                a, b = 0, 1
                for _ in range(n):
                    a, b = b, a + b
                return a
            return ('builtin', _fibonacci)
        if member == 'toWords':
            def _to_words(args, ctx):
                n = int(obj)
                if n == 0:
                    return 'zero'
                ones = ['','one','two','three','four','five','six','seven','eight','nine',
                        'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen',
                        'seventeen','eighteen','nineteen']
                tens = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
                def _chunk(num):
                    if num == 0:
                        return ''
                    if num < 20:
                        return ones[num]
                    if num < 100:
                        return tens[num // 10] + ('-' + ones[num % 10] if num % 10 else '')
                    return ones[num // 100] + ' hundred' + (' ' + _chunk(num % 100) if num % 100 else '')
                parts, scales = [], ['', ' thousand', ' million', ' billion']
                i, rem = 0, abs(n)
                while rem > 0:
                    if rem % 1000:
                        parts.append(_chunk(rem % 1000) + scales[i])
                    rem //= 1000
                    i += 1
                result = ' '.join(reversed(parts))
                return ('negative ' + result) if n < 0 else result
            return ('builtin', _to_words)
        if member == 'collatz':
            def _collatz(args, ctx):
                n, steps = int(obj), 0
                while n != 1:
                    n = n // 2 if n % 2 == 0 else 3 * n + 1
                    steps += 1
                return steps
            return ('builtin', _collatz)
        if member == 'nthPrime':
            def _nth_prime(args, ctx):
                count, candidate = 0, 2
                while True:
                    if all(candidate % i for i in range(2, int(candidate**0.5) + 1)):
                        count += 1
                        if count == int(obj):
                            return candidate
                    candidate += 1
            return ('builtin', _nth_prime)
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
