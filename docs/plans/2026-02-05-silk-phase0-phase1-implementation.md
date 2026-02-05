# Silk Language: Phase 0 + Phase 1 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Complete Phase 0 (80%+ test coverage, fix bugs, improve errors) and Phase 1 (struct, enum, pattern matching with exhaustiveness checks, Option/Result types) to make Silk production-ready for medical computing.

**Architecture:** Tree-walking interpreter in Python. Phase 0 stabilizes the foundation. Phase 1 adds type system features incrementally: struct → enum → match → Option/Result → impl blocks → interfaces. Each feature is fully tested before the next begins.

**Tech Stack:** Python 3.11+, pytest, pytest-cov. No external runtime dependencies.

---

## Phase 0: Foundation Completion

**Current State:**
- Coverage: 75% (target: 80%+)
- Tests: 86 total, 1 failing
- Missing: parser tests, golden tests, negative tests for edge cases

---

### Task 0.1: Fix Failing Test (Index Out of Bounds)

**Files:**
- Modify: `src/silk/interpreter.py:212-219`
- Test: `tests/test_interpreter_negative.py:48`

**Step 1: Read the failing test**

```python
# tests/test_interpreter_negative.py line 48
def test_index_out_of_bounds(self, interp):
    result = interp.run("let x = [1, 2, 3][10]")
    # Expects RuntimeError_, but gets Python IndexError
```

**Step 2: Fix interpreter to catch IndexError**

In `src/silk/interpreter.py`, modify the `evaluate` method around line 212-219:

```python
elif isinstance(node, IndexAccess):
    obj = self.evaluate(node.obj, env)
    idx = self.evaluate(node.index, env)
    if isinstance(obj, list):
        idx_int = int(idx)
        if idx_int < 0 or idx_int >= len(obj):
            raise RuntimeError_(f"Index {idx_int} out of bounds for array of length {len(obj)}")
        return obj[idx_int]
    elif isinstance(obj, str):
        idx_int = int(idx)
        if idx_int < 0 or idx_int >= len(obj):
            raise RuntimeError_(f"Index {idx_int} out of bounds for string of length {len(obj)}")
        return obj[idx_int]
    raise RuntimeError_(f"Cannot index into {type(obj).__name__}")
```

**Step 3: Run test to verify it passes**

```bash
pytest tests/test_interpreter_negative.py::TestRuntimeErrors::test_index_out_of_bounds -v
```
Expected: PASS

**Step 4: Run full test suite**

```bash
pytest --cov=src/silk -v
```
Expected: 86 passed, 0 failed

**Step 5: Commit**

```bash
git add src/silk/interpreter.py
git commit -m "fix: handle index out of bounds with proper RuntimeError"
```

---

### Task 0.2: Add Parser Tests

**Files:**
- Create: `tests/test_parser.py`
- Reference: `src/silk/parser.py`, `src/silk/ast.py`

**Step 1: Create parser test file with fixtures**

```python
"""
Parser Tests

Tests for the Silk parser, verifying AST construction.
"""

import pytest
from silk.lexer import Lexer
from silk.parser import Parser
from silk.ast import (
    Program, NumberLiteral, StringLiteral, BoolLiteral, NullLiteral,
    ArrayLiteral, Identifier, BinaryOp, UnaryOp, Assignment,
    CompoundAssignment, LetDeclaration, IfStatement, WhileLoop,
    ForLoop, FunctionDef, FunctionCall, ReturnStatement,
    BreakStatement, ContinueStatement, IndexAccess, MemberAccess
)
from silk.errors import ParseError


def parse(source: str) -> Program:
    """Helper to parse source code."""
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    return parser.parse()


class TestLiterals:
    """Test literal parsing."""

    def test_integer(self):
        ast = parse("42")
        assert len(ast.statements) == 1
        assert isinstance(ast.statements[0], NumberLiteral)
        assert ast.statements[0].value == 42

    def test_float(self):
        ast = parse("3.14")
        assert len(ast.statements) == 1
        assert isinstance(ast.statements[0], NumberLiteral)
        assert ast.statements[0].value == 3.14

    def test_string(self):
        ast = parse('"hello"')
        assert len(ast.statements) == 1
        assert isinstance(ast.statements[0], StringLiteral)
        assert ast.statements[0].value == "hello"

    def test_true(self):
        ast = parse("true")
        assert isinstance(ast.statements[0], BoolLiteral)
        assert ast.statements[0].value is True

    def test_false(self):
        ast = parse("false")
        assert isinstance(ast.statements[0], BoolLiteral)
        assert ast.statements[0].value is False

    def test_null(self):
        ast = parse("null")
        assert isinstance(ast.statements[0], NullLiteral)

    def test_array_empty(self):
        ast = parse("[]")
        assert isinstance(ast.statements[0], ArrayLiteral)
        assert ast.statements[0].elements == []

    def test_array_with_elements(self):
        ast = parse("[1, 2, 3]")
        arr = ast.statements[0]
        assert isinstance(arr, ArrayLiteral)
        assert len(arr.elements) == 3


class TestExpressions:
    """Test expression parsing."""

    def test_binary_add(self):
        ast = parse("1 + 2")
        expr = ast.statements[0]
        assert isinstance(expr, BinaryOp)
        assert expr.op == '+'

    def test_binary_precedence(self):
        ast = parse("1 + 2 * 3")
        expr = ast.statements[0]
        assert isinstance(expr, BinaryOp)
        assert expr.op == '+'
        assert isinstance(expr.right, BinaryOp)
        assert expr.right.op == '*'

    def test_parentheses(self):
        ast = parse("(1 + 2) * 3")
        expr = ast.statements[0]
        assert isinstance(expr, BinaryOp)
        assert expr.op == '*'
        assert isinstance(expr.left, BinaryOp)
        assert expr.left.op == '+'

    def test_power_right_associative(self):
        ast = parse("2 ** 3 ** 2")
        expr = ast.statements[0]
        assert isinstance(expr, BinaryOp)
        assert expr.op == '**'
        assert isinstance(expr.right, BinaryOp)
        assert expr.right.op == '**'

    def test_unary_minus(self):
        ast = parse("-5")
        expr = ast.statements[0]
        assert isinstance(expr, UnaryOp)
        assert expr.op == '-'

    def test_unary_not(self):
        ast = parse("not true")
        expr = ast.statements[0]
        assert isinstance(expr, UnaryOp)
        assert expr.op == 'not'

    def test_comparison(self):
        ast = parse("1 < 2")
        expr = ast.statements[0]
        assert isinstance(expr, BinaryOp)
        assert expr.op == '<'

    def test_logical_and(self):
        ast = parse("true and false")
        expr = ast.statements[0]
        assert isinstance(expr, BinaryOp)
        assert expr.op == 'and'

    def test_logical_or(self):
        ast = parse("true or false")
        expr = ast.statements[0]
        assert isinstance(expr, BinaryOp)
        assert expr.op == 'or'


class TestDeclarations:
    """Test declaration parsing."""

    def test_let_immutable(self):
        ast = parse("let x = 5")
        decl = ast.statements[0]
        assert isinstance(decl, LetDeclaration)
        assert decl.name == 'x'
        assert decl.mutable is False

    def test_let_mutable(self):
        ast = parse("let mut x = 5")
        decl = ast.statements[0]
        assert isinstance(decl, LetDeclaration)
        assert decl.mutable is True

    def test_let_with_type(self):
        ast = parse("let x: int = 5")
        decl = ast.statements[0]
        assert isinstance(decl, LetDeclaration)
        assert decl.type_hint == 'int'

    def test_assignment(self):
        ast = parse("x = 10")
        stmt = ast.statements[0]
        assert isinstance(stmt, Assignment)
        assert stmt.name == 'x'

    def test_compound_assignment_plus(self):
        ast = parse("x += 1")
        stmt = ast.statements[0]
        assert isinstance(stmt, CompoundAssignment)
        assert stmt.op == '+'

    def test_compound_assignment_minus(self):
        ast = parse("x -= 1")
        stmt = ast.statements[0]
        assert isinstance(stmt, CompoundAssignment)
        assert stmt.op == '-'


class TestFunctions:
    """Test function parsing."""

    def test_function_def_simple(self):
        ast = parse("fn add(a, b) { return a + b }")
        fn = ast.statements[0]
        assert isinstance(fn, FunctionDef)
        assert fn.name == 'add'
        assert len(fn.params) == 2

    def test_function_def_with_types(self):
        ast = parse("fn add(a: int, b: int) -> int { return a + b }")
        fn = ast.statements[0]
        assert fn.return_type == 'int'
        assert fn.params[0] == ('a', 'int')

    def test_function_call(self):
        ast = parse("add(1, 2)")
        call = ast.statements[0]
        assert isinstance(call, FunctionCall)
        assert len(call.args) == 2

    def test_return_with_value(self):
        ast = parse("fn f() { return 42 }")
        fn = ast.statements[0]
        ret = fn.body[0]
        assert isinstance(ret, ReturnStatement)
        assert ret.value is not None

    def test_return_empty(self):
        ast = parse("fn f() { return }")
        fn = ast.statements[0]
        ret = fn.body[0]
        assert isinstance(ret, ReturnStatement)
        assert ret.value is None


class TestControlFlow:
    """Test control flow parsing."""

    def test_if_simple(self):
        ast = parse("if true { print(1) }")
        stmt = ast.statements[0]
        assert isinstance(stmt, IfStatement)
        assert stmt.else_body is None

    def test_if_else(self):
        ast = parse("if true { print(1) } else { print(2) }")
        stmt = ast.statements[0]
        assert isinstance(stmt, IfStatement)
        assert stmt.else_body is not None

    def test_if_elif_else(self):
        ast = parse("if x { a() } elif y { b() } else { c() }")
        stmt = ast.statements[0]
        assert isinstance(stmt, IfStatement)
        assert len(stmt.elif_branches) == 1

    def test_while(self):
        ast = parse("while x < 10 { x += 1 }")
        stmt = ast.statements[0]
        assert isinstance(stmt, WhileLoop)

    def test_for_in(self):
        ast = parse("for i in items { print(i) }")
        stmt = ast.statements[0]
        assert isinstance(stmt, ForLoop)
        assert stmt.var_name == 'i'

    def test_break(self):
        ast = parse("while true { break }")
        stmt = ast.statements[0]
        assert isinstance(stmt.body[0], BreakStatement)

    def test_continue(self):
        ast = parse("while true { continue }")
        stmt = ast.statements[0]
        assert isinstance(stmt.body[0], ContinueStatement)


class TestAccess:
    """Test access expressions."""

    def test_index_access(self):
        ast = parse("arr[0]")
        expr = ast.statements[0]
        assert isinstance(expr, IndexAccess)

    def test_member_access(self):
        ast = parse("obj.length")
        expr = ast.statements[0]
        assert isinstance(expr, MemberAccess)
        assert expr.member == 'length'

    def test_chained_access(self):
        ast = parse("arr[0].length")
        expr = ast.statements[0]
        assert isinstance(expr, MemberAccess)
        assert isinstance(expr.obj, IndexAccess)
```

