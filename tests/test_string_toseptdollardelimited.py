"""
Tests for string .toSeptDollarDelimited() method - split words by $$$$$$$.
"""

from silk.interpreter import Interpreter


class TestStringToSeptDollarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptDollarDelimited_basic(self):
        output = self._run('print("hello world".toSeptDollarDelimited())')
        assert output[-1] == "hello$$$$$$$world"

    def test_toSeptDollarDelimited_three(self):
        output = self._run('print("a b c".toSeptDollarDelimited())')
        assert output[-1] == "a$$$$$$$b$$$$$$$c"
