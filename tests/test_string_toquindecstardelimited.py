"""
Tests for string .toQuindecStarDelimited() method - join words with 15 stars.
"""

from silk.interpreter import Interpreter


class TestStringToQuindecStarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuindecStarDelimited_basic(self):
        output = self._run('print("hello world".toQuindecStarDelimited())')
        assert output[-1] == "hello***************world"

    def test_toQuindecStarDelimited_three(self):
        output = self._run('print("a b c".toQuindecStarDelimited())')
        assert output[-1] == "a***************b***************c"
