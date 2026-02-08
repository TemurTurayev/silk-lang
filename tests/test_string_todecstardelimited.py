"""
Tests for string .toDecStarDelimited() method - split words by ********** (10 stars).
"""

from silk.interpreter import Interpreter


class TestStringToDecStarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecStarDelimited_basic(self):
        output = self._run('print("hello world".toDecStarDelimited())')
        assert output[-1] == "hello**********world"

    def test_toDecStarDelimited_three(self):
        output = self._run('print("a b c".toDecStarDelimited())')
        assert output[-1] == "a**********b**********c"
