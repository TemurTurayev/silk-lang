"""
Tests for string .toOctTildeDelimited() method - split words by ~~~~~~~~.
"""

from silk.interpreter import Interpreter


class TestStringToOctTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctTildeDelimited_basic(self):
        output = self._run('print("hello world".toOctTildeDelimited())')
        assert output[-1] == "hello~~~~~~~~world"

    def test_toOctTildeDelimited_three(self):
        output = self._run('print("a b c".toOctTildeDelimited())')
        assert output[-1] == "a~~~~~~~~b~~~~~~~~c"
