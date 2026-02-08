"""
Tests for string .toTripleDollarDelimited() method - split words by $$$.
"""

from silk.interpreter import Interpreter


class TestStringToTripleDollarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTripleDollarDelimited_basic(self):
        output = self._run('print("hello world".toTripleDollarDelimited())')
        assert output[-1] == "hello$$$world"

    def test_toTripleDollarDelimited_three(self):
        output = self._run('print("a b c".toTripleDollarDelimited())')
        assert output[-1] == "a$$$b$$$c"
