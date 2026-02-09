"""
Tests for string .toUndecBacktickDelimited() method - split words by ``````````` (11 backticks).
"""

from silk.interpreter import Interpreter


class TestStringToUndecBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecBacktickDelimited_basic(self):
        output = self._run('print("hello world".toUndecBacktickDelimited())')
        assert output[-1] == "hello```````````world"

    def test_toUndecBacktickDelimited_three(self):
        output = self._run('print("a b c".toUndecBacktickDelimited())')
        assert output[-1] == "a```````````b```````````c"
