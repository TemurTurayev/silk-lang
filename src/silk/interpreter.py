"""
Silk Interpreter

Tree-walking interpreter for the Silk language.
"""

from typing import Any

from .lexer import Lexer
from .parser import Parser
from .errors import (
    SilkError, LexerError, ParseError, RuntimeError_,
    ReturnSignal, BreakSignal, ContinueSignal
)
from .ast import (
    Program, NumberLiteral, StringLiteral, BoolLiteral, NullLiteral,
    ArrayLiteral, Identifier, BinaryOp, UnaryOp, Assignment,
    CompoundAssignment, LetDeclaration, IfStatement, WhileLoop,
    ForLoop, FunctionDef, FunctionCall, ReturnStatement,
    BreakStatement, ContinueStatement, IndexAccess, IndexAssign,
    MemberAccess, StructDef, StructInstance, EnumDef,
    MatchExpr, MatchArm, ImplBlock
)
from .builtins import ALL_BUILTINS
from .builtins.core import silk_repr


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


class Interpreter:
    """Tree-walking interpreter for Silk."""

    def __init__(self):
        self.global_env = Environment()
        self.output_lines: list[str] = []  # Capture output for testing
        self._setup_builtins()

    def _setup_builtins(self) -> None:
        """Register all built-in functions."""
        for name, func in ALL_BUILTINS.items():
            self.global_env.define(name, ('builtin', func), mutable=False)

        # Register None as a SilkOption
        self.global_env.define('None', SilkOption(is_some=False), mutable=False)

    def run(self, source: str) -> bool:
        """Run Silk source code."""
        try:
            lexer = Lexer(source)
            tokens = lexer.tokenize()
            parser = Parser(tokens)
            ast = parser.parse()
            self.execute(ast, self.global_env)
            return True
        except (LexerError, ParseError, RuntimeError_) as e:
            print(f"\n❌ Silk Error: {e}")
            return False

    def execute(self, node: Any, env: Environment) -> None:
        """Execute an AST node."""
        if isinstance(node, Program):
            for stmt in node.statements:
                self.execute(stmt, env)

        elif isinstance(node, LetDeclaration):
            value = self.evaluate(node.value, env)
            env.define(node.name, value, mutable=node.mutable)

        elif isinstance(node, Assignment):
            value = self.evaluate(node.value, env)
            env.set(node.name, value)

        elif isinstance(node, CompoundAssignment):
            current = env.get(node.name)
            right = self.evaluate(node.value, env)
            ops = {
                '+': lambda a, b: a + b,
                '-': lambda a, b: a - b,
                '*': lambda a, b: a * b,
                '/': lambda a, b: a / b,
            }
            env.set(node.name, ops[node.op](current, right))

        elif isinstance(node, IndexAssign):
            obj = self.evaluate(node.obj, env)
            idx = self.evaluate(node.index, env)
            val = self.evaluate(node.value, env)
            if isinstance(obj, list):
                obj[int(idx)] = val
            else:
                raise RuntimeError_("Index assignment only works on arrays")

        elif isinstance(node, IfStatement):
            cond = self.evaluate(node.condition, env)
            if _truthy(cond):
                self.execute_block(node.body, Environment(parent=env))
            else:
                matched = False
                for elif_cond, elif_body in node.elif_branches:
                    if _truthy(self.evaluate(elif_cond, env)):
                        self.execute_block(elif_body, Environment(parent=env))
                        matched = True
                        break
                if not matched and node.else_body:
                    self.execute_block(node.else_body, Environment(parent=env))

        elif isinstance(node, WhileLoop):
            while _truthy(self.evaluate(node.condition, env)):
                try:
                    self.execute_block(node.body, Environment(parent=env))
                except BreakSignal:
                    break
                except ContinueSignal:
                    continue

        elif isinstance(node, ForLoop):
            iterable = self.evaluate(node.iterable, env)
            if not isinstance(iterable, list):
                raise RuntimeError_("for..in requires an iterable (array or range)")
            for item in iterable:
                loop_env = Environment(parent=env)
                loop_env.define(node.var_name, item)
                try:
                    self.execute_block(node.body, loop_env)
                except BreakSignal:
                    break
                except ContinueSignal:
                    continue

        elif isinstance(node, FunctionDef):
            func = ('function', node.params, node.body, env)
            env.define(node.name, func, mutable=False)

        elif isinstance(node, ReturnStatement):
            value = self.evaluate(node.value, env) if node.value else None
            raise ReturnSignal(value)

        elif isinstance(node, BreakStatement):
            raise BreakSignal()

        elif isinstance(node, ContinueStatement):
            raise ContinueSignal()

        elif isinstance(node, StructDef):
            # Store struct definition with empty methods dict
            struct_info = (
                'struct_def',
                node.name,
                [(f.name, f.type_hint) for f in node.fields],
                {}  # methods dict, populated by impl blocks
            )
            env.define(node.name, struct_info, mutable=False)

        elif isinstance(node, EnumDef):
            variant_names = [v.name for v in node.variants]
            enum_info = ('enum_def', node.name, variant_names)
            env.define(node.name, enum_info, mutable=False)
            # Register each variant as an accessible value
            for variant in node.variants:
                variant_value = SilkEnumValue(node.name, variant.name)
                env.define(variant.name, variant_value, mutable=False)

        elif isinstance(node, ImplBlock):
            struct_info = env.get(node.struct_name)
            if not isinstance(struct_info, tuple) or struct_info[0] != 'struct_def':
                raise RuntimeError_(f"'{node.struct_name}' is not a struct")
            _, _, _, methods = struct_info
            for method in node.methods:
                methods[method.name] = (
                    'function', method.params, method.body, env
                )

        else:
            # Expression statement
            self.evaluate(node, env)

    def execute_block(self, statements: list, env: Environment) -> None:
        """Execute a block of statements."""
        for stmt in statements:
            self.execute(stmt, env)

    def evaluate(self, node: Any, env: Environment) -> Any:
        """Evaluate an AST node and return its value."""
        if isinstance(node, NumberLiteral):
            return node.value
        elif isinstance(node, StringLiteral):
            return node.value
        elif isinstance(node, BoolLiteral):
            return node.value
        elif isinstance(node, NullLiteral):
            return None
        elif isinstance(node, ArrayLiteral):
            return [self.evaluate(el, env) for el in node.elements]
        elif isinstance(node, Identifier):
            return env.get(node.name)
        elif isinstance(node, BinaryOp):
            return self._eval_binary(node, env)
        elif isinstance(node, UnaryOp):
            return self._eval_unary(node, env)
        elif isinstance(node, FunctionCall):
            return self._eval_call(node, env)
        elif isinstance(node, IndexAccess):
            obj = self.evaluate(node.obj, env)
            idx = self.evaluate(node.index, env)
            if isinstance(obj, list):
                idx_int = int(idx)
                if idx_int < 0 or idx_int >= len(obj):
                    raise RuntimeError_(f"Index {idx_int} out of bounds for array of length {len(obj)}")
                return obj[idx_int]
            elif isinstance(obj, str):
                idx_int = int(idx)
                if idx_int < 0 or idx_int >= len(obj):
                    raise RuntimeError_(f"Index {idx_int} out of bounds for string of length {len(obj)}")
                return obj[idx_int]
            raise RuntimeError_(f"Cannot index into {type(obj).__name__}")
        elif isinstance(node, MemberAccess):
            obj = self.evaluate(node.obj, env)
            return self._eval_member(obj, node.member, env)
        elif isinstance(node, StructInstance):
            struct_def = env.get(node.struct_name)
            if not isinstance(struct_def, tuple) or struct_def[0] != 'struct_def':
                raise RuntimeError_(f"'{node.struct_name}' is not a struct")

            _, _, field_defs, _ = struct_def
            field_names = {f[0] for f in field_defs}

            # Validate all required fields are provided
            for provided in node.field_values.keys():
                if provided not in field_names:
                    raise RuntimeError_(
                        f"Unknown field '{provided}' in struct '{node.struct_name}'"
                    )

            # Evaluate field values
            fields = {
                name: self.evaluate(expr, env)
                for name, expr in node.field_values.items()
            }

            return SilkStruct(node.struct_name, fields)
        elif isinstance(node, MatchExpr):
            return self._eval_match(node, env)
        else:
            raise RuntimeError_(f"Unknown AST node: {type(node).__name__}")

    def _eval_binary(self, node: BinaryOp, env: Environment) -> Any:
        """Evaluate binary operation."""
        left = self.evaluate(node.left, env)

        # Short-circuit for logical operators
        if node.op == 'and':
            return left if not _truthy(left) else self.evaluate(node.right, env)
        if node.op == 'or':
            return left if _truthy(left) else self.evaluate(node.right, env)

        right = self.evaluate(node.right, env)

        ops = {
            '+': lambda: left + right,
            '-': lambda: left - right,
            '*': lambda: _multiply(left, right),
            '/': lambda: _divide(left, right),
            '%': lambda: left % right,
            '**': lambda: left ** right,
            '==': lambda: left == right,
            '!=': lambda: left != right,
            '<': lambda: left < right,
            '>': lambda: left > right,
            '<=': lambda: left <= right,
            '>=': lambda: left >= right,
        }

        if node.op in ops:
            try:
                return ops[node.op]()
            except TypeError:
                raise RuntimeError_(
                    f"Cannot apply '{node.op}' to {type(left).__name__} "
                    f"and {type(right).__name__}"
                )
        raise RuntimeError_(f"Unknown operator: {node.op}")

    def _eval_unary(self, node: UnaryOp, env: Environment) -> Any:
        """Evaluate unary operation."""
        val = self.evaluate(node.operand, env)
        if node.op == '-':
            return -val
        if node.op == 'not':
            return not _truthy(val)
        raise RuntimeError_(f"Unknown unary operator: {node.op}")

    def _eval_call(self, node: FunctionCall, env: Environment) -> Any:
        """Evaluate function call."""
        args = [self.evaluate(a, env) for a in node.args]

        if isinstance(node.name, Identifier):
            func = env.get(node.name.name)
        elif isinstance(node.name, MemberAccess):
            # Method-style call: obj.method(args)
            obj = self.evaluate(node.name.obj, env)
            return self._eval_method(obj, node.name.member, args, env)
        else:
            func = self.evaluate(node.name, env)

        return self._call_function(func, args)

    def _call_function(self, func: Any, args: list) -> Any:
        """Call a function with arguments."""
        if isinstance(func, tuple):
            if func[0] == 'builtin':
                # Built-in function: pass context for print output capture
                context = {'output_lines': self.output_lines}
                return func[1](args, context)

            elif func[0] == 'function':
                _, params, body, closure_env = func
                fn_env = Environment(parent=closure_env)
                for (pname, _), arg in zip(params, args):
                    fn_env.define(pname, arg)
                try:
                    self.execute_block(body, fn_env)
                except ReturnSignal as r:
                    return r.value
                return None

        raise RuntimeError_("Not a callable function")

    def _eval_member(self, obj: Any, member: str, env: Environment | None = None) -> Any:
        """Evaluate member access."""
        # Handle struct field access and methods
        if isinstance(obj, SilkStruct):
            if member in obj.fields:
                return obj.fields[member]
            # Check for impl methods
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

        # Handle enum variant access
        if isinstance(obj, tuple) and len(obj) >= 3 and obj[0] == 'enum_def':
            _, enum_name, variants = obj
            if member in variants:
                return SilkEnumValue(enum_name, member)
            raise RuntimeError_(f"Enum '{enum_name}' has no variant '{member}'")

        if isinstance(obj, list):
            if member == 'length':
                return len(obj)

        elif isinstance(obj, str):
            if member == 'length':
                return len(obj)
            if member == 'upper':
                return ('builtin', lambda args, ctx: obj.upper())
            if member == 'lower':
                return ('builtin', lambda args, ctx: obj.lower())
            if member == 'strip':
                return ('builtin', lambda args, ctx: obj.strip())
            if member == 'replace':
                return ('builtin', lambda args, ctx: obj.replace(args[0], args[1]))
            if member == 'starts_with':
                return ('builtin', lambda args, ctx: obj.startswith(args[0]))
            if member == 'ends_with':
                return ('builtin', lambda args, ctx: obj.endswith(args[0]))

        raise RuntimeError_(f"'{type(obj).__name__}' has no member '{member}'")

    def _eval_method(self, obj: Any, method: str, args: list, env: Environment | None = None) -> Any:
        """Evaluate method call."""
        member = self._eval_member(obj, method, env)
        if isinstance(member, tuple) and member[0] == 'builtin':
            context = {'output_lines': self.output_lines}
            return member[1](args, context)
        if isinstance(member, tuple) and member[0] == 'bound_method':
            _, func, self_obj = member
            return self._call_function(func, [self_obj] + args)
        return member

    def _eval_match(self, node: MatchExpr, env: Environment) -> Any:
        """Evaluate match expression with exhaustiveness check."""
        value = self.evaluate(node.value, env)

        # Check exhaustiveness for enum types
        if isinstance(value, SilkEnumValue):
            self._check_enum_exhaustiveness(value.enum_name, node.arms, env)

        # Find matching arm
        for arm in node.arms:
            bindings = {}
            if self._pattern_matches(value, arm.pattern, env, bindings):
                # Check guard if present
                if arm.guard is not None:
                    guard_result = self.evaluate(arm.guard, env)
                    if not _truthy(guard_result):
                        continue

                # Create environment with pattern bindings
                match_env = Environment(parent=env)
                for name, val in bindings.items():
                    match_env.define(name, val, mutable=False)

                # Execute body
                if isinstance(arm.body, list):
                    # Block body
                    for stmt in arm.body:
                        self.execute(stmt, match_env)
                    return None
                else:
                    # Expression body
                    return self.evaluate(arm.body, match_env)

        raise RuntimeError_(f"No matching pattern for value: {value}")

    def _check_enum_exhaustiveness(
        self, enum_name: str, arms: list[MatchArm], env: Environment
    ) -> None:
        """Verify all enum variants are covered.

        CRITICAL for medical safety: Non-exhaustive matches MUST fail.
        """
        enum_def = env.get(enum_name)
        if not isinstance(enum_def, tuple) or enum_def[0] != 'enum_def':
            return  # Not an enum, skip check

        _, _, all_variants = enum_def
        covered_variants = set()
        has_wildcard = False

        for arm in arms:
            if isinstance(arm.pattern, Identifier) and arm.pattern.name == '_':
                has_wildcard = True
            elif isinstance(arm.pattern, MemberAccess):
                covered_variants.add(arm.pattern.member)
            elif isinstance(arm.pattern, Identifier):
                # Could be a variant name directly
                covered_variants.add(arm.pattern.name)

        if has_wildcard:
            return  # Wildcard covers everything

        missing = set(all_variants) - covered_variants
        if missing:
            raise RuntimeError_(
                f"Non-exhaustive match on enum '{enum_name}'. "
                f"Missing variants: {', '.join(sorted(missing))}. "
                f"Add missing cases or use '_' wildcard."
            )

    def _pattern_matches(
        self, value: Any, pattern: Any, env: Environment, bindings: dict | None = None
    ) -> bool:
        """Check if value matches pattern, optionally extracting bindings."""
        if bindings is None:
            bindings = {}

        if isinstance(pattern, Identifier):
            if pattern.name == '_':
                return True  # Wildcard matches everything
            # Check if it's an enum variant name
            if isinstance(value, SilkEnumValue):
                return value.variant == pattern.name
            return False

        if isinstance(pattern, MemberAccess):
            # EnumName.Variant pattern
            if isinstance(value, SilkEnumValue):
                return value.variant == pattern.member
            return False

        if isinstance(pattern, NumberLiteral):
            return value == pattern.value

        if isinstance(pattern, StringLiteral):
            return value == pattern.value

        if isinstance(pattern, BoolLiteral):
            return value == pattern.value

        if isinstance(pattern, FunctionCall):
            # Pattern like Ok(var) or Err(var) or Some(var)
            # pattern.name can be Identifier or a string depending on parsing
            pattern_name = pattern.name.name if isinstance(pattern.name, Identifier) else pattern.name
            if isinstance(value, SilkResult):
                if pattern_name == 'Ok' and value.is_ok:
                    if pattern.args and len(pattern.args) == 1:
                        arg = pattern.args[0]
                        if isinstance(arg, Identifier):
                            bindings[arg.name] = value.value
                    return True
                if pattern_name == 'Err' and not value.is_ok:
                    if pattern.args and len(pattern.args) == 1:
                        arg = pattern.args[0]
                        if isinstance(arg, Identifier):
                            bindings[arg.name] = value.error
                    return True
                return False
            if isinstance(value, SilkOption):
                if pattern_name == 'Some' and value.is_some:
                    if pattern.args and len(pattern.args) == 1:
                        arg = pattern.args[0]
                        if isinstance(arg, Identifier):
                            bindings[arg.name] = value.value
                    return True
                if pattern_name == 'None' and not value.is_some:
                    return True
                return False
            return False

        return False


# ═══════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════

def _truthy(value: Any) -> bool:
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


def _multiply(left: Any, right: Any) -> Any:
    """Multiply with string repetition support."""
    if isinstance(left, str) and isinstance(right, int):
        return left * right
    if isinstance(left, int) and isinstance(right, str):
        return right * left
    return left * right


def _divide(left: Any, right: Any) -> Any:
    """Divide with zero check and int result preservation."""
    if right == 0:
        raise RuntimeError_("Division by zero")
    if isinstance(left, int) and isinstance(right, int):
        result = left / right
        return int(result) if result == int(result) else result
    return left / right
