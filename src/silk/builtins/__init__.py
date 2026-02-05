"""
Silk Built-in Functions

All built-in functions available in the Silk language.
"""

from .core import CORE_BUILTINS
from .math_funcs import MATH_BUILTINS
from .medical import MEDICAL_BUILTINS

# Combine all built-ins
ALL_BUILTINS = {
    **CORE_BUILTINS,
    **MATH_BUILTINS,
    **MEDICAL_BUILTINS,
}

__all__ = ["ALL_BUILTINS", "CORE_BUILTINS", "MATH_BUILTINS", "MEDICAL_BUILTINS"]
