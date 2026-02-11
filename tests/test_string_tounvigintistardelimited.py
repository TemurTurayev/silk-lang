"""
Tests for string .toUnvigintiStarDelimited() method - join words with 21 stars.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiStarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiStarDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiStarDelimited())')
        assert output[-1] == "hello" + "*" * 21 + "world"

    def test_toUnvigintiStarDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiStarDelimited())')
        assert output[-1] == "a" + "*" * 21 + "b" + "*" * 21 + "c"
