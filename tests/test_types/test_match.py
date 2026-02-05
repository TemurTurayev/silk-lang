"""Tests for match expression parsing and evaluation."""

import pytest
from silk.lexer import Lexer
from silk.parser import Parser
from silk.ast import MatchExpr


def parse(source: str):
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    return parser.parse()


from silk.interpreter import Interpreter


class TestMatchExecution:
    """Test match runtime behavior."""

    @pytest.fixture
    def interp(self):
        return Interpreter()

    def test_match_enum(self, interp):
        interp.run("""
enum Status { Active, Inactive, Pending }
let s = Status.Active
match s {
    Active => print("is active"),
    Inactive => print("is inactive"),
    Pending => print("is pending")
}
""")
        assert interp.output_lines[-1] == "is active"

    def test_match_second_arm(self, interp):
        interp.run("""
enum Status { Active, Inactive }
let s = Status.Inactive
match s {
    Active => print("active"),
    Inactive => print("inactive")
}
""")
        assert interp.output_lines[-1] == "inactive"

    def test_match_with_wildcard(self, interp):
        interp.run("""
let x = 42
match x {
    1 => print("one"),
    2 => print("two"),
    _ => print("other")
}
""")
        assert interp.output_lines[-1] == "other"

    def test_match_returns_value(self, interp):
        interp.run("""
enum Status { Active, Inactive }
let s = Status.Active
let msg = match s {
    Active => "active",
    Inactive => "inactive"
}
print(msg)
""")
        assert interp.output_lines[-1] == "active"

    def test_match_with_guard(self, interp):
        interp.run("""
let x = 15
match x {
    _ if x < 10 => print("small"),
    _ if x < 20 => print("medium"),
    _ => print("large")
}
""")
        assert interp.output_lines[-1] == "medium"


class TestMatchExhaustiveness:
    """Test exhaustiveness checking - CRITICAL for medical safety."""

    @pytest.fixture
    def interp(self):
        return Interpreter()

    def test_non_exhaustive_match_fails(self, interp):
        """Non-exhaustive match MUST fail for medical safety."""
        result = interp.run("""
enum Status { Active, Inactive, Pending }
let s = Status.Active
match s {
    Active => print("active"),
    Inactive => print("inactive")
}
""")
        # This MUST fail - Pending is not covered
        assert result is False

    def test_exhaustive_match_passes(self, interp):
        result = interp.run("""
enum Status { Active, Inactive, Pending }
let s = Status.Active
match s {
    Active => print("active"),
    Inactive => print("inactive"),
    Pending => print("pending")
}
""")
        assert result is True

    def test_wildcard_makes_exhaustive(self, interp):
        result = interp.run("""
enum Status { Active, Inactive, Pending }
let s = Status.Active
match s {
    Active => print("active"),
    _ => print("other")
}
""")
        assert result is True


class TestMatchParsing:
    """Test match expression parsing."""

    def test_parse_simple_match(self):
        ast = parse("""
enum Status { Active, Inactive }
let s = Status.Active
match s {
    Active => print("active"),
    Inactive => print("inactive")
}
""")
        match_expr = ast.statements[2]
        assert isinstance(match_expr, MatchExpr)
        assert len(match_expr.arms) == 2

    def test_match_with_wildcard(self):
        ast = parse("""
let x = 5
match x {
    1 => print("one"),
    _ => print("other")
}
""")
        match_expr = ast.statements[1]
        assert len(match_expr.arms) == 2

    def test_match_with_block_body(self):
        ast = parse("""
let x = 1
match x {
    1 => {
        print("one")
        print("!")
    },
    _ => print("other")
}
""")
        match_expr = ast.statements[1]
        # First arm has a block body (list)
        assert isinstance(match_expr.arms[0].body, list)
