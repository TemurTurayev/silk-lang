"""Tests for interfaces - polymorphism and contract enforcement."""

import pytest
from silk.lexer import Lexer
from silk.parser import Parser
from silk.ast import InterfaceDef, InterfaceMethodSig, ImplBlock
from silk.interpreter import Interpreter


def parse(source: str):
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    return parser.parse()


class TestInterfaceParsing:
    """Test interface definition parsing."""

    def test_parse_simple_interface(self):
        ast = parse("""
interface Displayable {
    fn display(self)
}
""")
        assert len(ast.statements) == 1
        iface = ast.statements[0]
        assert isinstance(iface, InterfaceDef)
        assert iface.name == "Displayable"
        assert len(iface.methods) == 1

    def test_interface_method_names(self):
        ast = parse("""
interface Shape {
    fn area(self) -> float
    fn perimeter(self) -> float
}
""")
        iface = ast.statements[0]
        method_names = [m.name for m in iface.methods]
        assert method_names == ["area", "perimeter"]

    def test_interface_method_is_signature(self):
        ast = parse("""
interface Calculable {
    fn calculate(self, x: float) -> float
}
""")
        iface = ast.statements[0]
        method = iface.methods[0]
        assert isinstance(method, InterfaceMethodSig)
        assert method.name == "calculate"
        assert method.return_type == "float"
        assert len(method.params) == 2
        assert method.params[0] == ("self", None)
        assert method.params[1] == ("x", "float")

    def test_interface_method_no_return_type(self):
        ast = parse("""
interface Printable {
    fn print_info(self)
}
""")
        method = ast.statements[0].methods[0]
        assert method.return_type is None


class TestImplWithInterface:
    """Test impl blocks that implement an interface."""

    def test_parse_impl_with_interface(self):
        ast = parse("""
interface Displayable {
    fn display(self)
}
struct Patient { name: str }
impl Patient : Displayable {
    fn display(self) {
        print(self.name)
    }
}
""")
        impl = ast.statements[2]
        assert isinstance(impl, ImplBlock)
        assert impl.struct_name == "Patient"
        assert impl.interface_name == "Displayable"
        assert len(impl.methods) == 1

    def test_impl_without_interface_still_works(self):
        ast = parse("""
struct Point { x: float, y: float }
impl Point {
    fn sum(self) -> float {
        return self.x + self.y
    }
}
""")
        impl = ast.statements[1]
        assert impl.interface_name is None


class TestInterfaceExecution:
    """Test interface runtime behavior."""

    @pytest.fixture
    def interp(self):
        return Interpreter()

    def test_impl_satisfies_interface(self, interp):
        result = interp.run("""
interface Displayable {
    fn display(self)
}

struct Patient { name: str }

impl Patient : Displayable {
    fn display(self) {
        print("Patient: " + self.name)
    }
}

let p = Patient { name: "Ahmad" }
p.display()
""")
        assert result is True
        assert interp.output_lines[-1] == "Patient: Ahmad"

    def test_impl_multiple_interface_methods(self, interp):
        result = interp.run("""
interface Shape {
    fn area(self) -> float
    fn describe(self)
}

struct Circle { radius: float }

impl Circle : Shape {
    fn area(self) -> float {
        return 3.14159 * self.radius ** 2
    }
    fn describe(self) {
        print("Circle with radius " + str(self.radius))
    }
}

let c = Circle { radius: 5.0 }
print(round(c.area()))
c.describe()
""")
        assert result is True
        assert interp.output_lines[-2] == "79"
        assert interp.output_lines[-1] == "Circle with radius 5"

    def test_interface_method_with_params(self, interp):
        result = interp.run("""
interface Scalable {
    fn scale(self, factor: float) -> float
}

struct Measurement { value: float }

impl Measurement : Scalable {
    fn scale(self, factor: float) -> float {
        return self.value * factor
    }
}

let m = Measurement { value: 10.0 }
print(m.scale(2.5))
""")
        assert result is True
        assert interp.output_lines[-1] == "25"


class TestInterfaceErrors:
    """Test interface error handling."""

    @pytest.fixture
    def interp(self):
        return Interpreter()

    def test_missing_interface_method(self, interp):
        """Impl must implement ALL interface methods."""
        result = interp.run("""
interface Shape {
    fn area(self) -> float
    fn perimeter(self) -> float
}

struct Circle { radius: float }

impl Circle : Shape {
    fn area(self) -> float {
        return 3.14 * self.radius ** 2
    }
}
""")
        assert result is False  # Missing perimeter

    def test_impl_nonexistent_interface(self, interp):
        result = interp.run("""
struct Point { x: float }
impl Point : NonExistent {
    fn method(self) {
        return 1
    }
}
""")
        assert result is False

    def test_medical_interface_enforcement(self, interp):
        """Medical safety: interface enforces required methods."""
        result = interp.run("""
interface MedicalCheck {
    fn validate(self) -> bool
    fn calculate(self) -> float
    fn display_result(self)
}

struct DoseCalc {
    mg_per_kg: float,
    weight: float
}

impl DoseCalc : MedicalCheck {
    fn validate(self) -> bool {
        return self.mg_per_kg > 0 and self.weight > 0
    }
    fn calculate(self) -> float {
        return self.mg_per_kg * self.weight
    }
    fn display_result(self) {
        print("Dose: " + str(self.calculate()) + " mg")
    }
}

let d = DoseCalc { mg_per_kg: 15.0, weight: 25.0 }
print(d.validate())
d.display_result()
""")
        assert result is True
        assert interp.output_lines[-2] == "true"
        assert interp.output_lines[-1] == "Dose: 375 mg"
