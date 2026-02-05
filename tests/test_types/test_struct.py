"""Tests for struct parsing and evaluation."""

import pytest
from silk.lexer import Lexer
from silk.parser import Parser
from silk.ast import StructDef, StructField, StructInstance


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


class TestStructInstantiation:
    """Test struct instantiation parsing."""

    def test_parse_struct_instance(self):
        ast = parse("""
struct Point { x: float, y: float }
let p = Point { x: 1.0, y: 2.0 }
""")
        assert len(ast.statements) == 2
        let_stmt = ast.statements[1]
        assert isinstance(let_stmt.value, StructInstance)
        assert let_stmt.value.struct_name == "Point"

    def test_struct_instance_fields(self):
        ast = parse("""
struct Data { value: int }
let d = Data { value: 42 }
""")
        instance = ast.statements[1].value
        assert "value" in instance.field_values

    def test_struct_instance_multiple_fields(self):
        ast = parse("""
struct Patient { name: str, age: int, weight: float }
let p = Patient { name: "Ahmad", age: 8, weight: 25.0 }
""")
        instance = ast.statements[1].value
        assert instance.struct_name == "Patient"
        assert len(instance.field_values) == 3
