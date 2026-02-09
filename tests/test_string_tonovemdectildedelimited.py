"""
Tests for string .toNovemdecTildeDelimited() method - join words with 19 tildes.
"""

from silk.interpreter import Interpreter


class TestStringToNovemdecTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNovemdecTildeDelimited_basic(self):
        output = self._run('print("hello world".toNovemdecTildeDelimited())')
        assert output[-1] == "hello" + "~" * 19 + "world"

    def test_toNovemdecTildeDelimited_three(self):
        output = self._run('print("a b c".toNovemdecTildeDelimited())')
        assert output[-1] == "a" + "~" * 19 + "b" + "~" * 19 + "c"
