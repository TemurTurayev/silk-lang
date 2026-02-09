"""
Tests for string .toSedecTildeDelimited() method - join words with 16 tildes.
"""

from silk.interpreter import Interpreter


class TestStringToSedecTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecTildeDelimited_basic(self):
        output = self._run('print("hello world".toSedecTildeDelimited())')
        assert output[-1] == "hello" + "~" * 16 + "world"

    def test_toSedecTildeDelimited_three(self):
        output = self._run('print("a b c".toSedecTildeDelimited())')
        assert output[-1] == "a" + "~" * 16 + "b" + "~" * 16 + "c"
