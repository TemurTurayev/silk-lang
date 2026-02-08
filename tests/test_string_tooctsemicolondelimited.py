"""
Tests for string .toOctSemicolonDelimited() method - split words by ;;;;;;;;.
"""

from silk.interpreter import Interpreter


class TestStringToOctSemicolonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctSemicolonDelimited_basic(self):
        output = self._run('print("hello world".toOctSemicolonDelimited())')
        assert output[-1] == "hello;;;;;;;;world"

    def test_toOctSemicolonDelimited_three(self):
        output = self._run('print("a b c".toOctSemicolonDelimited())')
        assert output[-1] == "a;;;;;;;;b;;;;;;;;c"
