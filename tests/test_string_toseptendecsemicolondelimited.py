"""
Tests for string .toSeptendecSemicolonDelimited() method - join words with 17 semicolons.
"""

from silk.interpreter import Interpreter


class TestStringToSeptendecSemicolonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptendecSemicolonDelimited_basic(self):
        output = self._run('print("hello world".toSeptendecSemicolonDelimited())')
        assert output[-1] == "hello" + ";" * 17 + "world"

    def test_toSeptendecSemicolonDelimited_three(self):
        output = self._run('print("a b c".toSeptendecSemicolonDelimited())')
        assert output[-1] == "a" + ";" * 17 + "b" + ";" * 17 + "c"
