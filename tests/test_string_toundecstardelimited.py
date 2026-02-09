"""
Tests for string .toUndecStarDelimited() method - split words by *********** (11 stars).
"""

from silk.interpreter import Interpreter


class TestStringToUndecStarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecStarDelimited_basic(self):
        output = self._run('print("hello world".toUndecStarDelimited())')
        assert output[-1] == "hello***********world"

    def test_toUndecStarDelimited_three(self):
        output = self._run('print("a b c".toUndecStarDelimited())')
        assert output[-1] == "a***********b***********c"
