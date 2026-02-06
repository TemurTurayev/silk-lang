"""
Tests for the pipe operator (|>).

Syntax: value |> function
Desugars to: function(value)
"""

import pytest
from silk.lexer import Lexer
from silk.tokens import TokenType
from silk.parser import Parser
from silk.ast import BinaryOp
from silk.interpreter import Interpreter


class TestPipeLexer:

    def test_pipe_token(self):
        tokens = Lexer('x |> f').tokenize()
        assert tokens[1].type == TokenType.PIPE

    def test_pipe_in_chain(self):
        tokens = Lexer('x |> f |> g').tokenize()
        pipe_count = sum(1 for t in tokens if t.type == TokenType.PIPE)
        assert pipe_count == 2


class TestPipeParser:

    def test_parse_pipe(self):
        tokens = Lexer('x |> f').tokenize()
        ast = Parser(tokens).parse()
        assert isinstance(ast.statements[0], BinaryOp)
        assert ast.statements[0].op == '|>'

    def test_parse_pipe_chain(self):
        tokens = Lexer('x |> f |> g').tokenize()
        ast = Parser(tokens).parse()
        # Left-associative: (x |> f) |> g
        node = ast.statements[0]
        assert isinstance(node, BinaryOp)
        assert node.op == '|>'
        assert isinstance(node.left, BinaryOp)
        assert node.left.op == '|>'


class TestPipeInterpreter:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_pipe_basic(self):
        output = self._run('''
fn double(x) { return x * 2 }
let result = 5 |> double
print(result)
''')
        assert output[-1] == "10"

    def test_pipe_chain(self):
        output = self._run('''
fn double(x) { return x * 2 }
fn add_one(x) { return x + 1 }
let result = 5 |> double |> add_one
print(result)
''')
        assert output[-1] == "11"

    def test_pipe_with_lambda(self):
        output = self._run('''
let result = 10 |> fn(x) { return x * 3 }
print(result)
''')
        assert output[-1] == "30"

    def test_pipe_with_builtin(self):
        output = self._run('''
let result = [3, 1, 2] |> sort
print(result)
''')
        assert output[-1] == "[1, 2, 3]"

    def test_pipe_long_chain(self):
        output = self._run('''
fn add_one(x) { return x + 1 }
fn double(x) { return x * 2 }
fn negate(x) { return -x }
let result = 3 |> add_one |> double |> negate
print(result)
''')
        assert output[-1] == "-8"

    def test_pipe_with_string(self):
        output = self._run('''
fn exclaim(s) { return s + "!" }
let result = "hello" |> exclaim
print(result)
''')
        assert output[-1] == "hello!"

    def test_pipe_in_expression(self):
        output = self._run('''
fn double(x) { return x * 2 }
print(5 |> double)
''')
        assert output[-1] == "10"
