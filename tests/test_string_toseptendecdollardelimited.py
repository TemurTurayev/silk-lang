"""
Tests for string .toSeptendecDollarDelimited() method - join words with 17 dollar signs.
"""

from silk.interpreter import Interpreter


class TestStringToSeptendecDollarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptendecDollarDelimited_basic(self):
        output = self._run('print("hello world".toSeptendecDollarDelimited())')
        assert output[-1] == "hello" + "$" * 17 + "world"

    def test_toSeptendecDollarDelimited_three(self):
        output = self._run('print("a b c".toSeptendecDollarDelimited())')
        assert output[-1] == "a" + "$" * 17 + "b" + "$" * 17 + "c"