**Step 2: Run parser tests**

```bash
pytest tests/test_parser.py -v
```
Expected: All tests pass

**Step 3: Check coverage improvement**

```bash
pytest --cov=src/silk --cov-report=term-missing tests/test_parser.py
```

**Step 4: Commit**

```bash
git add tests/test_parser.py
git commit -m "test: add comprehensive parser tests"
```

---

### Task 0.3: Add Parser Negative Tests

**Files:**
- Create: `tests/test_parser_negative.py`

**Step 1: Create negative tests for parser errors**

```python
"""
Parser Negative Tests

Tests for parser error handling.
"""

import pytest
from silk.lexer import Lexer
from silk.parser import Parser
from silk.errors import ParseError


def parse(source: str):
    """Helper to parse source code."""
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    return parser.parse()


class TestParseErrors:
    """Test that parser raises appropriate errors."""

    def test_missing_rbrace(self):
        with pytest.raises(ParseError) as exc:
            parse("if true { print(1)")
        assert "RBRACE" in str(exc.value) or "}" in str(exc.value)

    def test_missing_rparen(self):
        with pytest.raises(ParseError) as exc:
            parse("fn add(a, b { return a }")
        assert "RPAREN" in str(exc.value) or ")" in str(exc.value)

    def test_missing_expression(self):
        with pytest.raises(ParseError) as exc:
            parse("let x =")
        # Should error on unexpected EOF

    def test_invalid_let_syntax(self):
        with pytest.raises(ParseError) as exc:
            parse("let = 5")
        assert "IDENTIFIER" in str(exc.value)

    def test_missing_in_keyword(self):
        with pytest.raises(ParseError) as exc:
            parse("for i items { }")
        assert "IN" in str(exc.value) or "in" in str(exc.value).lower()

    def test_unexpected_token(self):
        with pytest.raises(ParseError) as exc:
            parse("let x = )")
        # Should report unexpected token

    def test_unclosed_array(self):
        with pytest.raises(ParseError) as exc:
            parse("[1, 2, 3")
        assert "RBRACKET" in str(exc.value) or "]" in str(exc.value)

    def test_missing_condition(self):
        with pytest.raises(ParseError) as exc:
            parse("if { print(1) }")
        # Should error on missing condition

    def test_missing_function_body(self):
        with pytest.raises(ParseError) as exc:
            parse("fn test()")
        assert "LBRACE" in str(exc.value) or "{" in str(exc.value)

    def test_error_includes_line_col(self):
        with pytest.raises(ParseError) as exc:
            parse("let x =\nlet y = )")
        # ParseError should have line/col info
        error = exc.value
        assert hasattr(error, 'line') or 'line' in str(error).lower()
```

**Step 2: Run negative tests**

```bash
pytest tests/test_parser_negative.py -v
```

**Step 3: Commit**

```bash
git add tests/test_parser_negative.py
git commit -m "test: add parser negative tests for error handling"
```

---

