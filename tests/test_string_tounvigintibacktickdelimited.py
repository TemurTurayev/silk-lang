"""
Tests for string .toUnvigintiBacktickDelimited() method - join words with 21 backticks.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiBacktickDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiBacktickDelimited())')
        assert output[-1] == "hello" + "`" * 21 + "world"

    def test_toUnvigintiBacktickDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiBacktickDelimited())')
        assert output[-1] == "a" + "`" * 21 + "b" + "`" * 21 + "c"
