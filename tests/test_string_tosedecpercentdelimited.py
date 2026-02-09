"""
Tests for string .toSedecPercentDelimited() method - join words with 16 percent signs.
"""

from silk.interpreter import Interpreter


class TestStringToSedecPercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecPercentDelimited_basic(self):
        output = self._run('print("hello world".toSedecPercentDelimited())')
        assert output[-1] == "hello" + "%" * 16 + "world"

    def test_toSedecPercentDelimited_three(self):
        output = self._run('print("a b c".toSedecPercentDelimited())')
        assert output[-1] == "a" + "%" * 16 + "b" + "%" * 16 + "c"
