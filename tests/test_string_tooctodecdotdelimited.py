"""
Tests for string .toOctodecDotDelimited() method - join words with 18 dots.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecDotDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecDotDelimited_basic(self):
        output = self._run('print("hello world".toOctodecDotDelimited())')
        assert output[-1] == "hello" + "." * 18 + "world"

    def test_toOctodecDotDelimited_three(self):
        output = self._run('print("a b c".toOctodecDotDelimited())')
        assert output[-1] == "a" + "." * 18 + "b" + "." * 18 + "c"
