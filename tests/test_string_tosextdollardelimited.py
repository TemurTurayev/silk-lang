"""
Tests for string .toSextDollarDelimited() method - split words by $$$$$$.
"""

from silk.interpreter import Interpreter


class TestStringToSextDollarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSextDollarDelimited_basic(self):
        output = self._run('print("hello world".toSextDollarDelimited())')
        assert output[-1] == "hello$$$$$$world"

    def test_toSextDollarDelimited_three(self):
        output = self._run('print("a b c".toSextDollarDelimited())')
        assert output[-1] == "a$$$$$$b$$$$$$c"
