"""
Tests for string .toSextPercentDelimited() method - split words by %%%%%%.
"""

from silk.interpreter import Interpreter


class TestStringToSextPercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSextPercentDelimited_basic(self):
        output = self._run('print("hello world".toSextPercentDelimited())')
        assert output[-1] == "hello%%%%%%world"

    def test_toSextPercentDelimited_three(self):
        output = self._run('print("a b c".toSextPercentDelimited())')
        assert output[-1] == "a%%%%%%b%%%%%%c"
