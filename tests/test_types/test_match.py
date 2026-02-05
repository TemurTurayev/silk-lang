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
