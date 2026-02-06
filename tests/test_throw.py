"""
Tests for throw keyword.

Syntax: throw expression
Throws RuntimeError_ with the evaluated expression as the message.
Complementary to try/catch.
"""

import pytest
from silk.lexer import Lexer
from silk.tokens import TokenType
from silk.parser import Parser
from silk.ast import ThrowStatement
from silk.interpreter import Interpreter


# ═══════════════════════════════════════════════════════════
# LEXER
# ═══════════════════════════════════════════════════════════

class TestThrowLexer:

    def test_throw_token(self):
        tokens = Lexer('throw').tokenize()
        assert tokens[0].type == TokenType.THROW


# ═══════════════════════════════════════════════════════════
# PARSER
# ═══════════════════════════════════════════════════════════

class TestThrowParser:

    def test_parse_throw(self):
        tokens = Lexer('throw "error message"').tokenize()
        ast = Parser(tokens).parse()
        assert isinstance(ast.statements[0], ThrowStatement)

    def test_parse_throw_expression(self):
        tokens = Lexer('throw "error: " + msg').tokenize()
        ast = Parser(tokens).parse()
        assert isinstance(ast.statements[0], ThrowStatement)


# ═══════════════════════════════════════════════════════════
# INTERPRETER
# ═══════════════════════════════════════════════════════════

class TestThrowInterpreter:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_throw_caught_by_catch(self):
        output = self._run('''
try {
    throw "custom error"
} catch e {
    print(e)
}
''')
        assert output[-1] == "custom error"

    def test_throw_with_expression(self):
        output = self._run('''
try {
    let code = 404
    throw f"Error code: {code}"
} catch e {
    print(e)
}
''')
        assert "Error code: 404" in output[-1]

    def test_throw_in_function(self):
        output = self._run('''
fn validate(age) {
    if age < 0 {
        throw "Age cannot be negative"
    }
    return age
}
try {
    validate(-5)
} catch e {
    print(e)
}
''')
        assert output[-1] == "Age cannot be negative"

    def test_throw_propagates(self):
        """Throw propagates up through function calls."""
        output = self._run('''
fn inner() {
    throw "deep error"
}
fn outer() {
    inner()
}
try {
    outer()
} catch e {
    print(e)
}
''')
        assert output[-1] == "deep error"

    def test_throw_stops_execution(self):
        output = self._run('''
try {
    print("before")
    throw "stop"
    print("after")
} catch e {
    print("caught")
}
''')
        assert output[0] == "before"
        assert output[1] == "caught"

    def test_throw_number_message(self):
        output = self._run('''
try {
    throw 42
} catch e {
    print(e)
}
''')
        assert output[-1] == "42"

    def test_uncaught_throw(self):
        """Uncaught throw shows as Silk error."""
        interp = Interpreter()
        result = interp.run('throw "unhandled"')
        assert result is False
