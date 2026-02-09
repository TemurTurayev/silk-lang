"""
Tests for string .toOctodecStarDelimited() method - join words with 18 stars.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecStarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecStarDelimited_basic(self):
        output = self._run('print("hello world".toOctodecStarDelimited())')
        assert output[-1] == "hello" + "*" * 18 + "world"

    def test_toOctodecStarDelimited_three(self):
        output = self._run('print("a b c".toOctodecStarDelimited())')
        assert output[-1] == "a" + "*" * 18 + "b" + "*" * 18 + "c"
