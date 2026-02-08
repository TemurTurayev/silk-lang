"""
Tests for string .toUnicodeEscape() method - convert to \\uXXXX format.
"""

from silk.interpreter import Interpreter


class TestStringToUnicodeEscape:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnicodeEscape_A(self):
        output = self._run('print("A".toUnicodeEscape())')
        assert output[-1] == "\\u0041"

    def test_toUnicodeEscape_hi(self):
        output = self._run('print("hi".toUnicodeEscape())')
        assert output[-1] == "\\u0068\\u0069"
