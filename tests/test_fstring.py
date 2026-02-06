"""
Tests for string interpolation (f-strings).

Syntax: f"Hello {name}, you are {age} years old"
"""

import pytest
from silk.lexer import Lexer
from silk.tokens import TokenType
from silk.parser import Parser
from silk.ast import StringInterp
from silk.interpreter import Interpreter
from silk.errors import RuntimeError_


# ═══════════════════════════════════════════════════════════
# LEXER
# ═══════════════════════════════════════════════════════════

class TestFStringLexer:

    def test_fstring_token(self):
        tokens = Lexer('f"hello"').tokenize()
        assert tokens[0].type == TokenType.FSTRING

    def test_fstring_with_expr(self):
        tokens = Lexer('f"hello {name}"').tokenize()
        assert tokens[0].type == TokenType.FSTRING
        assert tokens[0].value == "hello {name}"

    def test_fstring_multiple_exprs(self):
        tokens = Lexer('f"{a} + {b} = {c}"').tokenize()
        assert tokens[0].type == TokenType.FSTRING
        assert tokens[0].value == "{a} + {b} = {c}"

    def test_fstring_no_exprs(self):
        tokens = Lexer('f"plain text"').tokenize()
        assert tokens[0].type == TokenType.FSTRING
        assert tokens[0].value == "plain text"


# ═══════════════════════════════════════════════════════════
# PARSER
# ═══════════════════════════════════════════════════════════

class TestFStringParser:

    def test_parse_fstring_simple(self):
        tokens = Lexer('f"hello {name}"').tokenize()
        ast = Parser(tokens).parse()
        assert isinstance(ast.statements[0], StringInterp)

    def test_parse_fstring_parts(self):
        tokens = Lexer('f"hello {name}"').tokenize()
        ast = Parser(tokens).parse()
        node = ast.statements[0]
        assert isinstance(node, StringInterp)
        # Should have string + expression parts
        assert len(node.parts) == 2

    def test_parse_fstring_no_expr(self):
        tokens = Lexer('f"plain text"').tokenize()
        ast = Parser(tokens).parse()
        node = ast.statements[0]
        assert isinstance(node, StringInterp)
        assert len(node.parts) == 1  # Just the string

    def test_parse_fstring_multiple_exprs(self):
        tokens = Lexer('f"{a} and {b}"').tokenize()
        ast = Parser(tokens).parse()
        node = ast.statements[0]
        assert isinstance(node, StringInterp)
        # "{a}" -> expr, " and " -> str, "{b}" -> expr
        assert len(node.parts) == 3


# ═══════════════════════════════════════════════════════════
# INTERPRETER
# ═══════════════════════════════════════════════════════════

class TestFStringInterpreter:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_fstring_basic(self):
        output = self._run('let name = "World"\nprint(f"Hello {name}")')
        assert output[-1] == "Hello World"

    def test_fstring_with_number(self):
        output = self._run('let x = 42\nprint(f"Value: {x}")')
        assert output[-1] == "Value: 42"

    def test_fstring_multiple_exprs(self):
        output = self._run(
            'let a = 2\nlet b = 3\nprint(f"{a} + {b} = {a + b}")'
        )
        assert output[-1] == "2 + 3 = 5"

    def test_fstring_no_exprs(self):
        output = self._run('print(f"plain text")')
        assert output[-1] == "plain text"

    def test_fstring_with_function_call(self):
        output = self._run(
            'fn double(x) { return x * 2 }\nprint(f"doubled: {double(5)}")'
        )
        assert output[-1] == "doubled: 10"

    def test_fstring_with_member_access(self):
        output = self._run('''
struct Point { x: int, y: int }
let p = Point { x: 3, y: 7 }
print(f"({p.x}, {p.y})")
''')
        assert output[-1] == "(3, 7)"

    def test_fstring_concatenation(self):
        output = self._run('let s = f"hello" + f" world"\nprint(s)')
        assert output[-1] == "hello world"

    def test_fstring_empty_string(self):
        output = self._run('print(f"")')
        assert output[-1] == ""

    def test_fstring_only_expr(self):
        output = self._run('let x = 99\nprint(f"{x}")')
        assert output[-1] == "99"

    def test_fstring_bool_value(self):
        output = self._run('let ok = true\nprint(f"status: {ok}")')
        assert output[-1] == "status: true"

    def test_fstring_in_variable(self):
        output = self._run('let name = "Silk"\nlet msg = f"Hello {name}"\nprint(msg)')
        assert output[-1] == "Hello Silk"
