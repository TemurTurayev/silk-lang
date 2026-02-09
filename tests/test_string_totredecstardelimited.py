"""
Tests for string .toTredecStarDelimited() method - join words with 13 stars.
"""

from silk.interpreter import Interpreter


class TestStringToTredecStarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTredecStarDelimited_basic(self):
        output = self._run('print("hello world".toTredecStarDelimited())')
        assert output[-1] == "hello*************world"

    def test_toTredecStarDelimited_three(self):
        output = self._run('print("a b c".toTredecStarDelimited())')
        assert output[-1] == "a*************b*************c"
