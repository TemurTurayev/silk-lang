"""
Tests for string .indent(n) method.
"""

from silk.interpreter import Interpreter


class TestStringIndent:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_indent_basic(self):
        output = self._run(r'print("hello\nworld".indent(2))')
        assert output[-1] == "  hello\n  world"

    def test_indent_single_line(self):
        output = self._run('print("hello".indent(4))')
        assert output[-1] == "    hello"

    def test_indent_zero(self):
        output = self._run('print("hello".indent(0))')
        assert output[-1] == "hello"
