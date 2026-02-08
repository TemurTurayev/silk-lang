"""
Tests for string .toDecDotDelimited() method - split words by .......... (10 dots).
"""

from silk.interpreter import Interpreter


class TestStringToDecDotDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecDotDelimited_basic(self):
        output = self._run('print("hello world".toDecDotDelimited())')
        assert output[-1] == "hello..........world"

    def test_toDecDotDelimited_three(self):
        output = self._run('print("a b c".toDecDotDelimited())')
        assert output[-1] == "a..........b..........c"
