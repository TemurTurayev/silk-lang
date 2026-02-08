"""
Tests for string .toNonTildeDelimited() method - split words by ~~~~~~~~~ (9 tildes).
"""

from silk.interpreter import Interpreter


class TestStringToNonTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonTildeDelimited_basic(self):
        output = self._run('print("hello world".toNonTildeDelimited())')
        assert output[-1] == "hello~~~~~~~~~world"

    def test_toNonTildeDelimited_three(self):
        output = self._run('print("a b c".toNonTildeDelimited())')
        assert output[-1] == "a~~~~~~~~~b~~~~~~~~~c"
