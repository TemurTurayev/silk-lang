"""
Parser Tests

Tests for the Silk parser, verifying AST construction.
"""

import pytest
from silk.lexer import Lexer
from silk.parser import Parser
from silk.ast import (
    Program, NumberLiteral, StringLiteral, BoolLiteral, NullLiteral,
    ArrayLiteral, Identifier, BinaryOp, UnaryOp, Assignment,
    CompoundAssignment, LetDeclaration, IfStatement, WhileLoop,
    ForLoop, FunctionDef, FunctionCall, ReturnStatement,
    BreakStatement, ContinueStatement, IndexAccess, MemberAccess
)
from silk.errors import ParseError


def parse(source: str) -> Program:
    """Helper to parse source code."""
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    return parser.parse()


class TestLiterals:
    """Test literal parsing."""

    def test_integer(self):
        ast = parse("42")
        assert len(ast.statements) == 1
        assert isinstance(ast.statements[0], NumberLiteral)
        assert ast.statements[0].value == 42

    def test_float(self):
        ast = parse("3.14")
        assert len(ast.statements) == 1
        assert isinstance(ast.statements[0], NumberLiteral)
        assert ast.statements[0].value == 3.14

    def test_string(self):
        ast = parse('"hello"')
        assert len(ast.statements) == 1
        assert isinstance(ast.statements[0], StringLiteral)
        assert ast.statements[0].value == "hello"

    def test_true(self):
        ast = parse("true")
        assert isinstance(ast.statements[0], BoolLiteral)
        assert ast.statements[0].value is True

    def test_false(self):
        ast = parse("false")
        assert isinstance(ast.statements[0], BoolLiteral)
        assert ast.statements[0].value is False

    def test_null(self):
        ast = parse("null")
        assert isinstance(ast.statements[0], NullLiteral)

    def test_array_empty(self):
        ast = parse("[]")
        assert isinstance(ast.statements[0], ArrayLiteral)
        assert ast.statements[0].elements == []

    def test_array_with_elements(self):
        ast = parse("[1, 2, 3]")
        arr = ast.statements[0]
        assert isinstance(arr, ArrayLiteral)
        assert len(arr.elements) == 3


class TestExpressions:
    """Test expression parsing."""

    def test_binary_add(self):
        ast = parse("1 + 2")
        expr = ast.statements[0]
        assert isinstance(expr, BinaryOp)
        assert expr.op == '+'

    def test_binary_precedence(self):
        ast = parse("1 + 2 * 3")
        expr = ast.statements[0]
        assert isinstance(expr, BinaryOp)
        assert expr.op == '+'
        assert isinstance(expr.right, BinaryOp)
        assert expr.right.op == '*'

    def test_parentheses(self):
        ast = parse("(1 + 2) * 3")
        expr = ast.statements[0]
        assert isinstance(expr, BinaryOp)
        assert expr.op == '*'
        assert isinstance(expr.left, BinaryOp)
        assert expr.left.op == '+'

    def test_power_right_associative(self):
        ast = parse("2 ** 3 ** 2")
        expr = ast.statements[0]
        assert isinstance(expr, BinaryOp)
        assert expr.op == '**'
        assert isinstance(expr.right, BinaryOp)
        assert expr.right.op == '**'

    def test_unary_minus(self):
        ast = parse("-5")
        expr = ast.statements[0]
        assert isinstance(expr, UnaryOp)
        assert expr.op == '-'

    def test_unary_not(self):
        ast = parse("not true")
        expr = ast.statements[0]
        assert isinstance(expr, UnaryOp)
        assert expr.op == 'not'

    def test_comparison(self):
        ast = parse("1 < 2")
        expr = ast.statements[0]
        assert isinstance(expr, BinaryOp)
        assert expr.op == '<'

    def test_logical_and(self):
        ast = parse("true and false")
        expr = ast.statements[0]
        assert isinstance(expr, BinaryOp)
        assert expr.op == 'and'

    def test_logical_or(self):
        ast = parse("true or false")
        expr = ast.statements[0]
        assert isinstance(expr, BinaryOp)
        assert expr.op == 'or'


