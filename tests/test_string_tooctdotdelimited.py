"""
Tests for string .toOctDotDelimited() method - split words by ........
"""

from silk.interpreter import Interpreter


class TestStringToOctDotDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctDotDelimited_basic(self):
        output = self._run('print("hello world".toOctDotDelimited())')
        assert output[-1] == "hello........world"

    def test_toOctDotDelimited_three(self):
        output = self._run('print("a b c".toOctDotDelimited())')
        assert output[-1] == "a........b........c"
