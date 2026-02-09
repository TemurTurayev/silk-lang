"""
Tests for string .toDecPlusDelimited() method - split words by ++++++++++ (10 plus signs).
"""

from silk.interpreter import Interpreter


class TestStringToDecPlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecPlusDelimited_basic(self):
        output = self._run('print("hello world".toDecPlusDelimited())')
        assert output[-1] == "hello++++++++++world"

    def test_toDecPlusDelimited_three(self):
        output = self._run('print("a b c".toDecPlusDelimited())')
        assert output[-1] == "a++++++++++b++++++++++c"
