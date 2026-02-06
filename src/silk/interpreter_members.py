"""
Silk Interpreter - Member Dispatch Mixin

Handles member access and method calls on built-in types
(dict, list, string) and user-defined types (struct, enum).
"""

from typing import Any

from .errors import RuntimeError_
from .builtins.core import silk_repr
from .types import (
    Environment, SilkStruct, SilkEnumValue,
)


class MemberMixin:
    """Mixin providing _eval_member and _eval_method for Interpreter."""

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
        if member == 'entries':
            return ('builtin', lambda args, ctx: [[k, v] for k, v in obj.items()])
        if member == 'merge':
            return ('builtin', lambda args, ctx: {**obj, **args[0]})
        if member == 'forEach':
            def _map_foreach(args, ctx):
                for k, v in obj.items():
                    self._call_function(args[0], [k, v])
                return None
            return ('builtin', _map_foreach)
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
        if member == 'every':
            def _arr_every(args, ctx):
                return all(self._call_function(args[0], [item]) for item in obj)
            return ('builtin', _arr_every)
        if member == 'some':
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
        raise RuntimeError_(f"'list' has no member '{member}'")

    def _eval_string_member(self, obj: str, member: str) -> Any:
        """Evaluate member access on a string."""
        if member == 'length':
            return len(obj)
        if member == 'upper':
            return ('builtin', lambda args, ctx: obj.upper())
        if member == 'lower':
            return ('builtin', lambda args, ctx: obj.lower())
        if member in ('strip', 'trim'):
            return ('builtin', lambda args, ctx: obj.strip())
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
        if member == 'substring':
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
        raise RuntimeError_(f"'str' has no member '{member}'")

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
