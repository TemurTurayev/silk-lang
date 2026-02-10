"""
Tests for string .toVigintiDollarDelimited() method - join words with 20 dollar signs.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiDollarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiDollarDelimited_basic(self):
        output = self._run('print("hello world".toVigintiDollarDelimited())')
        assert output[-1] == "hello" + "$" * 20 + "world"

    def test_toVigintiDollarDelimited_multi(self):
        output = self._run('print("a b c".toVigintiDollarDelimited())')
        assert output[-1] == "a" + "$" * 20 + "b" + "$" * 20 + "c"
