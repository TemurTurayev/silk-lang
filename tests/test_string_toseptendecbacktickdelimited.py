"""
Tests for string .toSeptendecBacktickDelimited() method - join words with 17 backticks.
"""

from silk.interpreter import Interpreter


class TestStringToSeptendecBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptendecBacktickDelimited_basic(self):
        output = self._run('print("hello world".toSeptendecBacktickDelimited())')
        assert output[-1] == "hello" + "`" * 17 + "world"

    def test_toSeptendecBacktickDelimited_three(self):
        output = self._run('print("a b c".toSeptendecBacktickDelimited())')
        assert output[-1] == "a" + "`" * 17 + "b" + "`" * 17 + "c"
