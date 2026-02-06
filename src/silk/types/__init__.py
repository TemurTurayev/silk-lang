"""
Silk Runtime Types

Environment, struct instances, enum values, Option/Result types, and helpers.
"""

from typing import Any
from ..builtins.core import silk_repr
from ..errors import RuntimeError_


# ═══════════════════════════════════════════════════════════
# ENVIRONMENT
# ═══════════════════════════════════════════════════════════

class Environment:
    """Variable scope with parent chain for closures."""

    def __init__(self, parent: 'Environment | None' = None):
        self.variables: dict[str, Any] = {}
        self.mutability: dict[str, bool] = {}
        self.parent = parent

    def define(self, name: str, value: Any, mutable: bool = True) -> None:
        """Define a new variable in current scope."""
        self.variables[name] = value
        self.mutability[name] = mutable

    def get(self, name: str) -> Any:
        """Get variable value, searching up scope chain."""
        if name in self.variables:
            return self.variables[name]
        if self.parent:
            return self.parent.get(name)
        raise RuntimeError_(f"Undefined variable: '{name}'")

    def set(self, name: str, value: Any) -> None:
        """Set variable value, checking mutability."""
        if name in self.variables:
            if not self.mutability.get(name, True):
                raise RuntimeError_(
                    f"Cannot reassign immutable variable '{name}'. "
                    "Use 'let mut' for mutable variables."
                )
            self.variables[name] = value
            return
        if self.parent:
            self.parent.set(name, value)
            return
        raise RuntimeError_(f"Undefined variable: '{name}'")

    def exists(self, name: str) -> bool:
        """Check if variable exists in any scope."""
        if name in self.variables:
            return True
        if self.parent:
            return self.parent.exists(name)
        return False


# ═══════════════════════════════════════════════════════════
# STRUCT INSTANCES
# ═══════════════════════════════════════════════════════════

class SilkStruct:
    """Runtime representation of a struct instance."""

    def __init__(self, struct_name: str, fields: dict):
        self.struct_name = struct_name
        self.fields = fields

    def __repr__(self) -> str:
        field_str = ", ".join(
            f"{k}: {silk_repr(v)}" for k, v in self.fields.items()
        )
        return f"{self.struct_name} {{ {field_str} }}"


# ═══════════════════════════════════════════════════════════
# ENUM VALUES
# ═══════════════════════════════════════════════════════════

class SilkEnumValue:
    """Runtime representation of an enum variant."""

    def __init__(self, enum_name: str, variant: str):
        self.enum_name = enum_name
        self.variant = variant

    def __eq__(self, other: object) -> bool:
        if isinstance(other, SilkEnumValue):
            return self.enum_name == other.enum_name and self.variant == other.variant
        return False

    def __repr__(self) -> str:
        return f"{self.enum_name}.{self.variant}"


# ═══════════════════════════════════════════════════════════
# OPTION TYPE
# ═══════════════════════════════════════════════════════════

class SilkOption:
    """Option type: Some(value) or None."""

    def __init__(self, value: Any = None, is_some: bool = False):
        self.value = value
        self.is_some = is_some

    def __eq__(self, other: object) -> bool:
        if isinstance(other, SilkOption):
            if self.is_some != other.is_some:
                return False
            if self.is_some:
                return self.value == other.value
            return True
        return False

    def __repr__(self) -> str:
        if self.is_some:
            return f"Some({silk_repr(self.value)})"
        return "None"


# ═══════════════════════════════════════════════════════════
# RESULT TYPE
# ═══════════════════════════════════════════════════════════

class SilkResult:
    """Result type: Ok(value) or Err(error)."""

    def __init__(
        self,
        value: Any = None,
        error: Any = None,
        is_ok: bool = True
    ):
        self.value = value
        self.error = error
        self.is_ok = is_ok

    def __eq__(self, other: object) -> bool:
        if isinstance(other, SilkResult):
            if self.is_ok != other.is_ok:
                return False
            if self.is_ok:
                return self.value == other.value
            return self.error == other.error
        return False

    def __repr__(self) -> str:
        if self.is_ok:
            return f"Ok({silk_repr(self.value)})"
        return f"Err({silk_repr(self.error)})"


# ═══════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════

def truthy(value: Any) -> bool:
    """Check if value is truthy."""
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return len(value) > 0
    if isinstance(value, list):
        return len(value) > 0
    return True


def multiply(left: Any, right: Any) -> Any:
    """Multiply with string repetition support."""
    if isinstance(left, str) and isinstance(right, int):
        return left * right
    if isinstance(left, int) and isinstance(right, str):
        return right * left
    return left * right


def divide(left: Any, right: Any) -> Any:
    """Divide with zero check and int result preservation."""
    if right == 0:
        raise RuntimeError_("Division by zero")
    if isinstance(left, int) and isinstance(right, int):
        result = left / right
        return int(result) if result == int(result) else result
    return left / right
