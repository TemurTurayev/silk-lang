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
class MemberAssign:
    """Member assignment: obj.field = value."""
    obj: Any
    member: str
    value: Any


@dataclass
class MemberCompoundAssign:
    """Compound member assignment: obj.field += value."""
    obj: Any
    member: str
    op: str
    value: Any


@dataclass
class IndexCompoundAssign:
    """Compound index assignment: arr[i] += value."""
    obj: Any
    index: Any
    op: str
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
    """While loop. else_body runs if loop completes without break."""
    condition: Any
    body: list
    else_body: list | None = None


@dataclass
class ForLoop:
    """For-in loop. index_name is set for 'for i, val in ...' form."""
    var_name: str
    iterable: Any
    body: list
    index_name: str | None = None
    else_body: list | None = None


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
    struct_ref: Any = None  # Optional expression resolving to struct def (namespaced)


# ═══════════════════════════════════════════════════════════
# ENUMS
# ═══════════════════════════════════════════════════════════

@dataclass
class EnumVariant:
    """A variant in an enum definition."""
    name: str


@dataclass
class EnumDef:
    """Enum definition: enum Name { Variant1, Variant2, ... }"""
    name: str
    variants: list  # list of EnumVariant


# ═══════════════════════════════════════════════════════════
# INTERFACES
# ═══════════════════════════════════════════════════════════

@dataclass
class InterfaceMethodSig:
    """Method signature in an interface (no body)."""
    name: str
    params: list  # list of (name, type_hint)
    return_type: str | None


@dataclass
class InterfaceDef:
    """Interface definition: interface Name { fn method(self) -> type }"""
    name: str
    methods: list  # list of InterfaceMethodSig


# ═══════════════════════════════════════════════════════════
# IMPL BLOCKS
# ═══════════════════════════════════════════════════════════

@dataclass
class ImplBlock:
    """Impl block: impl Name { ... } or impl Name : Interface { ... }"""
    struct_name: str
    methods: list  # list of FunctionDef
    interface_name: str | None = None


# ═══════════════════════════════════════════════════════════
# MODULES
# ═══════════════════════════════════════════════════════════

@dataclass
class ImportStmt:
    """Import statement: import path or import path as alias."""
    path: str  # e.g. "silk/math", "./utils", "./lib/geometry"
    alias: str | None  # explicit alias, or None (default = last segment)


# ═══════════════════════════════════════════════════════════
# MATCH EXPRESSIONS
# ═══════════════════════════════════════════════════════════

@dataclass
class MatchArm:
    """A single arm in a match expression."""
    pattern: Any  # Identifier, MemberAccess, literal, or '_' wildcard
    guard: Any | None  # Optional 'if' guard expression
    body: Any  # Expression or list of statements (block)


@dataclass
class MatchExpr:
    """Match expression: match value { pattern => expr, ... }"""
    value: Any
    arms: list  # list of MatchArm


# ═══════════════════════════════════════════════════════════
# TESTING
# ═══════════════════════════════════════════════════════════

@dataclass
class AssertStatement:
    """Assert statement: assert expression."""
    expression: Any


@dataclass
class TestBlock:
    """Test block: test "name" { body }"""
    name: str
    body: list  # list of statements


# ═══════════════════════════════════════════════════════════
# STRING INTERPOLATION
# ═══════════════════════════════════════════════════════════

@dataclass
class StringInterp:
    """String interpolation: f"Hello {name}, age {age}"

    parts is a list of StringLiteral and expression AST nodes.
    """
    parts: list  # alternating StringLiteral and expression nodes


# ═══════════════════════════════════════════════════════════
# ERROR HANDLING
# ═══════════════════════════════════════════════════════════

@dataclass
class TryCatch:
    """Try/catch statement: try { body } catch name { handler }"""
    try_body: list
    error_name: str
    catch_body: list


@dataclass
class ThrowStatement:
    """Throw statement: throw expression."""
    expression: Any


# ═══════════════════════════════════════════════════════════
# HASHMAP
# ═══════════════════════════════════════════════════════════

@dataclass
class HashMapLiteral:
    """HashMap literal: {"key": value, ...} or {:} for empty."""
    pairs: list  # list of (key_expr, value_expr) tuples


# ═══════════════════════════════════════════════════════════
# TERNARY / CONDITIONAL EXPRESSION
# ═══════════════════════════════════════════════════════════

@dataclass
class TernaryExpr:
    """Ternary expression: if condition then expr else expr."""
    condition: Any
    then_expr: Any
    else_expr: Any


# ═══════════════════════════════════════════════════════════
# SPREAD
# ═══════════════════════════════════════════════════════════

@dataclass
class SpreadExpr:
    """Spread expression: ...expr (used inside array literals)."""
    expr: Any


# ═══════════════════════════════════════════════════════════
# RANGE
# ═══════════════════════════════════════════════════════════

@dataclass
class RangeExpr:
    """Range expression: start..end (exclusive end)."""
    start: Any
    end: Any


# ═══════════════════════════════════════════════════════════
# TYPEOF
# ═══════════════════════════════════════════════════════════

@dataclass
class TypeofExpr:
    """Typeof expression: typeof expr -> string."""
    expr: Any


# ═══════════════════════════════════════════════════════════
# DESTRUCTURING
# ═══════════════════════════════════════════════════════════

@dataclass
class DestructureLetArray:
    """Destructuring let: let [a, b, ...rest] = expr."""
    names: list  # list of str
    rest_name: str | None  # name for ...rest, or None
    value: Any


@dataclass
class DestructureLetDict:
    """Destructuring let: let {a, b} = expr."""
    names: list  # list of str (keys to extract)
    value: Any


# ═══════════════════════════════════════════════════════════
# LAMBDA
# ═══════════════════════════════════════════════════════════

@dataclass
class LambdaExpr:
    """Lambda shorthand: |params| expr."""
    params: list  # list of param names (strings)
    body_expr: Any  # single expression


# ═══════════════════════════════════════════════════════════
# OPTIONAL CHAINING
# ═══════════════════════════════════════════════════════════

@dataclass
class OptionalChain:
    """Optional chaining: obj?.member -> null if obj is null."""
    obj: Any
    member: str
