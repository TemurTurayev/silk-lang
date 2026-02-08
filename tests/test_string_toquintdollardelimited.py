"""
Tests for string .toQuintDollarDelimited() method - split words by $$$$$.
"""

from silk.interpreter import Interpreter


class TestStringToQuintDollarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuintDollarDelimited_basic(self):
        output = self._run('print("hello world".toQuintDollarDelimited())')
        assert output[-1] == "hello$$$$$world"

    def test_toQuintDollarDelimited_three(self):
        output = self._run('print("a b c".toQuintDollarDelimited())')
        assert output[-1] == "a$$$$$b$$$$$c"
