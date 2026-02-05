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
    MemberAccess, StructDef, StructInstance
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
            # Store struct definition for later instantiation
            struct_info = (
                'struct_def',
                node.name,
                [(f.name, f.type_hint) for f in node.fields]
            )
            env.define(node.name, struct_info, mutable=False)

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
            return self._eval_member(obj, node.member)
        elif isinstance(node, StructInstance):
            struct_def = env.get(node.struct_name)
            if not isinstance(struct_def, tuple) or struct_def[0] != 'struct_def':
                raise RuntimeError_(f"'{node.struct_name}' is not a struct")

            _, _, field_defs = struct_def
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
            return self._eval_method(obj, node.name.member, args)
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

    def _eval_member(self, obj: Any, member: str) -> Any:
        """Evaluate member access."""
        # Handle struct field access
        if isinstance(obj, SilkStruct):
            if member in obj.fields:
                return obj.fields[member]
            raise RuntimeError_(
                f"Struct '{obj.struct_name}' has no field '{member}'"
            )

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

    def _eval_method(self, obj: Any, method: str, args: list) -> Any:
        """Evaluate method call."""
        member = self._eval_member(obj, method)
        if isinstance(member, tuple) and member[0] == 'builtin':
            context = {'output_lines': self.output_lines}
            return member[1](args, context)
        return member


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
