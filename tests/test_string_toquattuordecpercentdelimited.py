"""
Tests for string .toQuattuordecPercentDelimited() method - join words with 14 percent signs.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecPercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecPercentDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecPercentDelimited())')
        assert output[-1] == "hello%%%%%%%%%%%%%%world"

    def test_toQuattuordecPercentDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecPercentDelimited())')
        assert output[-1] == "a%%%%%%%%%%%%%%b%%%%%%%%%%%%%%c"
