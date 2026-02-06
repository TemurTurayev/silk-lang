"""
Tests for closures and anonymous functions (lambdas).

Syntax: fn(params) { body }  (no name = anonymous)
"""

import pytest
from silk.lexer import Lexer
from silk.parser import Parser
from silk.ast import FunctionDef
from silk.interpreter import Interpreter
from silk.errors import RuntimeError_


# ═══════════════════════════════════════════════════════════
# PARSER
# ═══════════════════════════════════════════════════════════

class TestLambdaParsing:

    def test_parse_anonymous_fn(self):
        tokens = Lexer('let f = fn(x) { return x * 2 }').tokenize()
        ast = Parser(tokens).parse()
        assert len(ast.statements) == 1

    def test_parse_lambda_no_params(self):
        tokens = Lexer('let f = fn() { return 42 }').tokenize()
        ast = Parser(tokens).parse()
        assert len(ast.statements) == 1

    def test_parse_lambda_multi_params(self):
        tokens = Lexer('let f = fn(a, b) { return a + b }').tokenize()
        ast = Parser(tokens).parse()
        assert len(ast.statements) == 1


# ═══════════════════════════════════════════════════════════
# INTERPRETER: ANONYMOUS FUNCTIONS
# ═══════════════════════════════════════════════════════════

class TestAnonymousFunctions:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_assign_lambda(self):
        output = self._run('''
let double = fn(x) { return x * 2 }
print(double(5))
''')
        assert output[-1] == "10"

    def test_lambda_no_params(self):
        output = self._run('''
let greet = fn() { return "hello" }
print(greet())
''')
        assert output[-1] == "hello"

    def test_lambda_multi_params(self):
        output = self._run('''
let add = fn(a, b) { return a + b }
print(add(3, 4))
''')
        assert output[-1] == "7"

    def test_lambda_as_argument(self):
        """Pass anonymous function as argument to another function."""
        output = self._run('''
fn apply(f, x) {
    return f(x)
}
print(apply(fn(x) { return x * 3 }, 7))
''')
        assert output[-1] == "21"

    def test_closure_captures_environment(self):
        output = self._run('''
let multiplier = 10
let scale = fn(x) { return x * multiplier }
print(scale(5))
''')
        assert output[-1] == "50"

    def test_closure_factory(self):
        """Function returning a closure."""
        output = self._run('''
fn make_adder(n) {
    return fn(x) { return x + n }
}
let add5 = make_adder(5)
print(add5(10))
''')
        assert output[-1] == "15"

    def test_closure_deep_nesting(self):
        output = self._run('''
fn outer(a) {
    return fn(b) {
        return fn(c) {
            return a + b + c
        }
    }
}
let f = outer(1)
let g = f(2)
print(g(3))
''')
        assert output[-1] == "6"

    def test_named_fn_still_works(self):
        """Named functions should still work as before."""
        output = self._run('''
fn square(x) { return x * x }
print(square(4))
''')
        assert output[-1] == "16"


# ═══════════════════════════════════════════════════════════
# HIGHER-ORDER BUILTINS
# ═══════════════════════════════════════════════════════════

class TestHigherOrderBuiltins:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_map_basic(self):
        output = self._run('''
let nums = [1, 2, 3]
let doubled = map(nums, fn(x) { return x * 2 })
print(doubled)
''')
        assert output[-1] == "[2, 4, 6]"

    def test_filter_basic(self):
        output = self._run('''
let nums = [1, 2, 3, 4, 5, 6]
let evens = filter(nums, fn(x) { return x % 2 == 0 })
print(evens)
''')
        assert output[-1] == "[2, 4, 6]"

    def test_map_with_named_fn(self):
        output = self._run('''
fn triple(x) { return x * 3 }
let result = map([2, 4], triple)
print(result)
''')
        assert output[-1] == "[6, 12]"

    def test_filter_with_named_fn(self):
        output = self._run('''
fn positive(x) { return x > 0 }
let result = filter([-1, 2, -3, 4], positive)
print(result)
''')
        assert output[-1] == "[2, 4]"

    def test_map_empty_array(self):
        output = self._run('''
let result = map([], fn(x) { return x * 2 })
print(result)
''')
        assert output[-1] == "[]"

    def test_filter_none_match(self):
        output = self._run('''
let result = filter([1, 2, 3], fn(x) { return x > 10 })
print(result)
''')
        assert output[-1] == "[]"

    def test_chained_map_filter(self):
        output = self._run('''
let nums = [1, 2, 3, 4, 5]
let result = filter(map(nums, fn(x) { return x * 2 }), fn(x) { return x > 5 })
print(result)
''')
        assert output[-1] == "[6, 8, 10]"
