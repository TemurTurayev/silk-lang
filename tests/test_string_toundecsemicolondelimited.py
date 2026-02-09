"""
Tests for string .toUndecSemicolonDelimited() method - split words by ;;;;;;;;;;; (11 semicolons).
"""

from silk.interpreter import Interpreter


class TestStringToUndecSemicolonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecSemicolonDelimited_basic(self):
        output = self._run('print("hello world".toUndecSemicolonDelimited())')
        assert output[-1] == "hello;;;;;;;;;;;world"

    def test_toUndecSemicolonDelimited_three(self):
        output = self._run('print("a b c".toUndecSemicolonDelimited())')
        assert output[-1] == "a;;;;;;;;;;;b;;;;;;;;;;;c"
