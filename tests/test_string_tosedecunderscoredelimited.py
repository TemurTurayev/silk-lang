"""
Tests for string .toSedecUnderscoreDelimited() method - join words with 16 underscores.
"""

from silk.interpreter import Interpreter


class TestStringToSedecUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toSedecUnderscoreDelimited())')
        assert output[-1] == "hello" + "_" * 16 + "world"

    def test_toSedecUnderscoreDelimited_three(self):
        output = self._run('print("a b c".toSedecUnderscoreDelimited())')
        assert output[-1] == "a" + "_" * 16 + "b" + "_" * 16 + "c"
