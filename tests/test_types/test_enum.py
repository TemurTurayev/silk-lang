"""Tests for enum parsing and evaluation."""

import pytest
from silk.lexer import Lexer
from silk.parser import Parser
from silk.interpreter import Interpreter
from silk.ast import EnumDef


def parse(source: str):
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    return parser.parse()


class TestEnumParsing:
    """Test enum parsing."""

    def test_parse_simple_enum(self):
        ast = parse("""
enum Status {
    Active,
    Inactive,
    Pending
}
""")
        enum = ast.statements[0]
        assert isinstance(enum, EnumDef)
        assert enum.name == "Status"
        assert len(enum.variants) == 3

    def test_enum_variant_names(self):
        ast = parse("enum Color { Red, Green, Blue }")
        enum = ast.statements[0]
        names = [v.name for v in enum.variants]
        assert names == ["Red", "Green", "Blue"]


class TestEnumExecution:
    """Test enum runtime behavior."""

    @pytest.fixture
    def interp(self):
        return Interpreter()

    def test_enum_variant_access(self, interp):
        interp.run("""
enum Status { Active, Inactive }
let s = Status.Active
print(s)
""")
        assert "Active" in interp.output_lines[-1]

    def test_enum_equality(self, interp):
        interp.run("""
enum Status { Active, Inactive }
let a = Status.Active
let b = Status.Active
print(a == b)
""")
        assert interp.output_lines[-1] == "true"

    def test_enum_inequality(self, interp):
        interp.run("""
enum Status { Active, Inactive }
let a = Status.Active
let b = Status.Inactive
print(a == b)
""")
        assert interp.output_lines[-1] == "false"
