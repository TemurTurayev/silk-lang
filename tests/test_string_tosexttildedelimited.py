"""
Tests for string .toSextTildeDelimited() method - split words by ~~~~~~.
"""

from silk.interpreter import Interpreter


class TestStringToSextTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSextTildeDelimited_basic(self):
        output = self._run('print("hello world".toSextTildeDelimited())')
        assert output[-1] == "hello~~~~~~world"

    def test_toSextTildeDelimited_three(self):
        output = self._run('print("a b c".toSextTildeDelimited())')
        assert output[-1] == "a~~~~~~b~~~~~~c"
