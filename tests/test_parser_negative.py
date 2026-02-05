"""
Parser Negative Tests

Tests for parser error handling.
"""

import pytest
from silk.lexer import Lexer
from silk.parser import Parser
from silk.errors import ParseError


def parse(source: str):
    """Helper to parse source code."""
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    return parser.parse()


class TestParseErrors:
    """Test that parser raises appropriate errors."""

    def test_missing_rbrace(self):
        with pytest.raises(ParseError) as exc:
            parse("if true { print(1)")
        # Parser reports unexpected EOF when brace is missing
        assert "RBRACE" in str(exc.value) or "}" in str(exc.value) or "EOF" in str(exc.value)

    def test_missing_rparen(self):
        with pytest.raises(ParseError) as exc:
            parse("fn add(a, b { return a }")
        assert "RPAREN" in str(exc.value) or ")" in str(exc.value)

    def test_missing_expression(self):
        with pytest.raises(ParseError) as exc:
            parse("let x =")
        # Should error on unexpected EOF

    def test_invalid_let_syntax(self):
        with pytest.raises(ParseError) as exc:
            parse("let = 5")
        assert "IDENTIFIER" in str(exc.value)

    def test_missing_in_keyword(self):
        with pytest.raises(ParseError) as exc:
            parse("for i items { }")
        assert "IN" in str(exc.value) or "in" in str(exc.value).lower()

    def test_unexpected_token(self):
        with pytest.raises(ParseError) as exc:
            parse("let x = )")
        # Should report unexpected token

    def test_unclosed_array(self):
        with pytest.raises(ParseError) as exc:
            parse("[1, 2, 3")
        assert "RBRACKET" in str(exc.value) or "]" in str(exc.value)

    def test_missing_condition(self):
        with pytest.raises(ParseError) as exc:
            parse("if { print(1) }")
        # Should error on missing condition

    def test_missing_function_body(self):
        with pytest.raises(ParseError) as exc:
            parse("fn test()")
        assert "LBRACE" in str(exc.value) or "{" in str(exc.value)

    def test_error_includes_line_col(self):
        with pytest.raises(ParseError) as exc:
            parse("let x =\nlet y = )")
        # ParseError should have line/col info
        error = exc.value
        assert hasattr(error, 'line') or 'line' in str(error).lower()