### Task 0.4: Add Golden Tests Infrastructure

**Files:**
- Create: `tests/golden/` directory
- Create: `tests/test_golden.py`
- Create: `tests/golden/basic.silk` + `tests/golden/basic.expected`

**Step 1: Create golden test runner**

```python
"""
Golden Tests

Tests that compare program output against expected output files.
"""

import pytest
from pathlib import Path
from silk.interpreter import Interpreter


GOLDEN_DIR = Path(__file__).parent / "golden"


def get_golden_tests():
    """Discover all .silk files with matching .expected files."""
    tests = []
    for silk_file in GOLDEN_DIR.glob("*.silk"):
        expected_file = silk_file.with_suffix(".expected")
        if expected_file.exists():
            tests.append((silk_file.stem, silk_file, expected_file))
    return tests


@pytest.mark.parametrize("name,silk_file,expected_file", get_golden_tests())
def test_golden(name, silk_file, expected_file):
    """Run silk file and compare output to expected."""
    source = silk_file.read_text()
    expected = expected_file.read_text().strip()

    interp = Interpreter()
    interp.run(source)

    actual = "\n".join(interp.output_lines).strip()
    assert actual == expected, f"Golden test '{name}' failed:\nExpected:\n{expected}\n\nActual:\n{actual}"
```

**Step 2: Create first golden test**

`tests/golden/basic.silk`:
```
let x = 5
let y = 10
print(x + y)
print("Hello, Silk!")
```

`tests/golden/basic.expected`:
```
15
Hello, Silk!
```

**Step 3: Create medical golden test**

`tests/golden/medical.silk`:
```
let weight = 70.0
let height = 1.75
let result = bmi(weight, height)
print(result)
```

`tests/golden/medical.expected`:
```
22.86
```

**Step 4: Create loops golden test**

`tests/golden/loops.silk`:
```
let mut sum = 0
for i in range(1, 6) {
    sum += i
}
print(sum)
```

`tests/golden/loops.expected`:
```
15
```

**Step 5: Run golden tests**

```bash
mkdir -p tests/golden
pytest tests/test_golden.py -v
```

**Step 6: Commit**

```bash
git add tests/golden/ tests/test_golden.py
git commit -m "test: add golden test infrastructure with basic tests"
```

---

### Task 0.5: Add More Interpreter Tests for Coverage

**Files:**
- Modify: `tests/test_interpreter.py`

**Step 1: Add tests for uncovered builtin functions**

Add to `tests/test_interpreter.py`:

```python
class TestBuiltinFunctions:
    """Test built-in functions for coverage."""

    def test_type_int(self, interp):
        interp.run('print(type(42))')
        assert interp.output_lines[-1] == "int"

    def test_type_str(self, interp):
        interp.run('print(type("hello"))')
        assert interp.output_lines[-1] == "str"

    def test_type_float(self, interp):
        interp.run('print(type(3.14))')
        assert interp.output_lines[-1] == "float"

    def test_type_bool(self, interp):
        interp.run('print(type(true))')
        assert interp.output_lines[-1] == "bool"

    def test_type_array(self, interp):
        interp.run('print(type([1, 2, 3]))')
        assert interp.output_lines[-1] == "list"

    def test_str_conversion(self, interp):
        interp.run('print(str(42))')
        assert interp.output_lines[-1] == "42"

    def test_int_conversion(self, interp):
        interp.run('print(int("42"))')
        assert interp.output_lines[-1] == "42"

    def test_float_conversion(self, interp):
        interp.run('print(float("3.14"))')
        assert interp.output_lines[-1] == "3.14"

    def test_bool_conversion_truthy(self, interp):
        interp.run('print(bool(1))')
        assert interp.output_lines[-1] == "true"

    def test_bool_conversion_falsy(self, interp):
        interp.run('print(bool(0))')
        assert interp.output_lines[-1] == "false"

    def test_len_array(self, interp):
        interp.run('print(len([1, 2, 3]))')
        assert interp.output_lines[-1] == "3"

    def test_len_string(self, interp):
        interp.run('print(len("hello"))')
        assert interp.output_lines[-1] == "5"

    def test_range_basic(self, interp):
        interp.run('print(range(5))')
        assert "[0, 1, 2, 3, 4]" in interp.output_lines[-1]

    def test_range_start_end(self, interp):
        interp.run('print(range(2, 5))')
        assert "[2, 3, 4]" in interp.output_lines[-1]

    def test_push(self, interp):
        interp.run('let mut arr = [1, 2]\npush(arr, 3)\nprint(arr)')
        assert "[1, 2, 3]" in interp.output_lines[-1]

    def test_pop(self, interp):
        interp.run('let mut arr = [1, 2, 3]\nlet x = pop(arr)\nprint(x)')
        assert interp.output_lines[-1] == "3"

    def test_slice(self, interp):
        interp.run('print(slice([1, 2, 3, 4], 1, 3))')
        assert "[2, 3]" in interp.output_lines[-1]

    def test_reverse(self, interp):
        interp.run('print(reverse([1, 2, 3]))')
        assert "[3, 2, 1]" in interp.output_lines[-1]

    def test_sort(self, interp):
        interp.run('print(sort([3, 1, 2]))')
        assert "[1, 2, 3]" in interp.output_lines[-1]

    def test_join(self, interp):
        interp.run('print(join(["a", "b", "c"], "-"))')
        assert interp.output_lines[-1] == "a-b-c"

    def test_split(self, interp):
        interp.run('print(split("a-b-c", "-"))')
        assert '["a", "b", "c"]' in interp.output_lines[-1]

    def test_contains_true(self, interp):
        interp.run('print(contains([1, 2, 3], 2))')
        assert interp.output_lines[-1] == "true"

    def test_contains_false(self, interp):
        interp.run('print(contains([1, 2, 3], 5))')
        assert interp.output_lines[-1] == "false"


class TestMathFunctions:
    """Test math functions."""

    def test_abs_positive(self, interp):
        interp.run('print(abs(5))')
        assert interp.output_lines[-1] == "5"

    def test_abs_negative(self, interp):
        interp.run('print(abs(-5))')
        assert interp.output_lines[-1] == "5"

    def test_round(self, interp):
        interp.run('print(round(3.7))')
        assert interp.output_lines[-1] == "4"

    def test_min(self, interp):
        interp.run('print(min(3, 1, 4, 1, 5))')
        assert interp.output_lines[-1] == "1"

    def test_max(self, interp):
        interp.run('print(max(3, 1, 4, 1, 5))')
        assert interp.output_lines[-1] == "5"

    def test_sum(self, interp):
        interp.run('print(sum([1, 2, 3, 4]))')
        assert interp.output_lines[-1] == "10"

    def test_sqrt(self, interp):
        interp.run('print(sqrt(16))')
        assert interp.output_lines[-1] == "4.0"

    def test_pow(self, interp):
        interp.run('print(pow(2, 3))')
        assert interp.output_lines[-1] == "8"

    def test_ceil(self, interp):
        interp.run('print(ceil(3.2))')
        assert interp.output_lines[-1] == "4"

    def test_floor(self, interp):
        interp.run('print(floor(3.8))')
        assert interp.output_lines[-1] == "3"


class TestMedicalFunctions:
    """Test medical calculation functions."""

    def test_bmi(self, interp):
        interp.run('print(bmi(70, 1.75))')
        assert "22.86" in interp.output_lines[-1]

    def test_bsa(self, interp):
        interp.run('print(bsa(70, 175))')
        # DuBois formula
        assert float(interp.output_lines[-1]) > 1.8

    def test_ideal_body_weight_male(self, interp):
        interp.run('print(ideal_body_weight(180, true))')
        assert float(interp.output_lines[-1]) > 70

    def test_ideal_body_weight_female(self, interp):
        interp.run('print(ideal_body_weight(165, false))')
        assert float(interp.output_lines[-1]) > 50

    def test_dose_per_kg(self, interp):
        interp.run('print(dose_per_kg(15, 25))')
        assert interp.output_lines[-1] == "375"

    def test_celsius_to_fahrenheit(self, interp):
        interp.run('print(celsius_to_fahrenheit(37))')
        assert "98.6" in interp.output_lines[-1]

    def test_fahrenheit_to_celsius(self, interp):
        interp.run('print(fahrenheit_to_celsius(98.6))')
        assert "37" in interp.output_lines[-1]

    def test_mean(self, interp):
        interp.run('print(mean([2, 4, 6, 8]))')
        assert interp.output_lines[-1] == "5.0"

    def test_median_odd(self, interp):
        interp.run('print(median([1, 3, 5, 7, 9]))')
        assert interp.output_lines[-1] == "5"

    def test_median_even(self, interp):
        interp.run('print(median([1, 2, 3, 4]))')
        assert interp.output_lines[-1] == "2.5"


class TestStringMethods:
    """Test string methods."""

    def test_upper(self, interp):
        interp.run('print("hello".upper())')
        assert interp.output_lines[-1] == "HELLO"

    def test_lower(self, interp):
        interp.run('print("HELLO".lower())')
        assert interp.output_lines[-1] == "hello"

    def test_strip(self, interp):
        interp.run('print("  hello  ".strip())')
        assert interp.output_lines[-1] == "hello"

    def test_replace(self, interp):
        interp.run('print("hello".replace("l", "L"))')
        assert interp.output_lines[-1] == "heLLo"

    def test_starts_with_true(self, interp):
        interp.run('print("hello".starts_with("he"))')
        assert interp.output_lines[-1] == "true"

    def test_starts_with_false(self, interp):
        interp.run('print("hello".starts_with("wo"))')
        assert interp.output_lines[-1] == "false"

    def test_ends_with_true(self, interp):
        interp.run('print("hello".ends_with("lo"))')
        assert interp.output_lines[-1] == "true"

    def test_ends_with_false(self, interp):
        interp.run('print("hello".ends_with("la"))')
        assert interp.output_lines[-1] == "false"
```

