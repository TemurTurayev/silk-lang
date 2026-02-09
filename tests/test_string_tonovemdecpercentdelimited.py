"""
Tests for string .toNovemdecPercentDelimited() method - join words with 19 percent signs.
"""

from silk.interpreter import Interpreter


class TestStringToNovemdecPercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNovemdecPercentDelimited_basic(self):
        output = self._run('print("hello world".toNovemdecPercentDelimited())')
        assert output[-1] == "hello%%%%%%%%%%%%%%%%%%%world"

    def test_toNovemdecPercentDelimited_multi(self):
        output = self._run('print("a b c".toNovemdecPercentDelimited())')
        assert output[-1] == "a%%%%%%%%%%%%%%%%%%%b%%%%%%%%%%%%%%%%%%%c"
