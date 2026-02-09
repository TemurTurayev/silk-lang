"""
Tests for string .toDecBacktickDelimited() method - split words by `````````` (10 backticks).
"""

from silk.interpreter import Interpreter


class TestStringToDecBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecBacktickDelimited_basic(self):
        output = self._run('print("hello world".toDecBacktickDelimited())')
        assert output[-1] == "hello``````````world"

    def test_toDecBacktickDelimited_three(self):
        output = self._run('print("a b c".toDecBacktickDelimited())')
        assert output[-1] == "a``````````b``````````c"