class TestDeclarations:
    """Test declaration parsing."""

    def test_let_immutable(self):
        ast = parse("let x = 5")
        decl = ast.statements[0]
        assert isinstance(decl, LetDeclaration)
        assert decl.name == 'x'
        assert decl.mutable is False

    def test_let_mutable(self):
        ast = parse("let mut x = 5")
        decl = ast.statements[0]
        assert isinstance(decl, LetDeclaration)
        assert decl.mutable is True

    def test_let_with_type(self):
        ast = parse("let x: int = 5")
        decl = ast.statements[0]
        assert isinstance(decl, LetDeclaration)
        assert decl.type_hint == 'int'

    def test_assignment(self):
        ast = parse("x = 10")
        stmt = ast.statements[0]
        assert isinstance(stmt, Assignment)
        assert stmt.name == 'x'

    def test_compound_assignment_plus(self):
        ast = parse("x += 1")
        stmt = ast.statements[0]
        assert isinstance(stmt, CompoundAssignment)
        assert stmt.op == '+'

    def test_compound_assignment_minus(self):
        ast = parse("x -= 1")
        stmt = ast.statements[0]
        assert isinstance(stmt, CompoundAssignment)
        assert stmt.op == '-'


class TestFunctions:
    """Test function parsing."""

    def test_function_def_simple(self):
        ast = parse("fn add(a, b) { return a + b }")
        fn = ast.statements[0]
        assert isinstance(fn, FunctionDef)
        assert fn.name == 'add'
        assert len(fn.params) == 2

    def test_function_def_with_types(self):
        ast = parse("fn add(a: int, b: int) -> int { return a + b }")
        fn = ast.statements[0]
        assert fn.return_type == 'int'
        assert fn.params[0] == ('a', 'int', None)

    def test_function_call(self):
        ast = parse("add(1, 2)")
        call = ast.statements[0]
        assert isinstance(call, FunctionCall)
        assert len(call.args) == 2

    def test_return_with_value(self):
        ast = parse("fn f() { return 42 }")
        fn = ast.statements[0]
        ret = fn.body[0]
        assert isinstance(ret, ReturnStatement)
        assert ret.value is not None

    def test_return_empty(self):
        ast = parse("fn f() { return }")
        fn = ast.statements[0]
        ret = fn.body[0]
        assert isinstance(ret, ReturnStatement)
        assert ret.value is None


class TestControlFlow:
    """Test control flow parsing."""

    def test_if_simple(self):
        ast = parse("if true { print(1) }")
        stmt = ast.statements[0]
        assert isinstance(stmt, IfStatement)
        assert stmt.else_body is None

    def test_if_else(self):
        ast = parse("if true { print(1) } else { print(2) }")
        stmt = ast.statements[0]
        assert isinstance(stmt, IfStatement)
        assert stmt.else_body is not None

    def test_if_elif_else(self):
        ast = parse("if x { a() } elif y { b() } else { c() }")
        stmt = ast.statements[0]
        assert isinstance(stmt, IfStatement)
        assert len(stmt.elif_branches) == 1

    def test_while(self):
        ast = parse("while x < 10 { x += 1 }")
        stmt = ast.statements[0]
        assert isinstance(stmt, WhileLoop)

    def test_for_in(self):
        ast = parse("for i in items { print(i) }")
        stmt = ast.statements[0]
        assert isinstance(stmt, ForLoop)
        assert stmt.var_name == 'i'

    def test_break(self):
        ast = parse("while true { break }")
        stmt = ast.statements[0]
        assert isinstance(stmt.body[0], BreakStatement)

    def test_continue(self):
        ast = parse("while true { continue }")
        stmt = ast.statements[0]
        assert isinstance(stmt.body[0], ContinueStatement)


class TestAccess:
    """Test access expressions."""

    def test_index_access(self):
        ast = parse("arr[0]")
        expr = ast.statements[0]
        assert isinstance(expr, IndexAccess)

    def test_member_access(self):
        ast = parse("obj.length")
        expr = ast.statements[0]
        assert isinstance(expr, MemberAccess)
        assert expr.member == 'length'

    def test_chained_access(self):
        ast = parse("arr[0].length")
        expr = ast.statements[0]
        assert isinstance(expr, MemberAccess)
        assert isinstance(expr.obj, IndexAccess)
