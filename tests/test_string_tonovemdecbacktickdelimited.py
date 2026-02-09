"""
Tests for string .toNovemdecBacktickDelimited() method - join words with 19 backticks.
"""

from silk.interpreter import Interpreter


class TestStringToNovemdecBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNovemdecBacktickDelimited_basic(self):
        output = self._run('print("hello world".toNovemdecBacktickDelimited())')
        assert output[-1] == "hello" + "`" * 19 + "world"

    def test_toNovemdecBacktickDelimited_multi(self):
        output = self._run('print("a b c".toNovemdecBacktickDelimited())')
        assert output[-1] == "a" + "`" * 19 + "b" + "`" * 19 + "c"
