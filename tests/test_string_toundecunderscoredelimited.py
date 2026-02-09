"""
Tests for string .toUndecUnderscoreDelimited() method - split words by ___________ (11 underscores).
"""

from silk.interpreter import Interpreter


class TestStringToUndecUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toUndecUnderscoreDelimited())')
        assert output[-1] == "hello___________world"

    def test_toUndecUnderscoreDelimited_three(self):
        output = self._run('print("a b c".toUndecUnderscoreDelimited())')
        assert output[-1] == "a___________b___________c"
