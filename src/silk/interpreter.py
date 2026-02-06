"""
Silk Interpreter

Tree-walking interpreter for the Silk language.
"""

from typing import Any
from pathlib import Path

from .lexer import Lexer
from .parser import Parser
from .errors import (
    SilkError, LexerError, ParseError, RuntimeError_,
    ReturnSignal, BreakSignal, ContinueSignal
)
from .ast import (
    Program, NumberLiteral, StringLiteral, BoolLiteral, NullLiteral,
    ArrayLiteral, Identifier, BinaryOp, UnaryOp, Assignment,
    CompoundAssignment, LetDeclaration, IfStatement, WhileLoop, DoWhileLoop,
    ForLoop, FunctionDef, FunctionCall, ReturnStatement,
    BreakStatement, ContinueStatement, IndexAccess, IndexAssign,
    MemberAccess, StructDef, StructInstance, EnumDef,
    MatchExpr, MatchArm, ImplBlock, InterfaceDef, ImportStmt,
    TestBlock, AssertStatement, StringInterp, TryCatch,
    HashMapLiteral, ThrowStatement, TernaryExpr, MemberAssign,
    MemberCompoundAssign, IndexCompoundAssign, SpreadExpr,
    RangeExpr, TypeofExpr, DestructureLetArray, DestructureLetDict,
    LambdaExpr, OptionalChain, RepeatLoop
)
from .builtins import ALL_BUILTINS
from .builtins.core import silk_repr
from .resolver import ModuleResolver, ModuleNotFoundError as ResolverNotFound
from .types import (
    Environment, SilkStruct, SilkEnumValue, SilkOption, SilkResult,
    truthy, multiply, divide
)
from .interpreter_members import MemberMixin

_COMPOUND_OPS = {
    '+': lambda a, b: a + b, '-': lambda a, b: a - b,
    '*': lambda a, b: a * b, '/': lambda a, b: a / b,
}


