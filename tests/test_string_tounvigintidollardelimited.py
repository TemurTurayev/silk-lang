"""
Tests for string .toUnvigintiDollarDelimited() method - join words with 21 dollar signs.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiDollarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiDollarDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiDollarDelimited())')
        assert output[-1] == "hello" + "$" * 21 + "world"

    def test_toUnvigintiDollarDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiDollarDelimited())')
        assert output[-1] == "a" + "$" * 21 + "b" + "$" * 21 + "c"