**Step 2: Run all tests and check coverage**

```bash
pytest --cov=src/silk --cov-report=term-missing -v
```
Expected: Coverage >= 80%

**Step 3: Commit**

```bash
git add tests/test_interpreter.py
git commit -m "test: add comprehensive builtin and medical function tests"
```

---

### Task 0.6: Improve Error Messages

**Files:**
- Modify: `src/silk/errors.py`
- Modify: `src/silk/interpreter.py`

**Step 1: Enhance error class with source context**

```python
# In src/silk/errors.py, replace the entire file:

"""
Silk Error Classes

Custom exceptions for lexer, parser, and runtime errors.
"""


class SilkError(Exception):
    """Base class for all Silk errors."""

    def __init__(self, message: str, line: int = 0, col: int = 0, source_line: str = ""):
        self.message = message
        self.line = line
        self.col = col
        self.source_line = source_line
        super().__init__(self._format_message())

    def _format_message(self) -> str:
        """Format error message with location and context."""
        msg = f"[Line {self.line}, Col {self.col}] {self.message}"
        if self.source_line:
            msg += f"\n  | {self.source_line}"
            if self.col > 0:
                msg += f"\n  | {' ' * (self.col - 1)}^"
        return msg


class LexerError(SilkError):
    """Error during tokenization."""
    pass


class ParseError(SilkError):
    """Error during parsing."""
    pass


class RuntimeError_(SilkError):
    """Error during execution."""
    pass


# Control flow signals (not actual errors)
class ReturnSignal(Exception):
    """Signal for function return."""
    def __init__(self, value=None):
        self.value = value


class BreakSignal(Exception):
    """Signal for loop break."""
    pass


class ContinueSignal(Exception):
    """Signal for loop continue."""
    pass
```

**Step 2: Update lexer to pass source line context**

In `src/silk/lexer.py`, modify error raising to include context:

```python
# When raising LexerError, include the source line:
# Find the current line from self.source
def _get_current_line(self) -> str:
    """Get the current source line for error context."""
    lines = self.source.split('\n')
    if 0 < self.line <= len(lines):
        return lines[self.line - 1]
    return ""
```

**Step 3: Run tests to ensure no regressions**

```bash
pytest -v
```

**Step 4: Commit**

```bash
git add src/silk/errors.py src/silk/lexer.py
git commit -m "feat: improve error messages with source context"
```

---

### Task 0.7: Verify 80%+ Coverage

**Files:**
- None (verification only)

**Step 1: Run full coverage report**

```bash
pytest --cov=src/silk --cov-report=term-missing --cov-report=html
```

**Step 2: Verify coverage >= 80%**

Expected: TOTAL coverage >= 80%

**Step 3: Open HTML report for review**

```bash
open htmlcov/index.html
```

**Step 4: Create Phase 0 completion commit**

```bash
git add .
git commit -m "milestone: Phase 0 complete - 80%+ test coverage achieved"
```

---

## Phase 1: Type System

**Architecture Decision:** Add type system features incrementally. Each feature is complete and tested before starting the next.

**Order:**
1. Struct (data only)
2. Enum (simple variants)
3. Match (with exhaustiveness checking)
4. Option<T> / Result<T,E> (built-in)
5. impl blocks (methods)
6. interface (polymorphism)

---

### Task 1.1: Add Struct Token Types

**Files:**
- Modify: `src/silk/tokens.py`

**Step 1: Add STRUCT token type**

In `src/silk/tokens.py`, add to TokenType enum:

```python
# In the TokenType enum, add after existing keywords:
STRUCT = auto()      # struct keyword
```

And in KEYWORDS dict:

```python
# In KEYWORDS dict:
'struct': TokenType.STRUCT,
```

**Step 2: Run lexer tests**

```bash
pytest tests/test_lexer.py -v
```

**Step 3: Add lexer test for struct keyword**

```python
# In tests/test_lexer.py, add:
def test_struct_keyword(self, lexer):
    tokens = lexer("struct").tokenize()
    assert tokens[0].type == TokenType.STRUCT
```

**Step 4: Commit**

```bash
git add src/silk/tokens.py tests/test_lexer.py
git commit -m "feat(lexer): add struct keyword token"
```

