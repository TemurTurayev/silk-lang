"""
Tests for string .toQuadSemicolonDelimited() method - split words by ;;;;.
"""

from silk.interpreter import Interpreter


class TestStringToQuadSemicolonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuadSemicolonDelimited_basic(self):
        output = self._run('print("hello world".toQuadSemicolonDelimited())')
        assert output[-1] == "hello;;;;world"

    def test_toQuadSemicolonDelimited_three(self):
        output = self._run('print("a b c".toQuadSemicolonDelimited())')
        assert output[-1] == "a;;;;b;;;;c"
