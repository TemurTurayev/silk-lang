"""
Tests for string .toNonSemicolonDelimited() method - split words by ;;;;;;;;; (9 semicolons).
"""

from silk.interpreter import Interpreter


class TestStringToNonSemicolonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonSemicolonDelimited_basic(self):
        output = self._run('print("hello world".toNonSemicolonDelimited())')
        assert output[-1] == "hello;;;;;;;;;world"

    def test_toNonSemicolonDelimited_three(self):
        output = self._run('print("a b c".toNonSemicolonDelimited())')
        assert output[-1] == "a;;;;;;;;;b;;;;;;;;;c"
