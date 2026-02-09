"""
Tests for string .toSedecDollarDelimited() method - join words with 16 dollar signs.
"""

from silk.interpreter import Interpreter


class TestStringToSedecDollarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecDollarDelimited_basic(self):
        output = self._run('print("hello world".toSedecDollarDelimited())')
        assert output[-1] == "hello" + "$" * 16 + "world"

    def test_toSedecDollarDelimited_three(self):
        output = self._run('print("a b c".toSedecDollarDelimited())')
        assert output[-1] == "a" + "$" * 16 + "b" + "$" * 16 + "c"
