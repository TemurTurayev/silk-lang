"""
Tests for string .toUndecPercentDelimited() method - split words by %%%%%%%%%%% (11 percents).
"""

from silk.interpreter import Interpreter


class TestStringToUndecPercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecPercentDelimited_basic(self):
        output = self._run('print("hello world".toUndecPercentDelimited())')
        assert output[-1] == "hello%%%%%%%%%%%world"

    def test_toUndecPercentDelimited_three(self):
        output = self._run('print("a b c".toUndecPercentDelimited())')
        assert output[-1] == "a%%%%%%%%%%%b%%%%%%%%%%%c"
