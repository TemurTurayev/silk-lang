"""
Silk Math Built-in Functions

Mathematical operations and utilities.
"""

import math
from typing import Callable


def builtin_abs(args: list, context: dict) -> float | int:
    """Absolute value."""
    return abs(args[0])


def builtin_round(args: list, context: dict) -> float:
    """Round to n decimal places."""
    if len(args) > 1:
        return round(args[0], int(args[1]))
    return round(args[0])


def builtin_min(args: list, context: dict) -> float | int:
    """Minimum value."""
    if len(args) == 1 and isinstance(args[0], list):
        return min(args[0])
    return min(args)


def builtin_max(args: list, context: dict) -> float | int:
    """Maximum value."""
    if len(args) == 1 and isinstance(args[0], list):
        return max(args[0])
    return max(args)


def builtin_sum(args: list, context: dict) -> float | int:
    """Sum of values."""
    if isinstance(args[0], list):
        return sum(args[0])
    return sum(args)


def builtin_sqrt(args: list, context: dict) -> float:
    """Square root."""
    return math.sqrt(args[0])


def builtin_pow(args: list, context: dict) -> float:
    """Power function."""
    return math.pow(args[0], args[1])


def builtin_log(args: list, context: dict) -> float:
    """Natural logarithm (or with base)."""
    if len(args) > 1:
        return math.log(args[0], args[1])
    return math.log(args[0])


def builtin_log10(args: list, context: dict) -> float:
    """Base-10 logarithm."""
    return math.log10(args[0])


def builtin_sin(args: list, context: dict) -> float:
    """Sine function."""
    return math.sin(args[0])


def builtin_cos(args: list, context: dict) -> float:
    """Cosine function."""
    return math.cos(args[0])


def builtin_tan(args: list, context: dict) -> float:
    """Tangent function."""
    return math.tan(args[0])


def builtin_pi(args: list, context: dict) -> float:
    """Pi constant."""
    return math.pi


def builtin_ceil(args: list, context: dict) -> int:
    """Ceiling function."""
    return math.ceil(args[0])


def builtin_floor(args: list, context: dict) -> int:
    """Floor function."""
    return math.floor(args[0])


# Export all math built-ins
MATH_BUILTINS: dict[str, Callable] = {
    'abs': builtin_abs,
    'round': builtin_round,
    'min': builtin_min,
    'max': builtin_max,
    'sum': builtin_sum,
    'sqrt': builtin_sqrt,
    'pow': builtin_pow,
    'log': builtin_log,
    'log10': builtin_log10,
    'sin': builtin_sin,
    'cos': builtin_cos,
    'tan': builtin_tan,
    'pi': builtin_pi,
    'ceil': builtin_ceil,
    'floor': builtin_floor,
}
