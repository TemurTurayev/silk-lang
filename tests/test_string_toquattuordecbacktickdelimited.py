"""
Tests for string .toQuattuordecBacktickDelimited() method - join words with 14 backticks.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecBacktickDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecBacktickDelimited())')
        assert output[-1] == "hello``````````````world"

    def test_toQuattuordecBacktickDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecBacktickDelimited())')
        assert output[-1] == "a``````````````b``````````````c"
