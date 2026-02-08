"""
Tests for string .toNonDollarDelimited() method - split words by $$$$$$$$$ (9 dollar signs).
"""

from silk.interpreter import Interpreter


class TestStringToNonDollarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonDollarDelimited_basic(self):
        output = self._run('print("hello world".toNonDollarDelimited())')
        assert output[-1] == "hello$$$$$$$$$world"

    def test_toNonDollarDelimited_three(self):
        output = self._run('print("a b c".toNonDollarDelimited())')
        assert output[-1] == "a$$$$$$$$$b$$$$$$$$$c"
