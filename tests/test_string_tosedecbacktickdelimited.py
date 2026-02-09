"""
Tests for string .toSedecBacktickDelimited() method - join words with 16 backticks.
"""

from silk.interpreter import Interpreter


class TestStringToSedecBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecBacktickDelimited_basic(self):
        output = self._run('print("hello world".toSedecBacktickDelimited())')
        assert output[-1] == "hello" + "`" * 16 + "world"

    def test_toSedecBacktickDelimited_three(self):
        output = self._run('print("a b c".toSedecBacktickDelimited())')
        assert output[-1] == "a" + "`" * 16 + "b" + "`" * 16 + "c"
