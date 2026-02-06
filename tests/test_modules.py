"""Tests for the module/import system."""

import pytest
from pathlib import Path
from silk.lexer import Lexer
from silk.parser import Parser
from silk.interpreter import Interpreter
from silk.ast import ImportStmt


def parse(source: str):
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    return parser.parse()


class TestImportParsing:
    """Test import statement parsing."""

    def test_simple_import(self):
        ast = parse("import silk/math")
        assert len(ast.statements) == 1
        stmt = ast.statements[0]
        assert isinstance(stmt, ImportStmt)
        assert stmt.path == "silk/math"
        assert stmt.alias is None

    def test_import_with_alias(self):
        ast = parse("import silk/medical/pediatrics as ped")
        stmt = ast.statements[0]
        assert isinstance(stmt, ImportStmt)
        assert stmt.path == "silk/medical/pediatrics"
        assert stmt.alias == "ped"

    def test_relative_import(self):
        ast = parse("import ./utils")
        stmt = ast.statements[0]
        assert isinstance(stmt, ImportStmt)
        assert stmt.path == "./utils"
        assert stmt.alias is None

    def test_relative_import_with_alias(self):
        ast = parse("import ./lib/geometry as geo")
        stmt = ast.statements[0]
        assert isinstance(stmt, ImportStmt)
        assert stmt.path == "./lib/geometry"
        assert stmt.alias == "geo"

    def test_deep_path_import(self):
        ast = parse("import silk/medical/dosing/pediatrics")
        stmt = ast.statements[0]
        assert stmt.path == "silk/medical/dosing/pediatrics"

    def test_multiple_imports(self):
        ast = parse("""
import silk/math
import ./utils as u
""")
        assert len(ast.statements) == 2
        assert ast.statements[0].path == "silk/math"
        assert ast.statements[1].path == "./utils"
        assert ast.statements[1].alias == "u"

    def test_import_bare_name(self):
        """Import without prefix defaults to relative."""
        ast = parse("import helpers")
        stmt = ast.statements[0]
        assert stmt.path == "helpers"
        assert stmt.alias is None


class TestModuleExecution:
    """Test import execution with real .silk files."""

    @pytest.fixture
    def module_dir(self, tmp_path):
        """Create a temp directory with module files."""
        # math_utils.silk
        (tmp_path / "math_utils.silk").write_text(
            'fn double(x) { return x * 2 }\n'
            'let PI = 3.14159\n'
        )
        # lib/ subdirectory
        lib_dir = tmp_path / "lib"
        lib_dir.mkdir()
        (lib_dir / "geometry.silk").write_text(
            'struct Circle { radius: float }\n'
            'fn area(r) { return 3.14159 * r * r }\n'
        )
        return tmp_path

    @pytest.fixture
    def interp(self):
        return Interpreter()

    def test_import_and_call_function(self, interp, module_dir):
        main = module_dir / "main.silk"
        main.write_text(
            'import ./math_utils\n'
            'print(math_utils.double(21))\n'
        )
        result = interp.run(main.read_text(), file_path=main)
        assert result is True
        assert interp.output_lines[-1] == "42"

    def test_import_and_access_variable(self, interp, module_dir):
        main = module_dir / "main.silk"
        main.write_text(
            'import ./math_utils\n'
            'print(math_utils.PI)\n'
        )
        result = interp.run(main.read_text(), file_path=main)
        assert result is True
        assert interp.output_lines[-1] == "3.14159"

    def test_import_with_alias(self, interp, module_dir):
        main = module_dir / "main.silk"
        main.write_text(
            'import ./math_utils as m\n'
            'print(m.double(5))\n'
        )
        result = interp.run(main.read_text(), file_path=main)
        assert result is True
        assert interp.output_lines[-1] == "10"

    def test_import_subdirectory(self, interp, module_dir):
        main = module_dir / "main.silk"
        main.write_text(
            'import ./lib/geometry as geo\n'
            'print(geo.area(10))\n'
        )
        result = interp.run(main.read_text(), file_path=main)
        assert result is True
        assert interp.output_lines[-1] == "314.159"

    def test_import_struct_from_module(self, interp, module_dir):
        main = module_dir / "main.silk"
        main.write_text(
            'import ./lib/geometry as geo\n'
            'let c = geo.Circle { radius: 5.0 }\n'
            'print(c.radius)\n'
        )
        result = interp.run(main.read_text(), file_path=main)
        assert result is True
        assert interp.output_lines[-1] == "5"

    def test_module_not_found(self, interp, module_dir):
        main = module_dir / "main.silk"
        main.write_text('import ./nonexistent\n')
        result = interp.run(main.read_text(), file_path=main)
        assert result is False

    def test_module_cached_not_executed_twice(self, interp, module_dir):
        """Module code runs only once even when imported twice."""
        counter = module_dir / "counter.silk"
        counter.write_text(
            'let mut count = 0\n'
            'count += 1\n'
            'print(count)\n'
        )
        main = module_dir / "main.silk"
        main.write_text(
            'import ./counter\n'
            'import ./counter\n'  # second import should be cached
        )
        result = interp.run(main.read_text(), file_path=main)
        assert result is True
        # count should only be printed once (module executes once)
        assert interp.output_lines.count("1") == 1

    def test_circular_import_detected(self, interp, module_dir):
        """Circular imports raise an error."""
        (module_dir / "a.silk").write_text('import ./b\n')
        (module_dir / "b.silk").write_text('import ./a\n')
        main = module_dir / "main.silk"
        main.write_text('import ./a\n')
        result = interp.run(main.read_text(), file_path=main)
        assert result is False


