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
            si = env.get(obj.struct_name)
            if isinstance(si, tuple) and si[0] == 'struct_def' and member in si[3]:
                return ('bound_method', si[3][member], obj)
        raise RuntimeError_(f"Struct '{obj.struct_name}' has no field or method '{member}'")

    def _eval_dict_member(self, obj: dict, member: str) -> Any:
        """Evaluate member access on a dict."""
        if member in ('length', 'size'):
            return len(obj)
        _noarg = {
            'keys': lambda: list(obj.keys()), 'values': lambda: list(obj.values()),
            'isEmpty': lambda: len(obj) == 0, 'clear': lambda: {},
            'invert': lambda: {v: k for k, v in obj.items()},
            'toSortedArray': lambda: [[k, obj[k]] for k in sorted(obj.keys())], 'sortByValue': lambda: [[k, v] for k, v in sorted(obj.items(), key=lambda x: x[1])],
            'toQueryString': lambda: '&'.join(f"{k}={v}" for k, v in obj.items()), 'toFormattedString': lambda: ', '.join(f"{k}: {silk_repr(v)}" for k, v in obj.items()),
            'toHeaderString': lambda: '\n'.join(f"{k}: {silk_repr(v)}" for k, v in obj.items()),
            'sumValues': lambda: sum(obj.values()), 'maxValue': lambda: max(obj.values()), 'minValue': lambda: min(obj.values()),
            'averageValue': lambda: (lambda r: int(r) if r == int(r) else r)(sum(obj.values()) / len(obj)), 'toProperties': lambda: '\n'.join(f"{k}={silk_repr(v)}" for k, v in obj.items()),
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
            return ('builtin', lambda args, ctx: [self._call_function(args[0], [k, v]) for k, v in obj.items()] and None)
        if member in ('filter', 'reject'):
            return ('builtin', lambda args, ctx: {k: v for k, v in obj.items() if (not self._call_function(args[0], [k, v]) if member == 'reject' else self._call_function(args[0], [k, v]))})
        if member == 'map':
            return ('builtin', lambda args, ctx: {k: self._call_function(args[0], [k, v]) for k, v in obj.items()})
        if member == 'count':
            return ('builtin', lambda args, ctx: sum(1 for k, v in obj.items() if self._call_function(args[0], [k, v])))
        if member in ('mapValues', 'mapValuesWithKey'):
            return ('builtin', lambda args, ctx: {k: self._call_function(args[0], [k, v] if member == 'mapValuesWithKey' else [v]) for k, v in obj.items()})
        if member == 'mapKeys':
            return ('builtin', lambda args, ctx: {self._call_function(args[0], [k]): v for k, v in obj.items()})
        if member in ('filterValues', 'filterKeys'):
            return ('builtin', lambda args, ctx: {k: v for k, v in obj.items() if self._call_function(args[0], [v if member == 'filterValues' else k])})
        if member in ('every', 'some'):
            return ('builtin', lambda args, ctx: (all if member == 'every' else any)(self._call_function(args[0], [k, v]) for k, v in obj.items()))
        if member in ('findKey', 'findValue'):
            return ('builtin', lambda args, ctx: next(((k if member == 'findKey' else v) for k, v in obj.items() if self._call_function(args[0], [k, v])), None))
        if member == 'toJson':
            return ('builtin', lambda args, ctx: json.dumps((f := lambda v: v if isinstance(v, (type(None), bool, int, float, str)) else [f(i) for i in v] if isinstance(v, list) else {str(k): f(val) for k, val in v.items()} if isinstance(v, dict) else str(v))(obj)))
        if member == 'mapEntries':
            return ('builtin', lambda args, ctx: {(p := self._call_function(args[0], [k, v]))[0]: p[1] for k, v in obj.items()})
        if member == 'flatMap':
            return ('builtin', lambda args, ctx: [x for k, v in obj.items() for x in self._call_function(args[0], [k, v])])
        if member == 'groupByValue':
            return ('builtin', lambda args, ctx: (lambda g: [g.setdefault(v, []).append(k) for k, v in obj.items()] and g or g)({}))
        if member == 'deepMerge':
            return ('builtin', lambda args, ctx: (m := lambda a, b: {k: m(a[k], v) if k in a and isinstance(a[k], dict) and isinstance(v, dict) else v for k, v in {**a, **b}.items()})(obj, args[0]))
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
        if member in ('valuesWhere', 'keysWhere'):
            return ('builtin', lambda args, ctx: [(v if member == 'valuesWhere' else k) for k, v in obj.items() if self._call_function(args[0], [k, v])])
        if member in ('toSortedKeys', 'sortByKey'):
            return ('builtin', lambda args, ctx: dict(sorted(obj.items())))
        if member == 'toSortedValues':
            return ('builtin', lambda args, ctx: sorted(obj.values()))
        if member == 'symmetricDifference':
            return ('builtin', lambda args, ctx: {**{k: v for k, v in obj.items() if k not in args[0]}, **{k: v for k, v in args[0].items() if k not in obj}})
        if member == 'intersectKeys':
            return ('builtin', lambda args, ctx: {k: v for k, v in obj.items() if k in args[0]})
        if member in ('countValues', 'valueCounts'):
            return ('builtin', lambda args, ctx: (lambda c: [c.update({v: c.get(v, 0) + 1}) for v in obj.values()] and c or c)({}))
        if member == 'paths':
            return ('builtin', lambda args, ctx: (p := lambda d, pfx='': [y for k, v in d.items() for y in (p(v, f"{pfx}.{k}" if pfx else k) if isinstance(v, dict) else [f"{pfx}.{k}" if pfx else k])])(obj))
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
        if member == 'toPrettyString':
            return ('builtin', lambda args, ctx: '{\n' + ',\n'.join(f'  {silk_repr(k)}: {silk_repr(v)}' for k, v in obj.items()) + '\n}')
        if member == 'toKeyValueStrings':
            return ('builtin', lambda args, ctx: [f"{silk_repr(k)}{args[0]}{silk_repr(v)}" for k, v in obj.items()])
        if member == 'deepGet':
            return ('builtin', lambda args, ctx: __import__('functools').reduce(lambda d, k: d.get(k) if isinstance(d, dict) else None, args[0].split('.'), obj))
        if member == 'deepSet':
            return ('builtin', lambda args, ctx: (s := lambda d, keys, v: {**d, keys[0]: s(d.get(keys[0], {}), keys[1:], v) if len(keys) > 1 else v} if isinstance(d, dict) else {keys[0]: s({}, keys[1:], v) if len(keys) > 1 else v})(obj, args[0].split('.'), args[1]))
        if member in ('toXML', 'toYAML', 'toINI', 'toEnvironment'):
            return ('builtin', lambda args, ctx: (lambda t: f"<{t}>" + ''.join(f"<{k}>{silk_repr(v)}</{k}>" for k, v in obj.items()) + f"</{t}>")(args[0] if args else 'root') if member == 'toXML' else '\n'.join(f"{'export ' if member == 'toEnvironment' else ''}{k}{'=' if member in ('toINI', 'toEnvironment') else ': '}{silk_repr(v)}" for k, v in obj.items()))
        if member in ('toSQLInsert', 'toSQLUpdate', 'toSQLWhere', 'toSQLDelete'):
            return ('builtin', lambda args, ctx: f"INSERT INTO {args[0]} ({', '.join(obj.keys())}) VALUES ({', '.join(silk_repr(v) for v in obj.values())})" if member == 'toSQLInsert' else f"UPDATE {args[0]} SET {', '.join(f'{k} = {silk_repr(v)}' for k, v in obj.items())}" if member == 'toSQLUpdate' else f"SELECT * FROM {args[0]} WHERE {' AND '.join(f'{k} = {silk_repr(v)}' for k, v in obj.items())}" if member == 'toSQLWhere' else f"DELETE FROM {args[0]} WHERE {' AND '.join(f'{k} = {silk_repr(v)}' for k, v in obj.items())}")
        if member in ('toDotNotation', 'fromDotNotation'):
            if member == 'toDotNotation':
                return ('builtin', lambda args, ctx: (f := lambda d, pfx='': {y: z for k, v in d.items() for y, z in (f(v, f"{pfx}.{k}" if pfx else k).items() if isinstance(v, dict) else [(f"{pfx}.{k}" if pfx else k, v)])})(obj))
            return ('builtin', lambda args, ctx: (lambda r: [((s := lambda d, keys, v: d.update({keys[0]: s(d.get(keys[0], {}), keys[1:], v)}) or d if len(keys) > 1 else d.update({keys[0]: v}) or d))(r, k.split('.'), v) for k, v in obj.items()] and r)({}))
        if member in ('toTOML', 'toGraphQL', 'toElixirMap', 'toScalaMap', 'toKotlinMap', 'toPhpArray', 'toRustStruct', 'toCSharpDict', 'toClojureMap', 'toHaskellMap', 'toGoMap', 'toSwiftDict', 'toPythonDict', 'toRubyHash', 'toLuaTable'):
            _qv = lambda v: json.dumps(v) if isinstance(v, str) else silk_repr(v)
            _m = {'toTOML': (None, '\n', lambda k, v: f'{k} = {_qv(v)}'), 'toGraphQL': ('{ ', ', ', lambda k, v: f'{k}: {silk_repr(v)}'), 'toElixirMap': ('%{', ', ', lambda k, v: f'{k}: {_qv(v)}'), 'toScalaMap': ('Map(', ', ', lambda k, v: f'"{k}" -> {_qv(v)}'), 'toKotlinMap': ('mapOf(', ', ', lambda k, v: f'"{k}" to {_qv(v)}'), 'toPhpArray': ('[', ', ', lambda k, v: f'"{k}" => {_qv(v)}'), 'toRustStruct': ('Data { ', ', ', lambda k, v: f'{k}: {_qv(v)}'), 'toCSharpDict': ('{', ', ', lambda k, v: f'{{"{k}", {_qv(v)}}}'), 'toClojureMap': ('{', ', ', lambda k, v: f':{k} {_qv(v)}'), 'toHaskellMap': ('fromList [', ', ', lambda k, v: f'("{k}", {_qv(v)})'), 'toGoMap': ('map[string]interface{}{', ', ', lambda k, v: f'"{k}": {_qv(v)}'), 'toSwiftDict': ('[', ', ', lambda k, v: f'"{k}": {silk_repr(v)}'), 'toPythonDict': ('{', ', ', lambda k, v: f'"{k}": {silk_repr(v)}'), 'toRubyHash': ('{', ', ', lambda k, v: f'"{k}" => {silk_repr(v)}'), 'toLuaTable': ('{', ', ', lambda k, v: f'{k} = {silk_repr(v)}')}[member]
            _cl = {'toGraphQL': ' }', 'toElixirMap': '}', 'toScalaMap': ')', 'toKotlinMap': ')', 'toPhpArray': ']', 'toRustStruct': ' }', 'toCSharpDict': '}', 'toClojureMap': '}', 'toHaskellMap': ']', 'toGoMap': '}', 'toSwiftDict': ']', 'toPythonDict': '}', 'toRubyHash': '}', 'toLuaTable': '}'}
            return ('builtin', lambda args, ctx, m=_m, cl=_cl: (m[1].join(m[2](k, v) for k, v in obj.items()) if m[0] is None else m[0] + m[1].join(m[2](k, v) for k, v in obj.items()) + cl.get(member, '')))
        if member == 'toJSONPretty':
            return ('builtin', lambda args, ctx: json.dumps((f := lambda v: v if isinstance(v, (type(None), bool, int, float, str)) else [f(i) for i in v] if isinstance(v, list) else {str(k): f(val) for k, val in v.items()} if isinstance(v, dict) else str(v))(obj), indent=2))
        if member in ('toHTMLList', 'toHTMLTable'):
            return ('builtin', lambda args, ctx: ('<ul>' + ''.join(f'<li>{k}: {silk_repr(v)}</li>' for k, v in obj.items()) + '</ul>') if member == 'toHTMLList' else ('<table><tr>' + ''.join(f'<th>{k}</th>' for k in obj.keys()) + '</tr><tr>' + ''.join(f'<td>{silk_repr(v)}</td>' for v in obj.values()) + '</tr></table>'))
        if member == 'toMarkdown':
            return ('builtin', lambda args, ctx: '| ' + ' | '.join(str(k) for k in obj.keys()) + ' |\n| ' + ' | '.join('---' for _ in obj) + ' |\n| ' + ' | '.join(silk_repr(v) for v in obj.values()) + ' |')
        if member in ('minByValue', 'maxByValue'):
            return ('builtin', lambda args, ctx: (min if member == 'minByValue' else max)(obj, key=obj.get))
        if member in ('toDSL', 'toProtobuf', 'toNginxConfig', 'toApacheConfig', 'toTerraformHCL', 'toHelmValues', 'toVaultPolicy', 'toNomadJob', 'toPrometheusConfig'):
            _sep = {'toProtobuf': ': ', 'toDSL': ' ', 'toNginxConfig': ' ', 'toApacheConfig': ' ', 'toTerraformHCL': ' = ', 'toHelmValues': ': ', 'toVaultPolicy': ' = ', 'toNomadJob': ' = ', 'toPrometheusConfig': ' = '}[member]
            _end = ';' if member == 'toNginxConfig' else ''
            return ('builtin', lambda args, ctx, s=_sep, e=_end: '\n'.join(f'{k}{s}{json.dumps(v) if isinstance(v, str) else silk_repr(v)}{e}' for k, v in obj.items()))
        if member in ('toTypeScript', 'toGraphQLSchema'):
            _tf = lambda v: ("boolean" if isinstance(v, bool) else "string" if isinstance(v, str) else "number" if isinstance(v, (int, float)) else "any") if member == 'toTypeScript' else ("Boolean" if isinstance(v, bool) else "String" if isinstance(v, str) else ("Int" if isinstance(v, int) else "Float") if isinstance(v, (int, float)) else "Any")
            return ('builtin', lambda args, ctx, tf=_tf: ('interface Data { ' + ' '.join(f'{k}: {tf(v)};' for k, v in obj.items()) + ' }') if member == 'toTypeScript' else ('type Data { ' + ' '.join(f'{k}: {tf(v)}' for k, v in obj.items()) + ' }'))
        if member == 'toKafkaConfig': member = 'toZookeeperConfig'
        if member in ('toRabbitmqConfig', 'toElasticConfig', 'toMysqlConfig', 'toMongoConfig', 'toCouchDBConfig', 'toInfluxDBConfig', 'toNeo4jConfig', 'toCassandraConfig', 'toClickHouseConfig', 'toTimescaleDBConfig', 'toDynamoDBConfig', 'toFirebirdConfig', 'toElasticsearchConfig', 'toMariaDBConfig', 'toSurrealDBConfig', 'toScyllaDBConfig', 'toCockroachDBConfig', 'toArangoDBConfig', 'toFoundationDBConfig', 'toRiakConfig', 'toOrientDBConfig', 'toVoltDBConfig', 'toNutsDBConfig', 'toH2Config', 'toTiDBConfig', 'toDgraphConfig', 'toQuestDBConfig', 'toImmuDBConfig'): member = {'toRabbitmqConfig': 'toGrafanaConfig', 'toElasticConfig': 'toConsulKV', 'toMysqlConfig': 'toGrafanaConfig', 'toMongoConfig': 'toConsulKV', 'toCouchDBConfig': 'toGrafanaConfig', 'toInfluxDBConfig': 'toGrafanaConfig', 'toNeo4jConfig': 'toZookeeperConfig', 'toCassandraConfig': 'toConsulKV', 'toClickHouseConfig': 'toGrafanaConfig', 'toTimescaleDBConfig': 'toPostgresConfig', 'toDynamoDBConfig': 'toGrafanaConfig', 'toFirebirdConfig': 'toGrafanaConfig', 'toElasticsearchConfig': 'toConsulKV', 'toMariaDBConfig': 'toGrafanaConfig', 'toSurrealDBConfig': 'toGrafanaConfig', 'toScyllaDBConfig': 'toConsulKV', 'toCockroachDBConfig': 'toZookeeperConfig', 'toArangoDBConfig': 'toGrafanaConfig', 'toFoundationDBConfig': 'toGrafanaConfig', 'toRiakConfig': 'toGrafanaConfig', 'toOrientDBConfig': 'toGrafanaConfig', 'toVoltDBConfig': 'toGrafanaConfig', 'toNutsDBConfig': 'toConsulKV', 'toH2Config': 'toGrafanaConfig', 'toTiDBConfig': 'toGrafanaConfig', 'toDgraphConfig': 'toGrafanaConfig', 'toQuestDBConfig': 'toGrafanaConfig', 'toImmuDBConfig': 'toGrafanaConfig'}[member]
        if member in ('toDockerEnv', 'toMakefileVars', 'toAnsibleYAML', 'toSystemdUnit', 'toConsulKV', 'toEtcdConfig', 'toDockerCompose', 'toKubernetesYAML', 'toGrafanaConfig', 'toRedisConfig', 'toNginxUpstream', 'toFluentBitConfig', 'toLogstashConfig', 'toSentinelConfig', 'toHAProxyConfig', 'toVarnishConfig', 'toEnvoyConfig', 'toTraefikConfig', 'toCaddyConfig', 'toZookeeperConfig', 'toMemcachedConfig', 'toPostgresConfig', 'toRedisClusterConfig', 'toSQLiteConfig'):
            _fmt = {'toDockerEnv': lambda k, v: f'ENV {k}={json.dumps(v) if isinstance(v, str) else silk_repr(v)}', 'toMakefileVars': lambda k, v: f'{k} := {v if isinstance(v, str) else silk_repr(v)}', 'toAnsibleYAML': lambda k, v: f'- {k}: {v if isinstance(v, str) else silk_repr(v)}', 'toSystemdUnit': lambda k, v: f'{k}={v if isinstance(v, str) else silk_repr(v)}', 'toConsulKV': lambda k, v: f'{k}: {v if isinstance(v, str) else silk_repr(v)}', 'toEtcdConfig': lambda k, v: f'/{k} {json.dumps(v) if isinstance(v, str) else silk_repr(v)}', 'toDockerCompose': lambda k, v: f'{k}: {v if isinstance(v, str) else silk_repr(v)}', 'toKubernetesYAML': lambda k, v: f'{k}: {v if isinstance(v, str) else silk_repr(v)}', 'toGrafanaConfig': lambda k, v: f'{k} = {v if isinstance(v, str) else silk_repr(v)}', 'toRedisConfig': lambda k, v: f'{k} {v if isinstance(v, str) else silk_repr(v)}', 'toNginxUpstream': lambda k, v: f'server {v if isinstance(v, str) else silk_repr(v)};', 'toFluentBitConfig': lambda k, v: f'{k} {v if isinstance(v, str) else silk_repr(v)}', 'toLogstashConfig': lambda k, v: f'{k} => {json.dumps(v) if isinstance(v, str) else silk_repr(v)}', 'toSentinelConfig': lambda k, v: f'sentinel {k} {v if isinstance(v, str) else silk_repr(v)}', 'toHAProxyConfig': lambda k, v: f'{k} {v if isinstance(v, str) else silk_repr(v)}', 'toVarnishConfig': lambda k, v: f'set {k} = {json.dumps(v) if isinstance(v, str) else silk_repr(v)};', 'toEnvoyConfig': lambda k, v: f'{k}: {json.dumps(v) if isinstance(v, str) else silk_repr(v)}', 'toTraefikConfig': lambda k, v: f'[{k}]\n  value = {json.dumps(v) if isinstance(v, str) else silk_repr(v)}', 'toCaddyConfig': lambda k, v: f'{k} {v if isinstance(v, str) else silk_repr(v)}', 'toZookeeperConfig': lambda k, v: f'{k}={v if isinstance(v, str) else silk_repr(v)}', 'toMemcachedConfig': lambda k, v: f'-{k} {v if isinstance(v, str) else silk_repr(v)}', 'toPostgresConfig': lambda k, v: f"{k} = '{v}'" if isinstance(v, str) else f'{k} = {silk_repr(v)}', 'toRedisClusterConfig': lambda k, v: f'cluster-{k} {v if isinstance(v, str) else silk_repr(v)}', 'toSQLiteConfig': lambda k, v: f'PRAGMA {k} = {v if isinstance(v, str) else silk_repr(v)};'}[member]
            return ('builtin', lambda args, ctx, f=_fmt: '\n'.join(f(k, v) for k, v in obj.items()))
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
            'prefixes': lambda: [obj[:i+1] for i in range(len(obj))], 'mapHeads': lambda: [obj[:i+1] for i in range(len(obj))], 'mapInits': lambda: [obj[:i+1] for i in range(len(obj))],
            'suffixes': lambda: [obj[i:] for i in range(len(obj))], 'mapTails': lambda: [obj[i:] for i in range(len(obj))],
            'dedup': lambda: [obj[i] for i in range(len(obj)) if i == 0 or obj[i] != obj[i-1]],
            'adjacentPairs': lambda: [[obj[i], obj[i+1]] for i in range(len(obj) - 1)], 'slidingPairs': lambda: [[obj[i], obj[i+1]] for i in range(len(obj) - 1)],
            'toString': lambda: silk_repr(obj),
            'zipWithIndex': lambda: [[v, i] for i, v in enumerate(obj)],
            'unzip': lambda: [list(t) for t in zip(*obj)] if obj else [],
            'maxIndex': lambda: obj.index(max(obj)), 'minIndex': lambda: obj.index(min(obj)),
            'accumulate': lambda: list(__import__('itertools').accumulate(obj)), 'cumulativeSum': lambda: list(__import__('itertools').accumulate(obj)),
            'adjacentDiff': lambda: [obj[i+1] - obj[i] for i in range(len(obj) - 1)],
            'runningAverage': lambda: [(lambda s: int(s) if s == int(s) else s)(sum(obj[:i+1]) / (i+1)) for i in range(len(obj))],
            'duplicates': lambda: list(dict.fromkeys(x for x in obj if obj.count(x) > 1)),
            'mapDistinct': lambda: list(dict.fromkeys(obj)), 'mapUniq': lambda: list(dict.fromkeys(obj)),
            'mapFlatten': lambda: [y for x in obj for y in (x if isinstance(x, list) else [x])],
            'mapEnumerate': lambda: [[i, v] for i, v in enumerate(obj)], 'mapZipIndex': lambda: [[v, i] for i, v in enumerate(obj)],
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
            'sample': lambda a: random.sample(list(obj), min(int(a[0]), len(obj))), 'takeRandom': lambda a: random.sample(list(obj), min(int(a[0]), len(obj))),
            'dotProduct': lambda a: sum(x * y for x, y in zip(obj, a[0])),
            'zipWith': lambda a: [self._call_function(a[1], [x, y]) for x, y in zip(obj, a[0])],
            'windows': lambda a: [obj[i:i+int(a[0])] for i in range(len(obj) - int(a[0]) + 1)], 'aperture': lambda a: [obj[i:i+int(a[0])] for i in range(len(obj) - int(a[0]) + 1)],
            'splitAt': lambda a: [obj[:int(a[0])], obj[int(a[0]):]],
            'cycle': lambda a: obj * int(a[0]),
            'takeRight': lambda a: obj[-int(a[0]):] if int(a[0]) > 0 else [],
            'dropRight': lambda a: obj[:-int(a[0])] if int(a[0]) > 0 else list(obj),
            'intersperse': lambda a: [x for i, v in enumerate(obj) for x in (([a[0], v] if i > 0 else [v]))],
            'takeEvery': lambda a: obj[::int(a[0])],
            'everyNth': lambda a: obj[int(a[0])-1::int(a[0])],
        }
        if member in _onearg:
            fn = _onearg[member]
            return ('builtin', lambda args, ctx: fn(args))
        if member == 'slice': return ('builtin', lambda args, ctx: obj[int(args[0]):int(args[1])])
        if member == 'zip3': return ('builtin', lambda args, ctx: [[x, y, z] for x, y, z in zip(obj, args[0], args[1])])
        if member == 'indexOf': return ('builtin', lambda args, ctx: obj.index(args[0]) if args[0] in obj else -1)
        if member in ('map', 'collectMap', 'mapAsync'): return ('builtin', lambda args, ctx: [self._call_function(args[0], [item]) for item in obj])
        if member == 'mapNotNull': return ('builtin', lambda args, ctx: [r for item in obj if (r := self._call_function(args[0], [item])) is not None])
        if member == 'filter': return ('builtin', lambda args, ctx: [item for item in obj if self._call_function(args[0], [item])])
        if member == 'forEach': return ('builtin', lambda args, ctx: [self._call_function(args[0], [x]) for x in obj] and None)
        if member == 'reduce': return ('builtin', lambda args, ctx: __import__('functools').reduce(lambda acc, x: self._call_function(args[0], [acc, x]), obj, args[1]))
        if member == 'find': return ('builtin', lambda args, ctx: next((x for x in obj if self._call_function(args[0], [x])), None))
        if member == 'findIndex': return ('builtin', lambda args, ctx: next((i for i, x in enumerate(obj) if self._call_function(args[0], [x])), -1))
        if member in ('every', 'all'): return ('builtin', lambda args, ctx: all(self._call_function(args[0], [item]) for item in obj))
        if member in ('some', 'any'): return ('builtin', lambda args, ctx: any(self._call_function(args[0], [item]) for item in obj))
        if member == 'flat': return ('builtin', lambda args, ctx: [x for i in obj for x in (i if isinstance(i, list) else [i])])
        if member == 'flattenDeep': return ('builtin', lambda args, ctx: (f := lambda a: [x for i in a for x in (f(i) if isinstance(i, list) else [i])])(obj))
        if member in ('flatMap', 'mapFlat'): return ('builtin', lambda args, ctx: [y for x in obj for y in (lambda m: m if isinstance(m, list) else [m])(self._call_function(args[0], [x]))])
        if member == 'unique': return ('builtin', lambda args, ctx: list(dict.fromkeys(obj)))
        if member == 'count': return ('builtin', lambda args, ctx: sum(1 for item in obj if self._call_function(args[0], [item])))
        if member == 'sortBy': return ('builtin', lambda args, ctx: sorted(obj, key=lambda item: self._call_function(args[0], [item])))
        if member == 'groupBy': return ('builtin', lambda args, ctx: (lambda g: [g.setdefault(self._call_function(args[0], [x]), []).append(x) for x in obj] and g or g)({}))
        if member == 'countBy': return ('builtin', lambda args, ctx: (lambda c: [c.update({(k := self._call_function(args[0], [x])): c.get(k, 0) + 1}) for x in obj] and c or c)({}))
        if member in ('chunked', 'chunk'): return ('builtin', lambda args, ctx: [obj[i:i+int(args[0])] for i in range(0, len(obj), int(args[0]))])
        if member in ('window', 'windowed'): return ('builtin', lambda args, ctx: [obj[i:i+int(args[0])] for i in range(len(obj) - int(args[0]) + 1)])
        if member == 'rotate': return ('builtin', lambda args, ctx: (lambda n: obj[-n:] + obj[:-n] if n else list(obj))(int(args[0]) % len(obj)) if obj else [])
        if member == 'partition': return ('builtin', lambda args, ctx: (lambda y, n: [(y if self._call_function(args[0], [x]) else n).append(x) for x in obj] and [y, n] or [y, n])([], []))
        if member == 'findLast': return ('builtin', lambda args, ctx: next((x for x in reversed(obj) if self._call_function(args[0], [x])), None))
        if member == 'findLastIndex': return ('builtin', lambda args, ctx: next((i for i in range(len(obj)-1, -1, -1) if self._call_function(args[0], [obj[i]])), -1))
        if member in ('tally', 'frequencies', 'histogram'): return ('builtin', lambda args, ctx: (lambda c: [c.update({x: c.get(x, 0) + 1}) for x in obj] and c or c)({}))
        if member == 'interleave': return ('builtin', lambda args, ctx: [x for i in range(max(len(obj), len(args[0]))) for x in ([obj[i]] if i < len(obj) else []) + ([args[0][i]] if i < len(args[0]) else [])])
        if member == 'interleaveAll': return ('builtin', lambda args, ctx: (lambda arrs: [arrs[j][i] for i in range(max(len(a) for a in arrs)) for j in range(len(arrs)) if i < len(arrs[j])])([obj] + list(args)))
        if member == 'flatten': return ('builtin', lambda args, ctx: (f := lambda a, d: [x for i in a for x in (f(i, d-1) if isinstance(i, list) and d > 0 else [i])])(obj, int(args[0]) if args else 1))
        if member == 'takeWhile': return ('builtin', lambda args, ctx: list(__import__('itertools').takewhile(lambda x: self._call_function(args[0], [x]), obj)))
        if member in ('skipWhile', 'dropWhile'): return ('builtin', lambda args, ctx: list(__import__('itertools').dropwhile(lambda x: self._call_function(args[0], [x]), obj)))
        if member in ('scan', 'scanRight'): return ('builtin', lambda args, ctx: (lambda r, items: [r.append(self._call_function(args[0], [r[-1], x])) or None for x in items] and (r[1:][::-1] if member == 'scanRight' else r[1:]))([args[1]], reversed(obj) if member == 'scanRight' else obj))
        if member == 'product': return ('builtin', lambda args, ctx: __import__('functools').reduce(lambda a, b: a * b, obj, 1))
        if member in ('mapIndexed', 'mapWithIndex'): return ('builtin', lambda args, ctx: [self._call_function(args[0], [i, item]) for i, item in enumerate(obj)])
        if member == 'average': return ('builtin', lambda args, ctx: (lambda r: int(r) if r == int(r) else r)(sum(obj) / len(obj)))
        if member == 'none': return ('builtin', lambda args, ctx: not any(self._call_function(args[0], [item]) for item in obj))
        if member == 'reject': return ('builtin', lambda args, ctx: [item for item in obj if not self._call_function(args[0], [item])])
        if member == 'union': return ('builtin', lambda args, ctx: list(dict.fromkeys(obj + args[0])))
        if member == 'shuffle': return ('builtin', lambda args, ctx: random.sample(obj, len(obj)))
        if member == 'forEachIndexed': return ('builtin', lambda args, ctx: [self._call_function(args[0], [i, x]) for i, x in enumerate(obj)] and None)
        if member == 'symmetricDifference': return ('builtin', lambda args, ctx: [x for x in obj if x not in args[0]] + [x for x in args[0] if x not in obj])
        if member == 'at': return ('builtin', lambda args, ctx: obj[int(args[0])] if -len(obj) <= int(args[0]) < len(obj) else None)
        if member == 'associate': return ('builtin', lambda args, ctx: {(p := self._call_function(args[0], [x]))[0]: p[1] for x in obj})
        if member == 'interpose': return ('builtin', lambda args, ctx: [x for i, v in enumerate(obj) for x in ([args[0], v] if i > 0 else [v])])
        if member == 'juxtapose': return ('builtin', lambda args, ctx: [[self._call_function(fn, [x]) for fn in args[0]] for x in obj])
        if member == 'crossProduct': return ('builtin', lambda args, ctx: [[a, b] for a in obj for b in args[0]])
        if member == 'interleaveN': return ('builtin', lambda args, ctx: (lambda arrs: [arrs[j][i] for i in range(max(len(a) for a in arrs)) for j in range(len(arrs)) if i < len(arrs[j])])([obj] + args[0]))
        if member == 'transpose': return ('builtin', lambda args, ctx: [list(row) for row in zip(*obj)])
        if member == 'combinations': return ('builtin', lambda args, ctx: [list(c) for c in __import__('itertools').combinations(obj, int(args[0]))])
        if member == 'permutations': return ('builtin', lambda args, ctx: [list(p) for p in __import__('itertools').permutations(obj)])
        if member == 'mapTruncateTo': return ('builtin', lambda args, ctx: obj[:int(args[0])])
        if member == 'mapPadLeft': return ('builtin', lambda args, ctx: [args[1]] * max(0, int(args[0]) - len(obj)) + obj)
        if member == 'median': return ('builtin', lambda args, ctx: (lambda s, n: s[n//2] if n % 2 else (lambda m: m/2 if m % 2 else m//2)(s[n//2-1]+s[n//2]))(sorted(obj), len(obj)))
        if member == 'mode': return ('builtin', lambda args, ctx: (lambda c: [k for k, v in c.items() if v == max(c.values())])((lambda c: [c.update({x: c.get(x, 0) + 1}) for x in obj] and c or c)({})))
        if member in ('stddev', 'variance'): return ('builtin', lambda args, ctx: (lambda r: int(r) if r == int(r) else r)((lambda v: v ** 0.5 if member == 'stddev' else v)(sum((x - sum(obj)/len(obj)) ** 2 for x in obj) / len(obj))))
        if member in ('chunkBy', 'partitionBy', 'segmentBy'): return ('builtin', lambda args, ctx: [list(g) for _, g in __import__('itertools').groupby(obj, key=lambda x: self._call_function(args[0], [x]))] if obj else [])
        if member == 'sliding': return ('builtin', lambda args, ctx: [obj[i:i+int(args[0])] for i in range(0, len(obj) - int(args[0]) + 1, int(args[1]))])
        if member in ('span', 'splitWhen'): return ('builtin', lambda args, ctx: (lambda i: [obj[:i], obj[i:]] if (member == 'span' or i < len(obj)) else [list(obj)])(next((i for i, x in enumerate(obj) if (not self._call_function(args[0], [x]) if member == 'span' else self._call_function(args[0], [x]))), len(obj))))
        if member == 'mapWhile': return ('builtin', lambda args, ctx: list(__import__('itertools').takewhile(lambda v: v is not False, (self._call_function(args[0], [x]) for x in obj))))
        if member == 'groupConsecutive': return ('builtin', lambda args, ctx: [list(g) for _, g in __import__('itertools').groupby(obj)] if obj else [])
        if member in ('mapFirst', 'mapLast'): return ('builtin', lambda args, ctx: [] if not obj else (lambda r: r.__setitem__(0 if member == 'mapFirst' else -1, self._call_function(args[0], [r[0 if member == 'mapFirst' else -1]])) or r)(list(obj)))
        if member in ('minBy', 'maxBy'): return ('builtin', lambda args, ctx: (min if member == 'minBy' else max)(obj, key=lambda x: self._call_function(args[0], [x])))
        if member in ('forEachRight', 'mapRight'): return ('builtin', lambda args, ctx: (lambda r: None if member == 'forEachRight' else r)([self._call_function(args[0], [x]) for x in reversed(obj)]))
        if member == 'tapEach': return ('builtin', lambda args, ctx: [self._call_function(args[0], [x]) for x in obj] and obj)
        if member in ('filterRight', 'findRight', 'findIndexRight', 'countRight'):
            return ('builtin', lambda args, ctx: [x for x in reversed(obj) if self._call_function(args[0], [x])] if member == 'filterRight' else next((x for x in reversed(obj) if self._call_function(args[0], [x])), None) if member == 'findRight' else sum(1 for x in obj if self._call_function(args[0], [x])) if member == 'countRight' else next((i for i in range(len(obj)-1, -1, -1) if self._call_function(args[0], [obj[i]])), -1))
        if member == 'mapWhileIndexed': return ('builtin', lambda args, ctx: list(__import__('itertools').takewhile(lambda v: v is not False, (self._call_function(args[0], [i, x]) for i, x in enumerate(obj)))))
        if member in ('noneIndexed', 'everyIndexed', 'someIndexed'): return ('builtin', lambda args, ctx, fn={'noneIndexed': lambda g: not any(g), 'everyIndexed': all, 'someIndexed': any}[member]: fn(self._call_function(args[0], [i, x]) for i, x in enumerate(obj)))
        if member == 'flatMapIndexed': return ('builtin', lambda args, ctx: [y for i, x in enumerate(obj) for y in (lambda m: m if isinstance(m, list) else [m])(self._call_function(args[0], [i, x]))])
        if member == 'reduceIndexed': return ('builtin', lambda args, ctx: __import__('functools').reduce(lambda acc, ix: self._call_function(args[0], [acc, ix[0], ix[1]]), enumerate(obj), args[1]))
        if member in ('filterIndexed', 'filterMapIndexed'): return ('builtin', lambda args, ctx: [x for i, x in enumerate(obj) if self._call_function(args[0], [i, x])])
        if member == 'groupByCount': return ('builtin', lambda args, ctx: (lambda n, s: [obj[i*s:(i+1)*s] for i in range(n)])(int(args[0]), len(obj) // int(args[0])))
        if member == 'uniqueBy': return ('builtin', lambda args, ctx: (lambda s: [x for x in obj if (k := self._call_function(args[0], [x])) not in s and not s.add(k)])(set()))
        if member in ('pairMap', 'mapPairs', 'mapWithNext', 'mapBetween'): return ('builtin', lambda args, ctx: [self._call_function(args[0], [obj[i], obj[i+1]]) for i in range(len(obj) - 1)])
        if member == 'runLengthEncode': return ('builtin', lambda args, ctx: [[k, sum(1 for _ in g)] for k, g in __import__('itertools').groupby(obj)] if obj else [])
        if member in ('mapAccum', 'mapAccumRight'): return ('builtin', lambda args, ctx: (lambda: (r := [[], args[1]]) and [r.__setitem__(1, (p := self._call_function(args[0], [r[1], x]))[1]) or r[0].append(p[0]) for x in (reversed(obj) if member == 'mapAccumRight' else obj)] and ([r[0][::-1], r[1]] if member == 'mapAccumRight' else r))())
        if member == 'toDict': return ('builtin', lambda args, ctx: dict(zip(obj, args[0])))
        if member == 'weightedAverage': return ('builtin', lambda args, ctx: (lambda r: int(r) if r == int(r) else r)(sum(v*w for v, w in zip(obj, args[0])) / sum(args[0])))
        if member in ('foldRight', 'reduceRight'): return ('builtin', lambda args, ctx: __import__('functools').reduce(lambda acc, x: self._call_function(args[0], [acc, x]), reversed(obj), args[1]))
        if member == 'reduceWhile': return ('builtin', lambda args, ctx: (lambda: (s := [args[0]]) and [((s.__setitem__(0, r) or True) if (r := self._call_function(args[1], [s[0], x])) is not False else None) for x in obj] and s[0])())
        if member in ('unfold', 'iterate'): return ('builtin', lambda args, ctx: (lambda s, fn, n: (r := [s]) and [r.append(fn(r[-1])) for _ in range(n-1)] and r)(args[0], lambda x: self._call_function(args[1], [x]), int(args[2])))
        if member == 'mapEvery': return ('builtin', lambda args, ctx: [self._call_function(args[1], [x]) if (i+1) % int(args[0]) == 0 else x for i, x in enumerate(obj)])
        if member in ('takeWhileRight', 'dropWhileRight'): return ('builtin', lambda args, ctx: (lambda r: list(reversed(r)) if member == 'takeWhileRight' else obj[:len(obj)-len(r)])(list(__import__('itertools').takewhile(lambda x: self._call_function(args[0], [x]), reversed(obj)))))
        if member in ('mapPrev', 'mapWithBoth'): return ('builtin', lambda args, ctx: [self._call_function(args[0], [obj[i-1] if i > 0 else obj[i], obj[i]] + ([obj[i+1] if i < len(obj)-1 else obj[i]] if member == 'mapWithBoth' else [])) for i in range(len(obj))])
        if member == 'mapWithContext': return ('builtin', lambda args, ctx: (lambda: (s := [args[0]]) and [s.append(self._call_function(args[1], [s[-1], x])) for x in obj] and s[1:])())
        if member == 'foldMap': return ('builtin', lambda args, ctx: sum(self._call_function(args[0], [x]) for x in obj))
        if member == 'mapZip': return ('builtin', lambda args, ctx: [self._call_function(args[1], [a, b]) for a, b in zip(obj, args[0])])
        if member == 'mapWithLast': return ('builtin', lambda args, ctx: (lambda: (r := [obj[0]]) and [r.append(self._call_function(args[0], [obj[i], r[-1]])) for i in range(1, len(obj))] and r)())
        if member == 'mapUntil': return ('builtin', lambda args, ctx: (lambda: (s := [False]) and [(x if s[0] else (s.__setitem__(0, True) or x) if self._call_function(args[0], [x]) else self._call_function(args[1], [x])) for x in obj])())
        if member == 'mapAdjacent': return ('builtin', lambda args, ctx: [self._call_function(args[1], obj[i:i+int(args[0])]) for i in range(len(obj) - int(args[0]) + 1)])
        if member == 'mapChunked': return ('builtin', lambda args, ctx: [self._call_function(args[1], obj[i:i+int(args[0])]) for i in range(0, len(obj), int(args[0]))])
        if member == 'mapWhere': return ('builtin', lambda args, ctx: [self._call_function(args[1], [x]) if self._call_function(args[0], [x]) else x for x in obj])
        if member == 'mapReverse': return ('builtin', lambda args, ctx: [self._call_function(args[0], [x]) for x in reversed(obj)])
        if member in ('mapFlatMap', 'mapConcat'): return ('builtin', lambda args, ctx: [y for x in obj for y in (lambda r: r if isinstance(r, list) else [r])(self._call_function(args[0], [x]))])
        if member == 'mapPairwise': return ('builtin', lambda args, ctx: [self._call_function(args[0], [obj[i], obj[i+1]]) for i in range(0, len(obj) - 1, 2)])
        if member in ('mapExcept', 'mapOnly'): return ('builtin', lambda args, ctx: [(self._call_function(args[1], [obj[i]]) if (i in args[0]) == (member == 'mapOnly') else obj[i]) for i in range(len(obj))])
        if member in ('mapSkip', 'mapTake'): return ('builtin', lambda args, ctx: [(obj[i] if i < int(args[0]) else self._call_function(args[1], [obj[i]])) if member == 'mapSkip' else (self._call_function(args[1], [obj[i]]) if i < int(args[0]) else obj[i]) for i in range(len(obj))])
        if member == 'mapIntersperse': return ('builtin', lambda args, ctx: [v for i, x in enumerate(obj) for v in (([args[0], x] if i else [x]))])
        if member == 'mapBatch': return ('builtin', lambda args, ctx: [self._call_function(args[1], [obj[i:i+int(args[0])]]) for i in range(0, len(obj), int(args[0]))])
        if member in ('mapTakeWhile', 'mapDropWhile'): return ('builtin', lambda args, ctx: list(__import__('itertools').takewhile(lambda x: self._call_function(args[0], [x]), obj)) if member == 'mapTakeWhile' else list(__import__('itertools').dropwhile(lambda x: self._call_function(args[0], [x]), obj)))
        if member == 'mapScan': return ('builtin', lambda args, ctx: list(__import__('itertools').accumulate(obj, lambda a, x: self._call_function(args[1], [a, x]), initial=args[0]))[1:])
        if member == 'mapPartition': return ('builtin', lambda args, ctx: [[x for x in obj if self._call_function(args[0], [x])], [x for x in obj if not self._call_function(args[0], [x])]])
        if member == 'mapGroupBy': return ('builtin', lambda args, ctx: (lambda d: [d.setdefault(self._call_function(args[0], [x]), []).append(x) for x in obj] and d)({}))
        if member == 'mapZipWith': return ('builtin', lambda args, ctx: [[a, b] for a, b in zip(obj, args[0])])
        if member == 'mapWindow': return ('builtin', lambda args, ctx: [obj[i:i+int(args[0])] for i in range(len(obj)-int(args[0])+1)])
        if member == 'mapChunkEvery': return ('builtin', lambda args, ctx: [obj[i:i+int(args[0])] for i in range(0, len(obj), int(args[0]))])
        if member == 'mapRotate': return ('builtin', lambda args, ctx: (lambda n: obj[n:] + obj[:n])(int(args[0]) % len(obj) if obj else 0))
        if member == 'mapConsecutive': return ('builtin', lambda args, ctx: [self._call_function(args[1], [obj[i:i+int(args[0])]]) for i in range(len(obj)-int(args[0])+1)])
        if member == 'mapStutter': return ('builtin', lambda args, ctx: [x for item in obj for x in [item] * int(args[0])])
        if member == 'mapDedupBy': return ('builtin', lambda args, ctx: (lambda s: [x for x in obj if (k := self._call_function(args[0], [x])) not in s and not s.add(k)])(set()))
        if member == 'mapSplitWhen': return ('builtin', lambda args, ctx: (lambda i: [obj[:i], obj[i:]])(next((i for i, x in enumerate(obj) if self._call_function(args[0], [x])), len(obj))))
        if member == 'mapRepeat': return ('builtin', lambda args, ctx: obj * int(args[0]))
        if member == 'mapCycle': return ('builtin', lambda args, ctx: [obj[i % len(obj)] for i in range(int(args[0]))])
        if member == 'mapPartitionAt': return ('builtin', lambda args, ctx: [obj[:int(args[0])], obj[int(args[0]):]])
        if member == 'mapInsertAt': return ('builtin', lambda args, ctx: obj[:int(args[0])] + [args[1]] + obj[int(args[0]):])
        if member == 'mapRemoveAt': return ('builtin', lambda args, ctx: obj[:int(args[0])] + obj[int(args[0])+1:])
        if member == 'mapSwapAt': return ('builtin', lambda args, ctx: (lambda r, i, j: r.__setitem__(i, obj[j]) or r.__setitem__(j, obj[i]) or r)(list(obj), int(args[0]), int(args[1])))
        if member == 'mapReplaceAt': return ('builtin', lambda args, ctx: obj[:int(args[0])] + [args[1]] + obj[int(args[0])+1:])
        if member == 'mapRotateLeft': return ('builtin', lambda args, ctx: (lambda n: obj[n:] + obj[:n])(int(args[0]) % len(obj) if obj else 0))
        if member == 'mapRotateRight': return ('builtin', lambda args, ctx: (lambda n: obj[-n:] + obj[:-n] if n else list(obj))(int(args[0]) % len(obj) if obj else 0))
        if member == 'mapFillTo': return ('builtin', lambda args, ctx: obj + [args[1]] * max(0, int(args[0]) - len(obj)))
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
            'isDigit': lambda: len(obj) > 0 and obj.isdigit(), 'isAlpha': lambda: len(obj) > 0 and obj.isalpha(),
            'isUpper': lambda: len(obj) > 0 and obj.isupper(), 'isLower': lambda: len(obj) > 0 and obj.islower(),
            'isBlank': lambda: len(obj.strip()) == 0, 'isAlphanumeric': lambda: len(obj) > 0 and obj.isalnum(),
            'rot13': lambda: ''.join(chr((ord(c) - (65 if c.isupper() else 97) + 13) % 26 + (65 if c.isupper() else 97)) if c.isalpha() else c for c in obj), 'isPalindrome': lambda: obj == obj[::-1],
            'wordCount': lambda: len(obj.split()) if obj.strip() else 0, 'initials': lambda: ''.join(w[0].upper() for w in obj.split() if w), 'codePoints': lambda: [ord(c) for c in obj], 'toCharCodes': lambda: [ord(c) for c in obj],
            'isHexColor': lambda: bool(__import__('re').match(r'^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$', obj)), 'normalize': lambda: ' '.join(obj.split()),
            'isIPv4': lambda: len(p := obj.split('.')) == 4 and all(s.isdigit() and 0 <= int(s) <= 255 for s in p), 'isPangram': lambda: set('abcdefghijklmnopqrstuvwxyz').issubset(obj.lower()),
            'collapseWhitespace': lambda: ' '.join(obj.split()), 'reverseWords': lambda: ' '.join(obj.split()[::-1]),
            'trimLines': lambda: '\n'.join(l.strip() for l in obj.split('\n')),
            'removeDuplicateChars': lambda: ''.join(obj[i] for i in range(len(obj)) if i == 0 or obj[i] != obj[i-1]),
            'toAcronym': lambda: ''.join(w[0].upper() for w in obj.split() if w), 'sizeInBytes': lambda: len(obj.encode('utf-8')),
            'isWhitespace': lambda: len(obj) > 0 and obj.isspace(), 'isHex': lambda: len(obj) > 0 and all(c in '0123456789abcdefABCDEF' for c in obj),
            'isAscii': lambda: all(ord(c) < 128 for c in obj), 'toHashCode': lambda: hash(obj),
            'isDate': lambda: bool(__import__('re').match(r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$', obj)),
            'toSentenceCase': lambda: obj[0].upper() + obj[1:].lower() if obj else '',
            'isPhoneNumber': lambda: bool(__import__('re').match(r'^[\+]?[\d\s\-\(\)]{7,}$', obj)), 'countVowels': lambda: sum(1 for c in obj.lower() if c in 'aeiou'),
            'countConsonants': lambda: sum(1 for c in obj.lower() if c.isalpha() and c not in 'aeiou'), 'mirror': lambda: obj + obj[::-1],
            'toAlternatingCase': lambda: ''.join(c.upper() if i % 2 else c.lower() for i, c in enumerate(obj)), 'isUpperCamelCase': lambda: bool(__import__('re').match(r'^[A-Z][a-zA-Z0-9]*$', obj)),
            'isCamelCase': lambda: bool(__import__('re').match(r'^[a-z][a-zA-Z0-9]*$', obj)) and '_' not in obj, 'isSnakeCase': lambda: bool(__import__('re').match(r'^[a-z][a-z0-9_]*$', obj)) and '__' not in obj,
            'isKebabCase': lambda: bool(__import__('re').match(r'^[a-z][a-z0-9\-]*$', obj)) and '--' not in obj, 'squeezeBlanks': lambda: __import__('re').sub(r'\n{3,}', '\n\n', obj),
            'removeVowels': lambda: ''.join(c for c in obj if c.lower() not in 'aeiou'), 'removeConsonants': lambda: ''.join(c for c in obj if not c.isalpha() or c.lower() in 'aeiou'),
            'toCamelWords': lambda: __import__('re').sub(r'([a-z])([A-Z])', r'\1_\2', obj).split('_'), 'toWordArray': lambda: obj.split(), 'charCount': lambda: len(set(obj)),
            'encodeURI': lambda: __import__('urllib.parse', fromlist=['quote']).quote(obj, safe=''), 'decodeURI': lambda: __import__('urllib.parse', fromlist=['unquote']).unquote(obj),
            'toSlug': lambda: __import__('re').sub(r'-+', '-', __import__('re').sub(r'[^a-z0-9]+', '-', obj.lower())).strip('-'),
            'toSnakeCase': lambda: __import__('re').sub(r'[\s\-]+', '_', __import__('re').sub(r'([a-z])([A-Z])', r'\1_\2', obj)).lower(),
            'toCamelCase': lambda: (lambda w: w[0].lower() + ''.join(x.title() for x in w[1:]) if w else '')(__import__('re').split(r'[\s_\-]+', obj)),
            'toKebabCase': lambda: __import__('re').sub(r'[\s_]+', '-', __import__('re').sub(r'([a-z])([A-Z])', r'\1-\2', obj)).lower(),
            'toBase64': lambda: __import__('base64').b64encode(obj.encode()).decode(),
            'fromBase64': lambda: __import__('base64').b64decode(obj.encode()).decode(),
            'toMd5': lambda: __import__('hashlib').md5(obj.encode()).hexdigest(),
            'toSha256': lambda: __import__('hashlib').sha256(obj.encode()).hexdigest(), 'toHex': lambda: obj.encode().hex(), 'fromHex': lambda: bytes.fromhex(obj).decode(),
            'toROT13': lambda: obj.translate(str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')),
            'toCRC32': lambda: format(__import__('zlib').crc32(obj.encode()) & 0xFFFFFFFF, '08x'),
            'toMorseCode': lambda: ' '.join({'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.'}[c] for c in obj.upper() if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'),
            'toBraille': lambda: ''.join(chr(0x2800 + [1,3,9,25,17,11,27,19,10,26][ord(c)-ord('a')]) if 'a' <= c <= 'j' else chr(0x2800 + [5,7,13,29,21,15,31,23,14,30][ord(c)-ord('k')]) if 'k' <= c <= 't' else chr(0x2800 + [37,39,58,45,61,53][ord(c)-ord('u')]) if 'u' <= c <= 'z' else c for c in obj.lower()),
            'toNato': lambda: ' '.join({'A':'Alfa','B':'Bravo','C':'Charlie','D':'Delta','E':'Echo','F':'Foxtrot','G':'Golf','H':'Hotel','I':'India','J':'Juliet','K':'Kilo','L':'Lima','M':'Mike','N':'November','O':'Oscar','P':'Papa','Q':'Quebec','R':'Romeo','S':'Sierra','T':'Tango','U':'Uniform','V':'Victor','W':'Whiskey','X':'X-ray','Y':'Yankee','Z':'Zulu'}.get(c, c) for c in obj.upper() if c.isalpha()),
            'toPhonetic': lambda: '-'.join(c for c in obj.lower() if c.isalpha()), 'toAtbash': lambda: ''.join(chr(219 - ord(c)) if 'a' <= c <= 'z' else chr(155 - ord(c)) if 'A' <= c <= 'Z' else c for c in obj),
            'toA1Z26': lambda: '-'.join(str(ord(c) - 96) for c in obj.lower() if c.isalpha()),
            'toTapCode': lambda: ' '.join((lambda p: f'{p//5+1},{p%5+1}')((lambda c: ord(c)-ord('a') if c < 'k' else ord(c)-ord('a')-1)(c)) for c in obj.lower().replace('k','c') if c.isalpha()),
            'toPolybius': lambda: ' '.join((lambda p: f'{p//5+1}{p%5+1}')((lambda c: ord(c)-ord('a') if c < 'k' else ord(c)-ord('a')-1)(c)) for c in obj.lower().replace('k','c') if c.isalpha()),
            'toBacon': lambda: ' '.join(bin(ord(c) - ord('a'))[2:].zfill(5).replace('0', 'A').replace('1', 'B') for c in obj.lower() if c.isalpha()),
            'toSemaphore': lambda: ' '.join(str(ord(c) - ord('a') + 1) for c in obj.lower() if c.isalpha()), 'toASCIIArt': lambda: ' '.join(str(ord(c)) for c in obj),
            'toBinary': lambda: ' '.join(format(ord(c), '08b') for c in obj), 'toOctal': lambda: ' '.join(format(ord(c), 'o') for c in obj), 'toDecimal': lambda: ','.join(str(ord(c)) for c in obj), 'toUnicodeEscape': lambda: ''.join(f'\\u{ord(c):04x}' for c in obj),
            'toHTMLEntities': lambda: obj.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;'), 'toURLEncode': lambda: __import__('urllib.parse', fromlist=['quote']).quote(obj), 'toURLDecode': lambda: __import__('urllib.parse', fromlist=['unquote']).unquote(obj),
            'toPigLatin': lambda: ' '.join((w + 'yay' if w[0].lower() in 'aeiou' else (lambda i: w[i:] + w[:i] + 'ay')(next((j for j in range(len(w)) if w[j].lower() in 'aeiou'), len(w)))) for w in obj.split()),
            'toBase32': lambda: __import__('base64').b32encode(obj.encode()).decode().rstrip('='),
            'toROT47': lambda: ''.join(chr(33 + (ord(c) - 33 + 47) % 94) if 33 <= ord(c) <= 126 else c for c in obj),
            'toCharFreq': lambda: ' '.join(f'{c}:{obj.count(c)}' for c in dict.fromkeys(obj)),
            'toZalgo': lambda: ''.join(c + ''.join(chr(r) for r in __import__('random').choices(range(0x0300, 0x036f), k=3)) for c in obj),
            'toSpongeCase': lambda: ''.join(c.upper() if i % 2 else c.lower() for i, c in enumerate(obj)),
            'toTitleSnakeCase': lambda: '_'.join(w.capitalize() for w in __import__('re').split(r'[\s_\-]+', obj)),
            'toScreamingKebab': lambda: '-'.join(w.upper() for w in __import__('re').split(r'[\s_\-]+', obj)),
            'toWordReverse': lambda: ' '.join(w[::-1] for w in obj.split()),
            'toDotNotation': lambda: '.'.join(__import__('re').split(r'[\s_\-]+', obj)),
            'toUpperFirst': lambda: ' '.join(w[0].upper() + w[1:] if w else '' for w in obj.split(' ')),
            'toLowerFirst': lambda: ' '.join(w[0].lower() + w[1:] if w else '' for w in obj.split(' ')),
            'toAbbreviation': lambda: ''.join(w[0].upper() for w in obj.split() if w),
            'toInitials': lambda: '.'.join(w[0].upper() for w in obj.split() if w) + '.',
            'toSlugCase': lambda: '-'.join(w.lower() for w in __import__('re').split(r'[\s_\-]+', obj)),
            'toHeaderCase': lambda: '-'.join(w.capitalize() for w in __import__('re').split(r'[\s_\-]+', obj)),
            'toSwapCase': lambda: obj.swapcase(),
            'toSqueeze': lambda: ''.join(c for i, c in enumerate(obj) if i == 0 or c != obj[i-1]),
            'toRunLength': lambda: ''.join(f'{k}{sum(1 for _ in g)}' for k, g in __import__('itertools').groupby(obj)), 'toCharArray': lambda: list(obj), 'toWordBoundary': lambda: [w for w in __import__('re').split(r'(?<=[a-z])(?=[A-Z])|[\s_\-]+', obj) if w], 'toReverse': lambda: obj[::-1], 'toDoubleQuoted': lambda: '"' + obj + '"', 'toSingleQuoted': lambda: "'" + obj + "'", 'toBackticked': lambda: '`' + obj + '`', 'toParenthesized': lambda: '(' + obj + ')', 'toBracketed': lambda: '[' + obj + ']', 'toCurlyBraced': lambda: '{' + obj + '}', 'toAngleBracketed': lambda: '<' + obj + '>', 'toPipeDelimited': lambda: '|'.join(obj.split()), 'toCommaDelimited': lambda: ','.join(obj.split()), 'toTabDelimited': lambda: '\t'.join(obj.split()), 'toColonDelimited': lambda: ':'.join(obj.split()), 'toSemicolonDelimited': lambda: ';'.join(obj.split()), 'toDashDelimited': lambda: '-'.join(obj.split()), 'toSpaceDelimited': lambda: ' '.join(__import__('re').split(r'[-_\s]+', obj)),
        }
        if member == 'toMorse': member = 'toMorseCode'
        if member in _noarg:
            fn = _noarg[member]
            return ('builtin', lambda args, ctx: fn())
        # Single-arg methods
        _onearg = {
            'contains': lambda a: a[0] in obj, 'includes': lambda a: a[0] in obj,
            'starts_with': lambda a: obj.startswith(a[0]), 'ends_with': lambda a: obj.endswith(a[0]),
            'indexOf': lambda a: obj.find(a[0]), 'lastIndexOf': lambda a: obj.rfind(a[0]),
            'count': lambda a: obj.count(a[0]), 'split': lambda a: obj.split(a[0] if a else " "), 'repeat': lambda a: obj * int(a[0]),
            'charAt': lambda a: obj[int(a[0])], 'charCodeAt': lambda a: ord(obj[int(a[0])]), 'zfill': lambda a: obj.zfill(int(a[0])),
            'countWords': lambda a: obj.split().count(a[0]), 'isAnagram': lambda a: sorted(obj.lower().replace(' ', '')) == sorted(a[0].lower().replace(' ', '')),
            'indent': lambda a: '\n'.join(' ' * int(a[0]) + l for l in obj.split('\n')), 'surround': lambda a: a[0] + obj + a[0], 'removeAt': lambda a: obj[:int(a[0])] + obj[int(a[0])+1:],
            'wordWrap': lambda a: (lambda w, words: '\n'.join(lines) if (lines := __import__('functools').reduce(lambda acc, word: acc[:-1] + [acc[-1] + ' ' + word] if acc and len(acc[-1]) + 1 + len(word) <= w else acc + [word], words, [])) else '')(int(a[0]), obj.split()),
            'caesarCipher': lambda a: ''.join(chr((ord(c) - (65 if c.isupper() else 97) + int(a[0])) % 26 + (65 if c.isupper() else 97)) if c.isalpha() else c for c in obj),
            'vigenereCipher': lambda a: ''.join(chr((ord(c) - 97 + ord(a[0][i % len(a[0])].lower()) - 97) % 26 + 97) if c.isalpha() else c for i, c in enumerate(obj.lower())),
            'toColumnar': lambda a: ''.join(obj[i::int(a[0])] for i in range(int(a[0]))),
            'toCenterPad': lambda a: obj.center(int(a[0])),
            'toNGram': lambda a: [obj[i:i+int(a[0])] for i in range(len(obj)-int(a[0])+1)],
        }
        if member in _onearg:
            fn = _onearg[member]
            return ('builtin', lambda args, ctx: fn(args))
        if member == 'toRailFence':
            def _rf(args, ctx):
                n, r = int(args[0]), ['' for _ in range(int(args[0]))]
                row, d = 0, 1
                for c in obj:
                    r[row] += c; row += d
                    if row == 0 or row == n - 1: d = -d
                return ''.join(r)
            return ('builtin', _rf)
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
            'insertAt': lambda a: obj[:int(a[0])] + a[1] + obj[int(a[0]):],
        }
        if member in _twoarg:
            fn = _twoarg[member]
            return ('builtin', lambda args, ctx: fn(args))
        if member in ('substring', 'slice'):
            return ('builtin', lambda args, ctx: obj[int(args[0]):int(args[1])] if len(args) > 1 else obj[int(args[0]):])
        if member in ('toInt', 'toFloat'):
            def _conv(args, ctx):
                try: v = int(obj) if member == 'toInt' else float(obj); return v if member == 'toInt' or v != int(v) else int(v)
                except ValueError: raise RuntimeError_(f"Cannot convert '{obj}' to {'int' if member == 'toInt' else 'float'}")
            return ('builtin', _conv)
        if member == 'format':
            return ('builtin', lambda args, ctx: __import__('functools').reduce(lambda r, a: r.replace('{}', silk_repr(a), 1), args, obj))
        if member in ('removePrefix', 'removeSuffix'):
            return ('builtin', lambda args, ctx: (obj[len(args[0]):] if obj.startswith(args[0]) else obj) if member == 'removePrefix' else (obj[:-len(args[0])] if obj.endswith(args[0]) else obj))
        if member == 'truncate':
            return ('builtin', lambda args, ctx: obj if len(obj) <= int(args[0]) else obj[:int(args[0]) - len(args[1] if len(args) > 1 else '')] + (args[1] if len(args) > 1 else ''))
        if member == 'isNumeric':
            def _n(args, ctx):
                try: return bool(obj) and float(obj) is not None
                except ValueError: return False
            return ('builtin', _n)
        if member == 'squeeze': return ('builtin', lambda args, ctx: __import__('re').sub(r' {2,}', ' ', obj))
        if member == 'at': return ('builtin', lambda args, ctx: obj[int(args[0])] if -len(obj) <= int(args[0]) < len(obj) else None)
        if member in ('camelCase', 'snakeCase', 'kebabCase', 'titleCase', 'toPascalCase', 'toConstantCase', 'toDotCase', 'toPathCase', 'toTrainCase'):
            def _cc(args, ctx, _re=__import__('re')):
                p = [w for s in _re.split(r'[-_\s]+', obj) for w in _re.sub(r'([a-z])([A-Z])', r'\1_\2', s).split('_') if w]
                if member == 'camelCase': return p[0].lower() + ''.join(w.capitalize() for w in p[1:])
                if member in ('titleCase', 'toPascalCase', 'toTrainCase'): return (' ' if member == 'titleCase' else '-' if member == 'toTrainCase' else '').join(w.capitalize() for w in p)
                sep = {'snakeCase': '_', 'toConstantCase': '_', 'toDotCase': '.', 'toPathCase': '/'}.get(member, '-')
                r = _re.sub(r'([a-z])([A-Z])', r'\1' + sep + r'\2', _re.sub(r'[-_\s]+', sep, obj))
                return r.upper() if member == 'toConstantCase' else r.lower()
            return ('builtin', _cc)
        if member == 'truncateWords':
            return ('builtin', lambda args, ctx: obj if len(w := obj.split()) <= int(args[0]) else ' '.join(w[:int(args[0])]) + '...')
        if member == 'isEmail':
            return ('builtin', lambda args, ctx: len(p := obj.split('@')) == 2 and len(p[0]) > 0 and '.' in p[1])
        if member == 'partition':
            return ('builtin', lambda args, ctx: list(obj.partition(args[0])))
        if member in ('commonPrefix', 'commonSuffix'):
            return ('builtin', lambda args, ctx: (lambda p: (lambda a, b, i: obj[:i] if member == 'commonPrefix' else (obj[len(obj)-i:] if i else ''))(p[0], p[1], next((i for i in range(min(len(p[0]), len(p[1]))) if p[0][i] != p[1][i]), min(len(p[0]), len(p[1])))))((obj, args[0]) if member == 'commonPrefix' else (obj[::-1], args[0][::-1])))
        if member == 'levenshtein':
            def _lev(args, ctx):
                o, m, n = args[0], len(obj), len(args[0])
                if not m or not n: return m or n
                return __import__('functools').reduce(lambda p, i: (c := [i+1]+[0]*n) and [c.__setitem__(j, min(c[j-1]+1, p[j]+1, p[j-1]+(obj[i]!=o[j-1]))) for j in range(1, n+1)] and c, range(m), list(range(n+1)))[n]
            return ('builtin', _lev)
        if member == 'hamming':
            return ('builtin', lambda args, ctx: sum(a != b for a, b in zip(obj, args[0])))
        if member == 'soundex':
            return ('builtin', lambda args, ctx, _c={c: d for d, cs in enumerate('AEIOUYHW,BFPV,CGJKQSXZ,DT,L,MN,R'.split(',')) for c in cs}: '' if not obj else (__import__('functools').reduce(lambda rp, ch: ((rp[0]+str(cd), cd or rp[1]) if (cd := _c.get(ch.upper(), 0)) > 0 and cd != rp[1] else (rp[0], cd or rp[1])), obj[1:], (obj[0].upper(), _c.get(obj[0].upper(), 0)))[0] + '000')[:4])
        if member == 'isUrl':
            return ('builtin', lambda args, ctx: obj.startswith(('http://', 'https://')) and '.' in obj.split('//')[1])
        if member == 'caesar':
            return ('builtin', lambda args, ctx: ''.join(chr((ord(c) - (65 if c.isupper() else 97) + int(args[0])) % 26 + (65 if c.isupper() else 97)) if c.isalpha() else c for c in obj))
        if member == 'charFrequency':
            return ('builtin', lambda args, ctx: (lambda f: [f.update({c: f.get(c, 0) + 1}) for c in obj] and f or f)({}))
        if member == 'dedent':
            return ('builtin', lambda args, ctx: (lambda ls, m: '\n'.join(l[m:] for l in ls))(obj.split('\n'), min((len(l)-len(l.lstrip()) for l in obj.split('\n') if l.strip()), default=0)))
        if member in ('slugify', 'toTitleSlug'):
            import re as _re; return ('builtin', lambda args, ctx: _re.sub(r'-+', '-', _re.sub(r'[^a-z0-9]+', '-', obj.lower())).strip('-'))
        if member == 'isJSON':
            def _ij(args, ctx):
                try: json.loads(obj); return True
                except: return False
            return ('builtin', _ij)
        if member in ('encodeBase64', 'decodeBase64'): return ('builtin', lambda args, ctx: (__import__('base64').b64encode if member == 'encodeBase64' else __import__('base64').b64decode)(obj.encode()).decode())
        if member == 'matchCount': return ('builtin', lambda args, ctx: len(__import__('re').findall(args[0], obj)))
        if member == 'extractNumbers': return ('builtin', lambda args, ctx: [int(n) if n.isdigit() else float(n) for n in __import__('re').findall(r'-?\d+\.?\d*', obj)])
        if member == 'extractEmails': return ('builtin', lambda args, ctx: __import__('re').findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', obj))
        if member == 'extractUrls': return ('builtin', lambda args, ctx: __import__('re').findall(r'https?://[^\s]+', obj))
        if member == 'parseXML': return ('builtin', lambda args, ctx: dict(__import__('re').findall(r'<(\w+)>([^<]*)</\1>', obj)))
        if member == 'wordFrequency': return ('builtin', lambda args, ctx: (lambda f: [f.update({w: f.get(w, 0) + 1}) for w in obj.split()] and f or f)({}) if obj.strip() else {})
        if member == 'isBalanced': return ('builtin', lambda args, ctx, _m={')':'(',']':'[','}':'{'}: __import__('functools').reduce(lambda s, c: None if s is None else (s + [c] if c in '([{' else (None if not s or s.pop() != _m[c] else s) if c in _m else s), obj, []) == [])
        if member == 'isISBN': return ('builtin', lambda args, ctx: len(obj) == 10 and obj[:9].isdigit() and sum((10-i)*int(c) for i, c in enumerate(obj[:9])) % 11 == (11 - int(obj[9])) % 11 if obj[9].isdigit() else False)
        if member == 'occurrences': return ('builtin', lambda args, ctx: [i for i in range(len(obj)) if obj[i:i+len(args[0])] == args[0]])
        if member == 'isCreditCard': return ('builtin', lambda args, ctx: obj.isdigit() and len(obj) >= 13 and sum(int(d) for d in obj[-1::-2]) + sum(sum(divmod(2 * int(d), 10)) for d in obj[-2::-2]) == 0 if not obj.isdigit() else (sum(int(d) for d in obj[-1::-2]) + sum(sum(divmod(2 * int(d), 10)) for d in obj[-2::-2])) % 10 == 0)
        raise RuntimeError_(f"'str' has no member '{member}'")

    def _eval_number_member(self, obj: int | float, member: str) -> Any:
        """Evaluate member access on a number."""
        def _to_base(n, base, _d='0123456789abcdefghijklmnopqrstuvwxyz'):
            if n == 0: return '0'
            neg, n, r = n < 0, abs(n), []
            while n: r.append(_d[n % base]); n //= base
            return ('-' if neg else '') + ''.join(reversed(r))
        _simple = {
            'abs': lambda: abs(obj), 'floor': lambda: math.floor(obj), 'ceil': lambda: math.ceil(obj), 'round': lambda: round(obj),
            'toString': lambda: str(obj), 'sqrt': lambda: math.sqrt(obj),
            'isEven': lambda: int(obj) % 2 == 0, 'isOdd': lambda: int(obj) % 2 != 0,
            'isPositive': lambda: obj > 0, 'isNegative': lambda: obj < 0,
            'isZero': lambda: obj == 0, 'isInteger': lambda: isinstance(obj, int), 'isFloat': lambda: isinstance(obj, float), 'sign': lambda: (1 if obj > 0 else (-1 if obj < 0 else 0)),
            'toRadians': lambda: obj * math.pi / 180, 'toDegrees': lambda: obj * 180 / math.pi, 'factorial': lambda: math.factorial(int(obj)), 'toBinary': lambda: bin(int(obj))[2:],
            'toHex': lambda: hex(int(obj))[2:], 'toOctal': lambda: oct(int(obj))[2:], 'toChar': lambda: chr(int(obj)), 'digitSum': lambda: sum(int(d) for d in str(abs(int(obj)))), 'digitCount': lambda: len(str(abs(int(obj)))),
            'isPerfect': lambda: int(obj) > 1 and sum(i for i in range(1, int(obj)) if int(obj) % i == 0) == int(obj), 'toScientific': lambda: f"{obj:.1e}", 'factors': lambda: sorted(i for i in range(1, int(obj) + 1) if int(obj) % i == 0),
            'divisorCount': lambda: sum(1 for i in range(1, int(obj) + 1) if int(obj) % i == 0), 'digitalRoot': lambda: 0 if obj == 0 else 1 + (int(obj) - 1) % 9, 'isHarshad': lambda: int(obj) > 0 and int(obj) % sum(int(d) for d in str(int(obj))) == 0,
            'sumTo': lambda: int(obj) * (int(obj) + 1) // 2, 'aliquotSum': lambda: sum(i for i in range(1, int(obj)) if int(obj) % i == 0),
            'isAutomorphic': lambda: str(int(obj) ** 2).endswith(str(int(obj))), 'toBits': lambda: [int(b) for b in bin(int(obj))[2:]], 'isKaprekar': lambda: (lambda n, sq: any(int(str(sq)[:i]) + int(str(sq)[i:]) == n for i in range(1, len(str(sq)))) if n > 0 else False)(int(obj), int(obj) ** 2),
            'cubeRoot': lambda: (lambda r: int(r) if r == int(r) else r)(round(obj ** (1/3), 10)), 'isAbundant': lambda: sum(i for i in range(1, int(obj)) if int(obj) % i == 0) > int(obj), 'isDeficient': lambda: sum(i for i in range(1, int(obj)) if int(obj) % i == 0) < int(obj),
            'isPowerOfTwo': lambda: int(obj) > 0 and (int(obj) & (int(obj) - 1)) == 0, 'sumOfSquares': lambda: sum(i * i for i in range(1, int(obj) + 1)), 'isNarcissistic': lambda: (lambda s, n: sum(int(d) ** n for d in s) == int(obj))(str(abs(int(obj))), len(str(abs(int(obj))))),
            'isSquare': lambda: int(obj) >= 0 and int(obj ** 0.5) ** 2 == int(obj), 'isCube': lambda: round(abs(int(obj)) ** (1/3)) ** 3 == abs(int(obj)),
            'isMersennePrime': lambda: (lambda n: n > 1 and (n + 1) & n == 0 and all(n % i for i in range(2, int(n**0.5) + 1)))(int(obj)), 'isTriangular': lambda: (lambda n: int((8*n+1)**0.5)**2 == 8*n+1)(int(obj)),
            'totient': lambda: sum(1 for i in range(1, int(obj) + 1) if math.gcd(i, int(obj)) == 1), 'harmonicSum': lambda: (lambda r: int(r) if r == int(r) else r)(sum(1/i for i in range(1, int(obj) + 1))),
            'isPronic': lambda: (lambda k: k * (k + 1) == int(obj))(int(int(obj) ** 0.5)),
            'digitProduct': lambda: __import__('functools').reduce(lambda a, b: a * b, (int(d) for d in str(abs(int(obj))))), 'reverseDigits': lambda: int(str(abs(int(obj)))[::-1]) * (1 if int(obj) >= 0 else -1), 'digitReverse': lambda: int(str(abs(int(obj)))[::-1]) * (1 if int(obj) >= 0 else -1),
            'isSmith': lambda: (lambda n, ds, pf: n > 1 and not all(n % i for i in range(2, int(n**0.5)+1)) and ds(n) == sum(ds(p) for p in pf(n)))(int(obj), lambda x: sum(int(d) for d in str(x)), lambda n: (f := lambda n, d: [] if n <= 1 else [d] + f(n//d, d) if n % d == 0 else f(n, d+1))(n, 2)), 'abundantBy': lambda: sum(i for i in range(1, int(obj)) if int(obj) % i == 0) - int(obj), 'abundance': lambda: sum(i for i in range(1, int(obj)) if int(obj) % i == 0) - int(obj),
            'isUntouchable': lambda: (lambda n: not any(sum(i for i in range(1, k) if k % i == 0) == n for k in range(2, 2*n+2)))(int(obj)), 'isSphenic': lambda: (lambda n, pf: len(pf) == 3 and len(set(pf)) == 3)((n := int(obj)), (f := lambda n, d: [] if n <= 1 else [d] + f(n//d, d) if n % d == 0 else f(n, d+1))(n, 2)), 'isSemiPrime': lambda: (lambda pf: len(pf) == 2)((f := lambda n, d: [] if n <= 1 else [d] + f(n//d, d) if n % d == 0 else f(n, d+1))(int(obj), 2)), 'isEmirp': lambda: (lambda n, ip: ip(n) and (r := int(str(n)[::-1])) != n and ip(r))(int(obj), lambda n: n >= 2 and all(n % i for i in range(2, int(n**0.5)+1))), 'pentagonal': lambda: int(obj) * (3 * int(obj) - 1) // 2, 'hexagonal': lambda: int(obj) * (2 * int(obj) - 1),
            'catalan': lambda: math.factorial(2 * int(obj)) // (math.factorial(int(obj) + 1) * math.factorial(int(obj))), 'bell': lambda: __import__('functools').reduce(lambda r, _: (s := [r[-1]]) and [s.append(s[-1]+v) for v in r] and s, range(int(obj)), [1])[0], 'derangements': lambda: round(math.factorial(int(obj)) * sum((-1)**k / math.factorial(k) for k in range(int(obj)+1))),
            'motzkin': lambda: __import__('functools').reduce(lambda ab, i: (ab[1], ((2*i+1)*ab[1] + 3*(i-1)*ab[0]) // (i+2)), range(1, int(obj)+1), (1, 1))[1] if int(obj) > 0 else 1,
            'tetrahedral': lambda: int(obj) * (int(obj) + 1) * (int(obj) + 2) // 6, 'pyramidal': lambda: int(obj) * (int(obj) + 1) * (2 * int(obj) + 1) // 6, 'star': lambda: 6 * int(obj) * (int(obj) - 1) + 1, 'oblong': lambda: int(obj) * (int(obj) + 1), 'pronic': lambda: int(obj) * (int(obj) + 1),
            'superFactorial': lambda: __import__('functools').reduce(lambda a, i: a * math.factorial(i), range(1, int(obj) + 1), 1), 'subfactorial': lambda: round(math.factorial(int(obj)) * sum((-1)**k / math.factorial(k) for k in range(int(obj)+1))), 'doubleFactorial': lambda: __import__('functools').reduce(lambda a, b: a * b, range(int(obj), 0, -2), 1),
            'primorial': lambda: __import__('functools').reduce(lambda a, b: a * b, [p for p in range(2, int(obj)+1) if all(p % i for i in range(2, int(p**0.5)+1))], 1), 'isLucky': lambda: (lambda n: (s := list(range(1, max(n*2, 10), 2))) and all((s := [s[j] for j in range(len(s)) if (j+1) % s[i] != 0]) or True for i in range(1, len(s)) if i < len(s) and s[i] <= len(s)) and n in s)(int(obj)),
            'isWieferich': lambda: (lambda n: n >= 2 and all(n % i for i in range(2, int(n**0.5)+1)) and pow(2, n-1, n*n) == 1)(int(obj)), 'isProth': lambda: (lambda n: n > 1 and any(n == k * (1 << e) + 1 and k < (1 << e) and k % 2 == 1 for e in range(1, n.bit_length()) for k in [((n-1) >> e)]))(int(obj)),
            'isHarmonious': lambda: (lambda n, d: n > 0 and (n * d) % sum(n // i for i in range(1, n+1) if n % i == 0) == 0)(int(obj), sum(1 for i in range(1, int(obj)+1) if int(obj) % i == 0)), 'sigma': lambda: sum(i for i in range(1, int(obj) + 1) if int(obj) % i == 0), 'divisorSum': lambda: sum(i for i in range(1, int(obj) + 1) if int(obj) % i == 0),
            'mobius': lambda: (lambda n, pf: 0 if len(pf) != len(set(pf)) else (-1)**len(pf))(int(obj), (f := lambda n, d: [] if n <= 1 else [d] + f(n//d, d) if n % d == 0 else f(n, d+1))(int(obj), 2)),
            'liouville': lambda: (-1)**len((f := lambda n, d: [] if n <= 1 else [d] + f(n//d, d) if n % d == 0 else f(n, d+1))(int(obj), 2)),
            'radical': lambda: __import__('functools').reduce(lambda a, b: a * b, set((f := lambda n, d: [] if n <= 1 else [d] + f(n//d, d) if n % d == 0 else f(n, d+1))(int(obj), 2)), 1),
            'omega': lambda: len(set((f := lambda n, d: [] if n <= 1 else [d] + f(n//d, d) if n % d == 0 else f(n, d+1))(int(obj), 2))), 'bigOmega': lambda: len((f := lambda n, d: [] if n <= 1 else [d] + f(n//d, d) if n % d == 0 else f(n, d+1))(int(obj), 2)),
            'isRegular': lambda: (lambda n, pf: n >= 1 and all(p in (2,3,5) for p in set(pf)))(int(obj), (lambda f, n: f(f, n, 2))(lambda s, n, d: [] if n <= 1 else [d] + s(s, n//d, d) if n % d == 0 else s(s, n, d+1), int(obj))),
            'isSquareFree': lambda: (lambda n: n >= 1 and all(n % (i*i) != 0 for i in range(2, int(n**0.5)+1)))(int(obj)),
            'isPractical': lambda: (lambda n: n >= 1 and (lambda ds: all(k <= 1 + sum(d for d in ds if d <= k) for k in range(1, n+1)))([i for i in range(1, n) if n % i == 0]))(int(obj)),
            'isHumble': lambda: (lambda n, pf: n >= 1 and all(p in (2,3,5,7) for p in set(pf)))(int(obj), (lambda f, n: f(f, n, 2))(lambda s, n, d: [] if n <= 1 else [d] + s(s, n//d, d) if n % d == 0 else s(s, n, d+1), int(obj))),
            'isSophieGermain': lambda: (lambda n, ip: ip(n) and ip(2*n+1))(int(obj), lambda n: n >= 2 and all(n % i for i in range(2, int(n**0.5)+1))),
            'isChen': lambda: (lambda n, ip, isp: ip(n) and (ip(n+2) or isp(n+2)))(int(obj), lambda n: n >= 2 and all(n % i for i in range(2, int(n**0.5)+1)), lambda n: len((f := lambda n, d: [] if n <= 1 else [d] + f(n//d, d) if n % d == 0 else f(n, d+1))(n, 2)) == 2),
            'isWasteful': lambda: (lambda n, pf: sum(len(str(p)) for p in pf) > len(str(n)))(int(obj), (lambda f, n: f(f, n, 2))(lambda s, n, d: [] if n <= 1 else [d] + s(s, n//d, d) if n % d == 0 else s(s, n, d+1), int(obj))),
            'isFrugal': lambda: (lambda n, pf: n > 1 and (lambda pe: sum(len(str(p)) + (len(str(e)) if e > 1 else 0) for p, e in pe) < len(str(n)))({p: pf.count(p) for p in set(pf)}.items()))(int(obj), (lambda f, n: f(f, n, 2))(lambda s, n, d: [] if n <= 1 else [d] + s(s, n//d, d) if n % d == 0 else s(s, n, d+1), int(obj))),
            'isEquidigital': lambda: (lambda n, pf: n > 1 and (lambda pe: sum(len(str(p)) + (len(str(e)) if e > 1 else 0) for p, e in pe) == len(str(n)))({p: pf.count(p) for p in set(pf)}.items()))(int(obj), (lambda f, n: f(f, n, 2))(lambda s, n, d: [] if n <= 1 else [d] + s(s, n//d, d) if n % d == 0 else s(s, n, d+1), int(obj))),
            'isSelfDescribing': lambda: (lambda s: all(int(s[i]) == s.count(str(i)) for i in range(len(s))))(str(int(obj))),
            'isTetrahedral': lambda: (lambda n: any(k*(k+1)*(k+2)//6 == n for k in range(int(n**(1/3))+3)))(int(obj)),
            'isOre': lambda: (lambda n, ds: len(ds) * n % sum(ds) == 0)(int(obj), [i for i in range(1, int(obj)+1) if int(obj) % i == 0]),
            'isPyramidal': lambda: (lambda n: any(k*(k+1)*(2*k+1)//6 == n for k in range(int((6*n)**(1/3))+2)))(int(obj)),
            'isStarNumber': lambda: (lambda n: n == 1 or (n > 0 and (n-1) % 6 == 0 and (lambda d: int(d**0.5)**2 == d)(1 + 4*((n-1)//6))))(int(obj)),
            'isCenteredSquare': lambda: (lambda n: n == 1 or (n > 0 and (n-1) % 2 == 0 and (lambda d: int(d**0.5)**2 == d)(1 + 4*((n-1)//2))))(int(obj)),
            'isCenteredHex': lambda: (lambda n: n == 1 or (n > 0 and (n-1) % 3 == 0 and (lambda d: int(d**0.5)**2 == d)(1 + 4*((n-1)//3))))(int(obj)),
            'isCenteredTriangular': lambda: (lambda n: n == 1 or (n > 0 and 2*(n-1) % 3 == 0 and (lambda d: int(d**0.5)**2 == d)(1 + 4*(2*(n-1)//3))))(int(obj)),
            'isDecagonal': lambda: (lambda n, d: d >= 0 and int(d**0.5)**2 == d and (3+int(d**0.5)) % 8 == 0)(int(obj), 9+16*int(obj)),
            'isHeptagonal': lambda: (lambda n, d: d >= 0 and int(d**0.5)**2 == d and (3+int(d**0.5)) % 10 == 0)(int(obj), 9+40*int(obj)),
            'isOctagonal': lambda: (lambda n, d: d >= 0 and int(d**0.5)**2 == d and (2+int(d**0.5)) % 6 == 0)(int(obj), 4+12*int(obj)),
            'isNonagonal': lambda: (lambda n, d: d >= 0 and int(d**0.5)**2 == d and (5+int(d**0.5)) % 14 == 0)(int(obj), 25+56*int(obj)),
            'isPowerful': lambda: (lambda n: n > 0 and any(n % (b**3) == 0 and int((n//(b**3))**0.5)**2 == n//(b**3) for b in range(1, int(n**(1/3))+2)))(int(obj)),
            'isAchilles': lambda: (lambda n: n > 1 and any(n % (b**3) == 0 and int((n//(b**3))**0.5)**2 == n//(b**3) for b in range(1, int(n**(1/3))+2)) and not any(round(n**(1/k)) ** k == n for k in range(2, int(n.bit_length())+1)))(int(obj)),
            'isTruncatablePrime': lambda: (lambda n: n > 1 and all((lambda m: m > 1 and all(m % i != 0 for i in range(2, int(m**0.5)+1)))(int(str(n)[:i])) for i in range(1, len(str(n))+1)))(int(obj)),
            'isCircularPrime': lambda: (lambda n, s: n > 1 and all((lambda m: m > 1 and all(m % i != 0 for i in range(2, int(m**0.5)+1)))(int(s[r:] + s[:r])) for r in range(len(s))))(int(obj), str(int(obj))),
            'isLeftTruncatablePrime': lambda: (lambda n: n > 1 and all((lambda m: m > 1 and all(m % i != 0 for i in range(2, int(m**0.5)+1)))(int(str(n)[i:])) for i in range(len(str(n)))))(int(obj)),
            'isKeith': lambda: (lambda n, ds: (lambda f: f(f, ds))((lambda f, s: True if s[-1] == n else False if s[-1] > n else f(f, s[1:] + [sum(s)]))))(int(obj), [int(d) for d in str(abs(int(obj)))]),
            'nearestPrime': lambda: (lambda n, ip: n if ip(n) else min((p for d in range(1, n) for p in (n-d, n+d) if p >= 2 and ip(p)), key=lambda p: (abs(p-n), p)))(int(obj), lambda n: n >= 2 and all(n % i for i in range(2, int(n**0.5)+1))),
            'digitPower': lambda: sum(int(d) ** (i+1) for i, d in enumerate(str(abs(int(obj))))),
            'digitRotateSum': lambda: (lambda s: sum(int(s[i:] + s[:i]) for i in range(len(s))))(str(int(obj))),
            'isPerfectSquareDigitSum': lambda: (lambda ds: int(ds**0.5)**2 == ds)(sum(int(d) for d in str(abs(int(obj))))),
            'coprimesUpTo': lambda: [i for i in range(1, int(obj)) if math.gcd(i, int(obj)) == 1],
            'digitFrequency': lambda: (lambda f: [f.update({int(d): f.get(int(d), 0) + 1}) for d in str(abs(int(obj)))] and f or f)({}),
            'digitGap': lambda: (lambda ds: max(abs(ds[i+1]-ds[i]) for i in range(len(ds)-1)))([int(d) for d in str(abs(int(obj)))]),
            'digitSort': lambda: int(''.join(sorted(str(abs(int(obj)))))),
            'digitSortDesc': lambda: int(''.join(sorted(str(abs(int(obj))), reverse=True))),
        }
        if member == 'isEconomical': member = 'isFrugal'
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
            'nthRoot': lambda a: (lambda r: int(r) if r == int(r) else r)(round(obj ** (1/a[0]), 10)),
            'isLychrel': lambda a: (f := lambda n, i: True if i <= 0 else (lambda r: False if str(r) == str(r)[::-1] else f(r, i-1))(n + int(str(n)[::-1])))(int(obj), int(a[0])),
            'sumOfDigitsPower': lambda a: sum(int(d) ** int(a[0]) for d in str(abs(int(obj)))),
            'stirling': lambda a: (lambda n, k: sum((-1)**(k-j) * math.comb(k, j) * j**n for j in range(k+1)) // math.factorial(k))(int(obj), int(a[0])),
            'centered': lambda a: int(a[0]) * int(obj) * (int(obj) - 1) // 2 + 1,
            'polygonal': lambda a: int(obj) * ((int(a[0]) - 2) * int(obj) - (int(a[0]) - 4)) // 2, 'nthDigit': lambda a: int(str(abs(int(obj)))[int(a[0])]), 'digitAt': lambda a: int(str(abs(int(obj)))[::-1][int(a[0])]), 'rotateDigits': lambda a: (lambda s, n: int(s[n:] + s[:n]))(str(int(obj)), int(a[0]) % len(str(int(obj)))), 'truncateDigits': lambda a: int(str(int(obj))[:int(a[0])]), 'padDigits': lambda a: str(int(obj)).zfill(int(a[0])),
            'isSmooth': lambda a: (lambda n, k: (lambda f: f(f, n, 2))((lambda f, n, d: n <= 1 if d > k else f(f, n // d, d) if n % d == 0 else f(f, n, d + 1))))(int(obj), int(a[0])),
            'isRough': lambda a: (lambda n, k: all(n % d != 0 for d in range(2, min(k, n))))(int(obj), int(a[0])),
            'isAlmostPrime': lambda a: (lambda n, k: (lambda f: f(f, n, 2, 0))((lambda f, n, d, c: c == k if n <= 1 else f(f, n//d, d, c+1) if n % d == 0 else f(f, n, d+1, c))))(int(obj), int(a[0])),
            'isHarshadInBase': lambda a: (lambda n, b: n > 0 and n % sum((lambda f: f(f, n, b))((lambda f, n, b: [n % b] + f(f, n // b, b) if n > 0 else []))) == 0)(int(obj), int(a[0])),
            'isPronicInRange': lambda a: (lambda n, mx: n <= mx and (lambda k: k * (k + 1) == n)(int(n ** 0.5)))(int(obj), int(a[0])),
            'isPalindromeInBase': lambda a: (lambda n, b: (lambda s: s == s[::-1])((lambda f: f(f, n, b, ''))((lambda f, n, b, r: r or '0' if n == 0 else f(f, n // b, b, chr(n % b + (48 if n % b < 10 else 87)) + r)))))(int(obj), int(a[0])),
            'primesBetween': lambda a: [p for p in range(int(obj), int(a[0])+1) if p >= 2 and all(p % i for i in range(2, int(p**0.5)+1))],
        }
        if member in _onearg:
            fn = _onearg[member]
            return ('builtin', lambda args, ctx: fn(args))
        if member == 'lerp': return ('builtin', lambda args, ctx: (lambda r: int(r) if r == int(r) else r)(obj + (args[0] - obj) * args[1]))
        if member == 'map':
            return ('builtin', lambda args, ctx: self._call_function(args[0], [obj]))
        if member in ('percent', 'percentOf'):
            return ('builtin', lambda args, ctx: (lambda r: int(r) if r == int(r) else r)((obj / 100) if member == 'percent' else (obj * args[0] / 100)))
        if member == 'toPercent':
            return ('builtin', lambda args, ctx: f"{int(v) if (v := round(obj * 100, 10)) == int(v) else v}%")
        if member == 'toOrdinal': return ('builtin', lambda args, ctx: (lambda n: f"{n}{'th' if 11 <= n % 100 <= 13 else ['th','st','nd','rd'][n % 10] if n % 10 < 4 else 'th'}")(int(obj)))
        if member == 'isPrime': return ('builtin', lambda args, ctx: int(obj) >= 2 and all(int(obj) % i for i in range(2, int(int(obj)**0.5) + 1)))
        if member == 'toRoman': return ('builtin', lambda args, ctx: __import__('functools').reduce(lambda nr, vs: (nr[0] % vs[0], nr[1] + vs[1] * (nr[0] // vs[0])), [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')], (int(obj), ''))[1])
        if member in ('fibonacci', 'lucasNumber', 'lucas', 'tribonacci', 'jacobsthal', 'pell'):
            def _fib(args, ctx):
                _m = 'lucasNumber' if member == 'lucas' else member
                if _m == 'tribonacci':
                    a, b, c = 0, 1, 1
                    for _ in range(int(obj)): a, b, c = b, c, a + b + c
                    return a
                a, b = {'fibonacci': (0, 1), 'lucasNumber': (2, 1), 'jacobsthal': (0, 1), 'pell': (0, 1)}[_m]
                for _ in range(int(obj)): a, b = b, ({'jacobsthal': b + 2*a, 'pell': 2*b + a}.get(_m, a + b))
                return a
            return ('builtin', _fib)
        if member == 'toWords':
            def _tw(args, ctx, _o=['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'], _t=['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']):
                n = int(obj)
                if n == 0: return 'zero'
                _ch = lambda num: '' if num == 0 else _o[num] if num < 20 else (_t[num // 10] + ('-' + _o[num % 10] if num % 10 else '')) if num < 100 else _o[num // 100] + ' hundred' + (' ' + _ch(num % 100) if num % 100 else '')
                p, s, rem = [], ['', ' thousand', ' million', ' billion'], abs(n)
                while rem > 0: (p.append(_ch(rem % 1000) + s[len(p)]) if rem % 1000 else None); rem //= 1000
                return ('negative ' if n < 0 else '') + ' '.join(reversed(p))
            return ('builtin', _tw)
        if member in ('collatz', 'collatzLength', 'collatzSequence'):
            def _cz(args, ctx):
                n, r = int(obj), [int(obj)]
                while n != 1: n = n // 2 if n % 2 == 0 else 3 * n + 1; r.append(n)
                return r if member == 'collatzSequence' else len(r) - 1
            return ('builtin', _cz)
        if member == 'nthPrime':
            def _np(args, ctx):
                c, p = 0, 1
                while c < int(obj): p += 1; c += all(p % i for i in range(2, int(p**0.5) + 1))
                return p
            return ('builtin', _np)
        if member == 'isHappy':
            return ('builtin', lambda args, ctx: (f := lambda n, s: True if n == 1 else False if n in s else f(sum(int(d)**2 for d in str(n)), s | {n}))(int(obj), set()))
        if member == 'toFraction':
            from fractions import Fraction as _F
            return ('builtin', lambda args, ctx: str(_F(obj).limit_denominator()))
        if member == 'toCurrency':
            return ('builtin', lambda args, ctx: f"${obj:,.2f}")
        if member == 'isAmicable':
            return ('builtin', lambda args, ctx: (lambda _ds, n: (lambda b: b != n and _ds(b) == n)(_ds(n)) if len(args) == 0 else (lambda a, b: a != b and _ds(a) == b and _ds(b) == a)(n, int(args[0])))(lambda n: sum(i for i in range(1, n) if n % i == 0), int(obj)))
        if member in ('primeFactors', 'primeFactorization'): return ('builtin', lambda args, ctx: (f := lambda n, d: [] if n <= 1 else [d] + f(n//d, d) if n % d == 0 else f(n, d+1))(int(obj), 2))
        if member in ('prevPrime', 'nextPrime'):
            def _pnp(args, ctx, d=(-1 if member == 'prevPrime' else 1)):
                n = int(obj) + d
                while n >= 2 and not all(n % i for i in range(2, int(n**0.5) + 1)): n += d
                return n if n >= 2 else None
            return ('builtin', _pnp)
        if member == 'asTime':
            return ('builtin', lambda args, ctx: (lambda n, h, m, s: f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}")(int(obj), int(obj) // 3600, (int(obj) % 3600) // 60, int(obj) % 60))
        if member in ('isStrongPrime', 'isWeakPrime', 'isBalancedPrime'):
            return ('builtin', lambda args, ctx: (lambda n, ip, np, pp, avg: ip(n) and (n > avg if member == 'isStrongPrime' else n < avg if member == 'isWeakPrime' else n * 2 == pp(n) + np(n)))(int(obj), lambda n: n >= 2 and all(n % i for i in range(2, int(n**0.5)+1)), lambda n: next(p for p in range(n+1, n*2) if all(p % i for i in range(2, int(p**0.5)+1))), lambda n: next(p for p in range(n-1, 1, -1) if all(p % i for i in range(2, int(p**0.5)+1))), (lambda pp, np: (pp(int(obj)) + np(int(obj))) / 2)(lambda n: next(p for p in range(n-1, 1, -1) if all(p % i for i in range(2, int(p**0.5)+1))), lambda n: next(p for p in range(n+1, n*2) if all(p % i for i in range(2, int(p**0.5)+1))))))
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
