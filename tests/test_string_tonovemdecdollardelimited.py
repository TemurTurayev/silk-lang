"""
Tests for string .toNovemdecDollarDelimited() method - join words with 19 dollar signs.
"""

from silk.interpreter import Interpreter


class TestStringToNovemdecDollarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNovemdecDollarDelimited_basic(self):
        output = self._run('print("hello world".toNovemdecDollarDelimited())')
        assert output[-1] == "hello$$$$$$$$$$$$$$$$$$$world"

    def test_toNovemdecDollarDelimited_multi(self):
        output = self._run('print("a b c".toNovemdecDollarDelimited())')
        assert output[-1] == "a$$$$$$$$$$$$$$$$$$$b$$$$$$$$$$$$$$$$$$$c"
