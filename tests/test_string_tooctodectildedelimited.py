"""
Tests for string .toOctodecTildeDelimited() method - join words with 18 tildes.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecTildeDelimited_basic(self):
        output = self._run('print("hello world".toOctodecTildeDelimited())')
        assert output[-1] == "hello" + "~" * 18 + "world"

    def test_toOctodecTildeDelimited_three(self):
        output = self._run('print("a b c".toOctodecTildeDelimited())')
        assert output[-1] == "a" + "~" * 18 + "b" + "~" * 18 + "c"
