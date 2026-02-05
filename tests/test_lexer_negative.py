"""
Lexer Negative Tests

These tests verify that the lexer correctly reports errors.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from silk.lexer import Lexer
from silk.errors import LexerError


class TestLexerErrors:
    """Test lexer error handling."""

    def test_unterminated_string(self, lexer):
        lex = lexer('"hello')
        with pytest.raises(LexerError) as exc_info:
            lex.tokenize()
        assert "Unterminated string" in str(exc_info.value)

    def test_unterminated_string_newline(self, lexer):
        lex = lexer('"hello\nworld"')
        with pytest.raises(LexerError) as exc_info:
            lex.tokenize()
        assert "Unterminated string" in str(exc_info.value)

    def test_unterminated_block_comment(self, lexer):
        lex = lexer("/* comment without end")
        with pytest.raises(LexerError) as exc_info:
            lex.tokenize()
        assert "Unterminated block comment" in str(exc_info.value)

    def test_unexpected_character(self, lexer):
        lex = lexer("@")
        with pytest.raises(LexerError) as exc_info:
            lex.tokenize()
        assert "Unexpected character" in str(exc_info.value)

    def test_standalone_exclamation(self, lexer):
        lex = lexer("!")
        with pytest.raises(LexerError) as exc_info:
            lex.tokenize()
        assert "Unexpected character '!'" in str(exc_info.value)

    def test_error_includes_line_number(self, lexer):
        lex = lexer('let x = 1\nlet y = "unterminated')
        with pytest.raises(LexerError) as exc_info:
            lex.tokenize()
        # Error should be on line 2
        assert exc_info.value.line == 2

    def test_invalid_unicode_character(self, lexer):
        # Test with a character that's not valid in Silk
        lex = lexer("let x = \u2603")  # snowman emoji
        with pytest.raises(LexerError) as exc_info:
            lex.tokenize()
        assert "Unexpected character" in str(exc_info.value)

    def test_hash_not_comment(self, lexer):
        # Silk uses // for comments, not #
        lex = lexer("# this is not a comment")
        with pytest.raises(LexerError) as exc_info:
            lex.tokenize()
        assert "Unexpected character '#'" in str(exc_info.value)

    def test_backtick_not_supported(self, lexer):
        lex = lexer("`template`")
        with pytest.raises(LexerError) as exc_info:
            lex.tokenize()
        assert "Unexpected character" in str(exc_info.value)

    def test_single_ampersand_not_supported(self, lexer):
        # Silk uses 'and' keyword, not &&
        lex = lexer("&")
        with pytest.raises(LexerError) as exc_info:
            lex.tokenize()
        assert "Unexpected character" in str(exc_info.value)
