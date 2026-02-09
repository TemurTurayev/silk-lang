"""
Tests for string .toQuattuordecDollarDelimited() method - join words with 14 dollar signs.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecDollarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecDollarDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecDollarDelimited())')
        assert output[-1] == "hello$$$$$$$$$$$$$$world"

    def test_toQuattuordecDollarDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecDollarDelimited())')
        assert output[-1] == "a$$$$$$$$$$$$$$b$$$$$$$$$$$$$$c"