---

### Task 1.2: Add Struct AST Node

**Files:**
- Modify: `src/silk/ast.py`

**Step 1: Add StructDef and StructInstance nodes**

```python
# In src/silk/ast.py, add:

@dataclass
class StructField:
    """A field in a struct definition."""
    name: str
    type_hint: str | None = None


@dataclass
class StructDef:
    """Struct definition: struct Name { field: type, ... }"""
    name: str
    fields: list[StructField]


@dataclass
class StructInstance:
    """Struct instantiation: Name { field: value, ... }"""
    struct_name: str
    field_values: dict[str, any]  # field_name -> value expression
```

**Step 2: Commit**

```bash
git add src/silk/ast.py
git commit -m "feat(ast): add StructDef and StructInstance nodes"
```

---

### Task 1.3: Parse Struct Definition

**Files:**
- Modify: `src/silk/parser.py`
- Create: `tests/test_types/test_struct.py`

**Step 1: Write failing test**

```python
# tests/test_types/test_struct.py
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
```

**Step 2: Run test to verify it fails**

```bash
pytest tests/test_types/test_struct.py -v
```
Expected: FAIL (struct parsing not implemented)

**Step 3: Implement struct parsing in parser.py**

```python
# In src/silk/parser.py, add import:
from .ast import (..., StructDef, StructField, StructInstance)

# In parse_statement(), add case for struct:
elif t.type == TokenType.STRUCT:
    return self.parse_struct_def()

# Add the method:
def parse_struct_def(self) -> StructDef:
    """Parse struct definition."""
    self.eat(TokenType.STRUCT)
    name = self.eat(TokenType.IDENTIFIER).value
    self.eat(TokenType.LBRACE)
    self.skip_newlines()

    fields = []
    while not self.match(TokenType.RBRACE):
        field_name = self.eat(TokenType.IDENTIFIER).value
        field_type = None
        if self.match(TokenType.COLON):
            self.eat(TokenType.COLON)
            field_type = self.eat(TokenType.IDENTIFIER).value
        fields.append(StructField(field_name, field_type))

        if self.match(TokenType.COMMA):
            self.eat(TokenType.COMMA)
        self.skip_newlines()

    self.eat(TokenType.RBRACE)
    return StructDef(name, fields)
```

**Step 4: Run test to verify it passes**

```bash
pytest tests/test_types/test_struct.py -v
```
Expected: PASS

**Step 5: Commit**

```bash
git add src/silk/parser.py tests/test_types/
git commit -m "feat(parser): implement struct definition parsing"
```

---

### Task 1.4: Parse Struct Instantiation

**Files:**
- Modify: `src/silk/parser.py`
- Modify: `tests/test_types/test_struct.py`

**Step 1: Write failing test**

```python
# Add to tests/test_types/test_struct.py:

from silk.ast import StructInstance

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
```

**Step 2: Run test to verify it fails**

```bash
pytest tests/test_types/test_struct.py::TestStructInstantiation -v
```

**Step 3: Implement struct instantiation parsing**

In `parse_primary()`, after identifier parsing, check for struct instantiation:

```python
elif t.type == TokenType.IDENTIFIER:
    self.pos += 1
    # Check if this is a struct instantiation: Name { ... }
    if self.match(TokenType.LBRACE):
        return self.parse_struct_instance(t.value)
    return Identifier(t.value)

def parse_struct_instance(self, struct_name: str) -> StructInstance:
    """Parse struct instantiation: Name { field: value, ... }"""
    self.eat(TokenType.LBRACE)
    self.skip_newlines()

    field_values = {}
    while not self.match(TokenType.RBRACE):
        field_name = self.eat(TokenType.IDENTIFIER).value
        self.eat(TokenType.COLON)
        field_value = self.parse_expression()
        field_values[field_name] = field_value

        if self.match(TokenType.COMMA):
            self.eat(TokenType.COMMA)
        self.skip_newlines()

    self.eat(TokenType.RBRACE)
    return StructInstance(struct_name, field_values)
```

**Step 4: Run test to verify it passes**

```bash
pytest tests/test_types/test_struct.py -v
```

**Step 5: Commit**

```bash
git add src/silk/parser.py tests/test_types/test_struct.py
git commit -m "feat(parser): implement struct instantiation parsing"
```

---

### Task 1.5: Interpret Struct Definition and Instantiation

**Files:**
- Modify: `src/silk/interpreter.py`
- Modify: `tests/test_types/test_struct.py`

**Step 1: Write failing test**

```python
# Add to tests/test_types/test_struct.py:

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
        assert interp.output_lines[-1] == "7.0"

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
```

**Step 2: Run test to verify it fails**

```bash
pytest tests/test_types/test_struct.py::TestStructExecution -v
```

**Step 3: Implement struct in interpreter**

```python
# In src/silk/interpreter.py, add imports:
from .ast import (..., StructDef, StructField, StructInstance)

# Create a SilkStruct class to represent instances:
class SilkStruct:
    """Runtime representation of a struct instance."""
    def __init__(self, struct_name: str, fields: dict):
        self.struct_name = struct_name
        self.fields = fields

    def __repr__(self):
        field_str = ", ".join(f"{k}: {silk_repr(v)}" for k, v in self.fields.items())
        return f"{self.struct_name} {{ {field_str} }}"

# In execute(), handle StructDef:
elif isinstance(node, StructDef):
    # Store struct definition for later instantiation
    struct_info = ('struct_def', node.name, [(f.name, f.type_hint) for f in node.fields])
    env.define(node.name, struct_info, mutable=False)

# In evaluate(), handle StructInstance:
elif isinstance(node, StructInstance):
    struct_def = env.get(node.struct_name)
    if not isinstance(struct_def, tuple) or struct_def[0] != 'struct_def':
        raise RuntimeError_(f"'{node.struct_name}' is not a struct")

    _, _, field_defs = struct_def
    field_names = {f[0] for f in field_defs}

    # Validate all required fields are provided
    for provided in node.field_values.keys():
        if provided not in field_names:
            raise RuntimeError_(f"Unknown field '{provided}' in struct '{node.struct_name}'")

    # Evaluate field values
    fields = {}
    for name, expr in node.field_values.items():
        fields[name] = self.evaluate(expr, env)

    return SilkStruct(node.struct_name, fields)

# In _eval_member(), handle SilkStruct:
if isinstance(obj, SilkStruct):
    if member in obj.fields:
        return obj.fields[member]
    raise RuntimeError_(f"Struct '{obj.struct_name}' has no field '{member}'")
```

**Step 4: Update silk_repr in builtins/core.py**

```python
# Add handling for SilkStruct in silk_repr:
def silk_repr(value) -> str:
    # ... existing code ...
    # Add before the final return:
    if hasattr(value, 'struct_name') and hasattr(value, 'fields'):
        # SilkStruct
        field_str = ", ".join(f"{k}: {silk_repr(v)}" for k, v in value.fields.items())
        return f"{value.struct_name} {{ {field_str} }}"
```

**Step 5: Run test to verify it passes**

