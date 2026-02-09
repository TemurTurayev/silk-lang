"""
Tests for string .toQuindecDollarDelimited() method - join words with 15 dollar signs.
"""

from silk.interpreter import Interpreter


class TestStringToQuindecDollarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuindecDollarDelimited_basic(self):
        output = self._run('print("hello world".toQuindecDollarDelimited())')
        assert output[-1] == "hello$$$$$$$$$$$$$$$world"

    def test_toQuindecDollarDelimited_three(self):
        output = self._run('print("a b c".toQuindecDollarDelimited())')
        assert output[-1] == "a$$$$$$$$$$$$$$$b$$$$$$$$$$$$$$$c"
