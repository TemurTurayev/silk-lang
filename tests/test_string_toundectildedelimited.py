"""
Tests for string .toUndecTildeDelimited() method - split words by ~~~~~~~~~~~ (11 tildes).
"""

from silk.interpreter import Interpreter


class TestStringToUndecTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecTildeDelimited_basic(self):
        output = self._run('print("hello world".toUndecTildeDelimited())')
        assert output[-1] == "hello~~~~~~~~~~~world"

    def test_toUndecTildeDelimited_three(self):
        output = self._run('print("a b c".toUndecTildeDelimited())')
        assert output[-1] == "a~~~~~~~~~~~b~~~~~~~~~~~c"
