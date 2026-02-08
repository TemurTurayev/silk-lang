"""
Tests for string .toOctBacktickDelimited() method - split words by ```````` (8 backticks).
"""

from silk.interpreter import Interpreter


class TestStringToOctBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctBacktickDelimited_basic(self):
        output = self._run('print("hello world".toOctBacktickDelimited())')
        assert output[-1] == "hello````````world"

    def test_toOctBacktickDelimited_three(self):
        output = self._run('print("a b c".toOctBacktickDelimited())')
        assert output[-1] == "a````````b````````c"
