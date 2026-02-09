"""
Tests for string .toDuodecBacktickDelimited() method - join words with 12 backticks.
"""

from silk.interpreter import Interpreter


class TestStringToDuodecBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuodecBacktickDelimited_basic(self):
        output = self._run('print("hello world".toDuodecBacktickDelimited())')
        assert output[-1] == "hello````````````world"

    def test_toDuodecBacktickDelimited_three(self):
        output = self._run('print("a b c".toDuodecBacktickDelimited())')
        assert output[-1] == "a````````````b````````````c"
