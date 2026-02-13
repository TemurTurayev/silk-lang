"""
Silk Runtime Types

Environment, struct instances, enum values, Option/Result types,
decimal type for precise medical calculations, and helpers.
"""

from typing import Any
from decimal import Decimal as PyDecimal, InvalidOperation, ROUND_HALF_UP
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
# DECIMAL TYPE (precise medical calculations)
# ═══════════════════════════════════════════════════════════

class SilkDecimal:
    """
    Exact decimal arithmetic for medical dosing.

    Unlike float (0.1 + 0.2 != 0.3), SilkDecimal guarantees
    exact decimal results — critical for drug dosing calculations.

    Usage in Silk:
        let dose = decimal("0.1")
        let total = dose + decimal("0.2")   // exactly 0.3
        let mg = decimal(15) * decimal("0.5")  // exactly 7.5
    """

    def __init__(self, value: 'str | int | float | PyDecimal | SilkDecimal'):
        if isinstance(value, SilkDecimal):
            self._value = value._value
        elif isinstance(value, PyDecimal):
            self._value = value
        elif isinstance(value, str):
            try:
                self._value = PyDecimal(value)
            except InvalidOperation:
                raise RuntimeError_(f"Invalid decimal value: '{value}'")
        elif isinstance(value, int):
            self._value = PyDecimal(value)
        elif isinstance(value, float):
            self._value = PyDecimal(str(value))
        else:
            raise RuntimeError_(
                f"Cannot create decimal from {type(value).__name__}"
            )

    @property
    def raw(self) -> PyDecimal:
        """Access underlying Python Decimal."""
        return self._value

    def __add__(self, other: object) -> 'SilkDecimal':
        if isinstance(other, SilkDecimal):
            return SilkDecimal(self._value + other._value)
        if isinstance(other, (int, float)):
            return SilkDecimal(self._value + PyDecimal(str(other)))
        return NotImplemented

    def __radd__(self, other: object) -> 'SilkDecimal':
        return self.__add__(other)

    def __sub__(self, other: object) -> 'SilkDecimal':
        if isinstance(other, SilkDecimal):
            return SilkDecimal(self._value - other._value)
        if isinstance(other, (int, float)):
            return SilkDecimal(self._value - PyDecimal(str(other)))
        return NotImplemented

    def __rsub__(self, other: object) -> 'SilkDecimal':
        if isinstance(other, (int, float)):
            return SilkDecimal(PyDecimal(str(other)) - self._value)
        return NotImplemented

    def __mul__(self, other: object) -> 'SilkDecimal':
        if isinstance(other, SilkDecimal):
            return SilkDecimal(self._value * other._value)
        if isinstance(other, (int, float)):
            return SilkDecimal(self._value * PyDecimal(str(other)))
        return NotImplemented

    def __rmul__(self, other: object) -> 'SilkDecimal':
        return self.__mul__(other)

    def __truediv__(self, other: object) -> 'SilkDecimal':
        other_val = None
        if isinstance(other, SilkDecimal):
            other_val = other._value
        elif isinstance(other, (int, float)):
            other_val = PyDecimal(str(other))
        else:
            return NotImplemented
        if other_val == 0:
            raise RuntimeError_("Division by zero")
        return SilkDecimal(self._value / other_val)

    def __rtruediv__(self, other: object) -> 'SilkDecimal':
        if isinstance(other, (int, float)):
            if self._value == 0:
                raise RuntimeError_("Division by zero")
            return SilkDecimal(PyDecimal(str(other)) / self._value)
        return NotImplemented

    def __mod__(self, other: object) -> 'SilkDecimal':
        if isinstance(other, SilkDecimal):
            return SilkDecimal(self._value % other._value)
        if isinstance(other, (int, float)):
            return SilkDecimal(self._value % PyDecimal(str(other)))
        return NotImplemented

    def __pow__(self, other: object) -> 'SilkDecimal':
        if isinstance(other, SilkDecimal):
            return SilkDecimal(self._value ** other._value)
        if isinstance(other, (int, float)):
            return SilkDecimal(self._value ** PyDecimal(str(other)))
        return NotImplemented

    def __neg__(self) -> 'SilkDecimal':
        return SilkDecimal(-self._value)

    def __abs__(self) -> 'SilkDecimal':
        return SilkDecimal(abs(self._value))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, SilkDecimal):
            return self._value == other._value
        if isinstance(other, (int, float)):
            return self._value == PyDecimal(str(other))
        return False

    def __lt__(self, other: object) -> bool:
        if isinstance(other, SilkDecimal):
            return self._value < other._value
        if isinstance(other, (int, float)):
            return self._value < PyDecimal(str(other))
        return NotImplemented

    def __le__(self, other: object) -> bool:
        if isinstance(other, SilkDecimal):
            return self._value <= other._value
        if isinstance(other, (int, float)):
            return self._value <= PyDecimal(str(other))
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, SilkDecimal):
            return self._value > other._value
        if isinstance(other, (int, float)):
            return self._value > PyDecimal(str(other))
        return NotImplemented

    def __ge__(self, other: object) -> bool:
        if isinstance(other, SilkDecimal):
            return self._value >= other._value
        if isinstance(other, (int, float)):
            return self._value >= PyDecimal(str(other))
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self._value)

    def __repr__(self) -> str:
        return f"decimal({self._value})"

    def __str__(self) -> str:
        return str(self._value)

    def to_int(self) -> int:
        """Convert to int, truncating toward zero."""
        return int(self._value)

    def to_float(self) -> float:
        """Convert to float (may lose precision)."""
        return float(self._value)

    def round(self, places: int = 0) -> 'SilkDecimal':
        """Round to given decimal places using ROUND_HALF_UP."""
        quantize_str = '0.' + '0' * places if places > 0 else '1'
        return SilkDecimal(
            self._value.quantize(PyDecimal(quantize_str), rounding=ROUND_HALF_UP)
        )


