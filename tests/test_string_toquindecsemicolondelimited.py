"""
Tests for string .toQuindecSemicolonDelimited() method - join words with 15 semicolons.
"""

from silk.interpreter import Interpreter


class TestStringToQuindecSemicolonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuindecSemicolonDelimited_basic(self):
        output = self._run('print("hello world".toQuindecSemicolonDelimited())')
        assert output[-1] == "hello;;;;;;;;;;;;;;;world"

    def test_toQuindecSemicolonDelimited_three(self):
        output = self._run('print("a b c".toQuindecSemicolonDelimited())')
        assert output[-1] == "a;;;;;;;;;;;;;;;b;;;;;;;;;;;;;;;c"
