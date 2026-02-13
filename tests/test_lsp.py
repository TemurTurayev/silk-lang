"""
Tests for the Silk LSP server components.

Tests analyzer, completion data, and server creation.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


# ─── Analyzer Tests ────────────────────────────────────────

class TestAnalyzer:
    """Test the LSP document analyzer."""

    def test_valid_code_no_diagnostics(self):
        from silk.lsp.analyzer import analyze_document
        source = 'let x = 42\nprint(x)\n'
        diagnostics, ast, symbols = analyze_document(source, "file:///test.silk")
        assert len(diagnostics) == 0
        assert len(ast) > 0

    def test_syntax_error_produces_diagnostic(self):
        from silk.lsp.analyzer import analyze_document
        source = 'let = \n'  # missing variable name
        diagnostics, ast, symbols = analyze_document(source, "file:///test.silk")
        assert len(diagnostics) > 0
        assert diagnostics[0].message  # has error message
        assert diagnostics[0].range.start.line >= 0

    def test_unclosed_string_produces_diagnostic(self):
        from silk.lsp.analyzer import analyze_document
        source = 'let x = "unclosed\n'
        diagnostics, ast, symbols = analyze_document(source, "file:///test.silk")
        assert len(diagnostics) > 0

    def test_function_def_produces_symbol(self):
        from silk.lsp.analyzer import analyze_document
        source = 'fn add(a: int, b: int) -> int {\n    return a + b\n}\n'
        diagnostics, ast, symbols = analyze_document(source, "file:///test.silk")
        assert len(diagnostics) == 0
        assert len(symbols) >= 1
        assert symbols[0].name == "add"

    def test_struct_def_produces_symbol(self):
        from silk.lsp.analyzer import analyze_document
        source = 'struct Patient {\n    name: str,\n    age: int\n}\n'
        diagnostics, ast, symbols = analyze_document(source, "file:///test.silk")
        assert len(diagnostics) == 0
        found = [s for s in symbols if s.name == "Patient"]
        assert len(found) == 1

    def test_enum_def_produces_symbol(self):
        from silk.lsp.analyzer import analyze_document
        source = 'enum Color {\n    Red,\n    Green,\n    Blue\n}\n'
        diagnostics, ast, symbols = analyze_document(source, "file:///test.silk")
        assert len(diagnostics) == 0
        found = [s for s in symbols if s.name == "Color"]
        assert len(found) == 1

    def test_let_declaration_produces_symbol(self):
        from silk.lsp.analyzer import analyze_document
        source = 'let name = "Silk"\n'
        diagnostics, ast, symbols = analyze_document(source, "file:///test.silk")
        assert len(diagnostics) == 0
        found = [s for s in symbols if s.name == "name"]
        assert len(found) == 1

    def test_test_block_produces_symbol(self):
        from silk.lsp.analyzer import analyze_document
        source = 'test "my test" {\n    assert true\n}\n'
        diagnostics, ast, symbols = analyze_document(source, "file:///test.silk")
        assert len(diagnostics) == 0
        found = [s for s in symbols if "my test" in s.name]
        assert len(found) == 1

    def test_impl_block_produces_symbol(self):
        from silk.lsp.analyzer import analyze_document
        source = 'struct Foo { x: int }\nimpl Foo {\n    fn get_x(self) -> int {\n        return self.x\n    }\n}\n'
        diagnostics, ast, symbols = analyze_document(source, "file:///test.silk")
        assert len(diagnostics) == 0
        impl_syms = [s for s in symbols if "impl" in s.name]
        assert len(impl_syms) >= 1

    def test_empty_source(self):
        from silk.lsp.analyzer import analyze_document
        diagnostics, ast, symbols = analyze_document("", "file:///test.silk")
        assert len(diagnostics) == 0

    def test_multiple_functions(self):
        from silk.lsp.analyzer import analyze_document
        source = 'fn foo() { }\nfn bar() { }\nfn baz() { }\n'
        diagnostics, ast, symbols = analyze_document(source, "file:///test.silk")
        assert len(diagnostics) == 0
        names = {s.name for s in symbols}
        assert "foo" in names
        assert "bar" in names
        assert "baz" in names


# ─── Word-at-Position Tests ───────────────────────────────

class TestWordAtPosition:
    """Test word extraction at cursor position."""

    def test_simple_word(self):
        from silk.lsp.analyzer import get_word_at_position
        source = "let count = 42"
        assert get_word_at_position(source, 0, 4) == "count"

    def test_function_name(self):
        from silk.lsp.analyzer import get_word_at_position
        source = "fn calculate_bmi(w, h) {"
        assert get_word_at_position(source, 0, 5) == "calculate_bmi"

    def test_beginning_of_line(self):
        from silk.lsp.analyzer import get_word_at_position
        source = "print(x)"
        assert get_word_at_position(source, 0, 0) == "print"

    def test_end_of_word(self):
        from silk.lsp.analyzer import get_word_at_position
        source = "bmi(70, 1.75)"
        assert get_word_at_position(source, 0, 2) == "bmi"

    def test_out_of_bounds(self):
        from silk.lsp.analyzer import get_word_at_position
        source = "let x = 1"
        assert get_word_at_position(source, 99, 0) is None

    def test_on_operator(self):
        from silk.lsp.analyzer import get_word_at_position
        source = "x + y"
        assert get_word_at_position(source, 0, 2) is None


# ─── Completion Data Tests ─────────────────────────────────

class TestCompletionData:
    """Test the completion data module."""

    def test_get_all_completions_not_empty(self):
        from silk.lsp.completion_data import get_all_completions
        items = get_all_completions()
        assert len(items) > 50  # keywords + builtins + medical

    def test_keywords_present(self):
        from silk.lsp.completion_data import get_all_completions
        items = get_all_completions()
        labels = {item.label for item in items}
        for kw in ["let", "fn", "struct", "enum", "match", "if", "for", "while", "test", "try"]:
            assert kw in labels, f"Missing keyword: {kw}"

    def test_core_functions_present(self):
        from silk.lsp.completion_data import get_all_completions
        items = get_all_completions()
        labels = {item.label for item in items}
        for fn in ["print", "len", "range", "map", "filter", "decimal", "unit"]:
            assert fn in labels, f"Missing core function: {fn}"

    def test_medical_functions_present(self):
        from silk.lsp.completion_data import get_all_completions
        items = get_all_completions()
        labels = {item.label for item in items}
        for fn in ["bmi", "bsa", "dose_per_kg", "creatinine_clearance", "egfr",
                    "pediatric_dose", "iv_drip_rate", "map_pressure", "anion_gap"]:
            assert fn in labels, f"Missing medical function: {fn}"

    def test_constructors_present(self):
        from silk.lsp.completion_data import get_all_completions
        items = get_all_completions()
        labels = {item.label for item in items}
        for c in ["Some", "Ok", "Err", "None"]:
            assert c in labels, f"Missing constructor: {c}"

    def test_items_have_documentation(self):
        from silk.lsp.completion_data import get_all_completions
        items = get_all_completions()
        # At least medical functions should have docs
        bmi_items = [i for i in items if i.label == "bmi"]
        assert len(bmi_items) == 1
        assert bmi_items[0].documentation is not None

    def test_items_have_detail(self):
        from silk.lsp.completion_data import get_all_completions
        items = get_all_completions()
        # Most items should have detail (signature)
        with_detail = [i for i in items if i.detail]
        assert len(with_detail) > 40


# ─── Server Creation Tests ─────────────────────────────────

class TestServerCreation:
    """Test the LSP server creation."""

    def test_create_server(self):
        from silk.lsp.server import create_server
        server = create_server()
        assert server is not None
        assert server.name == "silk-language-server"

    def test_server_has_hover_index(self):
        from silk.lsp.server import create_server
        server = create_server()
        assert len(server._hover_index) > 0
        assert "bmi" in server._hover_index
        assert "print" in server._hover_index

    def test_server_has_completions(self):
        from silk.lsp.server import create_server
        server = create_server()
        assert len(server._completions) > 50


# ─── Medical Function Hover Tests ──────────────────────────

class TestMedicalHover:
    """Test that medical functions have proper hover docs."""

    def test_bmi_hover(self):
        from silk.lsp.server import create_server
        server = create_server()
        hover = server._hover_index.get("bmi")
        assert hover is not None
        assert "Body Mass Index" in hover.value

    def test_creatinine_clearance_hover(self):
        from silk.lsp.server import create_server
        server = create_server()
        hover = server._hover_index.get("creatinine_clearance")
        assert hover is not None
        assert "Cockcroft-Gault" in hover.value

    def test_pediatric_dose_hover(self):
        from silk.lsp.server import create_server
        server = create_server()
        hover = server._hover_index.get("pediatric_dose")
        assert hover is not None
        assert "Clark" in hover.value

    def test_medical_disclaimer_in_hover(self):
        from silk.lsp.server import create_server
        server = create_server()
        hover = server._hover_index.get("bmi")
        assert hover is not None
        assert "clinical interpretation" in hover.value
