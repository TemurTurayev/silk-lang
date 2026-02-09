"""
Tests for string .toUndecDotDelimited() method - split words by ........... (11 dots).
"""

from silk.interpreter import Interpreter


class TestStringToUndecDotDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecDotDelimited_basic(self):
        output = self._run('print("hello world".toUndecDotDelimited())')
        assert output[-1] == "hello...........world"

    def test_toUndecDotDelimited_three(self):
        output = self._run('print("a b c".toUndecDotDelimited())')
        assert output[-1] == "a...........b...........c"
