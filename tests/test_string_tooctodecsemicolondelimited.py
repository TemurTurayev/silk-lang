"""
Tests for string .toOctodecSemicolonDelimited() method - join words with 18 semicolons.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecSemicolonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecSemicolonDelimited_basic(self):
        output = self._run('print("hello world".toOctodecSemicolonDelimited())')
        assert output[-1] == "hello" + ";" * 18 + "world"

    def test_toOctodecSemicolonDelimited_three(self):
        output = self._run('print("a b c".toOctodecSemicolonDelimited())')
        assert output[-1] == "a" + ";" * 18 + "b" + ";" * 18 + "c"