class TestNamespaceAccess:
    """Test namespace member access patterns."""

    @pytest.fixture
    def module_dir(self, tmp_path):
        (tmp_path / "math_mod.silk").write_text(
            'fn add(a, b) { return a + b }\n'
            'fn multiply(a, b) { return a * b }\n'
            'let VERSION = 1\n'
        )
        return tmp_path

    @pytest.fixture
    def interp(self):
        return Interpreter()

    def test_namespace_function_call(self, interp, module_dir):
        main = module_dir / "main.silk"
        main.write_text(
            'import ./math_mod\n'
            'let result = math_mod.add(3, 4)\n'
            'print(result)\n'
        )
        result = interp.run(main.read_text(), file_path=main)
        assert result is True
        assert interp.output_lines[-1] == "7"

    def test_namespace_chained_call(self, interp, module_dir):
        main = module_dir / "main.silk"
        main.write_text(
            'import ./math_mod as m\n'
            'print(m.add(m.multiply(2, 3), 4))\n'
        )
        result = interp.run(main.read_text(), file_path=main)
        assert result is True
        assert interp.output_lines[-1] == "10"

    def test_namespace_variable_access(self, interp, module_dir):
        main = module_dir / "main.silk"
        main.write_text(
            'import ./math_mod\n'
            'print(math_mod.VERSION)\n'
        )
        result = interp.run(main.read_text(), file_path=main)
        assert result is True
        assert interp.output_lines[-1] == "1"


class TestNativeModules:
    """Test native (Python-backed) module imports."""

    @pytest.fixture
    def interp(self):
        return Interpreter()

    @pytest.fixture
    def project_dir(self, tmp_path):
        return tmp_path

    def test_import_silk_math(self, interp, project_dir):
        main = project_dir / "main.silk"
        main.write_text(
            'import silk/math\n'
            'print(math.sqrt(16))\n'
        )
        result = interp.run(main.read_text(), file_path=main)
        assert result is True
        assert interp.output_lines[-1] == "4"  # Silk prints whole floats without decimal

    def test_silk_math_pi_constant(self, interp, project_dir):
        main = project_dir / "main.silk"
        main.write_text(
            'import silk/math\n'
            'print(math.pi)\n'
        )
        result = interp.run(main.read_text(), file_path=main)
        assert result is True
        assert "3.14159" in interp.output_lines[-1]

    def test_silk_math_with_alias(self, interp, project_dir):
        main = project_dir / "main.silk"
        main.write_text(
            'import silk/math as m\n'
            'print(m.ceil(3.2))\n'
        )
        result = interp.run(main.read_text(), file_path=main)
        assert result is True
        assert interp.output_lines[-1] == "4"

    def test_import_silk_medical(self, interp, project_dir):
        main = project_dir / "main.silk"
        main.write_text(
            'import silk/medical\n'
            'print(medical.bmi(70, 1.75))\n'
        )
        result = interp.run(main.read_text(), file_path=main)
        assert result is True
        assert "22.86" in interp.output_lines[-1]

    def test_native_module_cached(self, interp, project_dir):
        """Native modules are cached like file modules."""
        main = project_dir / "main.silk"
        main.write_text(
            'import silk/math\n'
            'import silk/math\n'  # second should be cached
            'print(math.sqrt(9))\n'
        )
        result = interp.run(main.read_text(), file_path=main)
        assert result is True
        assert interp.output_lines[-1] == "3"  # Silk prints whole floats without decimal
