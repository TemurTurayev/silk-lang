"""
Tests for string .toDuodecDollarDelimited() method - join words with 12 dollar signs.
"""

from silk.interpreter import Interpreter


class TestStringToDuodecDollarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuodecDollarDelimited_basic(self):
        output = self._run('print("hello world".toDuodecDollarDelimited())')
        assert output[-1] == "hello$$$$$$$$$$$$world"

    def test_toDuodecDollarDelimited_three(self):
        output = self._run('print("a b c".toDuodecDollarDelimited())')
        assert output[-1] == "a$$$$$$$$$$$$b$$$$$$$$$$$$c"
