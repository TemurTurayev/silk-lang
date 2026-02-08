"""
Tests for string .toNonStarDelimited() method - split words by ********* (9 stars).
"""

from silk.interpreter import Interpreter


class TestStringToNonStarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonStarDelimited_basic(self):
        output = self._run('print("hello world".toNonStarDelimited())')
        assert output[-1] == "hello*********world"

    def test_toNonStarDelimited_three(self):
        output = self._run('print("a b c".toNonStarDelimited())')
        assert output[-1] == "a*********b*********c"
