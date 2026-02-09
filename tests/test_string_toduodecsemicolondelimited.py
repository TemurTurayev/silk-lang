"""
Tests for string .toDuodecSemicolonDelimited() method - split words by ;;;;;;;;;;;; (12 semicolons).
"""

from silk.interpreter import Interpreter


class TestStringToDuodecSemicolonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuodecSemicolonDelimited_basic(self):
        output = self._run('print("hello world".toDuodecSemicolonDelimited())')
        assert output[-1] == "hello;;;;;;;;;;;;world"

    def test_toDuodecSemicolonDelimited_three(self):
        output = self._run('print("a b c".toDuodecSemicolonDelimited())')
        assert output[-1] == "a;;;;;;;;;;;;b;;;;;;;;;;;;c"
