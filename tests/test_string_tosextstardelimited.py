"""
Tests for string .toSextStarDelimited() method - split words by ******.
"""

from silk.interpreter import Interpreter


class TestStringToSextStarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSextStarDelimited_basic(self):
        output = self._run('print("hello world".toSextStarDelimited())')
        assert output[-1] == "hello******world"

    def test_toSextStarDelimited_three(self):
        output = self._run('print("a b c".toSextStarDelimited())')
        assert output[-1] == "a******b******c"