```bash
pytest tests/test_types/test_struct.py::TestStructExecution -v
```

**Step 6: Commit**

```bash
git add src/silk/interpreter.py src/silk/builtins/core.py tests/test_types/test_struct.py
git commit -m "feat(interpreter): implement struct definition and instantiation"
```

---

### Task 1.6: Add Enum Token and AST

**Files:**
- Modify: `src/silk/tokens.py`
- Modify: `src/silk/ast.py`

**Step 1: Add ENUM token**

```python
# In src/silk/tokens.py TokenType enum:
ENUM = auto()

# In KEYWORDS dict:
'enum': TokenType.ENUM,
```

**Step 2: Add EnumDef AST node**

```python
# In src/silk/ast.py:

@dataclass
class EnumVariant:
    """A variant in an enum definition."""
    name: str
    # For future: associated data


@dataclass
class EnumDef:
    """Enum definition: enum Name { Variant1, Variant2, ... }"""
    name: str
    variants: list[EnumVariant]


@dataclass
class EnumAccess:
    """Enum variant access: EnumName.Variant"""
    enum_name: str
    variant: str
```

**Step 3: Commit**

```bash
git add src/silk/tokens.py src/silk/ast.py
git commit -m "feat: add enum token and AST nodes"
```

---

### Task 1.7: Parse and Interpret Enum

**Files:**
- Modify: `src/silk/parser.py`
- Modify: `src/silk/interpreter.py`
- Create: `tests/test_types/test_enum.py`

**Step 1: Write failing tests**

```python
# tests/test_types/test_enum.py
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
```

**Step 2: Implement enum parsing**

```python
# In parser.py parse_statement():
elif t.type == TokenType.ENUM:
    return self.parse_enum_def()

def parse_enum_def(self) -> EnumDef:
    """Parse enum definition."""
    self.eat(TokenType.ENUM)
    name = self.eat(TokenType.IDENTIFIER).value
    self.eat(TokenType.LBRACE)
    self.skip_newlines()

    variants = []
    while not self.match(TokenType.RBRACE):
        variant_name = self.eat(TokenType.IDENTIFIER).value
        variants.append(EnumVariant(variant_name))

        if self.match(TokenType.COMMA):
            self.eat(TokenType.COMMA)
        self.skip_newlines()

    self.eat(TokenType.RBRACE)
    return EnumDef(name, variants)
```

**Step 3: Implement enum in interpreter**

```python
# In interpreter.py:

class SilkEnumValue:
    """Runtime representation of an enum variant."""
    def __init__(self, enum_name: str, variant: str):
        self.enum_name = enum_name
        self.variant = variant

    def __eq__(self, other):
        if isinstance(other, SilkEnumValue):
            return self.enum_name == other.enum_name and self.variant == other.variant
        return False

    def __repr__(self):
        return f"{self.enum_name}.{self.variant}"

# In execute(), handle EnumDef:
elif isinstance(node, EnumDef):
    variant_names = [v.name for v in node.variants]
    enum_info = ('enum_def', node.name, variant_names)
    env.define(node.name, enum_info, mutable=False)

# In _eval_member(), handle enum access:
# This happens when we see EnumName.Variant
if isinstance(obj, tuple) and obj[0] == 'enum_def':
    _, enum_name, variants = obj
    if member in variants:
        return SilkEnumValue(enum_name, member)
    raise RuntimeError_(f"Enum '{enum_name}' has no variant '{member}'")
```

**Step 4: Run tests**

```bash
pytest tests/test_types/test_enum.py -v
```

**Step 5: Commit**

```bash
git add src/silk/parser.py src/silk/interpreter.py tests/test_types/test_enum.py
git commit -m "feat: implement enum definition and variant access"
```

---

### Task 1.8: Add Match Token and AST

**Files:**
- Modify: `src/silk/tokens.py`
- Modify: `src/silk/ast.py`

**Step 1: Add MATCH token**

```python
# In tokens.py:
MATCH = auto()
ARROW_MATCH = auto()  # => for match arms

# In KEYWORDS:
'match': TokenType.MATCH,

# In lexer, recognize =>:
# After handling -> (ARROW), add:
elif self.char == '=' and self.peek() == '>':
    self.advance()
    self.advance()
    return Token(TokenType.ARROW_MATCH, '=>', self.line, start_col)
```

**Step 2: Add MatchExpr AST**

```python
# In ast.py:

@dataclass
class MatchArm:
    """A single arm in a match expression."""
    pattern: any  # Identifier, EnumAccess, or '_' wildcard
    guard: any | None  # Optional 'if' guard expression
    body: any  # Expression or block


@dataclass
class MatchExpr:
    """Match expression: match value { pattern => expr, ... }"""
    value: any
    arms: list[MatchArm]
```

**Step 3: Commit**

```bash
git add src/silk/tokens.py src/silk/ast.py src/silk/lexer.py
git commit -m "feat: add match token and AST nodes"
```

---

### Task 1.9: Parse Match Expression

**Files:**
- Modify: `src/silk/parser.py`
- Create: `tests/test_types/test_match.py`

**Step 1: Write failing tests**

```python
# tests/test_types/test_match.py
"""Tests for match expression parsing and evaluation."""

import pytest
from silk.lexer import Lexer
from silk.parser import Parser
from silk.interpreter import Interpreter
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
```

**Step 2: Implement match parsing**

```python
# In parser.py, add to parse_expression_statement() or parse_statement():
elif t.type == TokenType.MATCH:
    return self.parse_match()

def parse_match(self) -> MatchExpr:
    """Parse match expression."""
    self.eat(TokenType.MATCH)
    value = self.parse_expression()
    self.eat(TokenType.LBRACE)
    self.skip_newlines()

    arms = []
    while not self.match(TokenType.RBRACE):
        # Parse pattern
        if self.current().value == '_':
            pattern = Identifier('_')  # Wildcard
            self.pos += 1
        elif self.match(TokenType.IDENTIFIER):
            pattern = self.parse_postfix()  # Handles EnumName.Variant
        else:
            pattern = self.parse_primary()

        # Optional guard: if condition
        guard = None
        if self.match(TokenType.IF):
            self.eat(TokenType.IF)
            guard = self.parse_expression()

        self.eat(TokenType.ARROW_MATCH)

        # Parse body (expression or block)
        if self.match(TokenType.LBRACE):
            body = self.parse_block()
        else:
            body = self.parse_expression()

        arms.append(MatchArm(pattern, guard, body))

        if self.match(TokenType.COMMA):
            self.eat(TokenType.COMMA)
        self.skip_newlines()

    self.eat(TokenType.RBRACE)
    return MatchExpr(value, arms)
```

**Step 3: Run tests**

```bash
pytest tests/test_types/test_match.py::TestMatchParsing -v
```

**Step 4: Commit**

```bash
git add src/silk/parser.py tests/test_types/test_match.py
git commit -m "feat(parser): implement match expression parsing"
```

---

### Task 1.10: Implement Match with Exhaustiveness Check

