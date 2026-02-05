#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                    SILK Programming Language                  ║
║              Simple • Intuitive • Lightweight • Keen          ║
║                        Version 0.1.0                         ║
║                                                              ║
║  Inspired by: Python (simplicity), Go (clarity),             ║
║               Rust (safety), with a touch of medicine 🩺      ║
╚══════════════════════════════════════════════════════════════╝

Author: Temur Turayev
GitHub: github.com/TemurTurayev
"""

import sys
import math
import os
from enum import Enum, auto
from dataclasses import dataclass, field
from typing import Any, Optional


# ═══════════════════════════════════════════════════════════
# TOKEN TYPES
# ═══════════════════════════════════════════════════════════

class TokenType(Enum):
    # Literals
    INT = auto()
    FLOAT = auto()
    STRING = auto()
    BOOL = auto()
    IDENTIFIER = auto()

    # Keywords
    LET = auto()
    MUT = auto()
    FN = auto()
    RETURN = auto()
    IF = auto()
    ELIF = auto()
    ELSE = auto()
    WHILE = auto()
    FOR = auto()
    IN = auto()
    BREAK = auto()
    CONTINUE = auto()
    AND = auto()
    OR = auto()
    NOT = auto()
    TRUE = auto()
    FALSE = auto()
    NULL = auto()
    IMPORT = auto()

    # Type annotations
    TYPE_INT = auto()
    TYPE_FLOAT = auto()
    TYPE_STR = auto()
    TYPE_BOOL = auto()
    TYPE_ARRAY = auto()

    # Operators
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    PERCENT = auto()
    POWER = auto()
    ASSIGN = auto()
    PLUS_ASSIGN = auto()
    MINUS_ASSIGN = auto()
    STAR_ASSIGN = auto()
    SLASH_ASSIGN = auto()

    # Comparison
    EQ = auto()
    NEQ = auto()
    LT = auto()
    GT = auto()
    LTE = auto()
    GTE = auto()

    # Delimiters
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    COMMA = auto()
    COLON = auto()
    ARROW = auto()
    DOT = auto()
    NEWLINE = auto()
    EOF = auto()


KEYWORDS = {
    'let': TokenType.LET,
    'mut': TokenType.MUT,
    'fn': TokenType.FN,
    'return': TokenType.RETURN,
    'if': TokenType.IF,
    'elif': TokenType.ELIF,
    'else': TokenType.ELSE,
    'while': TokenType.WHILE,
    'for': TokenType.FOR,
    'in': TokenType.IN,
    'break': TokenType.BREAK,
    'continue': TokenType.CONTINUE,
    'and': TokenType.AND,
    'or': TokenType.OR,
    'not': TokenType.NOT,
    'true': TokenType.TRUE,
    'false': TokenType.FALSE,
    'null': TokenType.NULL,
    'import': TokenType.IMPORT,
    # Type names are just identifiers so they can also be used as functions
    # 'int', 'float', 'str', 'bool', 'array' are handled as identifiers
}


@dataclass
class Token:
    type: TokenType
    value: Any
    line: int
    col: int

    def __repr__(self):
        return f"Token({self.type.name}, {self.value!r}, L{self.line}:{self.col})"


# ═══════════════════════════════════════════════════════════
# LEXER
# ═══════════════════════════════════════════════════════════

class SilkError(Exception):
    """Base error for Silk language."""
    def __init__(self, message, line=None, col=None):
        self.line = line
        self.col = col
        prefix = f"[line {line}]" if line else ""
        super().__init__(f"{prefix} {message}")


class LexerError(SilkError):
    pass


class ParseError(SilkError):
    pass


class RuntimeError_(SilkError):
    pass


class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.col = 1
        self.tokens = []

    def peek(self, offset=0) -> str:
        pos = self.pos + offset
        if pos < len(self.source):
            return self.source[pos]
        return '\0'

    def advance(self) -> str:
        ch = self.source[self.pos]
        self.pos += 1
        if ch == '\n':
            self.line += 1
            self.col = 1
        else:
            self.col += 1
        return ch

    def add_token(self, type_: TokenType, value: Any = None):
        self.tokens.append(Token(type_, value, self.line, self.col))

    def skip_whitespace(self):
        while self.pos < len(self.source) and self.source[self.pos] in ' \t\r':
            self.advance()

    def skip_comment(self):
        if self.peek() == '/' and self.peek(1) == '/':
            while self.pos < len(self.source) and self.source[self.pos] != '\n':
                self.advance()
            return True
        if self.peek() == '/' and self.peek(1) == '*':
            self.advance()
            self.advance()
            while self.pos < len(self.source) - 1:
                if self.source[self.pos] == '*' and self.source[self.pos + 1] == '/':
                    self.advance()
                    self.advance()
                    return True
                self.advance()
            raise LexerError("Unterminated block comment", self.line, self.col)
        return False

    def read_string(self):
        quote = self.advance()  # consume opening quote
        start_line = self.line
        result = []
        while self.pos < len(self.source):
            ch = self.source[self.pos]
            if ch == '\\':
                self.advance()
                if self.pos >= len(self.source):
                    break
                esc = self.advance()
                escape_map = {'n': '\n', 't': '\t', 'r': '\r', '\\': '\\', '"': '"', "'": "'"}
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

    def read_number(self):
        start = self.pos
        is_float = False
        while self.pos < len(self.source) and (self.source[self.pos].isdigit() or self.source[self.pos] == '.'):
            if self.source[self.pos] == '.':
                if is_float:
                    break
                if self.pos + 1 < len(self.source) and self.source[self.pos + 1].isdigit():
                    is_float = True
                else:
                    break
            self.pos += 1
            self.col += 1
        text = self.source[start:self.pos]
        if is_float:
            self.add_token(TokenType.FLOAT, float(text))
        else:
            self.add_token(TokenType.INT, int(text))

    def read_identifier(self):
        start = self.pos
        while self.pos < len(self.source) and (self.source[self.pos].isalnum() or self.source[self.pos] == '_'):
            self.pos += 1
            self.col += 1
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

    def tokenize(self) -> list:
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
            elif ch.isalpha() or ch == '_':
                self.read_identifier()
            elif ch == '+':
                self.advance()
                if self.peek() == '=' and self.pos < len(self.source):
                    # check previous char was already consumed
                    if self.source[self.pos] == '=':
                        self.advance()
                        self.add_token(TokenType.PLUS_ASSIGN)
                    else:
                        self.add_token(TokenType.PLUS)
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
                if self.pos < len(self.source) and self.source[self.pos] == '=':
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
                self.advance()
                self.add_token(TokenType.DOT)
            else:
                raise LexerError(f"Unexpected character '{ch}'", self.line, self.col)

        self.add_token(TokenType.EOF)
        return self.tokens


# ═══════════════════════════════════════════════════════════
# AST NODES
# ═══════════════════════════════════════════════════════════

@dataclass
class NumberLiteral:
    value: float | int

@dataclass
class StringLiteral:
    value: str

@dataclass
class BoolLiteral:
    value: bool

@dataclass
class NullLiteral:
    pass

@dataclass
class ArrayLiteral:
    elements: list

@dataclass
class Identifier:
    name: str

@dataclass
class BinaryOp:
    left: Any
    op: str
    right: Any

@dataclass
class UnaryOp:
    op: str
    operand: Any

@dataclass
class Assignment:
    name: str
    value: Any

@dataclass
class CompoundAssignment:
    name: str
    op: str
    value: Any

@dataclass
class LetDeclaration:
    name: str
    mutable: bool
    type_hint: str | None
    value: Any

@dataclass
class IfStatement:
    condition: Any
    body: list
    elif_branches: list  # list of (condition, body)
    else_body: list | None

@dataclass
class WhileLoop:
    condition: Any
    body: list

@dataclass
class ForLoop:
    var_name: str
    iterable: Any
    body: list

@dataclass
class FunctionDef:
    name: str
    params: list  # list of (name, type_hint)
    return_type: str | None
    body: list

@dataclass
class FunctionCall:
    name: Any  # can be Identifier or MemberAccess
    args: list

@dataclass
class ReturnStatement:
    value: Any

@dataclass
class BreakStatement:
    pass

@dataclass
class ContinueStatement:
    pass

@dataclass
class IndexAccess:
    obj: Any
    index: Any

@dataclass
class IndexAssign:
    obj: Any
    index: Any
    value: Any

@dataclass
class MemberAccess:
    obj: Any
    member: str

@dataclass
class Program:
    statements: list


# ═══════════════════════════════════════════════════════════
# PARSER
# ═══════════════════════════════════════════════════════════

class Parser:
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.pos = 0

    def current(self) -> Token:
        return self.tokens[self.pos]

    def peek(self, offset=1) -> Token:
        idx = self.pos + offset
        if idx < len(self.tokens):
            return self.tokens[idx]
        return self.tokens[-1]

    def eat(self, type_: TokenType) -> Token:
        token = self.current()
        if token.type != type_:
            raise ParseError(
                f"Expected {type_.name}, got {token.type.name} ({token.value!r})",
                token.line, token.col
            )
        self.pos += 1
        return token

    def skip_newlines(self):
        while self.pos < len(self.tokens) and self.current().type == TokenType.NEWLINE:
            self.pos += 1

    def match(self, *types) -> bool:
        return self.current().type in types

    def parse(self) -> Program:
        statements = []
        self.skip_newlines()
        while not self.match(TokenType.EOF):
            stmt = self.parse_statement()
            if stmt is not None:
                statements.append(stmt)
            self.skip_newlines()
        return Program(statements)

    def parse_statement(self):
        self.skip_newlines()
        t = self.current()

        if t.type == TokenType.LET:
            return self.parse_let()
        elif t.type == TokenType.FN:
            return self.parse_function_def()
        elif t.type == TokenType.IF:
            return self.parse_if()
        elif t.type == TokenType.WHILE:
            return self.parse_while()
        elif t.type == TokenType.FOR:
            return self.parse_for()
        elif t.type == TokenType.RETURN:
            return self.parse_return()
        elif t.type == TokenType.BREAK:
            self.pos += 1
            return BreakStatement()
        elif t.type == TokenType.CONTINUE:
            self.pos += 1
            return ContinueStatement()
        else:
            return self.parse_expression_statement()

    def parse_let(self):
        self.eat(TokenType.LET)
        mutable = False
        if self.match(TokenType.MUT):
            self.eat(TokenType.MUT)
            mutable = True

        name = self.eat(TokenType.IDENTIFIER).value
        type_hint = None

        if self.match(TokenType.COLON):
            self.eat(TokenType.COLON)
            type_hint = self.current().value
            self.pos += 1

        self.eat(TokenType.ASSIGN)
        value = self.parse_expression()
        return LetDeclaration(name, mutable, type_hint, value)

    def parse_function_def(self):
        self.eat(TokenType.FN)
        name = self.eat(TokenType.IDENTIFIER).value
        self.eat(TokenType.LPAREN)

        params = []
        while not self.match(TokenType.RPAREN):
            pname = self.eat(TokenType.IDENTIFIER).value
            ptype = None
            if self.match(TokenType.COLON):
                self.eat(TokenType.COLON)
                ptype = self.current().value
                self.pos += 1
            params.append((pname, ptype))
            if self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)

        self.eat(TokenType.RPAREN)

        return_type = None
        if self.match(TokenType.ARROW):
            self.eat(TokenType.ARROW)
            return_type = self.current().value
            self.pos += 1

        body = self.parse_block()
        return FunctionDef(name, params, return_type, body)

    def parse_if(self):
        self.eat(TokenType.IF)
        condition = self.parse_expression()
        body = self.parse_block()

        elif_branches = []
        else_body = None

        self.skip_newlines()
        while self.match(TokenType.ELIF):
            self.eat(TokenType.ELIF)
            elif_cond = self.parse_expression()
            elif_body = self.parse_block()
            elif_branches.append((elif_cond, elif_body))
            self.skip_newlines()

        if self.match(TokenType.ELSE):
            self.eat(TokenType.ELSE)
            else_body = self.parse_block()

        return IfStatement(condition, body, elif_branches, else_body)

    def parse_while(self):
        self.eat(TokenType.WHILE)
        condition = self.parse_expression()
        body = self.parse_block()
        return WhileLoop(condition, body)

    def parse_for(self):
        self.eat(TokenType.FOR)
        var_name = self.eat(TokenType.IDENTIFIER).value
        self.eat(TokenType.IN)
        iterable = self.parse_expression()
        body = self.parse_block()
        return ForLoop(var_name, iterable, body)

    def parse_return(self):
        self.eat(TokenType.RETURN)
        value = None
        if not self.match(TokenType.NEWLINE, TokenType.EOF, TokenType.RBRACE):
            value = self.parse_expression()
        return ReturnStatement(value)

    def parse_block(self) -> list:
        self.skip_newlines()
        self.eat(TokenType.LBRACE)
        statements = []
        self.skip_newlines()
        while not self.match(TokenType.RBRACE):
            stmt = self.parse_statement()
            if stmt is not None:
                statements.append(stmt)
            self.skip_newlines()
        self.eat(TokenType.RBRACE)
        return statements

    def parse_expression_statement(self):
        expr = self.parse_expression()

        # Check for assignment
        if isinstance(expr, Identifier) and self.match(TokenType.ASSIGN):
            self.eat(TokenType.ASSIGN)
            value = self.parse_expression()
            return Assignment(expr.name, value)

        # Compound assignment
        if isinstance(expr, Identifier) and self.match(
            TokenType.PLUS_ASSIGN, TokenType.MINUS_ASSIGN,
            TokenType.STAR_ASSIGN, TokenType.SLASH_ASSIGN
        ):
            op_map = {
                TokenType.PLUS_ASSIGN: '+',
                TokenType.MINUS_ASSIGN: '-',
                TokenType.STAR_ASSIGN: '*',
                TokenType.SLASH_ASSIGN: '/',
            }
            op = op_map[self.current().type]
            self.pos += 1
            value = self.parse_expression()
            return CompoundAssignment(expr.name, op, value)

        # Index assignment: arr[i] = val
        if isinstance(expr, IndexAccess) and self.match(TokenType.ASSIGN):
            self.eat(TokenType.ASSIGN)
            value = self.parse_expression()
            return IndexAssign(expr.obj, expr.index, value)

        return expr

    # ─── Expression parsing (precedence climbing) ───

    def parse_expression(self):
        return self.parse_or()

    def parse_or(self):
        left = self.parse_and()
        while self.match(TokenType.OR):
            self.pos += 1
            right = self.parse_and()
            left = BinaryOp(left, 'or', right)
        return left

    def parse_and(self):
        left = self.parse_not()
        while self.match(TokenType.AND):
            self.pos += 1
            right = self.parse_not()
            left = BinaryOp(left, 'and', right)
        return left

    def parse_not(self):
        if self.match(TokenType.NOT):
            self.pos += 1
            operand = self.parse_not()
            return UnaryOp('not', operand)
        return self.parse_comparison()

    def parse_comparison(self):
        left = self.parse_addition()
        while self.match(TokenType.EQ, TokenType.NEQ, TokenType.LT, TokenType.GT, TokenType.LTE, TokenType.GTE):
            op_map = {
                TokenType.EQ: '==', TokenType.NEQ: '!=',
                TokenType.LT: '<', TokenType.GT: '>',
                TokenType.LTE: '<=', TokenType.GTE: '>=',
            }
            op = op_map[self.current().type]
            self.pos += 1
            right = self.parse_addition()
            left = BinaryOp(left, op, right)
        return left

    def parse_addition(self):
        left = self.parse_multiplication()
        while self.match(TokenType.PLUS, TokenType.MINUS):
            op = '+' if self.current().type == TokenType.PLUS else '-'
            self.pos += 1
            right = self.parse_multiplication()
            left = BinaryOp(left, op, right)
        return left

    def parse_multiplication(self):
        left = self.parse_power()
        while self.match(TokenType.STAR, TokenType.SLASH, TokenType.PERCENT):
            op_map = {TokenType.STAR: '*', TokenType.SLASH: '/', TokenType.PERCENT: '%'}
            op = op_map[self.current().type]
            self.pos += 1
            right = self.parse_power()
            left = BinaryOp(left, op, right)
        return left

    def parse_power(self):
        left = self.parse_unary()
        if self.match(TokenType.POWER):
            self.pos += 1
            right = self.parse_power()  # right-associative
            left = BinaryOp(left, '**', right)
        return left

    def parse_unary(self):
        if self.match(TokenType.MINUS):
            self.pos += 1
            operand = self.parse_unary()
            return UnaryOp('-', operand)
        return self.parse_postfix()

    def parse_postfix(self):
        expr = self.parse_primary()
        while True:
            if self.match(TokenType.LPAREN):
                # Function call
                self.eat(TokenType.LPAREN)
                args = []
                while not self.match(TokenType.RPAREN):
                    args.append(self.parse_expression())
                    if self.match(TokenType.COMMA):
                        self.eat(TokenType.COMMA)
                self.eat(TokenType.RPAREN)
                expr = FunctionCall(expr, args)
            elif self.match(TokenType.LBRACKET):
                # Index access
                self.eat(TokenType.LBRACKET)
                index = self.parse_expression()
                self.eat(TokenType.RBRACKET)
                expr = IndexAccess(expr, index)
            elif self.match(TokenType.DOT):
                # Member access
                self.eat(TokenType.DOT)
                member = self.eat(TokenType.IDENTIFIER).value
                expr = MemberAccess(expr, member)
            else:
                break
        return expr

    def parse_primary(self):
        t = self.current()

        if t.type == TokenType.INT:
            self.pos += 1
            return NumberLiteral(t.value)
        elif t.type == TokenType.FLOAT:
            self.pos += 1
            return NumberLiteral(t.value)
        elif t.type == TokenType.STRING:
            self.pos += 1
            return StringLiteral(t.value)
        elif t.type == TokenType.BOOL:
            self.pos += 1
            return BoolLiteral(t.value)
        elif t.type == TokenType.NULL:
            self.pos += 1
            return NullLiteral()
        elif t.type == TokenType.IDENTIFIER:
            self.pos += 1
            return Identifier(t.value)
        elif t.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            expr = self.parse_expression()
            self.eat(TokenType.RPAREN)
            return expr
        elif t.type == TokenType.LBRACKET:
            return self.parse_array_literal()
        else:
            raise ParseError(f"Unexpected token: {t.type.name} ({t.value!r})", t.line, t.col)

    def parse_array_literal(self):
        self.eat(TokenType.LBRACKET)
        elements = []
        while not self.match(TokenType.RBRACKET):
            elements.append(self.parse_expression())
            if self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)
        self.eat(TokenType.RBRACKET)
        return ArrayLiteral(elements)


# ═══════════════════════════════════════════════════════════
# ENVIRONMENT (Variable Scope)
# ═══════════════════════════════════════════════════════════

class Environment:
    def __init__(self, parent=None):
        self.variables = {}
        self.mutability = {}  # track which vars are mutable
        self.parent = parent

    def define(self, name: str, value: Any, mutable: bool = True):
        self.variables[name] = value
        self.mutability[name] = mutable

    def get(self, name: str) -> Any:
        if name in self.variables:
            return self.variables[name]
        if self.parent:
            return self.parent.get(name)
        raise RuntimeError_(f"Undefined variable: '{name}'")

    def set(self, name: str, value: Any):
        if name in self.variables:
            if not self.mutability.get(name, True):
                raise RuntimeError_(f"Cannot reassign immutable variable '{name}'. Use 'let mut' for mutable variables.")
            self.variables[name] = value
            return
        if self.parent:
            self.parent.set(name, value)
            return
        raise RuntimeError_(f"Undefined variable: '{name}'")

    def exists(self, name: str) -> bool:
        if name in self.variables:
            return True
        if self.parent:
            return self.parent.exists(name)
        return False


# ═══════════════════════════════════════════════════════════
# SIGNALS FOR CONTROL FLOW
# ═══════════════════════════════════════════════════════════

class ReturnSignal(Exception):
    def __init__(self, value):
        self.value = value

class BreakSignal(Exception):
    pass

class ContinueSignal(Exception):
    pass


# ═══════════════════════════════════════════════════════════
# INTERPRETER
# ═══════════════════════════════════════════════════════════

class Interpreter:
    def __init__(self):
        self.global_env = Environment()
        self.output_lines = []  # capture output for testing
        self._setup_builtins()

    def _setup_builtins(self):
        """Register all built-in functions."""
        builtins = {
            # I/O
            'print': self._builtin_print,
            'input': self._builtin_input,
            'type': self._builtin_type,
            'str': self._builtin_str,

            # Type conversions
            'int': self._builtin_int,
            'float': self._builtin_float,
            'bool': self._builtin_bool,

            # Collections
            'len': self._builtin_len,
            'range': self._builtin_range,
            'push': self._builtin_push,
            'pop': self._builtin_pop,
            'slice': self._builtin_slice,
            'reverse': self._builtin_reverse,
            'sort': self._builtin_sort,
            'map': self._builtin_map,
            'filter': self._builtin_filter,
            'join': self._builtin_join,
            'split': self._builtin_split,
            'contains': self._builtin_contains,

            # Math
            'abs': lambda args: abs(args[0]),
            'round': lambda args: round(args[0], int(args[1])) if len(args) > 1 else round(args[0]),
            'min': lambda args: min(args[0]) if len(args) == 1 and isinstance(args[0], list) else min(args),
            'max': lambda args: max(args[0]) if len(args) == 1 and isinstance(args[0], list) else max(args),
            'sum': lambda args: sum(args[0]) if isinstance(args[0], list) else sum(args),
            'sqrt': lambda args: math.sqrt(args[0]),
            'pow': lambda args: math.pow(args[0], args[1]),
            'log': lambda args: math.log(args[0], args[1]) if len(args) > 1 else math.log(args[0]),
            'log10': lambda args: math.log10(args[0]),
            'sin': lambda args: math.sin(args[0]),
            'cos': lambda args: math.cos(args[0]),
            'tan': lambda args: math.tan(args[0]),
            'pi': lambda args: math.pi,
            'ceil': lambda args: math.ceil(args[0]),
            'floor': lambda args: math.floor(args[0]),

            # Medical/Scientific helpers
            'bmi': lambda args: round(args[0] / (args[1] ** 2), 2),  # bmi(weight_kg, height_m)
            'bsa': lambda args: round(0.007184 * (args[0] ** 0.425) * (args[1] ** 0.725), 2),  # bsa(weight_kg, height_cm) Du Bois
            'dose_per_kg': lambda args: round(args[0] * args[1], 2),  # dose_per_kg(mg_per_kg, weight_kg)
            'fahrenheit_to_celsius': lambda args: round((args[0] - 32) * 5 / 9, 2),
            'celsius_to_fahrenheit': lambda args: round(args[0] * 9 / 5 + 32, 2),
            'ideal_body_weight': lambda args: round(  # ibw(height_cm, is_male: bool)
                50 + 0.91 * (args[0] - 152.4) if args[1] else 45.5 + 0.91 * (args[0] - 152.4), 1
            ),
            'mean': lambda args: round(sum(args[0]) / len(args[0]), 4) if isinstance(args[0], list) else None,
            'median': lambda args: _median(args[0]) if isinstance(args[0], list) else None,
            'stdev': lambda args: _stdev(args[0]) if isinstance(args[0], list) else None,
        }

        for name, func in builtins.items():
            self.global_env.define(name, ('builtin', func), mutable=False)

    # ─── Built-in function implementations ───

    def _builtin_print(self, args):
        output = ' '.join(silk_repr(a) for a in args)
        print(output)
        self.output_lines.append(output)
        return None

    def _builtin_input(self, args):
        prompt = args[0] if args else ""
        return input(silk_repr(prompt) if prompt else "")

    def _builtin_type(self, args):
        v = args[0]
        if isinstance(v, bool):
            return "bool"
        elif isinstance(v, int):
            return "int"
        elif isinstance(v, float):
            return "float"
        elif isinstance(v, str):
            return "str"
        elif isinstance(v, list):
            return "array"
        elif v is None:
            return "null"
        elif isinstance(v, tuple) and v[0] in ('function', 'builtin'):
            return "function"
        return "unknown"

    def _builtin_str(self, args):
        return silk_repr(args[0])

    def _builtin_int(self, args):
        return int(args[0])

    def _builtin_float(self, args):
        return float(args[0])

    def _builtin_bool(self, args):
        return bool(args[0])

    def _builtin_len(self, args):
        v = args[0]
        if isinstance(v, (str, list)):
            return len(v)
        raise RuntimeError_(f"len() expects string or array, got {type(v).__name__}")

    def _builtin_range(self, args):
        if len(args) == 1:
            return list(range(int(args[0])))
        elif len(args) == 2:
            return list(range(int(args[0]), int(args[1])))
        elif len(args) == 3:
            return list(range(int(args[0]), int(args[1]), int(args[2])))
        raise RuntimeError_("range() takes 1 to 3 arguments")

    def _builtin_push(self, args):
        if not isinstance(args[0], list):
            raise RuntimeError_("push() expects an array as first argument")
        args[0].append(args[1])
        return args[0]

    def _builtin_pop(self, args):
        if not isinstance(args[0], list):
            raise RuntimeError_("pop() expects an array")
        return args[0].pop()

    def _builtin_slice(self, args):
        arr = args[0]
        start = int(args[1]) if len(args) > 1 else 0
        end = int(args[2]) if len(args) > 2 else len(arr)
        return arr[start:end]

    def _builtin_reverse(self, args):
        if isinstance(args[0], list):
            return args[0][::-1]
        elif isinstance(args[0], str):
            return args[0][::-1]
        raise RuntimeError_("reverse() expects array or string")

    def _builtin_sort(self, args):
        if not isinstance(args[0], list):
            raise RuntimeError_("sort() expects an array")
        return sorted(args[0])

    def _builtin_map(self, args):
        fn, arr = args[0], args[1]
        if not isinstance(arr, list):
            raise RuntimeError_("map() second arg must be an array")
        return [self._call_function(fn, [item]) for item in arr]

    def _builtin_filter(self, args):
        fn, arr = args[0], args[1]
        if not isinstance(arr, list):
            raise RuntimeError_("filter() second arg must be an array")
        return [item for item in arr if self._call_function(fn, [item])]

    def _builtin_join(self, args):
        arr = args[0]
        sep = args[1] if len(args) > 1 else ""
        if not isinstance(arr, list):
            raise RuntimeError_("join() expects an array as first argument")
        return sep.join(silk_repr(item) for item in arr)

    def _builtin_split(self, args):
        s = args[0]
        sep = args[1] if len(args) > 1 else " "
        if not isinstance(s, str):
            raise RuntimeError_("split() expects a string")
        return s.split(sep)

    def _builtin_contains(self, args):
        collection, item = args[0], args[1]
        return item in collection

    def _call_function(self, func, args):
        if isinstance(func, tuple):
            if func[0] == 'builtin':
                return func[1](args)
            elif func[0] == 'function':
                _, params, body, closure_env = func
                fn_env = Environment(parent=closure_env)
                for (pname, _), arg in zip(params, args):
                    fn_env.define(pname, arg)
                try:
                    self.execute_block(body, fn_env)
                except ReturnSignal as r:
                    return r.value
                return None
        raise RuntimeError_("Not a callable function")

    # ─── Main execution ───

    def run(self, source: str):
        try:
            lexer = Lexer(source)
            tokens = lexer.tokenize()
            parser = Parser(tokens)
            ast = parser.parse()
            self.execute(ast, self.global_env)
        except (LexerError, ParseError, RuntimeError_) as e:
            print(f"\n❌ Silk Error: {e}")
            return False
        return True

    def execute(self, node, env: Environment):
        if isinstance(node, Program):
            for stmt in node.statements:
                self.execute(stmt, env)

        elif isinstance(node, LetDeclaration):
            value = self.evaluate(node.value, env)
            env.define(node.name, value, mutable=node.mutable)

        elif isinstance(node, Assignment):
            value = self.evaluate(node.value, env)
            env.set(node.name, value)

        elif isinstance(node, CompoundAssignment):
            current = env.get(node.name)
            right = self.evaluate(node.value, env)
            ops = {'+': lambda a, b: a + b, '-': lambda a, b: a - b,
                   '*': lambda a, b: a * b, '/': lambda a, b: a / b}
            env.set(node.name, ops[node.op](current, right))

        elif isinstance(node, IndexAssign):
            obj = self.evaluate(node.obj, env)
            idx = self.evaluate(node.index, env)
            val = self.evaluate(node.value, env)
            if isinstance(obj, list):
                obj[int(idx)] = val
            else:
                raise RuntimeError_("Index assignment only works on arrays")

        elif isinstance(node, IfStatement):
            cond = self.evaluate(node.condition, env)
            if _truthy(cond):
                self.execute_block(node.body, Environment(parent=env))
            else:
                matched = False
                for elif_cond, elif_body in node.elif_branches:
                    if _truthy(self.evaluate(elif_cond, env)):
                        self.execute_block(elif_body, Environment(parent=env))
                        matched = True
                        break
                if not matched and node.else_body:
                    self.execute_block(node.else_body, Environment(parent=env))

        elif isinstance(node, WhileLoop):
            while _truthy(self.evaluate(node.condition, env)):
                try:
                    self.execute_block(node.body, Environment(parent=env))
                except BreakSignal:
                    break
                except ContinueSignal:
                    continue

        elif isinstance(node, ForLoop):
            iterable = self.evaluate(node.iterable, env)
            if not isinstance(iterable, list):
                raise RuntimeError_("for..in requires an iterable (array or range)")
            for item in iterable:
                loop_env = Environment(parent=env)
                loop_env.define(node.var_name, item)
                try:
                    self.execute_block(node.body, loop_env)
                except BreakSignal:
                    break
                except ContinueSignal:
                    continue

        elif isinstance(node, FunctionDef):
            func = ('function', node.params, node.body, env)
            env.define(node.name, func, mutable=False)

        elif isinstance(node, ReturnStatement):
            value = self.evaluate(node.value, env) if node.value else None
            raise ReturnSignal(value)

        elif isinstance(node, BreakStatement):
            raise BreakSignal()

        elif isinstance(node, ContinueStatement):
            raise ContinueSignal()

        else:
            # Expression statement
            self.evaluate(node, env)

    def execute_block(self, statements, env):
        for stmt in statements:
            self.execute(stmt, env)

    def evaluate(self, node, env: Environment) -> Any:
        if isinstance(node, NumberLiteral):
            return node.value
        elif isinstance(node, StringLiteral):
            return node.value
        elif isinstance(node, BoolLiteral):
            return node.value
        elif isinstance(node, NullLiteral):
            return None
        elif isinstance(node, ArrayLiteral):
            return [self.evaluate(el, env) for el in node.elements]
        elif isinstance(node, Identifier):
            return env.get(node.name)
        elif isinstance(node, BinaryOp):
            return self._eval_binary(node, env)
        elif isinstance(node, UnaryOp):
            return self._eval_unary(node, env)
        elif isinstance(node, FunctionCall):
            return self._eval_call(node, env)
        elif isinstance(node, IndexAccess):
            obj = self.evaluate(node.obj, env)
            idx = self.evaluate(node.index, env)
            if isinstance(obj, list):
                return obj[int(idx)]
            elif isinstance(obj, str):
                return obj[int(idx)]
            raise RuntimeError_(f"Cannot index into {type(obj).__name__}")
        elif isinstance(node, MemberAccess):
            obj = self.evaluate(node.obj, env)
            return self._eval_member(obj, node.member)
        else:
            raise RuntimeError_(f"Unknown AST node: {type(node).__name__}")

    def _eval_binary(self, node: BinaryOp, env) -> Any:
        left = self.evaluate(node.left, env)
        # Short-circuit for logical operators
        if node.op == 'and':
            return left if not _truthy(left) else self.evaluate(node.right, env)
        if node.op == 'or':
            return left if _truthy(left) else self.evaluate(node.right, env)

        right = self.evaluate(node.right, env)

        ops = {
            '+': lambda: left + right,
            '-': lambda: left - right,
            '*': lambda: _multiply(left, right),
            '/': lambda: _divide(left, right),
            '%': lambda: left % right,
            '**': lambda: left ** right,
            '==': lambda: left == right,
            '!=': lambda: left != right,
            '<': lambda: left < right,
            '>': lambda: left > right,
            '<=': lambda: left <= right,
            '>=': lambda: left >= right,
        }

        if node.op in ops:
            try:
                return ops[node.op]()
            except TypeError:
                raise RuntimeError_(
                    f"Cannot apply '{node.op}' to {type(left).__name__} and {type(right).__name__}"
                )
        raise RuntimeError_(f"Unknown operator: {node.op}")

    def _eval_unary(self, node: UnaryOp, env) -> Any:
        val = self.evaluate(node.operand, env)
        if node.op == '-':
            return -val
        if node.op == 'not':
            return not _truthy(val)
        raise RuntimeError_(f"Unknown unary operator: {node.op}")

    def _eval_call(self, node: FunctionCall, env) -> Any:
        args = [self.evaluate(a, env) for a in node.args]

        if isinstance(node.name, Identifier):
            func = env.get(node.name.name)
        elif isinstance(node.name, MemberAccess):
            # method-style call: obj.method(args)
            obj = self.evaluate(node.name.obj, env)
            return self._eval_method(obj, node.name.member, args)
        else:
            func = self.evaluate(node.name, env)

        return self._call_function(func, args)

    def _eval_member(self, obj, member):
        """Handle member access like arr.length, str.upper, etc."""
        if isinstance(obj, list):
            if member == 'length':
                return len(obj)
        elif isinstance(obj, str):
            if member == 'length':
                return len(obj)
            if member == 'upper':
                return ('builtin', lambda args: obj.upper())
            if member == 'lower':
                return ('builtin', lambda args: obj.lower())
            if member == 'strip':
                return ('builtin', lambda args: obj.strip())
            if member == 'replace':
                return ('builtin', lambda args: obj.replace(args[0], args[1]))
            if member == 'starts_with':
                return ('builtin', lambda args: obj.startswith(args[0]))
            if member == 'ends_with':
                return ('builtin', lambda args: obj.endswith(args[0]))
        raise RuntimeError_(f"'{type(obj).__name__}' has no member '{member}'")

    def _eval_method(self, obj, method, args):
        """Handle method calls like obj.method(args)."""
        member = self._eval_member(obj, method)
        if isinstance(member, tuple) and member[0] == 'builtin':
            return member[1](args)
        return member


# ═══════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════

def _truthy(value) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return len(value) > 0
    if isinstance(value, list):
        return len(value) > 0
    return True

def _multiply(left, right):
    if isinstance(left, str) and isinstance(right, int):
        return left * right
    if isinstance(left, int) and isinstance(right, str):
        return right * left
    return left * right

def _divide(left, right):
    if right == 0:
        raise RuntimeError_("Division by zero")
    if isinstance(left, int) and isinstance(right, int):
        result = left / right
        return int(result) if result == int(result) else result
    return left / right

def _median(arr):
    s = sorted(arr)
    n = len(s)
    if n % 2 == 1:
        return s[n // 2]
    return (s[n // 2 - 1] + s[n // 2]) / 2

def _stdev(arr):
    n = len(arr)
    if n < 2:
        return 0.0
    m = sum(arr) / n
    variance = sum((x - m) ** 2 for x in arr) / (n - 1)
    return round(math.sqrt(variance), 4)

def silk_repr(value) -> str:
    """Convert a Silk value to its string representation."""
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, float):
        if value == int(value):
            return str(int(value))
        return str(value)
    if isinstance(value, list):
        items = ', '.join(silk_repr(item) for item in value)
        return f"[{items}]"
    if isinstance(value, tuple) and len(value) >= 1:
        if value[0] == 'function':
            return "<function>"
        if value[0] == 'builtin':
            return "<builtin>"
    return str(value)


# ═══════════════════════════════════════════════════════════
# REPL (Interactive Mode)
# ═══════════════════════════════════════════════════════════

SILK_BANNER = """
\033[96m╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ╔═╗╦╦  ╦╔═  ╦  ╔═╗╔╗╔╔═╗                                 ║
║   ╚═╗║║  ╠╩╗  ║  ╠═╣║║║║ ╦                                  ║
║   ╚═╝╩╩═╝╩ ╩  ╩═╝╩ ╩╝╚╝╚═╝  v0.1.0                        ║
║                                                              ║
║   Simple • Intuitive • Lightweight • Keen                    ║
║   Type 'help' for commands, 'exit' to quit                   ║
╚══════════════════════════════════════════════════════════════╝\033[0m
"""

HELP_TEXT = """
\033[93m━━━ Silk Language Quick Reference ━━━\033[0m

\033[96mVariables:\033[0m
  let name = "Silk"          // immutable
  let mut count = 0          // mutable
  count = count + 1

\033[96mFunctions:\033[0m
  fn greet(name: str) -> str {
      return "Hello, " + name
  }

\033[96mControl Flow:\033[0m
  if x > 0 { ... }
  elif x == 0 { ... }
  else { ... }

  while condition { ... }

  for i in range(10) { ... }
  for item in array { ... }

\033[96mData Types:\033[0m
  42, 3.14              // numbers
  "hello"               // string
  true, false           // booleans
  [1, 2, 3]             // array
  null                  // null

\033[96mBuilt-in Functions:\033[0m
  print(x)              // output
  len(arr), range(n)    // collections
  sqrt(x), abs(x)       // math
  type(x), str(x)       // conversion
  push(arr, item)       // array ops
  sort(arr), reverse(arr)

\033[96mMedical Functions:\033[0m
  bmi(weight_kg, height_m)
  bsa(weight_kg, height_cm)
  dose_per_kg(mg_per_kg, weight_kg)
  ideal_body_weight(height_cm, is_male)
  mean(arr), median(arr), stdev(arr)

\033[96mREPL Commands:\033[0m
  help     - Show this help
  clear    - Clear screen
  exit     - Exit REPL
"""


def repl():
    """Start the interactive REPL."""
    print(SILK_BANNER)
    interpreter = Interpreter()
    buffer = []
    brace_depth = 0

    while True:
        try:
            prompt = "\033[92msilk>\033[0m " if not buffer else "\033[90m  ...\033[0m "
            line = input(prompt)

            # REPL commands
            stripped = line.strip()
            if not buffer:
                if stripped == 'exit' or stripped == 'quit':
                    print("\033[96m👋 Goodbye!\033[0m")
                    break
                if stripped == 'help':
                    print(HELP_TEXT)
                    continue
                if stripped == 'clear':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(SILK_BANNER)
                    continue
                if stripped == '':
                    continue

            buffer.append(line)
            brace_depth += line.count('{') - line.count('}')

            if brace_depth <= 0:
                source = '\n'.join(buffer)
                buffer = []
                brace_depth = 0

                # For single expressions, print the result
                try:
                    lexer = Lexer(source)
                    tokens = lexer.tokenize()
                    parser = Parser(tokens)
                    ast = parser.parse()

                    if (len(ast.statements) == 1 and
                        not isinstance(ast.statements[0], (LetDeclaration, Assignment,
                            CompoundAssignment, IfStatement, WhileLoop, ForLoop,
                            FunctionDef, ReturnStatement))):
                        result = interpreter.evaluate(ast.statements[0], interpreter.global_env)
                        if result is not None:
                            print(f"\033[93m→ {silk_repr(result)}\033[0m")
                    else:
                        interpreter.execute(ast, interpreter.global_env)

                except (LexerError, ParseError, RuntimeError_) as e:
                    print(f"\033[91m❌ {e}\033[0m")

        except KeyboardInterrupt:
            print("\n\033[96m(Use 'exit' to quit)\033[0m")
            buffer = []
            brace_depth = 0
        except EOFError:
            print("\n\033[96m👋 Goodbye!\033[0m")
            break


# ═══════════════════════════════════════════════════════════
# MAIN ENTRY POINT
# ═══════════════════════════════════════════════════════════

def main():
    if len(sys.argv) < 2:
        repl()
    else:
        filepath = sys.argv[1]
        if not os.path.exists(filepath):
            print(f"❌ File not found: {filepath}")
            sys.exit(1)

        with open(filepath, 'r', encoding='utf-8') as f:
            source = f.read()

        interpreter = Interpreter()
        success = interpreter.run(source)
        if not success:
            sys.exit(1)


if __name__ == '__main__':
    main()
