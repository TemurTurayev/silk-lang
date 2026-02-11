"""
Tests for string .toDuovigintiDollarDelimited() method - join words with 22 dollar chars.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiDollarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiDollarDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiDollarDelimited())')
        assert output[-1] == "hello" + "$" * 22 + "world"

    def test_toDuovigintiDollarDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiDollarDelimited())')
        assert output[-1] == "a" + "$" * 22 + "b" + "$" * 22 + "c"
