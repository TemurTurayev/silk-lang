"""
Pytest configuration and fixtures for Silk tests.
"""

import sys
import os
import pytest

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from silk.lexer import Lexer
from silk.parser import Parser
from silk.interpreter import Interpreter


@pytest.fixture
def lexer():
    """Create a fresh lexer factory."""
    def _lexer(source: str) -> Lexer:
        return Lexer(source)
    return _lexer


@pytest.fixture
def parser():
    """Create a fresh parser factory."""
    def _parser(source: str) -> Parser:
        lex = Lexer(source)
        tokens = lex.tokenize()
        return Parser(tokens)
    return _parser


@pytest.fixture
def interpreter():
    """Create a fresh interpreter."""
    return Interpreter()


@pytest.fixture
def interp():
    """Create a fresh interpreter for testing with run() and output_lines."""
    return Interpreter()


@pytest.fixture
def run_silk():
    """Run Silk code and return interpreter."""
    def _run(source: str) -> Interpreter:
        interp = Interpreter()
        interp.run(source)
        return interp
    return _run


@pytest.fixture
def evaluate_silk():
    """Evaluate a Silk expression and return result."""
    def _evaluate(source: str):
        interp = Interpreter()
        lex = Lexer(source)
        tokens = lex.tokenize()
        par = Parser(tokens)
        ast = par.parse()
        if ast.statements:
            return interp.evaluate(ast.statements[0], interp.global_env)
        return None
    return _evaluate
