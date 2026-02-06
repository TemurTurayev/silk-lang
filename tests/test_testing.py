"""
Tests for Silk's built-in test framework.

Phase 2: test keyword, assert keyword, test runner.
"""

import pytest
from pathlib import Path
from silk.lexer import Lexer
from silk.tokens import TokenType
from silk.parser import Parser
from silk.ast import TestBlock, AssertStatement
from silk.interpreter import Interpreter
from silk.errors import RuntimeError_


# ═══════════════════════════════════════════════════════════
# LEXER TESTS
# ═══════════════════════════════════════════════════════════

class TestLexerTokens:
    """Test that 'test' and 'assert' are recognized as keywords."""

    def test_test_keyword(self):
        tokens = Lexer('test').tokenize()
        assert tokens[0].type == TokenType.TEST

    def test_assert_keyword(self):
        tokens = Lexer('assert').tokenize()
        assert tokens[0].type == TokenType.ASSERT

    def test_test_with_string(self):
        tokens = Lexer('test "my test"').tokenize()
        assert tokens[0].type == TokenType.TEST
        assert tokens[1].type == TokenType.STRING
        assert tokens[1].value == "my test"

    def test_assert_with_expression(self):
        tokens = Lexer('assert x == 5').tokenize()
        assert tokens[0].type == TokenType.ASSERT
        assert tokens[1].type == TokenType.IDENTIFIER


# ═══════════════════════════════════════════════════════════
# PARSER TESTS
# ═══════════════════════════════════════════════════════════

class TestParserTestBlock:
    """Test parsing of test blocks."""

    def test_parse_test_block(self):
        tokens = Lexer('test "basic math" {\n  assert 1 == 1\n}').tokenize()
        ast = Parser(tokens).parse()
        assert len(ast.statements) == 1
        assert isinstance(ast.statements[0], TestBlock)
        assert ast.statements[0].name == "basic math"

    def test_parse_test_block_body(self):
        tokens = Lexer('test "setup" {\n  let x = 5\n  assert x == 5\n}').tokenize()
        ast = Parser(tokens).parse()
        block = ast.statements[0]
        assert isinstance(block, TestBlock)
        assert len(block.body) == 2  # let + assert

    def test_parse_assert_statement(self):
        tokens = Lexer('test "t" {\n  assert true\n}').tokenize()
        ast = Parser(tokens).parse()
        block = ast.statements[0]
        assert isinstance(block.body[0], AssertStatement)

    def test_parse_assert_with_comparison(self):
        tokens = Lexer('test "t" {\n  assert 2 + 2 == 4\n}').tokenize()
        ast = Parser(tokens).parse()
        block = ast.statements[0]
        assert isinstance(block.body[0], AssertStatement)

    def test_parse_multiple_tests(self):
        source = '''
test "first" {
    assert true
}
test "second" {
    assert 1 == 1
}
'''
        tokens = Lexer(source).tokenize()
        ast = Parser(tokens).parse()
        assert len(ast.statements) == 2
        assert isinstance(ast.statements[0], TestBlock)
        assert isinstance(ast.statements[1], TestBlock)
        assert ast.statements[0].name == "first"
        assert ast.statements[1].name == "second"

    def test_parse_assert_outside_test(self):
        """Assert works as a standalone statement too."""
        tokens = Lexer('assert 1 == 1').tokenize()
        ast = Parser(tokens).parse()
        assert len(ast.statements) == 1
        assert isinstance(ast.statements[0], AssertStatement)


# ═══════════════════════════════════════════════════════════
# INTERPRETER: ASSERT STATEMENT
# ═══════════════════════════════════════════════════════════

class TestAssertExecution:
    """Test assert statement execution."""

    def test_assert_true_passes(self):
        interp = Interpreter()
        interp.run('assert true')

    def test_assert_false_fails(self):
        interp = Interpreter()
        source = 'assert false'
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        with pytest.raises(RuntimeError_, match="Assertion failed"):
            interp.execute(ast, interp.global_env)

    def test_assert_comparison_true(self):
        interp = Interpreter()
        source = 'assert 2 + 2 == 4'
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interp.execute(ast, interp.global_env)  # Should not raise

    def test_assert_comparison_false(self):
        interp = Interpreter()
        source = 'assert 2 + 2 == 5'
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        with pytest.raises(RuntimeError_, match="Assertion failed"):
            interp.execute(ast, interp.global_env)

    def test_assert_with_variables(self):
        interp = Interpreter()
        source = 'let x = 10\nassert x == 10'
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interp.execute(ast, interp.global_env)  # Should not raise

    def test_assert_null_fails(self):
        interp = Interpreter()
        source = 'assert null'
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        with pytest.raises(RuntimeError_, match="Assertion failed"):
            interp.execute(ast, interp.global_env)

    def test_assert_zero_fails(self):
        interp = Interpreter()
        source = 'assert 0'
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        with pytest.raises(RuntimeError_, match="Assertion failed"):
            interp.execute(ast, interp.global_env)


