"""
Tests for string .toDecTildeDelimited() method - split words by ~~~~~~~~~~ (10 tildes).
"""

from silk.interpreter import Interpreter


class TestStringToDecTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecTildeDelimited_basic(self):
        output = self._run('print("hello world".toDecTildeDelimited())')
        assert output[-1] == "hello~~~~~~~~~~world"

    def test_toDecTildeDelimited_three(self):
        output = self._run('print("a b c".toDecTildeDelimited())')
        assert output[-1] == "a~~~~~~~~~~b~~~~~~~~~~c"
