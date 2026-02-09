"""
Tests for string .toTredecBacktickDelimited() method - join words with 13 backticks.
"""

from silk.interpreter import Interpreter


class TestStringToTredecBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTredecBacktickDelimited_basic(self):
        output = self._run('print("hello world".toTredecBacktickDelimited())')
        assert output[-1] == "hello`````````````world"

    def test_toTredecBacktickDelimited_three(self):
        output = self._run('print("a b c".toTredecBacktickDelimited())')
        assert output[-1] == "a`````````````b`````````````c"
