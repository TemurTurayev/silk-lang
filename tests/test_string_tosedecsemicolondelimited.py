"""
Tests for string .toSedecSemicolonDelimited() method - join words with 16 semicolons.
"""

from silk.interpreter import Interpreter


class TestStringToSedecSemicolonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecSemicolonDelimited_basic(self):
        output = self._run('print("hello world".toSedecSemicolonDelimited())')
        assert output[-1] == "hello" + ";" * 16 + "world"

    def test_toSedecSemicolonDelimited_three(self):
        output = self._run('print("a b c".toSedecSemicolonDelimited())')
        assert output[-1] == "a" + ";" * 16 + "b" + ";" * 16 + "c"