# ═══════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════
# UNIT TYPE (medical unit safety)
# ═══════════════════════════════════════════════════════════

# Units organized by dimension. Units in the same dimension can convert
# to each other; units in different dimensions cannot be mixed.
UNIT_DIMENSIONS: dict[str, str] = {
    # Mass
    'kg': 'mass', 'g': 'mass', 'mg': 'mass', 'mcg': 'mass', 'ug': 'mass',
    # Volume
    'L': 'volume', 'mL': 'volume', 'dL': 'volume',
    # Length
    'm': 'length', 'cm': 'length', 'mm': 'length',
    # Temperature
    'C': 'temperature', 'F': 'temperature',
    # Time
    'hr': 'time', 'min': 'time', 'sec': 'time',
    # Dosing (compound units)
    'mg/kg': 'dose_per_mass', 'mcg/kg': 'dose_per_mass',
    'mg/mL': 'concentration', 'mcg/mL': 'concentration', 'g/L': 'concentration',
    'mL/hr': 'flow_rate', 'L/hr': 'flow_rate',
    'bpm': 'heart_rate', 'mmHg': 'pressure',
    '%': 'percentage',
    'IU': 'international_unit', 'mIU': 'international_unit',
    'mEq': 'equivalent', 'mEq/L': 'eq_concentration',
    'mmol': 'molar_amount', 'mmol/L': 'molar_concentration',
}

# Conversion factors to base unit within each dimension
UNIT_TO_BASE: dict[str, tuple[str, float]] = {
    # Mass -> kg
    'kg': ('kg', 1.0), 'g': ('kg', 0.001), 'mg': ('kg', 1e-6),
    'mcg': ('kg', 1e-9), 'ug': ('kg', 1e-9),
    # Volume -> L
    'L': ('L', 1.0), 'mL': ('L', 0.001), 'dL': ('L', 0.1),
    # Length -> m
    'm': ('m', 1.0), 'cm': ('m', 0.01), 'mm': ('m', 0.001),
    # Time -> sec
    'hr': ('sec', 3600.0), 'min': ('sec', 60.0), 'sec': ('sec', 1.0),
}


