"""
Tests for string .toTredecSemicolonDelimited() method - join words with 13 semicolons.
"""

from silk.interpreter import Interpreter


class TestStringToTredecSemicolonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTredecSemicolonDelimited_basic(self):
        output = self._run('print("hello world".toTredecSemicolonDelimited())')
        assert output[-1] == "hello;;;;;;;;;;;;;world"

    def test_toTredecSemicolonDelimited_three(self):
        output = self._run('print("a b c".toTredecSemicolonDelimited())')
        assert output[-1] == "a;;;;;;;;;;;;;b;;;;;;;;;;;;;c"