# ═══════════════════════════════════════════════════════════
# INTERPRETER: TEST RUNNER
# ═══════════════════════════════════════════════════════════

class TestRunner:
    """Test the test runner functionality."""

    def test_tests_not_executed_in_normal_mode(self):
        """In normal run(), test blocks are skipped."""
        interp = Interpreter()
        source = '''
let x = 1
test "should not run" {
    assert false
}
'''
        assert interp.run(source) is True  # Should succeed, test not executed

    def test_run_tests_all_pass(self):
        """run_tests() executes all test blocks and returns results."""
        interp = Interpreter()
        source = '''
fn add(a, b) {
    return a + b
}

test "addition" {
    assert add(2, 3) == 5
}

test "negative" {
    assert add(-1, 1) == 0
}
'''
        results = interp.run_tests(source)
        assert results['passed'] == 2
        assert results['failed'] == 0
        assert results['total'] == 2

    def test_run_tests_with_failure(self):
        """Failing test is captured, doesn't crash."""
        interp = Interpreter()
        source = '''
test "passes" {
    assert 1 == 1
}

test "fails" {
    assert 1 == 2
}
'''
        results = interp.run_tests(source)
        assert results['passed'] == 1
        assert results['failed'] == 1
        assert results['total'] == 2

    def test_run_tests_failure_details(self):
        """Failed test includes name and error message."""
        interp = Interpreter()
        source = '''
test "bad math" {
    assert 2 + 2 == 5
}
'''
        results = interp.run_tests(source)
        assert results['failed'] == 1
        assert len(results['failures']) == 1
        assert results['failures'][0]['name'] == 'bad math'
        assert 'Assertion failed' in results['failures'][0]['error']

    def test_run_tests_isolation(self):
        """Each test runs in its own environment."""
        interp = Interpreter()
        source = '''
test "first" {
    let x = 42
    assert x == 42
}

test "second" {
    // x should not be visible from first test
    let x = 99
    assert x == 99
}
'''
        results = interp.run_tests(source)
        assert results['passed'] == 2
        assert results['failed'] == 0

    def test_run_tests_access_module_defs(self):
        """Tests can access functions and structs defined in the module."""
        interp = Interpreter()
        source = '''
fn double(x) {
    return x * 2
}

struct Point {
    x: int,
    y: int
}

test "function access" {
    assert double(5) == 10
}

test "struct access" {
    let p = Point { x: 1, y: 2 }
    assert p.x == 1
}
'''
        results = interp.run_tests(source)
        assert results['passed'] == 2
        assert results['failed'] == 0

    def test_run_tests_with_setup(self):
        """Tests can have setup code before assertions."""
        interp = Interpreter()
        source = '''
test "complex setup" {
    let values = [1, 2, 3, 4, 5]
    let mut total = 0
    for v in values {
        total += v
    }
    assert total == 15
}
'''
        results = interp.run_tests(source)
        assert results['passed'] == 1

    def test_run_tests_runtime_error_in_test(self):
        """Runtime error in test is captured as failure."""
        interp = Interpreter()
        source = '''
test "runtime error" {
    let x = 1 / 0
}
'''
        results = interp.run_tests(source)
        assert results['failed'] == 1
        assert 'Division by zero' in results['failures'][0]['error']

    def test_run_tests_empty(self):
        """No tests found returns zero counts."""
        interp = Interpreter()
        source = 'let x = 5'
        results = interp.run_tests(source)
        assert results['total'] == 0
        assert results['passed'] == 0
        assert results['failed'] == 0

    def test_run_tests_output_lines(self):
        """Test runner captures output summary."""
        interp = Interpreter()
        source = '''
test "passing" {
    assert true
}
'''
        results = interp.run_tests(source)
        # Check that output includes test results
        output = '\n'.join(interp.output_lines)
        assert 'passing' in output.lower() or 'PASS' in output or '1 passed' in output
