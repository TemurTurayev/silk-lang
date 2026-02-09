"""
Tests for string .toOctodecBacktickDelimited() method - join words with 18 backticks.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecBacktickDelimited_basic(self):
        output = self._run('print("hello world".toOctodecBacktickDelimited())')
        assert output[-1] == "hello" + "`" * 18 + "world"

    def test_toOctodecBacktickDelimited_three(self):
        output = self._run('print("a b c".toOctodecBacktickDelimited())')
        assert output[-1] == "a" + "`" * 18 + "b" + "`" * 18 + "c"
