"""
Tests for string .toQuindecBacktickDelimited() method - join words with 15 backticks.
"""

from silk.interpreter import Interpreter


class TestStringToQuindecBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuindecBacktickDelimited_basic(self):
        output = self._run('print("hello world".toQuindecBacktickDelimited())')
        assert output[-1] == "hello" + "`" * 15 + "world"

    def test_toQuindecBacktickDelimited_three(self):
        output = self._run('print("a b c".toQuindecBacktickDelimited())')
        assert output[-1] == "a" + "`" * 15 + "b" + "`" * 15 + "c"
