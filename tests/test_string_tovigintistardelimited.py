"""
Tests for string .toVigintiStarDelimited() method - join words with 20 asterisks.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiStarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiStarDelimited_basic(self):
        output = self._run('print("hello world".toVigintiStarDelimited())')
        assert output[-1] == "hello" + "*" * 20 + "world"

    def test_toVigintiStarDelimited_multi(self):
        output = self._run('print("a b c".toVigintiStarDelimited())')
        assert output[-1] == "a" + "*" * 20 + "b" + "*" * 20 + "c"