class Interpreter(MemberMixin):
    """Tree-walking interpreter for Silk."""

    def __init__(self):
        self.global_env = Environment()
        self.output_lines: list[str] = []  # Capture output for testing
        self._module_cache: dict[str, Environment] = {}  # path -> module env
        self._loading_set: set[str] = set()  # circular import detection
        self._resolver = ModuleResolver()
        self._current_file: Path | None = None  # track importing file
        self._setup_builtins()

    def _setup_builtins(self) -> None:
        """Register all built-in functions."""
        for name, func in ALL_BUILTINS.items():
            self.global_env.define(name, ('builtin', func), mutable=False)

        # Register None as a SilkOption
        self.global_env.define('None', SilkOption(is_some=False), mutable=False)

        # Array namespace with static methods
        array_ns = Environment()
        array_ns.define('filled', ('builtin', lambda args, ctx: [args[1]] * int(args[0])), mutable=False)
        self.global_env.define('Array', array_ns, mutable=False)

    def run(self, source: str, file_path: Path | None = None) -> bool:
        """Run Silk source code."""
        self._current_file = file_path
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

        elif isinstance(node, DestructureLetArray):
            value = self.evaluate(node.value, env)
            if not isinstance(value, list):
                raise RuntimeError_("Destructuring requires an array")
            for i, name in enumerate(node.names):
                env.define(name, value[i] if i < len(value) else None)
            if node.rest_name is not None:
                rest = value[len(node.names):]
                env.define(node.rest_name, rest)

        elif isinstance(node, DestructureLetDict):
            value = self.evaluate(node.value, env)
            if isinstance(value, SilkStruct):
                for name in node.names:
                    env.define(name, value.fields.get(name))
            elif isinstance(value, dict):
                for name in node.names:
                    env.define(name, value.get(name))
            else:
                raise RuntimeError_("Dict destructuring requires a map or struct")

        elif isinstance(node, Assignment):
            value = self.evaluate(node.value, env)
            env.set(node.name, value)

        elif isinstance(node, CompoundAssignment):
            current = env.get(node.name)
            right = self.evaluate(node.value, env)
            env.set(node.name, _COMPOUND_OPS[node.op](current, right))

        elif isinstance(node, IndexAssign):
            obj = self.evaluate(node.obj, env)
            idx = self.evaluate(node.index, env)
            val = self.evaluate(node.value, env)
            if isinstance(obj, list):
                obj[int(idx)] = val
            elif isinstance(obj, dict):
                obj[idx] = val
            else:
                raise RuntimeError_("Index assignment only works on arrays and maps")

        elif isinstance(node, MemberAssign):
            obj = self.evaluate(node.obj, env)
            val = self.evaluate(node.value, env)
            if isinstance(obj, SilkStruct):
                if node.member not in obj.fields:
                    raise RuntimeError_(
                        f"Struct '{obj.struct_name}' has no field '{node.member}'"
                    )
                obj.fields[node.member] = val
            elif isinstance(obj, dict):
                obj[node.member] = val
            else:
                raise RuntimeError_(
                    f"Cannot assign to member '{node.member}' on {type(obj).__name__}"
                )

        elif isinstance(node, MemberCompoundAssign):
            obj = self.evaluate(node.obj, env)
            right = self.evaluate(node.value, env)
            if isinstance(obj, SilkStruct):
                current = obj.fields[node.member]
                obj.fields[node.member] = _COMPOUND_OPS[node.op](current, right)
            elif isinstance(obj, dict):
                current = obj[node.member]
                obj[node.member] = _COMPOUND_OPS[node.op](current, right)
            else:
                raise RuntimeError_(
                    f"Cannot compound-assign member '{node.member}' on {type(obj).__name__}"
                )

        elif isinstance(node, IndexCompoundAssign):
            obj = self.evaluate(node.obj, env)
            idx = self.evaluate(node.index, env)
            right = self.evaluate(node.value, env)
            if isinstance(obj, list):
                i = int(idx)
                obj[i] = _COMPOUND_OPS[node.op](obj[i], right)
            elif isinstance(obj, dict):
                obj[idx] = _COMPOUND_OPS[node.op](obj[idx], right)
            else:
                raise RuntimeError_("Compound index assignment only works on arrays and maps")

        elif isinstance(node, IfStatement):
            cond = self.evaluate(node.condition, env)
            if truthy(cond):
                self.execute_block(node.body, Environment(parent=env))
            else:
                matched = False
                for elif_cond, elif_body in node.elif_branches:
                    if truthy(self.evaluate(elif_cond, env)):
                        self.execute_block(elif_body, Environment(parent=env))
                        matched = True
                        break
                if not matched and node.else_body:
                    self.execute_block(node.else_body, Environment(parent=env))

        elif isinstance(node, WhileLoop):
            broke = False
            while truthy(self.evaluate(node.condition, env)):
                try:
                    self.execute_block(node.body, Environment(parent=env))
                except BreakSignal:
                    broke = True
                    break
                except ContinueSignal:
                    continue
            if not broke and node.else_body:
                self.execute_block(node.else_body, Environment(parent=env))

        elif isinstance(node, DoWhileLoop):
            while True:
                try:
                    self.execute_block(node.body, Environment(parent=env))
                except BreakSignal:
                    break
                except ContinueSignal:
                    pass
                if not truthy(self.evaluate(node.condition, env)):
                    break

        elif isinstance(node, RepeatLoop):
            count = int(self.evaluate(node.count, env))
            for _ in range(count):
                try:
                    self.execute_block(node.body, Environment(parent=env))
                except BreakSignal:
                    break
                except ContinueSignal:
                    continue

        elif isinstance(node, ForLoop):
            iterable = self.evaluate(node.iterable, env)
            is_dict = isinstance(iterable, dict)
            if is_dict:
                entries = list(iterable.items())
            elif isinstance(iterable, list):
                entries = None
            else:
                raise RuntimeError_("for..in requires an iterable (array, range, or map)")
            broke = False
            for i, item in enumerate(entries if is_dict else iterable):
                loop_env = Environment(parent=env)
                if is_dict:
                    key, val = item
                    loop_env.define(node.var_name, val if node.index_name else key)
                    if node.index_name:
                        loop_env.define(node.index_name, key)
                else:
                    loop_env.define(node.var_name, item)
                    if node.index_name:
                        loop_env.define(node.index_name, i)
                try:
                    self.execute_block(node.body, loop_env)
                except BreakSignal:
                    broke = True
                    break
                except ContinueSignal:
                    continue
            if not broke and node.else_body:
                self.execute_block(node.else_body, Environment(parent=env))

        elif isinstance(node, FunctionDef):
            func = ('function', node.params, node.body, env)
            if node.name:
                env.define(node.name, func, mutable=False)

        elif isinstance(node, ReturnStatement):
            value = self.evaluate(node.value, env) if node.value else None
            raise ReturnSignal(value)

        elif isinstance(node, BreakStatement):
            raise BreakSignal()

        elif isinstance(node, ContinueStatement):
            raise ContinueSignal()

        elif isinstance(node, StructDef):
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
            for variant in node.variants:
                variant_value = SilkEnumValue(node.name, variant.name)
                env.define(variant.name, variant_value, mutable=False)

        elif isinstance(node, InterfaceDef):
            iface_info = (
                'interface_def',
                node.name,
                [(m.name, m.params, m.return_type) for m in node.methods]
            )
            env.define(node.name, iface_info, mutable=False)

        elif isinstance(node, ImplBlock):
            struct_info = env.get(node.struct_name)
            if not isinstance(struct_info, tuple) or struct_info[0] != 'struct_def':
                raise RuntimeError_(f"'{node.struct_name}' is not a struct")
            _, _, _, methods = struct_info
            for method in node.methods:
                methods[method.name] = (
                    'function', method.params, method.body, env
                )
            if node.interface_name:
                self._check_interface_conformance(
                    node.struct_name, node.interface_name, methods, env
                )

        elif isinstance(node, ImportStmt):
            self._execute_import(node, env)

        elif isinstance(node, TestBlock):
            pass  # Skipped in normal mode

        elif isinstance(node, AssertStatement):
            self._execute_assert(node, env)

        elif isinstance(node, TryCatch):
            try:
                self.execute_block(node.try_body, Environment(parent=env))
            except RuntimeError_ as e:
                catch_env = Environment(parent=env)
                catch_env.define(node.error_name, str(e), mutable=False)
                self.execute_block(node.catch_body, catch_env)

        elif isinstance(node, ThrowStatement):
            value = self.evaluate(node.expression, env)
            raise RuntimeError_(silk_repr(value))

        else:
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
            result = []
            for el in node.elements:
                if isinstance(el, SpreadExpr):
                    result.extend(self.evaluate(el.expr, env))
                else:
                    result.append(self.evaluate(el, env))
            return result
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
                if idx_int < -len(obj) or idx_int >= len(obj):
                    raise RuntimeError_(f"Index {idx_int} out of bounds for array of length {len(obj)}")
                return obj[idx_int]
            elif isinstance(obj, str):
                idx_int = int(idx)
                if idx_int < -len(obj) or idx_int >= len(obj):
                    raise RuntimeError_(f"Index {idx_int} out of bounds for string of length {len(obj)}")
                return obj[idx_int]
            elif isinstance(obj, dict):
                if idx not in obj:
                    raise RuntimeError_(f"Key {silk_repr(idx)} not found in map")
                return obj[idx]
            raise RuntimeError_(f"Cannot index into {type(obj).__name__}")
        elif isinstance(node, MemberAccess):
            obj = self.evaluate(node.obj, env)
            return self._eval_member(obj, node.member, env)
        elif isinstance(node, OptionalChain):
            obj = self.evaluate(node.obj, env)
            if obj is None:
                return None
            return self._eval_member(obj, node.member, env)
        elif isinstance(node, StructInstance):
            if node.struct_ref is not None:
                struct_def = self.evaluate(node.struct_ref, env)
            else:
                struct_def = env.get(node.struct_name)
            if not isinstance(struct_def, tuple) or struct_def[0] != 'struct_def':
                raise RuntimeError_(f"'{node.struct_name}' is not a struct")

            _, _, field_defs, _ = struct_def
            field_names = {f[0] for f in field_defs}

            for provided in node.field_values.keys():
                if provided not in field_names:
                    raise RuntimeError_(
                        f"Unknown field '{provided}' in struct '{node.struct_name}'"
                    )

            fields = {
                name: self.evaluate(expr, env)
                for name, expr in node.field_values.items()
            }

            return SilkStruct(node.struct_name, fields)
        elif isinstance(node, MatchExpr):
            return self._eval_match(node, env)
        elif isinstance(node, StringInterp):
            result_parts = []
            for part in node.parts:
                if isinstance(part, StringLiteral):
                    result_parts.append(part.value)
                else:
                    val = self.evaluate(part, env)
                    result_parts.append(silk_repr(val))
            return ''.join(result_parts)
        elif isinstance(node, HashMapLiteral):
            result = {}
            for key_expr, val_expr in node.pairs:
                key = self.evaluate(key_expr, env)
                val = self.evaluate(val_expr, env)
                result[key] = val
            return result
        elif isinstance(node, TernaryExpr):
            cond = self.evaluate(node.condition, env)
            if truthy(cond):
                return self.evaluate(node.then_expr, env)
            else:
                return self.evaluate(node.else_expr, env)
        elif isinstance(node, RangeExpr):
            start = int(self.evaluate(node.start, env))
            end = int(self.evaluate(node.end, env))
            return list(range(start, end))
        elif isinstance(node, TypeofExpr):
            val = self.evaluate(node.expr, env)
            return self._typeof(val)
        elif isinstance(node, LambdaExpr):
            params = [(p, None, None) for p in node.params]
            body = [ReturnStatement(node.body_expr)]
            return ('function', params, body, env)
        elif isinstance(node, FunctionDef):
            return ('function', node.params, node.body, env)
        else:
            raise RuntimeError_(f"Unknown AST node: {type(node).__name__}")

    def _eval_binary(self, node: BinaryOp, env: Environment) -> Any:
        """Evaluate binary operation."""
        left = self.evaluate(node.left, env)

        if node.op == '|>':
            func = self.evaluate(node.right, env)
            return self._call_function(func, [left])

        if node.op == '??':
            return left if left is not None else self.evaluate(node.right, env)
        if node.op == 'and':
            return left if not truthy(left) else self.evaluate(node.right, env)
        if node.op == 'or':
            return left if truthy(left) else self.evaluate(node.right, env)

        right = self.evaluate(node.right, env)

        ops = {
            '+': lambda: left + right,
            '-': lambda: left - right,
            '*': lambda: multiply(left, right),
            '/': lambda: divide(left, right),
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
            return not truthy(val)
        raise RuntimeError_(f"Unknown unary operator: {node.op}")

    def _eval_call(self, node: FunctionCall, env: Environment) -> Any:
        """Evaluate function call."""
        args = [self.evaluate(a, env) for a in node.args]

        if isinstance(node.name, Identifier):
            func = env.get(node.name.name)
        elif isinstance(node.name, MemberAccess):
            obj = self.evaluate(node.name.obj, env)
            return self._eval_method(obj, node.name.member, args, env)
        else:
            func = self.evaluate(node.name, env)

        return self._call_function(func, args)

    def _call_function(self, func: Any, args: list) -> Any:
        """Call a function with arguments."""
        if isinstance(func, tuple):
            if func[0] == 'builtin':
                context = {
                    'output_lines': self.output_lines,
                    'call_function': self._call_function,
                }
                return func[1](args, context)

            elif func[0] == 'function':
                _, params, body, closure_env = func
                fn_env = Environment(parent=closure_env)
                for i, param in enumerate(params):
                    pname = param[0]
                    if i < len(args):
                        fn_env.define(pname, args[i])
                    elif len(param) >= 3 and param[2] is not None:
                        default_val = self.evaluate(param[2], closure_env)
                        fn_env.define(pname, default_val)
                    else:
                        fn_env.define(pname, None)
                try:
                    self.execute_block(body, fn_env)
                except ReturnSignal as r:
                    return r.value
                return None

        raise RuntimeError_("Not a callable function")

    def _execute_import(self, node: ImportStmt, env: Environment) -> None:
        """Execute an import statement."""
        importing_file = self._current_file
        if importing_file is None:
            raise RuntimeError_(
                "Cannot use 'import' without a file context. "
                "Run from a .silk file, not the REPL."
            )

        try:
            resolved = self._resolver.resolve(node.path, importing_file)
        except ResolverNotFound as e:
            raise RuntimeError_(str(e))

        if resolved is None:
            native_env = self._load_native_module(node.path)
            if native_env is None:
                raise RuntimeError_(f"Module '{node.path}' not found")
            alias = node.alias or ModuleResolver.default_alias(node.path)
            env.define(alias, native_env, mutable=False)
            return

        abs_path = str(resolved.resolve())

        if abs_path in self._loading_set:
            raise RuntimeError_(
                f"Circular import detected: '{node.path}'"
            )

        if abs_path not in self._module_cache:
            self._loading_set.add(abs_path)
            try:
                source = resolved.read_text()
                module_env = Environment()
                for name, func in ALL_BUILTINS.items():
                    module_env.define(name, ('builtin', func), mutable=False)
                module_env.define('None', SilkOption(is_some=False), mutable=False)

                prev_file = self._current_file
                self._current_file = resolved

                lexer = Lexer(source)
                tokens = lexer.tokenize()
                parser = Parser(tokens)
                ast = parser.parse()
                self.execute(ast, module_env)

                self._current_file = prev_file
                self._module_cache[abs_path] = module_env
            finally:
                self._loading_set.discard(abs_path)

        alias = node.alias or ModuleResolver.default_alias(node.path)
        env.define(alias, self._module_cache[abs_path], mutable=False)

    def _execute_assert(self, node: AssertStatement, env: Environment) -> None:
        value = self.evaluate(node.expression, env)
        if not truthy(value):
            if isinstance(node.expression, BinaryOp) and node.expression.op in ('==', '!=', '<', '>', '<=', '>='):
                left = self.evaluate(node.expression.left, env)
                right = self.evaluate(node.expression.right, env)
                raise RuntimeError_(f"Assertion failed: {silk_repr(left)} {node.expression.op} {silk_repr(right)}")
            raise RuntimeError_("Assertion failed")

    def run_tests(
        self, source: str, file_path: Path | None = None
    ) -> dict:
        """Run all test blocks in source and return results."""
        self._current_file = file_path
        results = {
            'passed': 0, 'failed': 0, 'total': 0, 'failures': []
        }

        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()

        test_blocks = []
        for stmt in ast.statements:
            if isinstance(stmt, TestBlock):
                test_blocks.append(stmt)
            else:
                self.execute(stmt, self.global_env)

        results['total'] = len(test_blocks)

        for test in test_blocks:
            test_env = Environment(parent=self.global_env)
            try:
                self.execute_block(test.body, test_env)
                results['passed'] += 1
                self.output_lines.append(f"  PASS: {test.name}")
            except (RuntimeError_, ReturnSignal) as e:
                results['failed'] += 1
                error_msg = str(e)
                results['failures'].append({
                    'name': test.name, 'error': error_msg
                })
                self.output_lines.append(f"  FAIL: {test.name}")
                self.output_lines.append(f"    {error_msg}")

        self.output_lines.append(
            f"\nResults: {results['passed']} passed, "
            f"{results['failed']} failed, {results['total']} total"
        )

        return results

    def _load_native_module(self, path: str) -> Environment | None:
        """Load a Python-backed native module."""
        cache_key = f"native:{path}"
        if cache_key in self._module_cache:
            return self._module_cache[cache_key]

        from .builtins.math_funcs import MATH_BUILTINS
        from .builtins.medical import MEDICAL_BUILTINS
        import math as pymath

        native_modules = {
            "silk/math": {
                **{name: func for name, func in MATH_BUILTINS.items()},
                "pi": None,
            },
            "silk/medical": {
                name: func for name, func in MEDICAL_BUILTINS.items()
            },
        }

        if path not in native_modules:
            return None

        env = Environment()
        for name, func in native_modules[path].items():
            if name == "pi":
                env.define(name, pymath.pi, mutable=False)
            else:
                env.define(name, ('builtin', func), mutable=False)

        self._module_cache[cache_key] = env
        return env

    def _eval_match(self, node: MatchExpr, env: Environment) -> Any:
        """Evaluate match expression with exhaustiveness check."""
        value = self.evaluate(node.value, env)

        if isinstance(value, SilkEnumValue):
            self._check_enum_exhaustiveness(value.enum_name, node.arms, env)

        for arm in node.arms:
            bindings = {}
            if self._pattern_matches(value, arm.pattern, env, bindings):
                if arm.guard is not None:
                    guard_result = self.evaluate(arm.guard, env)
                    if not truthy(guard_result):
                        continue

                match_env = Environment(parent=env)
                for name, val in bindings.items():
                    match_env.define(name, val, mutable=False)

                if isinstance(arm.body, list):
                    for stmt in arm.body:
                        self.execute(stmt, match_env)
                    return None
                else:
                    return self.evaluate(arm.body, match_env)

        raise RuntimeError_(f"No matching pattern for value: {value}")

    def _check_interface_conformance(self, struct_name: str, interface_name: str,
                                     methods: dict, env: Environment) -> None:
        iface = env.get(interface_name)
        if not isinstance(iface, tuple) or iface[0] != 'interface_def':
            raise RuntimeError_(f"'{interface_name}' is not an interface")
        _, _, required_methods = iface
        missing = [m for m, _, _ in required_methods if m not in methods]
        if missing:
            raise RuntimeError_(
                f"Struct '{struct_name}' does not fully implement interface "
                f"'{interface_name}'. Missing methods: {', '.join(missing)}")

    def _check_enum_exhaustiveness(self, enum_name: str, arms: list[MatchArm],
                                   env: Environment) -> None:
        enum_def = env.get(enum_name)
        if not isinstance(enum_def, tuple) or enum_def[0] != 'enum_def':
            return
        _, _, all_variants = enum_def
        covered_variants = set()
        for arm in arms:
            if isinstance(arm.pattern, Identifier) and arm.pattern.name == '_':
                return
            elif isinstance(arm.pattern, MemberAccess):
                covered_variants.add(arm.pattern.member)
            elif isinstance(arm.pattern, Identifier):
                covered_variants.add(arm.pattern.name)
        missing = set(all_variants) - covered_variants
        if missing:
            raise RuntimeError_(
                f"Non-exhaustive match on enum '{enum_name}'. "
                f"Missing variants: {', '.join(sorted(missing))}. "
                f"Add missing cases or use '_' wildcard.")

    def _pattern_matches(
        self, value: Any, pattern: Any, env: Environment, bindings: dict | None = None
    ) -> bool:
        """Check if value matches pattern, optionally extracting bindings."""
        if bindings is None:
            bindings = {}

        if isinstance(pattern, Identifier):
            if pattern.name == '_':
                return True
            if isinstance(value, SilkEnumValue):
                return value.variant == pattern.name
            return False

        if isinstance(pattern, MemberAccess):
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
