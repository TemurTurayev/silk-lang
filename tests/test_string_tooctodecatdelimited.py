"""
Tests for string .toOctodecAtDelimited() method - join words with 18 at signs.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecAtDelimited_basic(self):
        output = self._run('print("hello world".toOctodecAtDelimited())')
        assert output[-1] == "hello" + "@" * 18 + "world"

    def test_toOctodecAtDelimited_three(self):
        output = self._run('print("a b c".toOctodecAtDelimited())')
        assert output[-1] == "a" + "@" * 18 + "b" + "@" * 18 + "c"
