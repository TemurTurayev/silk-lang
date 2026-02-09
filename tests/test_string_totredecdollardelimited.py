"""
Tests for string .toTredecDollarDelimited() method - join words with 13 dollar signs.
"""

from silk.interpreter import Interpreter


class TestStringToTredecDollarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTredecDollarDelimited_basic(self):
        output = self._run('print("hello world".toTredecDollarDelimited())')
        assert output[-1] == "hello$$$$$$$$$$$$$world"

    def test_toTredecDollarDelimited_three(self):
        output = self._run('print("a b c".toTredecDollarDelimited())')
        assert output[-1] == "a$$$$$$$$$$$$$b$$$$$$$$$$$$$c"
