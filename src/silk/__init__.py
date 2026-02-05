"""
Silk Programming Language
Simple • Intuitive • Lightweight • Keen

A modern programming language designed for medical professionals
with power for experienced developers.

Version: 0.2.0
Author: Temur Turayev
"""

__version__ = "0.2.0"
__author__ = "Temur Turayev"

from .lexer import Lexer
from .parser import Parser
from .interpreter import Interpreter
from .errors import SilkError, LexerError, ParseError, RuntimeError_

__all__ = [
    "Lexer",
    "Parser",
    "Interpreter",
    "SilkError",
    "LexerError",
    "ParseError",
    "RuntimeError_",
    "__version__",
]
