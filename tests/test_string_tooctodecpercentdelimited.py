"""
Tests for string .toOctodecPercentDelimited() method - join words with 18 percent signs.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecPercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecPercentDelimited_basic(self):
        output = self._run('print("hello world".toOctodecPercentDelimited())')
        assert output[-1] == "hello" + "%" * 18 + "world"

    def test_toOctodecPercentDelimited_three(self):
        output = self._run('print("a b c".toOctodecPercentDelimited())')
        assert output[-1] == "a" + "%" * 18 + "b" + "%" * 18 + "c"
