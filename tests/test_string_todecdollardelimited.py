"""
Tests for string .toDecDollarDelimited() method - split words by $$$$$$$$$$ (10 dollars).
"""

from silk.interpreter import Interpreter


class TestStringToDecDollarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecDollarDelimited_basic(self):
        output = self._run('print("hello world".toDecDollarDelimited())')
        assert output[-1] == "hello$$$$$$$$$$world"

    def test_toDecDollarDelimited_three(self):
        output = self._run('print("a b c".toDecDollarDelimited())')
        assert output[-1] == "a$$$$$$$$$$b$$$$$$$$$$c"
