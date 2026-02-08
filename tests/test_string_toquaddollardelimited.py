"""
Tests for string .toQuadDollarDelimited() method - split words by $$$$.
"""

from silk.interpreter import Interpreter


class TestStringToQuadDollarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuadDollarDelimited_basic(self):
        output = self._run('print("hello world".toQuadDollarDelimited())')
        assert output[-1] == "hello$$$$world"

    def test_toQuadDollarDelimited_three(self):
        output = self._run('print("a b c".toQuadDollarDelimited())')
        assert output[-1] == "a$$$$b$$$$c"
