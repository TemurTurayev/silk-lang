"""
Tests for string .toNonPercentDelimited() method - split words by %%%%%%%%% (9 percent signs).
"""

from silk.interpreter import Interpreter


class TestStringToNonPercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonPercentDelimited_basic(self):
        output = self._run('print("hello world".toNonPercentDelimited())')
        assert output[-1] == "hello%%%%%%%%%world"

    def test_toNonPercentDelimited_three(self):
        output = self._run('print("a b c".toNonPercentDelimited())')
        assert output[-1] == "a%%%%%%%%%b%%%%%%%%%c"
