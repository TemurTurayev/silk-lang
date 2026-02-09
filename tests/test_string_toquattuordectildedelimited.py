"""
Tests for string .toQuattuordecTildeDelimited() method - join words with 14 tildes.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecTildeDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecTildeDelimited())')
        assert output[-1] == "hello~~~~~~~~~~~~~~world"

    def test_toQuattuordecTildeDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecTildeDelimited())')
        assert output[-1] == "a~~~~~~~~~~~~~~b~~~~~~~~~~~~~~c"
