"""
Tests for string .toTredecTildeDelimited() method - join words with 13 tildes.
"""

from silk.interpreter import Interpreter


class TestStringToTredecTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTredecTildeDelimited_basic(self):
        output = self._run('print("hello world".toTredecTildeDelimited())')
        assert output[-1] == "hello~~~~~~~~~~~~~world"

    def test_toTredecTildeDelimited_three(self):
        output = self._run('print("a b c".toTredecTildeDelimited())')
        assert output[-1] == "a~~~~~~~~~~~~~b~~~~~~~~~~~~~c"
