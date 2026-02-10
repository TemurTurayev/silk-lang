"""
Tests for string .toVigintiBacktickDelimited() method - join words with 20 backticks.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiBacktickDelimited_basic(self):
        output = self._run('print("hello world".toVigintiBacktickDelimited())')
        assert output[-1] == "hello" + "`" * 20 + "world"

    def test_toVigintiBacktickDelimited_multi(self):
        output = self._run('print("a b c".toVigintiBacktickDelimited())')
        assert output[-1] == "a" + "`" * 20 + "b" + "`" * 20 + "c"
