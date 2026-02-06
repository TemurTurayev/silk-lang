"""
Silk Lexer

Converts source code into a stream of tokens.
"""

from typing import Any
from .tokens import Token, TokenType, KEYWORDS
from .errors import LexerError


class Lexer:
    """Tokenizer for the Silk language."""

    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.col = 1
        self.tokens: list[Token] = []

    def peek(self, offset: int = 0) -> str:
        """Look at character at current position + offset."""
        pos = self.pos + offset
        if pos < len(self.source):
            return self.source[pos]
        return '\0'

    def advance(self) -> str:
        """Move to next character and return current."""
        ch = self.source[self.pos]
        self.pos += 1
        if ch == '\n':
            self.line += 1
            self.col = 1
        else:
            self.col += 1
        return ch

    def add_token(self, type_: TokenType, value: Any = None) -> None:
        """Add a token to the list."""
        self.tokens.append(Token(type_, value, self.line, self.col))

    def skip_whitespace(self) -> None:
        """Skip spaces and tabs (but not newlines)."""
        while self.pos < len(self.source) and self.source[self.pos] in ' \t\r':
            self.advance()

    def skip_comment(self) -> bool:
        """Skip single-line (//) or block (/* */) comments."""
        if self.peek() == '/' and self.peek(1) == '/':
            # Single-line comment
            while self.pos < len(self.source) and self.source[self.pos] != '\n':
                self.advance()
            return True

        if self.peek() == '/' and self.peek(1) == '*':
            # Block comment
            self.advance()  # consume /
            self.advance()  # consume *
            while self.pos < len(self.source) - 1:
                if self.source[self.pos] == '*' and self.source[self.pos + 1] == '/':
                    self.advance()  # consume *
                    self.advance()  # consume /
                    return True
                self.advance()
            raise LexerError("Unterminated block comment", self.line, self.col)

        return False

    def read_string(self) -> None:
        """Read a string literal."""
        quote = self.advance()  # consume opening quote
        start_line = self.line
        result: list[str] = []

        while self.pos < len(self.source):
            ch = self.source[self.pos]

            if ch == '\\':
                # Escape sequence
                self.advance()
                if self.pos >= len(self.source):
                    break
                esc = self.advance()
                escape_map = {
                    'n': '\n',
                    't': '\t',
                    'r': '\r',
                    '\\': '\\',
                    '"': '"',
                    "'": "'"
                }
                result.append(escape_map.get(esc, '\\' + esc))

            elif ch == quote:
                self.advance()
                self.add_token(TokenType.STRING, ''.join(result))
                return

            elif ch == '\n':
                raise LexerError("Unterminated string", start_line, self.col)

            else:
                result.append(self.advance())

        raise LexerError("Unterminated string", start_line, self.col)

    def read_number(self) -> None:
        """Read an integer or float literal."""
        start = self.pos
        is_float = False

        while self.pos < len(self.source):
            ch = self.source[self.pos]

            if ch.isdigit():
                self.pos += 1
                self.col += 1
            elif ch == '.':
                if is_float:
                    break  # Second dot, stop
                # Check if next char is a digit (otherwise it's member access)
                if self.pos + 1 < len(self.source) and self.source[self.pos + 1].isdigit():
                    is_float = True
                    self.pos += 1
                    self.col += 1
                else:
                    break
            else:
                break

        text = self.source[start:self.pos]

        if is_float:
            self.add_token(TokenType.FLOAT, float(text))
        else:
            self.add_token(TokenType.INT, int(text))

    def read_fstring(self) -> None:
        """Read an f-string: f"text {expr} text"."""
        self.advance()  # consume 'f'
        self.advance()  # consume '"'
        start_line = self.line
        result: list[str] = []

        while self.pos < len(self.source):
            ch = self.source[self.pos]

            if ch == '\\':
                self.advance()
                if self.pos >= len(self.source):
                    break
                esc = self.advance()
                escape_map = {
                    'n': '\n', 't': '\t', 'r': '\r',
                    '\\': '\\', '"': '"', "'": "'",
                }
                result.append(escape_map.get(esc, '\\' + esc))
            elif ch == '"':
                self.advance()
                self.add_token(TokenType.FSTRING, ''.join(result))
                return
            elif ch == '\n':
                raise LexerError("Unterminated f-string", start_line, self.col)
            else:
                result.append(self.advance())

        raise LexerError("Unterminated f-string", start_line, self.col)

    def read_identifier(self) -> None:
        """Read an identifier or keyword."""
        start = self.pos

        while self.pos < len(self.source):
            ch = self.source[self.pos]
            if ch.isalnum() or ch == '_':
                self.pos += 1
                self.col += 1
            else:
                break

        text = self.source[start:self.pos]

        if text in KEYWORDS:
            tt = KEYWORDS[text]
            if tt == TokenType.TRUE:
                self.add_token(TokenType.BOOL, True)
            elif tt == TokenType.FALSE:
                self.add_token(TokenType.BOOL, False)
            else:
                self.add_token(tt, text)
        else:
            self.add_token(TokenType.IDENTIFIER, text)

    def tokenize(self) -> list[Token]:
        """Convert source code to a list of tokens."""
        while self.pos < len(self.source):
            self.skip_whitespace()

            if self.pos >= len(self.source):
                break

            if self.skip_comment():
                continue

            ch = self.source[self.pos]

            if ch == '\n':
                self.add_token(TokenType.NEWLINE)
                self.advance()

            elif ch in ('"', "'"):
                self.read_string()

            elif ch.isdigit():
                self.read_number()

            elif ch == 'f' and self.peek(1) == '"':
                self.read_fstring()

            elif ch.isalpha() or ch == '_':
                self.read_identifier()

            elif ch == '+':
                self.advance()
                if self.pos < len(self.source) and self.source[self.pos] == '=':
                    self.advance()
                    self.add_token(TokenType.PLUS_ASSIGN)
                else:
                    self.add_token(TokenType.PLUS)

            elif ch == '-':
                self.advance()
                if self.pos < len(self.source) and self.source[self.pos] == '>':
                    self.advance()
                    self.add_token(TokenType.ARROW)
                elif self.pos < len(self.source) and self.source[self.pos] == '=':
                    self.advance()
                    self.add_token(TokenType.MINUS_ASSIGN)
                else:
                    self.add_token(TokenType.MINUS)

            elif ch == '*':
                self.advance()
                if self.pos < len(self.source) and self.source[self.pos] == '*':
                    self.advance()
                    self.add_token(TokenType.POWER)
                elif self.pos < len(self.source) and self.source[self.pos] == '=':
                    self.advance()
                    self.add_token(TokenType.STAR_ASSIGN)
                else:
                    self.add_token(TokenType.STAR)

            elif ch == '/':
                self.advance()
                if self.pos < len(self.source) and self.source[self.pos] == '=':
                    self.advance()
                    self.add_token(TokenType.SLASH_ASSIGN)
                else:
                    self.add_token(TokenType.SLASH)

            elif ch == '%':
                self.advance()
                self.add_token(TokenType.PERCENT)

            elif ch == '=':
                self.advance()
                if self.pos < len(self.source) and self.source[self.pos] == '>':
                    self.advance()
                    self.add_token(TokenType.ARROW_MATCH)
                elif self.pos < len(self.source) and self.source[self.pos] == '=':
                    self.advance()
                    self.add_token(TokenType.EQ)
                else:
                    self.add_token(TokenType.ASSIGN)

            elif ch == '!':
                self.advance()
                if self.pos < len(self.source) and self.source[self.pos] == '=':
                    self.advance()
                    self.add_token(TokenType.NEQ)
                else:
                    raise LexerError(f"Unexpected character '!'", self.line, self.col)

            elif ch == '<':
                self.advance()
                if self.pos < len(self.source) and self.source[self.pos] == '=':
                    self.advance()
                    self.add_token(TokenType.LTE)
                else:
                    self.add_token(TokenType.LT)

            elif ch == '>':
                self.advance()
                if self.pos < len(self.source) and self.source[self.pos] == '=':
                    self.advance()
                    self.add_token(TokenType.GTE)
                else:
                    self.add_token(TokenType.GT)

            elif ch == '(':
                self.advance()
                self.add_token(TokenType.LPAREN)

            elif ch == ')':
                self.advance()
                self.add_token(TokenType.RPAREN)

            elif ch == '{':
                self.advance()
                self.add_token(TokenType.LBRACE)

            elif ch == '}':
                self.advance()
                self.add_token(TokenType.RBRACE)

            elif ch == '[':
                self.advance()
                self.add_token(TokenType.LBRACKET)

            elif ch == ']':
                self.advance()
                self.add_token(TokenType.RBRACKET)

            elif ch == ',':
                self.advance()
                self.add_token(TokenType.COMMA)

            elif ch == ':':
                self.advance()
                self.add_token(TokenType.COLON)

            elif ch == '.':
                if self.peek(1) == '.' and self.peek(2) == '.':
                    self.advance()  # first .
                    self.advance()  # second .
                    self.advance()  # third .
                    self.add_token(TokenType.SPREAD)
                elif self.peek(1) == '.':
                    self.advance()  # first .
                    self.advance()  # second .
                    self.add_token(TokenType.DOTDOT)
                else:
                    self.advance()
                    self.add_token(TokenType.DOT)

            elif ch == '|':
                self.advance()
                if self.pos < len(self.source) and self.source[self.pos] == '>':
                    self.advance()
                    self.add_token(TokenType.PIPE)
                else:
                    raise LexerError("Expected '>' after '|' (pipe operator is |>)", self.line, self.col)

            else:
                raise LexerError(f"Unexpected character '{ch}'", self.line, self.col)

        self.add_token(TokenType.EOF)
        return self.tokens
