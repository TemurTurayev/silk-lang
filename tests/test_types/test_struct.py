"""Tests for struct parsing and evaluation."""

import pytest
from silk.lexer import Lexer
from silk.parser import Parser
from silk.ast import StructDef, StructField


def parse(source: str):
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    return parser.parse()


class TestStructParsing:
    """Test struct definition parsing."""

    def test_parse_simple_struct(self):
        ast = parse("""
struct Patient {
    name: str,
    age: int
}
""")
        assert len(ast.statements) == 1
        struct = ast.statements[0]
        assert isinstance(struct, StructDef)
        assert struct.name == "Patient"
        assert len(struct.fields) == 2

    def test_struct_field_names(self):
        ast = parse("struct Point { x: float, y: float }")
        struct = ast.statements[0]
        assert struct.fields[0].name == "x"
        assert struct.fields[1].name == "y"

    def test_struct_field_types(self):
        ast = parse("struct Data { value: int }")
        struct = ast.statements[0]
        assert struct.fields[0].type_hint == "int"

    def test_struct_single_field(self):
        ast = parse("struct Single { field: str }")
        struct = ast.statements[0]
        assert len(struct.fields) == 1
        assert struct.fields[0].name == "field"
