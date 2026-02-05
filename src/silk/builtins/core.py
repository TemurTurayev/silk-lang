"""
Silk Core Built-in Functions

I/O, type conversion, and collection operations.
"""

from typing import Any, Callable
from ..errors import RuntimeError_


def silk_repr(value: Any) -> str:
    """Convert a Silk value to its string representation."""
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, float):
        if value == int(value):
            return str(int(value))
        return str(value)
    if isinstance(value, list):
        items = ', '.join(silk_repr(item) for item in value)
        return f"[{items}]"
    if isinstance(value, tuple) and len(value) >= 1:
        if value[0] == 'function':
            return "<function>"
        if value[0] == 'builtin':
            return "<builtin>"
    return str(value)


def builtin_print(args: list, context: dict) -> None:
    """Print values to stdout."""
    output = ' '.join(silk_repr(a) for a in args)
    print(output)
    if 'output_lines' in context:
        context['output_lines'].append(output)
    return None


def builtin_input(args: list, context: dict) -> str:
    """Read input from stdin."""
    prompt = args[0] if args else ""
    return input(silk_repr(prompt) if prompt else "")


def builtin_type(args: list, context: dict) -> str:
    """Get type name of a value."""
    v = args[0]
    if isinstance(v, bool):
        return "bool"
    elif isinstance(v, int):
        return "int"
    elif isinstance(v, float):
        return "float"
    elif isinstance(v, str):
        return "str"
    elif isinstance(v, list):
        return "array"
    elif v is None:
        return "null"
    elif isinstance(v, tuple) and v[0] in ('function', 'builtin'):
        return "function"
    return "unknown"


def builtin_str(args: list, context: dict) -> str:
    """Convert value to string."""
    return silk_repr(args[0])


def builtin_int(args: list, context: dict) -> int:
    """Convert value to integer."""
    return int(args[0])


def builtin_float(args: list, context: dict) -> float:
    """Convert value to float."""
    return float(args[0])


def builtin_bool(args: list, context: dict) -> bool:
    """Convert value to boolean."""
    return bool(args[0])


def builtin_len(args: list, context: dict) -> int:
    """Get length of array or string."""
    v = args[0]
    if isinstance(v, (str, list)):
        return len(v)
    raise RuntimeError_(f"len() expects string or array, got {type(v).__name__}")


def builtin_range(args: list, context: dict) -> list:
    """Generate a range of integers."""
    if len(args) == 1:
        return list(range(int(args[0])))
    elif len(args) == 2:
        return list(range(int(args[0]), int(args[1])))
    elif len(args) == 3:
        return list(range(int(args[0]), int(args[1]), int(args[2])))
    raise RuntimeError_("range() takes 1 to 3 arguments")


def builtin_push(args: list, context: dict) -> list:
    """Append item to array."""
    if not isinstance(args[0], list):
        raise RuntimeError_("push() expects an array as first argument")
    args[0].append(args[1])
    return args[0]


def builtin_pop(args: list, context: dict) -> Any:
    """Remove and return last item from array."""
    if not isinstance(args[0], list):
        raise RuntimeError_("pop() expects an array")
    return args[0].pop()


def builtin_slice(args: list, context: dict) -> Any:
    """Get slice of array or string."""
    arr = args[0]
    start = int(args[1]) if len(args) > 1 else 0
    end = int(args[2]) if len(args) > 2 else len(arr)
    return arr[start:end]


def builtin_reverse(args: list, context: dict) -> Any:
    """Reverse array or string."""
    if isinstance(args[0], list):
        return args[0][::-1]
    elif isinstance(args[0], str):
        return args[0][::-1]
    raise RuntimeError_("reverse() expects array or string")


def builtin_sort(args: list, context: dict) -> list:
    """Sort array and return new sorted array."""
    if not isinstance(args[0], list):
        raise RuntimeError_("sort() expects an array")
    return sorted(args[0])


def builtin_join(args: list, context: dict) -> str:
    """Join array elements into string."""
    arr = args[0]
    sep = args[1] if len(args) > 1 else ""
    if not isinstance(arr, list):
        raise RuntimeError_("join() expects an array as first argument")
    return sep.join(silk_repr(item) for item in arr)


def builtin_split(args: list, context: dict) -> list:
    """Split string into array."""
    s = args[0]
    sep = args[1] if len(args) > 1 else " "
    if not isinstance(s, str):
        raise RuntimeError_("split() expects a string")
    return s.split(sep)


def builtin_contains(args: list, context: dict) -> bool:
    """Check if collection contains item."""
    collection, item = args[0], args[1]
    return item in collection


# Export all core built-ins
CORE_BUILTINS: dict[str, Callable] = {
    'print': builtin_print,
    'input': builtin_input,
    'type': builtin_type,
    'str': builtin_str,
    'int': builtin_int,
    'float': builtin_float,
    'bool': builtin_bool,
    'len': builtin_len,
    'range': builtin_range,
    'push': builtin_push,
    'pop': builtin_pop,
    'slice': builtin_slice,
    'reverse': builtin_reverse,
    'sort': builtin_sort,
    'join': builtin_join,
    'split': builtin_split,
    'contains': builtin_contains,
}
