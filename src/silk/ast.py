"""
Silk Abstract Syntax Tree (AST) Nodes

All AST node types for the Silk language.
"""

from dataclasses import dataclass
from typing import Any


# ═══════════════════════════════════════════════════════════
# LITERALS
# ═══════════════════════════════════════════════════════════

@dataclass
class NumberLiteral:
    """Numeric literal (int or float)."""
    value: float | int


@dataclass
class StringLiteral:
    """String literal."""
    value: str


@dataclass
class BoolLiteral:
    """Boolean literal (true/false)."""
    value: bool


@dataclass
class NullLiteral:
    """Null literal."""
    pass


@dataclass
class ArrayLiteral:
    """Array literal [1, 2, 3]."""
    elements: list


# ═══════════════════════════════════════════════════════════
# EXPRESSIONS
# ═══════════════════════════════════════════════════════════

@dataclass
class Identifier:
    """Variable or function name."""
    name: str


@dataclass
class BinaryOp:
    """Binary operation (a + b, a == b, etc.)."""
    left: Any
    op: str
    right: Any


@dataclass
class UnaryOp:
    """Unary operation (-x, not x)."""
    op: str
    operand: Any


@dataclass
class FunctionCall:
    """Function call: func(args)."""
    name: Any  # can be Identifier or MemberAccess
    args: list


@dataclass
class IndexAccess:
    """Index access: arr[i]."""
    obj: Any
    index: Any


@dataclass
class MemberAccess:
    """Member access: obj.member."""
    obj: Any
    member: str


# ═══════════════════════════════════════════════════════════
# STATEMENTS
# ═══════════════════════════════════════════════════════════

@dataclass
class Assignment:
    """Variable assignment: name = value."""
    name: str
    value: Any


@dataclass
class CompoundAssignment:
    """Compound assignment: name += value."""
    name: str
    op: str
    value: Any


@dataclass
class IndexAssign:
    """Index assignment: arr[i] = value."""
    obj: Any
    index: Any
    value: Any


@dataclass
class LetDeclaration:
    """Variable declaration: let name = value."""
    name: str
    mutable: bool
    type_hint: str | None
    value: Any


@dataclass
class IfStatement:
    """If/elif/else statement."""
    condition: Any
    body: list
    elif_branches: list  # list of (condition, body)
    else_body: list | None


@dataclass
class WhileLoop:
    """While loop."""
    condition: Any
    body: list


@dataclass
class ForLoop:
    """For-in loop."""
    var_name: str
    iterable: Any
    body: list


@dataclass
class FunctionDef:
    """Function definition."""
    name: str
    params: list  # list of (name, type_hint)
    return_type: str | None
    body: list


@dataclass
class ReturnStatement:
    """Return statement."""
    value: Any


@dataclass
class BreakStatement:
    """Break statement."""
    pass


@dataclass
class ContinueStatement:
    """Continue statement."""
    pass


# ═══════════════════════════════════════════════════════════
# PROGRAM
# ═══════════════════════════════════════════════════════════

@dataclass
class Program:
    """Root node containing all statements."""
    statements: list


# ═══════════════════════════════════════════════════════════
# STRUCTS
# ═══════════════════════════════════════════════════════════

@dataclass
class StructField:
    """A field in a struct definition."""
    name: str
    type_hint: str | None = None


@dataclass
class StructDef:
    """Struct definition: struct Name { field: type, ... }"""
    name: str
    fields: list  # list of StructField


@dataclass
class StructInstance:
    """Struct instantiation: Name { field: value, ... }"""
    struct_name: str
    field_values: dict  # field_name -> value expression
