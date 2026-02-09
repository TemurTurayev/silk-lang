"""
Tests for string .toOctodecDollarDelimited() method - join words with 18 dollar signs.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecDollarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecDollarDelimited_basic(self):
        output = self._run('print("hello world".toOctodecDollarDelimited())')
        assert output[-1] == "hello" + "$" * 18 + "world"

    def test_toOctodecDollarDelimited_three(self):
        output = self._run('print("a b c".toOctodecDollarDelimited())')
        assert output[-1] == "a" + "$" * 18 + "b" + "$" * 18 + "c"