class SilkUnit:
    """
    A numeric value with a physical unit attached.

    Prevents dangerous unit mismatches in medical calculations:
        10.mg + 5.mL  -> ERROR (mass + volume)
        10.mg + 5.g   -> 5010.mg (auto-converted)

    Usage in Silk:
        let dose = unit(500, "mg")
        let weight = unit(70, "kg")
        let per_kg = dose / weight   // -> unit(7.14, "mg/kg")
    """

    def __init__(
        self,
        value: 'int | float | SilkDecimal',
        unit_name: str,
    ):
        if unit_name not in UNIT_DIMENSIONS:
            raise RuntimeError_(
                f"Unknown unit: '{unit_name}'. "
                f"Supported: {', '.join(sorted(UNIT_DIMENSIONS.keys()))}"
            )
        if isinstance(value, SilkDecimal):
            self._value = float(value.raw)
        else:
            self._value = float(value)
        self._unit = unit_name

    @property
    def value(self) -> float:
        return self._value

    @property
    def unit(self) -> str:
        return self._unit

    @property
    def dimension(self) -> str:
        return UNIT_DIMENSIONS[self._unit]

    def _check_compatible(self, other: 'SilkUnit', op: str) -> None:
        """Raise error if units are incompatible for addition/subtraction."""
        if self.dimension != other.dimension:
            raise RuntimeError_(
                f"Unit mismatch: cannot {op} '{self._unit}' and '{other._unit}' "
                f"({self.dimension} vs {other.dimension})"
            )

    def _convert_to_same_unit(self, other: 'SilkUnit') -> tuple[float, float, str]:
        """Convert both values to the same unit (self's unit)."""
        if self._unit == other._unit:
            return self._value, other._value, self._unit

        if self._unit in UNIT_TO_BASE and other._unit in UNIT_TO_BASE:
            self_base, self_factor = UNIT_TO_BASE[self._unit]
            other_base, other_factor = UNIT_TO_BASE[other._unit]
            converted = round(other._value * (other_factor / self_factor), 10)
            return self._value, converted, self._unit

        raise RuntimeError_(
            f"Cannot auto-convert between '{other._unit}' and '{self._unit}'"
        )

    def __add__(self, other: object) -> 'SilkUnit':
        if isinstance(other, SilkUnit):
            self._check_compatible(other, 'add')
            a, b, u = self._convert_to_same_unit(other)
            return SilkUnit(a + b, u)
        if isinstance(other, (int, float)):
            return SilkUnit(self._value + other, self._unit)
        return NotImplemented

    def __radd__(self, other: object) -> 'SilkUnit':
        if isinstance(other, (int, float)):
            return SilkUnit(other + self._value, self._unit)
        return NotImplemented

    def __sub__(self, other: object) -> 'SilkUnit':
        if isinstance(other, SilkUnit):
            self._check_compatible(other, 'subtract')
            a, b, u = self._convert_to_same_unit(other)
            return SilkUnit(a - b, u)
        if isinstance(other, (int, float)):
            return SilkUnit(self._value - other, self._unit)
        return NotImplemented

    def __mul__(self, other: object) -> 'SilkUnit':
        if isinstance(other, (int, float)):
            return SilkUnit(self._value * other, self._unit)
        if isinstance(other, SilkUnit):
            raise RuntimeError_(
                f"Cannot multiply '{self._unit}' by '{other._unit}' directly. "
                "Use .value to extract the number first."
            )
        return NotImplemented

    def __rmul__(self, other: object) -> 'SilkUnit':
        if isinstance(other, (int, float)):
            return SilkUnit(other * self._value, self._unit)
        return NotImplemented

    def __truediv__(self, other: object) -> 'SilkUnit':
        if isinstance(other, (int, float)):
            if other == 0:
                raise RuntimeError_("Division by zero")
            return SilkUnit(self._value / other, self._unit)
        if isinstance(other, SilkUnit):
            if other._value == 0:
                raise RuntimeError_("Division by zero")
            if self.dimension == other.dimension:
                a, b, _ = self._convert_to_same_unit(other)
                return a / b
            compound = f"{self._unit}/{other._unit}"
            if compound in UNIT_DIMENSIONS:
                return SilkUnit(self._value / other._value, compound)
            return self._value / other._value
        return NotImplemented

    def __neg__(self) -> 'SilkUnit':
        return SilkUnit(-self._value, self._unit)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, SilkUnit):
            if self.dimension != other.dimension:
                return False
            a, b, _ = self._convert_to_same_unit(other)
            return abs(a - b) < 1e-10
        return False

    def __lt__(self, other: object) -> bool:
        if isinstance(other, SilkUnit):
            self._check_compatible(other, 'compare')
            a, b, _ = self._convert_to_same_unit(other)
            return a < b
        return NotImplemented

    def __le__(self, other: object) -> bool:
        if isinstance(other, SilkUnit):
            self._check_compatible(other, 'compare')
            a, b, _ = self._convert_to_same_unit(other)
            return a <= b
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, SilkUnit):
            self._check_compatible(other, 'compare')
            a, b, _ = self._convert_to_same_unit(other)
            return a > b
        return NotImplemented

    def __ge__(self, other: object) -> bool:
        if isinstance(other, SilkUnit):
            self._check_compatible(other, 'compare')
            a, b, _ = self._convert_to_same_unit(other)
            return a >= b
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self._value, self._unit))

    def __repr__(self) -> str:
        if self._value == int(self._value):
            return f"{int(self._value)} {self._unit}"
        return f"{self._value} {self._unit}"

    def __str__(self) -> str:
        return self.__repr__()

    def convert_to(self, target_unit: str) -> 'SilkUnit':
        """Convert to another unit in the same dimension."""
        if target_unit not in UNIT_DIMENSIONS:
            raise RuntimeError_(f"Unknown unit: '{target_unit}'")
        if UNIT_DIMENSIONS[target_unit] != self.dimension:
            raise RuntimeError_(
                f"Cannot convert '{self._unit}' to '{target_unit}': "
                f"different dimensions ({self.dimension} vs {UNIT_DIMENSIONS[target_unit]})"
            )
        if self._unit == target_unit:
            return SilkUnit(self._value, target_unit)

        if self._unit in UNIT_TO_BASE and target_unit in UNIT_TO_BASE:
            _, self_factor = UNIT_TO_BASE[self._unit]
            _, target_factor = UNIT_TO_BASE[target_unit]
            converted = self._value * (self_factor / target_factor)
            rounded = round(converted, 10)
            if rounded == int(rounded):
                rounded = int(rounded)
            return SilkUnit(rounded, target_unit)

        raise RuntimeError_(
            f"No conversion path from '{self._unit}' to '{target_unit}'"
        )


def truthy(value: Any) -> bool:
    """Check if value is truthy."""
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    if isinstance(value, SilkDecimal):
        return value.raw != 0
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