**Files:**
- Modify: `src/silk/interpreter.py`
- Modify: `tests/test_types/test_match.py`

**Step 1: Write failing tests**

```python
# Add to tests/test_types/test_match.py:

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
        assert result is False  # Indicates error

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
```

**Step 2: Implement match evaluation with exhaustiveness**

```python
# In interpreter.py evaluate():

elif isinstance(node, MatchExpr):
    return self._eval_match(node, env)

def _eval_match(self, node: MatchExpr, env: Environment) -> Any:
    """Evaluate match expression with exhaustiveness check."""
    value = self.evaluate(node.value, env)

    # Check exhaustiveness for enum types
    if isinstance(value, SilkEnumValue):
        self._check_enum_exhaustiveness(value.enum_name, node.arms, env)

    # Find matching arm
    for arm in node.arms:
        if self._pattern_matches(value, arm.pattern, env):
            # Check guard if present
            if arm.guard is not None:
                guard_result = self.evaluate(arm.guard, env)
                if not _truthy(guard_result):
                    continue

            # Execute body
            if isinstance(arm.body, list):
                # Block
                match_env = Environment(parent=env)
                for stmt in arm.body:
                    result = self.execute(stmt, match_env)
                return None
            else:
                # Expression
                return self.evaluate(arm.body, env)

    raise RuntimeError_(f"No matching pattern for value: {value}")

def _check_enum_exhaustiveness(self, enum_name: str, arms: list, env: Environment) -> None:
    """Verify all enum variants are covered."""
    enum_def = env.get(enum_name)
    if not isinstance(enum_def, tuple) or enum_def[0] != 'enum_def':
        return  # Not an enum, skip check

    _, _, all_variants = enum_def
    covered_variants = set()
    has_wildcard = False

    for arm in arms:
        if isinstance(arm.pattern, Identifier) and arm.pattern.name == '_':
            has_wildcard = True
        elif isinstance(arm.pattern, MemberAccess):
            covered_variants.add(arm.pattern.member)
        elif isinstance(arm.pattern, Identifier):
            # Could be a variant name directly
            covered_variants.add(arm.pattern.name)

    if has_wildcard:
        return  # Wildcard covers everything

    missing = set(all_variants) - covered_variants
    if missing:
        raise RuntimeError_(
            f"Non-exhaustive match on enum '{enum_name}'. "
            f"Missing variants: {', '.join(sorted(missing))}. "
            f"Add missing cases or use '_' wildcard."
        )

def _pattern_matches(self, value: Any, pattern: Any, env: Environment) -> bool:
    """Check if value matches pattern."""
    if isinstance(pattern, Identifier):
        if pattern.name == '_':
            return True  # Wildcard matches everything
        # Check if it's an enum variant name
        if isinstance(value, SilkEnumValue):
            return value.variant == pattern.name
        return False

    if isinstance(pattern, MemberAccess):
        # EnumName.Variant pattern
        if isinstance(value, SilkEnumValue):
            return value.variant == pattern.member
        return False

    if isinstance(pattern, (NumberLiteral, StringLiteral, BoolLiteral)):
        return value == pattern.value

    return False
```

**Step 3: Run tests**

```bash
pytest tests/test_types/test_match.py -v
```

**Step 4: Commit**

```bash
git add src/silk/interpreter.py tests/test_types/test_match.py
git commit -m "feat: implement match with exhaustiveness checking (critical for medical safety)"
```

---

### Task 1.11: Add Option<T> Built-in Type

**Files:**
- Modify: `src/silk/interpreter.py`
- Modify: `src/silk/builtins/core.py`
- Create: `tests/test_types/test_option.py`

**Step 1: Write failing tests**

```python
# tests/test_types/test_option.py
"""Tests for Option<T> type."""

import pytest
from silk.interpreter import Interpreter


class TestOption:
    """Test Option<T> type."""

    @pytest.fixture
    def interp(self):
        return Interpreter()

    def test_some_value(self, interp):
        interp.run("""
let x = Some(42)
print(x)
""")
        assert "Some(42)" in interp.output_lines[-1]

    def test_none_value(self, interp):
        interp.run("""
let x = None
print(x)
""")
        assert interp.output_lines[-1] == "None"

    def test_match_some(self, interp):
        interp.run("""
let x = Some(42)
match x {
    Some(v) => print(v),
    None => print("nothing")
}
""")
        assert interp.output_lines[-1] == "42"

    def test_match_none(self, interp):
        interp.run("""
let x = None
match x {
    Some(v) => print(v),
    None => print("nothing")
}
""")
        assert interp.output_lines[-1] == "nothing"

    def test_option_exhaustiveness(self, interp):
        """Option match must cover both Some and None."""
        result = interp.run("""
let x = Some(42)
match x {
    Some(v) => print(v)
}
""")
        assert result is False  # Missing None case
```

**Step 2: Implement Option type**

```python
# In interpreter.py:

class SilkOption:
    """Option type: Some(value) or None."""
    def __init__(self, value=None, is_some: bool = False):
        self.value = value
        self.is_some = is_some

    def __repr__(self):
        if self.is_some:
            return f"Some({silk_repr(self.value)})"
        return "None"

    def __eq__(self, other):
        if isinstance(other, SilkOption):
            if self.is_some != other.is_some:
                return False
            if self.is_some:
                return self.value == other.value
            return True
        return False

# Add Some() builtin function:
def builtin_some(args, ctx):
    if len(args) != 1:
        raise RuntimeError_("Some() takes exactly 1 argument")
    return SilkOption(args[0], is_some=True)

# Add to ALL_BUILTINS:
'Some': builtin_some,

# Make None a SilkOption in the global env or handle specially
```

**Step 3: Update match to handle Option**

```python
# In _eval_match and _pattern_matches, add Option handling:

def _check_option_exhaustiveness(self, arms: list) -> None:
    """Verify Option is fully matched."""
    has_some = False
    has_none = False
    has_wildcard = False

    for arm in arms:
        if isinstance(arm.pattern, Identifier):
            if arm.pattern.name == '_':
                has_wildcard = True
            elif arm.pattern.name == 'None':
                has_none = True
        elif isinstance(arm.pattern, FunctionCall):
            if isinstance(arm.pattern.name, Identifier):
                if arm.pattern.name.name == 'Some':
                    has_some = True

    if has_wildcard:
        return

    missing = []
    if not has_some:
        missing.append('Some(_)')
    if not has_none:
        missing.append('None')

    if missing:
        raise RuntimeError_(
            f"Non-exhaustive Option match. Missing: {', '.join(missing)}"
        )
```

**Step 4: Run tests**

```bash
pytest tests/test_types/test_option.py -v
```

**Step 5: Commit**

```bash
git add src/silk/interpreter.py src/silk/builtins/core.py tests/test_types/test_option.py
git commit -m "feat: implement Option<T> with exhaustive match"
```

---

### Task 1.12: Add Result<T, E> Built-in Type

**Files:**
- Modify: `src/silk/interpreter.py`
- Modify: `src/silk/builtins/core.py`
- Create: `tests/test_types/test_result.py`

**Step 1: Write failing tests**

