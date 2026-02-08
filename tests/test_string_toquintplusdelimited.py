"""
Tests for string .toQuintPlusDelimited() method - split words by +++++.
"""

from silk.interpreter import Interpreter


class TestStringToQuintPlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuintPlusDelimited_basic(self):
        output = self._run('print("hello world".toQuintPlusDelimited())')
        assert output[-1] == "hello+++++world"

    def test_toQuintPlusDelimited_three(self):
        output = self._run('print("a b c".toQuintPlusDelimited())')
        assert output[-1] == "a+++++b+++++c"
