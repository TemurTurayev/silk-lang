"""
Tests for string .toDuodecTildeDelimited() method - split words by ~~~~~~~~~~~~ (12 tildes).
"""

from silk.interpreter import Interpreter


class TestStringToDuodecTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuodecTildeDelimited_basic(self):
        output = self._run('print("hello world".toDuodecTildeDelimited())')
        assert output[-1] == "hello~~~~~~~~~~~~world"

    def test_toDuodecTildeDelimited_three(self):
        output = self._run('print("a b c".toDuodecTildeDelimited())')
        assert output[-1] == "a~~~~~~~~~~~~b~~~~~~~~~~~~c"
