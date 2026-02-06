"""
Tests for ternary/conditional expressions.

Syntax: if condition then expr else expr
Used as an expression (returns a value).
"""

import pytest
from silk.lexer import Lexer
from silk.tokens import TokenType
from silk.parser import Parser
from silk.interpreter import Interpreter


class TestTernaryLexer:

    def test_then_token(self):
        tokens = Lexer('then').tokenize()
        assert tokens[0].type == TokenType.THEN


class TestTernaryParser:

    def test_parse_ternary(self):
        tokens = Lexer('if true then 1 else 2').tokenize()
        ast = Parser(tokens).parse()
        assert len(ast.statements) == 1

    def test_parse_ternary_in_let(self):
        tokens = Lexer('let x = if true then 1 else 0').tokenize()
        ast = Parser(tokens).parse()
        assert len(ast.statements) == 1


class TestTernaryInterpreter:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_ternary_true(self):
        output = self._run('print(if true then "yes" else "no")')
        assert output[-1] == "yes"

    def test_ternary_false(self):
        output = self._run('print(if false then "yes" else "no")')
        assert output[-1] == "no"

    def test_ternary_with_comparison(self):
        output = self._run('''
let age = 20
let status = if age >= 18 then "adult" else "minor"
print(status)
''')
        assert output[-1] == "adult"

    def test_ternary_in_expression(self):
        output = self._run('''
let x = 5
print(if x > 3 then x * 2 else x)
''')
        assert output[-1] == "10"

    def test_ternary_nested(self):
        output = self._run('''
let x = 5
let label = if x > 10 then "big" else if x > 3 then "medium" else "small"
print(label)
''')
        assert output[-1] == "medium"

    def test_ternary_in_function(self):
        output = self._run('''
fn abs(x) {
    return if x < 0 then -x else x
}
print(abs(-7))
print(abs(3))
''')
        assert output[0] == "7"
        assert output[1] == "3"

    def test_ternary_in_array(self):
        output = self._run('''
let x = true
let arr = [if x then 1 else 0, if x then 2 else 0]
print(arr)
''')
        assert output[-1] == "[1, 2]"

    def test_ternary_as_argument(self):
        output = self._run('''
fn double(x) { return x * 2 }
let flag = true
print(double(if flag then 5 else 10))
''')
        assert output[-1] == "10"
