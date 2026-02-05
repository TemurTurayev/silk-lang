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


from silk.interpreter import Interpreter


class TestStructExecution:
    """Test struct runtime behavior."""

    @pytest.fixture
    def interp(self):
        return Interpreter()

    def test_struct_instance_creation(self, interp):
        interp.run("""
struct Patient {
    name: str,
    age: int
}
let p = Patient { name: "Ahmad", age: 8 }
print(p.name)
""")
        assert interp.output_lines[-1] == "Ahmad"

    def test_struct_field_access(self, interp):
        interp.run("""
struct Point { x: float, y: float }
let p = Point { x: 3.0, y: 4.0 }
print(p.x + p.y)
""")
        # Silk prints whole floats without decimal (e.g., 7.0 -> "7")
        assert interp.output_lines[-1] == "7"

    def test_struct_in_function(self, interp):
        interp.run("""
struct Patient { weight: float, height: float }

fn calc_bmi(p: Patient) -> float {
    return bmi(p.weight, p.height)
}

let patient = Patient { weight: 70.0, height: 1.75 }
print(calc_bmi(patient))
""")
        assert "22.86" in interp.output_lines[-1]

    def test_struct_print(self, interp):
        interp.run("""
struct Point { x: int, y: int }
let p = Point { x: 1, y: 2 }
print(p)
""")
        # Should print something like "Point { x: 1, y: 2 }"
        assert "Point" in interp.output_lines[-1]
        assert "x" in interp.output_lines[-1]
