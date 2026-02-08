"""
Tests for string .toOctUnderscoreDelimited() method - split words by ________ (8 underscores).
"""

from silk.interpreter import Interpreter


class TestStringToOctUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toOctUnderscoreDelimited())')
        assert output[-1] == "hello________world"

    def test_toOctUnderscoreDelimited_three(self):
        output = self._run('print("a b c".toOctUnderscoreDelimited())')
        assert output[-1] == "a________b________c"
