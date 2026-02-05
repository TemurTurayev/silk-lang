"""
Lexer Tests - Golden Tests

These tests verify that the lexer correctly tokenizes various inputs.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from silk.lexer import Lexer
from silk.tokens import TokenType


class TestLexerNumbers:
    """Test number tokenization."""

    def test_integer(self, lexer):
        lex = lexer("42")
        tokens = lex.tokenize()
        assert tokens[0].type == TokenType.INT
        assert tokens[0].value == 42

    def test_float(self, lexer):
        lex = lexer("3.14")
        tokens = lex.tokenize()
        assert tokens[0].type == TokenType.FLOAT
        assert tokens[0].value == 3.14

    def test_negative_handled_as_unary(self, lexer):
        lex = lexer("-5")
        tokens = lex.tokenize()
        assert tokens[0].type == TokenType.MINUS
        assert tokens[1].type == TokenType.INT
        assert tokens[1].value == 5


class TestLexerStrings:
    """Test string tokenization."""

    def test_double_quoted_string(self, lexer):
        lex = lexer('"hello"')
        tokens = lex.tokenize()
        assert tokens[0].type == TokenType.STRING
        assert tokens[0].value == "hello"

    def test_single_quoted_string(self, lexer):
        lex = lexer("'world'")
        tokens = lex.tokenize()
        assert tokens[0].type == TokenType.STRING
        assert tokens[0].value == "world"

    def test_escape_sequences(self, lexer):
        lex = lexer('"hello\\nworld"')
        tokens = lex.tokenize()
        assert tokens[0].value == "hello\nworld"


class TestLexerKeywords:
    """Test keyword tokenization."""

    def test_let(self, lexer):
        lex = lexer("let")
        tokens = lex.tokenize()
        assert tokens[0].type == TokenType.LET

    def test_mut(self, lexer):
        lex = lexer("mut")
        tokens = lex.tokenize()
        assert tokens[0].type == TokenType.MUT

    def test_fn(self, lexer):
        lex = lexer("fn")
        tokens = lex.tokenize()
        assert tokens[0].type == TokenType.FN

    def test_true_false(self, lexer):
        lex = lexer("true false")
        tokens = lex.tokenize()
        assert tokens[0].type == TokenType.BOOL
        assert tokens[0].value is True
        assert tokens[1].type == TokenType.BOOL
        assert tokens[1].value is False

    def test_struct_keyword(self, lexer):
        lex = lexer("struct")
        tokens = lex.tokenize()
        assert tokens[0].type == TokenType.STRUCT


class TestLexerOperators:
    """Test operator tokenization."""

    def test_arithmetic_operators(self, lexer):
        lex = lexer("+ - * / % **")
        tokens = lex.tokenize()
        assert tokens[0].type == TokenType.PLUS
        assert tokens[1].type == TokenType.MINUS
        assert tokens[2].type == TokenType.STAR
        assert tokens[3].type == TokenType.SLASH
        assert tokens[4].type == TokenType.PERCENT
        assert tokens[5].type == TokenType.POWER

    def test_comparison_operators(self, lexer):
        lex = lexer("== != < > <= >=")
        tokens = lex.tokenize()
        assert tokens[0].type == TokenType.EQ
        assert tokens[1].type == TokenType.NEQ
        assert tokens[2].type == TokenType.LT
        assert tokens[3].type == TokenType.GT
        assert tokens[4].type == TokenType.LTE
        assert tokens[5].type == TokenType.GTE

    def test_compound_assignment(self, lexer):
        lex = lexer("+= -= *= /=")
        tokens = lex.tokenize()
        assert tokens[0].type == TokenType.PLUS_ASSIGN
        assert tokens[1].type == TokenType.MINUS_ASSIGN
        assert tokens[2].type == TokenType.STAR_ASSIGN
        assert tokens[3].type == TokenType.SLASH_ASSIGN


class TestLexerComments:
    """Test comment handling."""

    def test_single_line_comment(self, lexer):
        lex = lexer("42 // this is a comment\n43")
        tokens = lex.tokenize()
        assert tokens[0].type == TokenType.INT
        assert tokens[0].value == 42
        assert tokens[1].type == TokenType.NEWLINE
        assert tokens[2].type == TokenType.INT
        assert tokens[2].value == 43

    def test_block_comment(self, lexer):
        lex = lexer("1 /* comment */ 2")
        tokens = lex.tokenize()
        assert tokens[0].type == TokenType.INT
        assert tokens[0].value == 1
        assert tokens[1].type == TokenType.INT
        assert tokens[1].value == 2


class TestLexerDelimiters:
    """Test delimiter tokenization."""

    def test_parentheses(self, lexer):
        lex = lexer("()")
        tokens = lex.tokenize()
        assert tokens[0].type == TokenType.LPAREN
        assert tokens[1].type == TokenType.RPAREN

    def test_braces(self, lexer):
        lex = lexer("{}")
        tokens = lex.tokenize()
        assert tokens[0].type == TokenType.LBRACE
        assert tokens[1].type == TokenType.RBRACE

    def test_brackets(self, lexer):
        lex = lexer("[]")
        tokens = lex.tokenize()
        assert tokens[0].type == TokenType.LBRACKET
        assert tokens[1].type == TokenType.RBRACKET

    def test_arrow(self, lexer):
        lex = lexer("->")
        tokens = lex.tokenize()
        assert tokens[0].type == TokenType.ARROW
