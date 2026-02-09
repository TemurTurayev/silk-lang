"""
Tests for string .toQuindecTildeDelimited() method - join words with 15 tildes.
"""

from silk.interpreter import Interpreter


class TestStringToQuindecTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuindecTildeDelimited_basic(self):
        output = self._run('print("hello world".toQuindecTildeDelimited())')
        assert output[-1] == "hello~~~~~~~~~~~~~~~world"

    def test_toQuindecTildeDelimited_three(self):
        output = self._run('print("a b c".toQuindecTildeDelimited())')
        assert output[-1] == "a~~~~~~~~~~~~~~~b~~~~~~~~~~~~~~~c"
