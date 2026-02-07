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
            'sumValues': lambda: sum(obj.values()),
            'maxValue': lambda: max(obj.values()), 'minValue': lambda: min(obj.values()),
            'averageValue': lambda: (lambda r: int(r) if r == int(r) else r)(sum(obj.values()) / len(obj)),
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
        if member in ('entries', 'toArray', 'toPairs'):
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
                for k, v in obj.items(): self._call_function(args[0], [k, v])
            return ('builtin', _fe)
        if member in ('filter', 'reject'):
            return ('builtin', lambda args, ctx: {k: v for k, v in obj.items() if (not self._call_function(args[0], [k, v]) if member == 'reject' else self._call_function(args[0], [k, v]))})
        if member == 'map':
            return ('builtin', lambda args, ctx: {k: self._call_function(args[0], [k, v]) for k, v in obj.items()})
        if member == 'count':
            return ('builtin', lambda args, ctx: sum(1 for k, v in obj.items() if self._call_function(args[0], [k, v])))
        if member == 'mapValues':
            return ('builtin', lambda args, ctx: {k: self._call_function(args[0], [v]) for k, v in obj.items()})
        if member == 'mapKeys':
            return ('builtin', lambda args, ctx: {self._call_function(args[0], [k]): v for k, v in obj.items()})
        if member in ('filterValues', 'filterKeys'):
            return ('builtin', lambda args, ctx: {k: v for k, v in obj.items() if self._call_function(args[0], [v if member == 'filterValues' else k])})
        if member in ('every', 'some'):
            return ('builtin', lambda args, ctx: (all if member == 'every' else any)(self._call_function(args[0], [k, v]) for k, v in obj.items()))
        if member in ('findKey', 'findValue'):
            def _find(args, ctx):
                for k, v in obj.items():
                    if self._call_function(args[0], [k, v]):
                        return k if member == 'findKey' else v
            return ('builtin', _find)
        if member == 'toJson':
            def _tj(args, ctx):
                def _c(v):
                    if isinstance(v, (type(None), bool, int, float, str)): return v
                    if isinstance(v, list): return [_c(i) for i in v]
                    return {str(k): _c(val) for k, val in v.items()} if isinstance(v, dict) else str(v)
                return json.dumps(_c(obj))
            return ('builtin', _tj)
        if member == 'mapEntries':
            def _me(args, ctx):
                return {(p := self._call_function(args[0], [k, v]))[0]: p[1] for k, v in obj.items()}
            return ('builtin', _me)
        if member == 'flatMap':
            def _fm(args, ctx):
                return [x for k, v in obj.items() for x in self._call_function(args[0], [k, v])]
            return ('builtin', _fm)
        if member == 'groupByValue':
            return ('builtin', lambda args, ctx: (lambda g: [g.setdefault(v, []).append(k) for k, v in obj.items()] and g or g)({}))
        if member == 'deepMerge':
            def _dm(args, ctx):
                def _m(a, b):
                    r = dict(a)
                    for k, v in b.items(): r[k] = _m(r[k], v) if k in r and isinstance(r[k], dict) and isinstance(v, dict) else v
                    return r
                return _m(obj, args[0])
            return ('builtin', _dm)
        if member == 'renameKey':
            return ('builtin', lambda args, ctx: {(args[1] if k == args[0] else k): v for k, v in obj.items()})
        if member == 'selectKeys':
            return ('builtin', lambda args, ctx: {k: obj[k] for k in args[0] if k in obj})
        if member == 'invertGrouped':
            return ('builtin', lambda args, ctx: (lambda r: [r.setdefault(v, []).append(k) for k, v in obj.items()] and r or r)({}))
        if member == 'diffKeys':
            return ('builtin', lambda args, ctx: [k for k in obj if k not in args[0]])
        if member == 'commonKeys':
            return ('builtin', lambda args, ctx: [k for k in obj if k in args[0]])
        if member == 'valuesWhere':
            return ('builtin', lambda args, ctx: [v for k, v in obj.items() if self._call_function(args[0], [k, v])])
        if member in ('toSortedKeys', 'sortByKey'):
            return ('builtin', lambda args, ctx: dict(sorted(obj.items())))
        if member == 'toSortedValues':
            return ('builtin', lambda args, ctx: sorted(obj.values()))
        if member == 'countValues':
            return ('builtin', lambda args, ctx: (lambda c: [c.update({v: c.get(v, 0) + 1}) for v in obj.values()] and c or c)({}))
        if member == 'paths':
            def _ps(args, ctx):
                def _p(d, pfx=''):
                    return [y for k, v in d.items() for y in (_p(v, f"{pfx}.{k}" if pfx else k) if isinstance(v, dict) else [f"{pfx}.{k}" if pfx else k])]
                return _p(obj)
            return ('builtin', _ps)
        if member == 'toCSV':
            return ('builtin', lambda args, ctx: ','.join(str(k) for k in obj.keys()) + '\n' + ','.join(str(v) for v in obj.values()))
        if member == 'updateIn':
            return ('builtin', lambda args, ctx: {k: (self._call_function(args[1], [v]) if k == args[0] else v) for k, v in obj.items()})
        if member == 'keysByValue':
            return ('builtin', lambda args, ctx: [k for k, v in obj.items() if v == args[0]])
        if member == 'valueSet':
            return ('builtin', lambda args, ctx: list(dict.fromkeys(obj.values())))
        if member == 'swapKeyValue':
            return ('builtin', lambda args, ctx: {v: k for k, v in obj.items()})
        if member == 'withDefaults':
            return ('builtin', lambda args, ctx: {**args[0], **obj})
        if member == 'keyOf':
            return ('builtin', lambda args, ctx: next((k for k, v in obj.items() if v == args[0]), None))
        if member == 'toTuples':
            return ('builtin', lambda args, ctx: [[k, v] for k, v in obj.items()])
        if member == 'pluck':
            return ('builtin', lambda args, ctx: [obj[k] for k in args[0] if k in obj])
        if member == 'transformEntries':
            return ('builtin', lambda args, ctx: {self._call_function(args[0], [k]): self._call_function(args[1], [v]) for k, v in obj.items()})
        if member == 'mapToArray':
            return ('builtin', lambda args, ctx: [self._call_function(args[0], [k, v]) for k, v in obj.items()])
        if member in ('minByValue', 'maxByValue'):
            return ('builtin', lambda args, ctx: (min if member == 'minByValue' else max)(obj, key=obj.get))
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
            'prefixes': lambda: [obj[:i+1] for i in range(len(obj))],
            'suffixes': lambda: [obj[i:] for i in range(len(obj))],
            'dedup': lambda: [obj[i] for i in range(len(obj)) if i == 0 or obj[i] != obj[i-1]],
            'adjacentPairs': lambda: [[obj[i], obj[i+1]] for i in range(len(obj) - 1)],
            'toString': lambda: silk_repr(obj),
            'zipWithIndex': lambda: [[v, i] for i, v in enumerate(obj)],
            'unzip': lambda: [list(t) for t in zip(*obj)] if obj else [],
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
            'skip': lambda a: obj[int(a[0]):], 'dropFirst': lambda a: obj[int(a[0]):],
            'tail': lambda a: obj[-int(a[0]):] if int(a[0]) <= len(obj) else list(obj),
            'without': lambda a: [x for x in obj if x not in a[0]],
            'difference': lambda a: [x for x in obj if x not in a[0]],
            'intersection': lambda a: [x for x in obj if x in a[0]],
            'zip': lambda a: [[x, y] for x, y in zip(obj, a[0])],
            'sample': lambda a: random.sample(list(obj), min(int(a[0]), len(obj))),
            'dotProduct': lambda a: sum(x * y for x, y in zip(obj, a[0])),
            'zipWith': lambda a: [self._call_function(a[1], [x, y]) for x, y in zip(obj, a[0])],
            'windows': lambda a: [obj[i:i+int(a[0])] for i in range(len(obj) - int(a[0]) + 1)], 'aperture': lambda a: [obj[i:i+int(a[0])] for i in range(len(obj) - int(a[0]) + 1)],
            'splitAt': lambda a: [obj[:int(a[0])], obj[int(a[0]):]],
            'cycle': lambda a: obj * int(a[0]),
            'takeRight': lambda a: obj[-int(a[0]):] if int(a[0]) > 0 else [],
            'dropRight': lambda a: obj[:-int(a[0])] if int(a[0]) > 0 else list(obj),
            'intersperse': lambda a: [x for i, v in enumerate(obj) for x in (([a[0], v] if i > 0 else [v]))],
        }
        if member in _onearg:
            fn = _onearg[member]
            return ('builtin', lambda args, ctx: fn(args))
        if member == 'slice':
            return ('builtin', lambda args, ctx: obj[int(args[0]):int(args[1])])
        if member == 'zip3':
            return ('builtin', lambda args, ctx: [[x, y, z] for x, y, z in zip(obj, args[0], args[1])])
        if member == 'indexOf':
            return ('builtin', lambda args, ctx: obj.index(args[0]) if args[0] in obj else -1)
        if member == 'map':
            return ('builtin', lambda args, ctx: [self._call_function(args[0], [item]) for item in obj])
        if member == 'filter':
            return ('builtin', lambda args, ctx: [item for item in obj if self._call_function(args[0], [item])])
        if member == 'forEach':
            def _fe(args, ctx):
                for x in obj: self._call_function(args[0], [x])
            return ('builtin', _fe)
        if member == 'reduce':
            def _reduce(args, ctx):
                acc = args[1]
                for x in obj: acc = self._call_function(args[0], [acc, x])
                return acc
            return ('builtin', _reduce)
        if member == 'find':
            return ('builtin', lambda args, ctx: next((x for x in obj if self._call_function(args[0], [x])), None))
        if member == 'findIndex':
            return ('builtin', lambda args, ctx: next((i for i, x in enumerate(obj) if self._call_function(args[0], [x])), -1))
        if member in ('every', 'all'):
            return ('builtin', lambda args, ctx: all(self._call_function(args[0], [item]) for item in obj))
        if member in ('some', 'any'):
            return ('builtin', lambda args, ctx: any(self._call_function(args[0], [item]) for item in obj))
        if member == 'flat':
            return ('builtin', lambda args, ctx: [x for i in obj for x in (i if isinstance(i, list) else [i])])
        if member == 'flattenDeep':
            return ('builtin', lambda args, ctx: (f := lambda a: [x for i in a for x in (f(i) if isinstance(i, list) else [i])])(obj))
        if member == 'flatMap':
            def _fm(args, ctx):
                return [y for x in obj for y in (lambda m: m if isinstance(m, list) else [m])(self._call_function(args[0], [x]))]
            return ('builtin', _fm)
        if member == 'unique':
            return ('builtin', lambda args, ctx: list(dict.fromkeys(obj)))
        if member == 'count':
            return ('builtin', lambda args, ctx: sum(1 for item in obj if self._call_function(args[0], [item])))
        if member == 'sortBy':
            return ('builtin', lambda args, ctx: sorted(obj, key=lambda item: self._call_function(args[0], [item])))
        if member == 'groupBy':
            return ('builtin', lambda args, ctx: (lambda g: [g.setdefault(self._call_function(args[0], [x]), []).append(x) for x in obj] and g or g)({}))
        if member == 'countBy':
            return ('builtin', lambda args, ctx: (lambda c: [c.update({(k := self._call_function(args[0], [x])): c.get(k, 0) + 1}) for x in obj] and c or c)({}))
        if member in ('chunked', 'chunk'):
            return ('builtin', lambda args, ctx: [obj[i:i+int(args[0])] for i in range(0, len(obj), int(args[0]))])
        if member in ('window', 'windowed'):
            return ('builtin', lambda args, ctx: [obj[i:i+int(args[0])] for i in range(len(obj) - int(args[0]) + 1)])
        if member == 'rotate':
            return ('builtin', lambda args, ctx: (lambda n: obj[-n:] + obj[:-n] if n else list(obj))(int(args[0]) % len(obj)) if obj else [])
        if member == 'partition':
            return ('builtin', lambda args, ctx: (lambda y, n: [(y if self._call_function(args[0], [x]) else n).append(x) for x in obj] and [y, n] or [y, n])([], []))
        if member == 'findLast':
            return ('builtin', lambda args, ctx: next((x for x in reversed(obj) if self._call_function(args[0], [x])), None))
        if member == 'findLastIndex':
            return ('builtin', lambda args, ctx: next((i for i in range(len(obj)-1, -1, -1) if self._call_function(args[0], [obj[i]])), -1))
        if member in ('tally', 'frequencies'):
            return ('builtin', lambda args, ctx: (lambda c: [c.update({x: c.get(x, 0) + 1}) for x in obj] and c or c)({}))
        if member == 'interleave':
            return ('builtin', lambda args, ctx: [x for i in range(max(len(obj), len(args[0]))) for x in ([obj[i]] if i < len(obj) else []) + ([args[0][i]] if i < len(args[0]) else [])])
        if member == 'interleaveAll':
            return ('builtin', lambda args, ctx: (lambda arrs: [arrs[j][i] for i in range(max(len(a) for a in arrs)) for j in range(len(arrs)) if i < len(arrs[j])])([obj] + list(args)))
        if member == 'flatten':
            return ('builtin', lambda args, ctx: (f := lambda a, d: [x for i in a for x in (f(i, d-1) if isinstance(i, list) and d > 0 else [i])])(obj, int(args[0]) if args else 1))
        if member == 'takeWhile':
            return ('builtin', lambda args, ctx: list(__import__('itertools').takewhile(lambda x: self._call_function(args[0], [x]), obj)))
        if member in ('skipWhile', 'dropWhile'):
            return ('builtin', lambda args, ctx: list(__import__('itertools').dropwhile(lambda x: self._call_function(args[0], [x]), obj)))
        if member == 'scan':
            def _scan(args, ctx):
                r, acc = [], args[1]
                for x in obj: acc = self._call_function(args[0], [acc, x]); r.append(acc)
                return r
            return ('builtin', _scan)
        if member == 'product':
            return ('builtin', lambda args, ctx: __import__('functools').reduce(lambda a, b: a * b, obj, 1))
        if member == 'mapIndexed':
            return ('builtin', lambda args, ctx: [self._call_function(args[0], [i, item]) for i, item in enumerate(obj)])
        if member == 'average':
            return ('builtin', lambda args, ctx: (lambda r: int(r) if r == int(r) else r)(sum(obj) / len(obj)))
        if member == 'none':
            return ('builtin', lambda args, ctx: not any(self._call_function(args[0], [item]) for item in obj))
        if member == 'reject':
            return ('builtin', lambda args, ctx: [item for item in obj if not self._call_function(args[0], [item])])
        if member == 'union':
            return ('builtin', lambda args, ctx: list(dict.fromkeys(obj + args[0])))
        if member == 'shuffle':
            return ('builtin', lambda args, ctx: random.sample(obj, len(obj)))
        if member == 'forEachIndexed':
            def _fei(args, ctx):
                for i, x in enumerate(obj): self._call_function(args[0], [i, x])
            return ('builtin', _fei)
        if member == 'symmetricDifference':
            return ('builtin', lambda args, ctx: [x for x in obj if x not in args[0]] + [x for x in args[0] if x not in obj])
        if member == 'at':
            return ('builtin', lambda args, ctx: obj[int(args[0])] if -len(obj) <= int(args[0]) < len(obj) else None)
        if member == 'associate':
            return ('builtin', lambda args, ctx: {(p := self._call_function(args[0], [x]))[0]: p[1] for x in obj})
        if member == 'interpose':
            return ('builtin', lambda args, ctx: [x for i, v in enumerate(obj) for x in ([args[0], v] if i > 0 else [v])])
        if member == 'transpose':
            return ('builtin', lambda args, ctx: [list(row) for row in zip(*obj)])
        if member == 'combinations':
            return ('builtin', lambda args, ctx: [list(c) for c in __import__('itertools').combinations(obj, int(args[0]))])
        if member == 'permutations':
            return ('builtin', lambda args, ctx: [list(p) for p in __import__('itertools').permutations(obj)])
        if member == 'median':
            def _med(args, ctx):
                s, n = sorted(obj), len(obj)
                if n % 2 == 1: return s[n // 2]
                mid = s[n // 2 - 1] + s[n // 2]
                return mid / 2 if mid % 2 else mid // 2
            return ('builtin', _med)
        if member == 'mode':
            return ('builtin', lambda args, ctx: (lambda c: [k for k, v in c.items() if v == max(c.values())])((lambda c: [c.update({x: c.get(x, 0) + 1}) for x in obj] and c or c)({})))
        if member in ('stddev', 'variance'):
            def _sv(args, ctx):
                v = sum((x - sum(obj) / len(obj)) ** 2 for x in obj) / len(obj)
                r = v ** 0.5 if member == 'stddev' else v
                return int(r) if r == int(r) else r
            return ('builtin', _sv)
        if member in ('chunkBy', 'partitionBy'):
            def _cb(args, ctx):
                if not obj: return []
                r, g, p = [], [obj[0]], self._call_function(args[0], [obj[0]])
                for x in obj[1:]:
                    k = self._call_function(args[0], [x])
                    if k == p: g.append(x)
                    else: r.append(g); g = [x]; p = k
                return r + [g]
            return ('builtin', _cb)
        if member == 'sliding':
            return ('builtin', lambda args, ctx: [obj[i:i+int(args[0])] for i in range(0, len(obj) - int(args[0]) + 1, int(args[1]))])
        if member == 'span':
            return ('builtin', lambda args, ctx: (lambda i: [obj[:i], obj[i:]])(next((i for i, x in enumerate(obj) if not self._call_function(args[0], [x])), len(obj))))
        if member == 'mapWhile':
            def _mw(args, ctx):
                r = []
                for x in obj:
                    v = self._call_function(args[0], [x])
                    if v is False: break
                    r.append(v)
                return r
            return ('builtin', _mw)
        if member == 'groupConsecutive':
            def _gc(args, ctx):
                if not obj: return []
                r, g = [], [obj[0]]
                for x in obj[1:]:
                    if x == g[-1]: g.append(x)
                    else: r.append(g); g = [x]
                return r + [g]
            return ('builtin', _gc)
        if member in ('mapFirst', 'mapLast'):
            return ('builtin', lambda args, ctx: [] if not obj else (lambda r: r.__setitem__(0 if member == 'mapFirst' else -1, self._call_function(args[0], [r[0 if member == 'mapFirst' else -1]])) or r)(list(obj)))
        if member in ('minBy', 'maxBy'):
            return ('builtin', lambda args, ctx: (min if member == 'minBy' else max)(obj, key=lambda x: self._call_function(args[0], [x])))
        if member == 'runLengthEncode':
            def _rle(args, ctx):
                if not obj: return []
                r = [[obj[0], 1]]
                for x in obj[1:]:
                    if x == r[-1][0]: r[-1][1] += 1
                    else: r.append([x, 1])
                return r
            return ('builtin', _rle)
        if member == 'foldRight':
            def _fr(args, ctx):
                acc = args[1]
                for x in reversed(obj): acc = self._call_function(args[0], [acc, x])
                return acc
            return ('builtin', _fr)
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
            'wordCount': lambda: len(obj.split()) if obj.strip() else 0,
            'initials': lambda: ''.join(w[0].upper() for w in obj.split() if w), 'codePoints': lambda: [ord(c) for c in obj],
            'isHexColor': lambda: bool(__import__('re').match(r'^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$', obj)),
            'normalize': lambda: ' '.join(obj.split()),
            'isIPv4': lambda: len(p := obj.split('.')) == 4 and all(s.isdigit() and 0 <= int(s) <= 255 for s in p),
            'isPangram': lambda: set('abcdefghijklmnopqrstuvwxyz').issubset(obj.lower()),
            'collapseWhitespace': lambda: ' '.join(obj.split()),
            'reverseWords': lambda: ' '.join(obj.split()[::-1]),
            'trimLines': lambda: '\n'.join(l.strip() for l in obj.split('\n')),
            'removeDuplicateChars': lambda: ''.join(obj[i] for i in range(len(obj)) if i == 0 or obj[i] != obj[i-1]),
            'toAcronym': lambda: ''.join(w[0].upper() for w in obj.split() if w),
            'sizeInBytes': lambda: len(obj.encode('utf-8')),
            'isWhitespace': lambda: len(obj) > 0 and obj.isspace(),
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
            'countWords': lambda a: obj.split().count(a[0]),
            'isAnagram': lambda a: sorted(obj.lower().replace(' ', '')) == sorted(a[0].lower().replace(' ', '')),
            'indent': lambda a: '\n'.join(' ' * int(a[0]) + l for l in obj.split('\n')),
            'surround': lambda a: a[0] + obj + a[0],
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
            'center': lambda a: obj.center(int(a[0]), a[1]), 'centerPad': lambda a: obj.center(int(a[0]), a[1]),
            'wrap': lambda a: a[0] + obj + a[1],
            'mask': lambda a: a[0] * (len(obj) - int(a[1])) + obj[-int(a[1]):] if len(obj) > int(a[1]) else obj,
            'padCenter': lambda a: obj.center(int(a[0]), a[1]),
            'wrapEach': lambda a: ''.join(a[0] + c + a[1] for c in obj),
            'replaceAt': lambda a: obj[:int(a[0])] + a[1] + obj[int(a[0])+1:],
        }
        if member in _twoarg:
            fn = _twoarg[member]
            return ('builtin', lambda args, ctx: fn(args))
        if member in ('substring', 'slice'):
            return ('builtin', lambda args, ctx: obj[int(args[0]):int(args[1])] if len(args) > 1 else obj[int(args[0]):])
        if member in ('toInt', 'toFloat'):
            def _conv(args, ctx):
                try:
                    v = int(obj) if member == 'toInt' else float(obj)
                    return v if member == 'toInt' or v != int(v) else int(v)
                except ValueError:
                    raise RuntimeError_(f"Cannot convert '{obj}' to {'int' if member == 'toInt' else 'float'}")
            return ('builtin', _conv)
        if member == 'format':
            def _fmt(args, ctx):
                r = obj
                for a in args: r = r.replace('{}', silk_repr(a), 1)
                return r
            return ('builtin', _fmt)
        if member in ('removePrefix', 'removeSuffix'):
            return ('builtin', lambda args, ctx: (obj[len(args[0]):] if obj.startswith(args[0]) else obj) if member == 'removePrefix' else (obj[:-len(args[0])] if obj.endswith(args[0]) else obj))
        if member == 'truncate':
            return ('builtin', lambda args, ctx: obj if len(obj) <= int(args[0]) else obj[:int(args[0]) - len(args[1] if len(args) > 1 else '')] + (args[1] if len(args) > 1 else ''))
        if member == 'isNumeric':
            def _n(args, ctx):
                try: return bool(obj) and float(obj) is not None
                except ValueError: return False
            return ('builtin', _n)
        if member == 'squeeze':
            return ('builtin', lambda args, ctx: __import__('re').sub(r' {2,}', ' ', obj))
        if member == 'at':
            return ('builtin', lambda args, ctx: obj[int(args[0])] if -len(obj) <= int(args[0]) < len(obj) else None)
        if member in ('camelCase', 'snakeCase', 'kebabCase', 'titleCase'):
            def _cc(args, ctx, _re=__import__('re')):
                p = _re.split(r'[-_\s]+', obj)
                if member == 'camelCase': return p[0].lower() + ''.join(w.capitalize() for w in p[1:])
                if member == 'titleCase': return ' '.join(w.capitalize() for w in p)
                sep = '_' if member == 'snakeCase' else '-'
                return _re.sub(r'([a-z])([A-Z])', r'\1' + sep + r'\2', _re.sub(r'[-_\s]+', sep, obj)).lower()
            return ('builtin', _cc)
        if member == 'truncateWords':
            return ('builtin', lambda args, ctx: obj if len(w := obj.split()) <= int(args[0]) else ' '.join(w[:int(args[0])]) + '...')
        if member == 'isEmail':
            return ('builtin', lambda args, ctx: len(p := obj.split('@')) == 2 and len(p[0]) > 0 and '.' in p[1])
        if member == 'partition':
            return ('builtin', lambda args, ctx: list(obj.partition(args[0])))
        if member in ('commonPrefix', 'commonSuffix'):
            def _cp(args, ctx):
                a, b = (obj, args[0]) if member == 'commonPrefix' else (obj[::-1], args[0][::-1])
                i = next((i for i in range(min(len(a), len(b))) if a[i] != b[i]), min(len(a), len(b)))
                return obj[:i] if member == 'commonPrefix' else (obj[len(obj)-i:] if i else '')
            return ('builtin', _cp)
        if member == 'levenshtein':
            def _lev(args, ctx):
                o, m, n = args[0], len(obj), len(args[0])
                if not m or not n: return m or n
                p = list(range(n + 1))
                for i in range(1, m + 1):
                    c = [i] + [0]*n
                    for j in range(1, n+1): c[j] = min(c[j-1]+1, p[j]+1, p[j-1]+(obj[i-1]!=o[j-1]))
                    p = c
                return p[n]
            return ('builtin', _lev)
        if member == 'hamming':
            return ('builtin', lambda args, ctx: sum(a != b for a, b in zip(obj, args[0])))
        if member == 'soundex':
            def _sx(args, ctx, _c={c: d for d, cs in enumerate('AEIOUYHW,BFPV,CGJKQSXZ,DT,L,MN,R'.split(',')) for c in cs}):
                if not obj: return ''
                r, p = obj[0].upper(), _c.get(obj[0].upper(), 0)
                for ch in obj[1:]:
                    cd = _c.get(ch.upper(), 0)
                    if cd > 0 and cd != p: r += str(cd)
                    p = cd or p
                return (r + '000')[:4]
            return ('builtin', _sx)
        if member == 'isUrl':
            return ('builtin', lambda args, ctx: obj.startswith(('http://', 'https://')) and '.' in obj.split('//')[1])
        if member == 'caesar':
            return ('builtin', lambda args, ctx: ''.join(chr((ord(c) - (65 if c.isupper() else 97) + int(args[0])) % 26 + (65 if c.isupper() else 97)) if c.isalpha() else c for c in obj))
        if member == 'charFrequency':
            return ('builtin', lambda args, ctx: (lambda f: [f.update({c: f.get(c, 0) + 1}) for c in obj] and f or f)({}))
        if member == 'dedent':
            def _dd(args, ctx):
                ls = obj.split('\n')
                m = min((len(l) - len(l.lstrip()) for l in ls if l.strip()), default=0)
                return '\n'.join(l[m:] for l in ls)
            return ('builtin', _dd)
        if member == 'slugify':
            import re as _re; return ('builtin', lambda args, ctx: _re.sub(r'-+', '-', _re.sub(r'[^a-z0-9]+', '-', obj.lower())).strip('-'))
        if member == 'isJSON':
            def _ij(args, ctx):
                try: json.loads(obj); return True
                except (ValueError, TypeError): return False
            return ('builtin', _ij)
        if member in ('encodeBase64', 'decodeBase64'):
            import base64 as _b64
            return ('builtin', lambda args, ctx: (_b64.b64encode if member == 'encodeBase64' else _b64.b64decode)(obj.encode()).decode())
        if member == 'matchCount':
            import re as _re
            return ('builtin', lambda args, ctx: len(_re.findall(args[0], obj)))
        if member == 'extractNumbers':
            return ('builtin', lambda args, ctx: [int(n) if n.isdigit() else float(n) for n in __import__('re').findall(r'-?\d+\.?\d*', obj)])
        if member == 'wordFrequency':
            return ('builtin', lambda args, ctx: (lambda f: [f.update({w: f.get(w, 0) + 1}) for w in obj.split()] and f or f)({}) if obj.strip() else {})
        if member == 'isBalanced':
            def _ib(args, ctx, _m={')':'(',']':'[','}':'{'}):
                s = []
                for c in obj:
                    if c in '([{': s.append(c)
                    elif c in _m and (not s or s.pop() != _m[c]): return False
                return not s
            return ('builtin', _ib)
        if member == 'isISBN':
            return ('builtin', lambda args, ctx: len(obj) == 10 and obj[:9].isdigit() and sum((10-i)*int(c) for i, c in enumerate(obj[:9])) % 11 == (11 - int(obj[9])) % 11 if obj[9].isdigit() else False)
        if member == 'occurrences':
            return ('builtin', lambda args, ctx: [i for i in range(len(obj)) if obj[i:i+len(args[0])] == args[0]])
        if member == 'isCreditCard':
            return ('builtin', lambda args, ctx: obj.isdigit() and len(obj) >= 13 and sum(int(d) for d in obj[-1::-2]) + sum(sum(divmod(2 * int(d), 10)) for d in obj[-2::-2]) == 0 if not obj.isdigit() else (sum(int(d) for d in obj[-1::-2]) + sum(sum(divmod(2 * int(d), 10)) for d in obj[-2::-2])) % 10 == 0)
        raise RuntimeError_(f"'str' has no member '{member}'")

    def _eval_number_member(self, obj: int | float, member: str) -> Any:
        """Evaluate member access on a number."""
        def _to_base(n, base, _d='0123456789abcdefghijklmnopqrstuvwxyz'):
            if n == 0: return '0'
            neg, n, r = n < 0, abs(n), []
            while n: r.append(_d[n % base]); n //= base
            return ('-' if neg else '') + ''.join(reversed(r))
        _simple = {
            'abs': lambda: abs(obj), 'floor': lambda: math.floor(obj),
            'ceil': lambda: math.ceil(obj), 'round': lambda: round(obj),
            'toString': lambda: str(obj), 'sqrt': lambda: math.sqrt(obj),
            'isEven': lambda: int(obj) % 2 == 0, 'isOdd': lambda: int(obj) % 2 != 0,
            'isPositive': lambda: obj > 0, 'isNegative': lambda: obj < 0,
            'isZero': lambda: obj == 0, 'isInteger': lambda: isinstance(obj, int), 'isFloat': lambda: isinstance(obj, float),
            'sign': lambda: (1 if obj > 0 else (-1 if obj < 0 else 0)),
            'toRadians': lambda: obj * math.pi / 180, 'toDegrees': lambda: obj * 180 / math.pi,
            'factorial': lambda: math.factorial(int(obj)), 'toBinary': lambda: bin(int(obj))[2:],
            'toHex': lambda: hex(int(obj))[2:], 'toChar': lambda: chr(int(obj)),
            'digitSum': lambda: sum(int(d) for d in str(abs(int(obj)))), 'digitCount': lambda: len(str(abs(int(obj)))),
            'isPerfect': lambda: int(obj) > 1 and sum(i for i in range(1, int(obj)) if int(obj) % i == 0) == int(obj), 'toScientific': lambda: f"{obj:.1e}",
            'factors': lambda: sorted(i for i in range(1, int(obj) + 1) if int(obj) % i == 0),
            'digitalRoot': lambda: 0 if obj == 0 else 1 + (int(obj) - 1) % 9, 'isHarshad': lambda: int(obj) > 0 and int(obj) % sum(int(d) for d in str(int(obj))) == 0,
            'sumTo': lambda: int(obj) * (int(obj) + 1) // 2,
            'aliquotSum': lambda: sum(i for i in range(1, int(obj)) if int(obj) % i == 0),
            'isAutomorphic': lambda: str(int(obj) ** 2).endswith(str(int(obj))),
            'toBits': lambda: [int(b) for b in bin(int(obj))[2:]],
            'isKaprekar': lambda: (lambda n, sq: any(int(str(sq)[:i]) + int(str(sq)[i:]) == n for i in range(1, len(str(sq)))) if n > 0 else False)(int(obj), int(obj) ** 2),
            'cubeRoot': lambda: (lambda r: int(r) if r == int(r) else r)(round(obj ** (1/3), 10)),
            'isAbundant': lambda: sum(i for i in range(1, int(obj)) if int(obj) % i == 0) > int(obj), 'isDeficient': lambda: sum(i for i in range(1, int(obj)) if int(obj) % i == 0) < int(obj),
            'isPowerOfTwo': lambda: int(obj) > 0 and (int(obj) & (int(obj) - 1)) == 0,
            'sumOfSquares': lambda: sum(i * i for i in range(1, int(obj) + 1)),
            'isNarcissistic': lambda: (lambda s, n: sum(int(d) ** n for d in s) == int(obj))(str(abs(int(obj))), len(str(abs(int(obj))))),
            'isSquare': lambda: int(obj) >= 0 and int(obj ** 0.5) ** 2 == int(obj),
            'isCube': lambda: round(abs(int(obj)) ** (1/3)) ** 3 == abs(int(obj)),
            'isMersennePrime': lambda: (lambda n: n > 1 and (n + 1) & n == 0 and all(n % i for i in range(2, int(n**0.5) + 1)))(int(obj)),
            'isTriangular': lambda: (lambda n: int((8*n+1)**0.5)**2 == 8*n+1)(int(obj)),
            'totient': lambda: sum(1 for i in range(1, int(obj) + 1) if math.gcd(i, int(obj)) == 1),
        }
        if member in _simple:
            fn = _simple[member]
            return ('builtin', lambda args, ctx: fn())
        _onearg = {
            'clampMin': lambda a: max(obj, a[0]), 'clampMax': lambda a: min(obj, a[0]),
            'toFixed': lambda a: f"{obj:.{int(a[0])}f}", 'pow': lambda a: obj ** int(a[0]),
            'gcd': lambda a: math.gcd(int(obj), int(a[0])), 'lcm': lambda a: abs(int(obj) * int(a[0])) // math.gcd(int(obj), int(a[0])),
            'clamp': lambda a: max(a[0], min(obj, a[1])),
            'isBetween': lambda a: a[0] <= obj <= a[1],
            'toBase': lambda a: _to_base(int(obj), int(a[0])),
            'toBinaryString': lambda a: bin(int(obj))[2:].zfill(int(a[0])),
            'isCoprime': lambda a: math.gcd(int(obj), int(a[0])) == 1,
            'toBinaryArray': lambda a: [int(b) for b in bin(int(obj))[2:].zfill(int(a[0]))],
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
            return ('builtin', lambda args, ctx: (lambda n: f"{n}{'th' if 11 <= n % 100 <= 13 else ['th','st','nd','rd'][n % 10] if n % 10 < 4 else 'th'}")(int(obj)))
        if member == 'isPrime':
            return ('builtin', lambda args, ctx: int(obj) >= 2 and all(int(obj) % i for i in range(2, int(int(obj)**0.5) + 1)))
        if member == 'toRoman':
            def _rm(args, ctx):
                n, r = int(obj), ''
                for v, s in [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]:
                    while n >= v: r += s; n -= v
                return r
            return ('builtin', _rm)
        if member == 'fibonacci':
            def _fib(args, ctx):
                a, b = 0, 1
                for _ in range(int(obj)): a, b = b, a + b
                return a
            return ('builtin', _fib)
        if member == 'toWords':
            def _tw(args, ctx, _o=['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'], _t=['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']):
                n = int(obj)
                if n == 0: return 'zero'
                def _ch(num):
                    if num == 0: return ''
                    if num < 20: return _o[num]
                    if num < 100: return _t[num // 10] + ('-' + _o[num % 10] if num % 10 else '')
                    return _o[num // 100] + ' hundred' + (' ' + _ch(num % 100) if num % 100 else '')
                p, s, i, rem = [], ['', ' thousand', ' million', ' billion'], 0, abs(n)
                while rem > 0:
                    if rem % 1000: p.append(_ch(rem % 1000) + s[i])
                    rem //= 1000; i += 1
                return ('negative ' if n < 0 else '') + ' '.join(reversed(p))
            return ('builtin', _tw)
        if member == 'collatz':
            def _cz(args, ctx):
                n, s = int(obj), 0
                while n != 1: n, s = (n // 2 if n % 2 == 0 else 3 * n + 1), s + 1
                return s
            return ('builtin', _cz)
        if member == 'nthPrime':
            def _np(args, ctx):
                c, p = 0, 1
                while c < int(obj):
                    p += 1
                    if all(p % i for i in range(2, int(p**0.5) + 1)): c += 1
                return p
            return ('builtin', _np)
        if member == 'isHappy':
            def _ih(args, ctx):
                n, s = int(obj), set()
                while n != 1 and n not in s: s.add(n); n = sum(int(d) ** 2 for d in str(n))
                return n == 1
            return ('builtin', _ih)
        if member == 'toFraction':
            from fractions import Fraction as _F
            return ('builtin', lambda args, ctx: str(_F(obj).limit_denominator()))
        if member == 'toCurrency':
            return ('builtin', lambda args, ctx: f"${obj:,.2f}")
        if member == 'isAmicable':
            return ('builtin', lambda args, ctx: (lambda _ds: (lambda a, b: a != b and _ds(a) == b and _ds(b) == a)(int(obj), int(args[0])))(lambda n: sum(i for i in range(1, n) if n % i == 0)))
        if member == 'primeFactors':
            def _pf(args, ctx):
                n, f, d = int(obj), [], 2
                while d * d <= n:
                    while n % d == 0: f.append(d); n //= d
                    d += 1
                return f + ([n] if n > 1 else [])
            return ('builtin', _pf)
        if member in ('prevPrime', 'nextPrime'):
            def _pnp(args, ctx):
                n, d = int(obj) + (-1 if member == 'prevPrime' else 1), -1 if member == 'prevPrime' else 1
                while n >= 2 and not all(n % i for i in range(2, int(n**0.5) + 1)): n += d
                return n if n >= 2 else None
            return ('builtin', _pnp)
        if member == 'asTime':
            def _at(args, ctx):
                n = int(obj)
                h, m, s = n // 3600, (n % 3600) // 60, n % 60
                return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"
            return ('builtin', _at)
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
