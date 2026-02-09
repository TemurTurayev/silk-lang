"""
Tests for string .toNovemdecStarDelimited() method - join words with 19 stars.
"""

from silk.interpreter import Interpreter


class TestStringToNovemdecStarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNovemdecStarDelimited_basic(self):
        output = self._run('print("hello world".toNovemdecStarDelimited())')
        assert output[-1] == "hello" + "*" * 19 + "world"

    def test_toNovemdecStarDelimited_three(self):
        output = self._run('print("a b c".toNovemdecStarDelimited())')
        assert output[-1] == "a" + "*" * 19 + "b" + "*" * 19 + "c"
