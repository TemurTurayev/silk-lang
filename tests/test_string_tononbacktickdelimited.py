"""
Tests for string .toNonBacktickDelimited() method - split words by ````````` (9 backticks).
"""

from silk.interpreter import Interpreter


class TestStringToNonBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonBacktickDelimited_basic(self):
        output = self._run('print("hello world".toNonBacktickDelimited())')
        assert output[-1] == "hello`````````world"

    def test_toNonBacktickDelimited_three(self):
        output = self._run('print("a b c".toNonBacktickDelimited())')
        assert output[-1] == "a`````````b`````````c"
