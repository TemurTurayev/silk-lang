"""
Tests for try/catch error handling.

Syntax: try { body } catch err { handler }
"""

import pytest
from silk.lexer import Lexer
from silk.tokens import TokenType
from silk.parser import Parser
from silk.ast import TryCatch
from silk.interpreter import Interpreter


# ═══════════════════════════════════════════════════════════
# LEXER
# ═══════════════════════════════════════════════════════════

class TestTryCatchLexer:

    def test_try_token(self):
        tokens = Lexer('try').tokenize()
        assert tokens[0].type == TokenType.TRY

    def test_catch_token(self):
        tokens = Lexer('catch').tokenize()
        assert tokens[0].type == TokenType.CATCH


# ═══════════════════════════════════════════════════════════
# PARSER
# ═══════════════════════════════════════════════════════════

class TestTryCatchParser:

    def test_parse_try_catch(self):
        source = 'try { let x = 1 } catch e { print(e) }'
        tokens = Lexer(source).tokenize()
        ast = Parser(tokens).parse()
        assert isinstance(ast.statements[0], TryCatch)

    def test_parse_try_catch_parts(self):
        source = 'try { let x = 1 } catch err { print(err) }'
        tokens = Lexer(source).tokenize()
        ast = Parser(tokens).parse()
        node = ast.statements[0]
        assert isinstance(node, TryCatch)
        assert node.error_name == "err"
        assert len(node.try_body) >= 1
        assert len(node.catch_body) >= 1


# ═══════════════════════════════════════════════════════════
# INTERPRETER
# ═══════════════════════════════════════════════════════════

class TestTryCatchInterpreter:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_try_no_error(self):
        """Try body runs normally when no error."""
        output = self._run('''
try {
    print("ok")
} catch e {
    print("error")
}
''')
        assert output[-1] == "ok"

    def test_catch_division_by_zero(self):
        output = self._run('''
try {
    let x = 1 / 0
} catch e {
    print(e)
}
''')
        assert "Division by zero" in output[-1]

    def test_catch_undefined_variable(self):
        output = self._run('''
try {
    print(undefined_var)
} catch e {
    print("caught")
}
''')
        assert output[-1] == "caught"

    def test_catch_error_binding(self):
        """Error message is bound to the catch variable."""
        output = self._run('''
try {
    let x = 1 / 0
} catch err {
    print(f"Error: {err}")
}
''')
        assert "Error:" in output[-1]
        assert "Division by zero" in output[-1]

    def test_try_catch_doesnt_leak_scope(self):
        """Variables in try block don't leak to outer scope."""
        output = self._run('''
try {
    let inner = 42
} catch e {
    print(e)
}
// inner should not be accessible here
try {
    print(inner)
} catch e {
    print("not found")
}
''')
        assert output[-1] == "not found"

    def test_try_catch_continues_after(self):
        """Execution continues normally after try/catch."""
        output = self._run('''
try {
    let x = 1 / 0
} catch e {
    print("caught")
}
print("continued")
''')
        assert output[0] == "caught"
        assert output[1] == "continued"

    def test_nested_try_catch(self):
        output = self._run('''
try {
    try {
        let x = 1 / 0
    } catch e {
        print(f"inner: {e}")
    }
    print("outer ok")
} catch e {
    print("outer caught")
}
''')
        assert "inner:" in output[0]
        assert output[1] == "outer ok"

    def test_catch_assertion_error(self):
        output = self._run('''
try {
    assert false
} catch e {
    print("assertion caught")
}
''')
        assert output[-1] == "assertion caught"

    def test_try_catch_with_return_in_function(self):
        output = self._run('''
fn safe_divide(a, b) {
    try {
        return a / b
    } catch e {
        return 0
    }
}
print(safe_divide(10, 0))
print(safe_divide(10, 2))
''')
        assert output[0] == "0"
        assert output[1] == "5"

    def test_catch_type_error(self):
        output = self._run('''
try {
    let x = "hello" - 5
} catch e {
    print("type error caught")
}
''')
        assert output[-1] == "type error caught"
