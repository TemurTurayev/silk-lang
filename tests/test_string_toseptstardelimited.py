"""
Tests for string .toSeptStarDelimited() method - split words by *******.
"""

from silk.interpreter import Interpreter


class TestStringToSeptStarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptStarDelimited_basic(self):
        output = self._run('print("hello world".toSeptStarDelimited())')
        assert output[-1] == "hello*******world"

    def test_toSeptStarDelimited_three(self):
        output = self._run('print("a b c".toSeptStarDelimited())')
        assert output[-1] == "a*******b*******c"
