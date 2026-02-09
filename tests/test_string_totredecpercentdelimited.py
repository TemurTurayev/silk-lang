"""
Tests for string .toTredecPercentDelimited() method - join words with 13 percent signs.
"""

from silk.interpreter import Interpreter


class TestStringToTredecPercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTredecPercentDelimited_basic(self):
        output = self._run('print("hello world".toTredecPercentDelimited())')
        assert output[-1] == "hello%%%%%%%%%%%%%world"

    def test_toTredecPercentDelimited_three(self):
        output = self._run('print("a b c".toTredecPercentDelimited())')
        assert output[-1] == "a%%%%%%%%%%%%%b%%%%%%%%%%%%%c"
