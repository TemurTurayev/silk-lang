"""Tests for impl blocks - methods on structs."""

import pytest
from silk.lexer import Lexer
from silk.parser import Parser
from silk.ast import ImplBlock, FunctionDef
from silk.interpreter import Interpreter


def parse(source: str):
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    return parser.parse()


class TestImplParsing:
    """Test impl block parsing."""

    def test_parse_simple_impl(self):
        ast = parse("""
struct Point { x: float, y: float }

impl Point {
    fn magnitude(self) -> float {
        return sqrt(self.x ** 2 + self.y ** 2)
    }
}
""")
        assert len(ast.statements) == 2
        impl = ast.statements[1]
        assert isinstance(impl, ImplBlock)
        assert impl.struct_name == "Point"
        assert len(impl.methods) == 1

    def test_impl_method_names(self):
        ast = parse("""
struct Patient { name: str, age: int }

impl Patient {
    fn display(self) {
        print(self.name)
    }
    fn is_adult(self) -> bool {
        return self.age >= 18
    }
}
""")
        impl = ast.statements[1]
        assert isinstance(impl, ImplBlock)
        method_names = [m.name for m in impl.methods]
        assert method_names == ["display", "is_adult"]

    def test_impl_method_is_function_def(self):
        ast = parse("""
struct Data { value: int }
impl Data {
    fn get_value(self) -> int {
        return self.value
    }
}
""")
        impl = ast.statements[1]
        method = impl.methods[0]
        assert isinstance(method, FunctionDef)
        assert method.name == "get_value"
        assert method.params[0] == ("self", None, None)

    def test_impl_method_with_params(self):
        ast = parse("""
struct Counter { count: int }
impl Counter {
    fn add(self, n: int) -> int {
        return self.count + n
    }
}
""")
        impl = ast.statements[1]
        method = impl.methods[0]
        assert len(method.params) == 2
        assert method.params[0] == ("self", None, None)
        assert method.params[1] == ("n", "int", None)


class TestImplExecution:
    """Test impl block runtime behavior."""

    @pytest.fixture
    def interp(self):
        return Interpreter()

    def test_simple_method_call(self, interp):
        interp.run("""
struct Point { x: float, y: float }

impl Point {
    fn sum(self) -> float {
        return self.x + self.y
    }
}

let p = Point { x: 3.0, y: 4.0 }
print(p.sum())
""")
        assert interp.output_lines[-1] == "7"

    def test_method_with_args(self, interp):
        interp.run("""
struct Counter { count: int }

impl Counter {
    fn add(self, n: int) -> int {
        return self.count + n
    }
}

let c = Counter { count: 10 }
print(c.add(5))
""")
        assert interp.output_lines[-1] == "15"

    def test_method_accessing_fields(self, interp):
        interp.run("""
struct Patient {
    name: str,
    weight: float,
    height: float
}

impl Patient {
    fn bmi(self) -> float {
        return bmi(self.weight, self.height)
    }
}

let p = Patient { name: "Ahmad", weight: 70.0, height: 1.75 }
print(p.bmi())
""")
        assert "22.86" in interp.output_lines[-1]

    def test_method_with_print(self, interp):
        interp.run("""
struct Greeter { name: str }

impl Greeter {
    fn greet(self) {
        print("Hello, " + self.name + "!")
    }
}

let g = Greeter { name: "World" }
g.greet()
""")
        assert interp.output_lines[-1] == "Hello, World!"

    def test_method_returning_bool(self, interp):
        interp.run("""
struct Patient { age: int }

impl Patient {
    fn is_adult(self) -> bool {
        return self.age >= 18
    }
}

let child = Patient { age: 8 }
let adult = Patient { age: 25 }
print(child.is_adult())
print(adult.is_adult())
""")
        assert interp.output_lines[-2] == "false"
        assert interp.output_lines[-1] == "true"

    def test_method_result_in_expression(self, interp):
        interp.run("""
struct Rect { width: float, height: float }

impl Rect {
    fn area(self) -> float {
        return self.width * self.height
    }
}

let r = Rect { width: 5.0, height: 3.0 }
let a = r.area()
print(a * 2)
""")
        assert interp.output_lines[-1] == "30"

    def test_multiple_methods(self, interp):
        interp.run("""
struct Circle { radius: float }

impl Circle {
    fn area(self) -> float {
        return 3.14159 * self.radius ** 2
    }
    fn circumference(self) -> float {
        return 2 * 3.14159 * self.radius
    }
}

let c = Circle { radius: 5.0 }
print(round(c.area()))
print(round(c.circumference()))
""")
        assert interp.output_lines[-2] == "79"
        assert interp.output_lines[-1] == "31"

    def test_method_on_medical_struct(self, interp):
        """Medical use case: methods on patient struct."""
        interp.run("""
struct Vitals {
    weight_kg: float,
    height_m: float,
    temp_c: float
}

impl Vitals {
    fn bmi_value(self) -> float {
        return bmi(self.weight_kg, self.height_m)
    }
    fn temp_f(self) -> float {
        return celsius_to_fahrenheit(self.temp_c)
    }
}

let v = Vitals { weight_kg: 70.0, height_m: 1.75, temp_c: 37.0 }
print(v.bmi_value())
print(v.temp_f())
""")
        assert "22.86" in interp.output_lines[-2]
        assert "98.6" in interp.output_lines[-1]


class TestImplErrors:
    """Test impl block error handling."""

    @pytest.fixture
    def interp(self):
        return Interpreter()

    def test_impl_nonexistent_struct(self, interp):
        result = interp.run("""
impl NonExistent {
    fn method(self) {
        return 1
    }
}
""")
        assert result is False

    def test_call_nonexistent_method(self, interp):
        result = interp.run("""
struct Point { x: float, y: float }
let p = Point { x: 1.0, y: 2.0 }
p.nonexistent()
""")
        assert result is False
