"""
Tests for string .toOctPlusDelimited() method - split words by ++++++++.
"""

from silk.interpreter import Interpreter


class TestStringToOctPlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctPlusDelimited_basic(self):
        output = self._run('print("hello world".toOctPlusDelimited())')
        assert output[-1] == "hello++++++++world"

    def test_toOctPlusDelimited_three(self):
        output = self._run('print("a b c".toOctPlusDelimited())')
        assert output[-1] == "a++++++++b++++++++c"
