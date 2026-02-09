"""
Tests for string .toUndecDollarDelimited() method - split words by $$$$$$$$$$$ (11 dollars).
"""

from silk.interpreter import Interpreter


class TestStringToUndecDollarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecDollarDelimited_basic(self):
        output = self._run('print("hello world".toUndecDollarDelimited())')
        assert output[-1] == "hello$$$$$$$$$$$world"

    def test_toUndecDollarDelimited_three(self):
        output = self._run('print("a b c".toUndecDollarDelimited())')
        assert output[-1] == "a$$$$$$$$$$$b$$$$$$$$$$$c"