```python
# tests/test_types/test_result.py
"""Tests for Result<T, E> type."""

import pytest
from silk.interpreter import Interpreter


class TestResult:
    """Test Result<T, E> type."""

    @pytest.fixture
    def interp(self):
        return Interpreter()

    def test_ok_value(self, interp):
        interp.run("""
let x = Ok(42)
print(x)
""")
        assert "Ok(42)" in interp.output_lines[-1]

    def test_err_value(self, interp):
        interp.run("""
let x = Err("something went wrong")
print(x)
""")
        assert "Err" in interp.output_lines[-1]

    def test_match_ok(self, interp):
        interp.run("""
let x = Ok(42)
match x {
    Ok(v) => print(v),
    Err(e) => print(e)
}
""")
        assert interp.output_lines[-1] == "42"

    def test_match_err(self, interp):
        interp.run("""
let x = Err("error!")
match x {
    Ok(v) => print(v),
    Err(e) => print(e)
}
""")
        assert interp.output_lines[-1] == "error!"

    def test_result_exhaustiveness(self, interp):
        """Result match must cover both Ok and Err."""
        result = interp.run("""
let x = Ok(42)
match x {
    Ok(v) => print(v)
}
""")
        assert result is False  # Missing Err case

    def test_safe_division(self, interp):
        interp.run("""
fn safe_divide(a, b) -> Result {
    if b == 0 {
        return Err("Division by zero")
    }
    return Ok(a / b)
}

let result = safe_divide(10, 2)
match result {
    Ok(v) => print(v),
    Err(e) => print(e)
}
""")
        assert interp.output_lines[-1] == "5"
```

**Step 2: Implement Result type (similar to Option)**

```python
# In interpreter.py:

class SilkResult:
    """Result type: Ok(value) or Err(error)."""
    def __init__(self, value=None, error=None, is_ok: bool = True):
        self.value = value
        self.error = error
        self.is_ok = is_ok

    def __repr__(self):
        if self.is_ok:
            return f"Ok({silk_repr(self.value)})"
        return f"Err({silk_repr(self.error)})"

# Builtins:
def builtin_ok(args, ctx):
    if len(args) != 1:
        raise RuntimeError_("Ok() takes exactly 1 argument")
    return SilkResult(value=args[0], is_ok=True)

def builtin_err(args, ctx):
    if len(args) != 1:
        raise RuntimeError_("Err() takes exactly 1 argument")
    return SilkResult(error=args[0], is_ok=False)
```

**Step 3: Update exhaustiveness checking for Result**

```python
def _check_result_exhaustiveness(self, arms: list) -> None:
    """Verify Result is fully matched."""
    has_ok = False
    has_err = False
    has_wildcard = False

    for arm in arms:
        if isinstance(arm.pattern, Identifier) and arm.pattern.name == '_':
            has_wildcard = True
        elif isinstance(arm.pattern, FunctionCall):
            if isinstance(arm.pattern.name, Identifier):
                name = arm.pattern.name.name
                if name == 'Ok':
                    has_ok = True
                elif name == 'Err':
                    has_err = True

    if has_wildcard:
        return

    missing = []
    if not has_ok:
        missing.append('Ok(_)')
    if not has_err:
        missing.append('Err(_)')

    if missing:
        raise RuntimeError_(
            f"Non-exhaustive Result match. Missing: {', '.join(missing)}"
        )
```

**Step 4: Run tests**

```bash
pytest tests/test_types/test_result.py -v
```

**Step 5: Commit**

```bash
git add src/silk/interpreter.py src/silk/builtins/core.py tests/test_types/test_result.py
git commit -m "feat: implement Result<T, E> with exhaustive match"
```

---

### Task 1.13: Final Phase 1 Verification

**Files:**
- None (verification only)

**Step 1: Run full test suite**

```bash
pytest --cov=src/silk --cov-report=term-missing -v
```
Expected: All tests pass, coverage >= 80%

**Step 2: Create example medical code with new features**

Create `examples/patient_assessment.silk`:
```silk
// Patient Assessment with Silk Type System

struct Patient {
    id: str,
    name: str,
    age: int,
    weight: float,
    height: float
}

enum BMICategory {
    Underweight,
    Normal,
    Overweight,
    Obese
}

fn classify_bmi(patient: Patient) -> BMICategory {
    let bmi_value = bmi(patient.weight, patient.height)
    match bmi_value {
        _ if bmi_value < 18.5 => Underweight,
        _ if bmi_value < 25.0 => Normal,
        _ if bmi_value < 30.0 => Overweight,
        _ => Obese
    }
}

fn safe_dose(mg_per_kg: float, weight: float) -> Result {
    if weight <= 0 {
        return Err("Invalid weight")
    }
    if mg_per_kg <= 0 {
        return Err("Invalid dosage")
    }
    return Ok(mg_per_kg * weight)
}

// Main program
let patient = Patient {
    id: "P001",
    name: "Ahmad",
    age: 8,
    weight: 25.0,
    height: 1.20
}

print("Patient: " + patient.name)
print("BMI: " + str(bmi(patient.weight, patient.height)))

match classify_bmi(patient) {
    Underweight => print("Status: Consider nutritional support"),
    Normal => print("Status: Healthy weight"),
    Overweight => print("Status: Recommend lifestyle changes"),
    Obese => print("Status: Medical intervention needed")
}

// Calculate medication dose
let amox_dose = safe_dose(15.0, patient.weight)
match amox_dose {
    Ok(dose) => print("Amoxicillin dose: " + str(dose) + " mg"),
    Err(e) => print("Error: " + e)
}
```

**Step 3: Run example**

```bash
silk run examples/patient_assessment.silk
```

**Step 4: Create Phase 1 milestone commit**

```bash
git add .
git commit -m "milestone: Phase 1 complete - struct, enum, match with exhaustiveness, Option, Result"
```

---

## Summary

**Phase 0 Tasks:**
- 0.1: Fix index out of bounds bug ✓
- 0.2: Add parser tests ✓
- 0.3: Add parser negative tests ✓
- 0.4: Add golden tests ✓
- 0.5: Add builtin function tests ✓
- 0.6: Improve error messages ✓
- 0.7: Verify 80%+ coverage ✓

**Phase 1 Tasks:**
- 1.1-1.5: Struct (tokens, AST, parsing, interpretation)
- 1.6-1.7: Enum (tokens, AST, parsing, interpretation)
- 1.8-1.10: Match with exhaustiveness checking
- 1.11: Option<T> type
- 1.12: Result<T, E> type
- 1.13: Final verification

**Key Safety Feature:** Exhaustiveness checking on match expressions is MANDATORY for medical safety. Non-exhaustive matches produce errors, not warnings.

---

Plan complete and saved to `docs/plans/2026-02-05-silk-phase0-phase1-implementation.md`. Two execution options:

**1. Subagent-Driven (this session)** - I dispatch fresh subagent per task, review between tasks, fast iteration

**2. Parallel Session (separate)** - Open new session with executing-plans, batch execution with checkpoints

**Which approach?**
