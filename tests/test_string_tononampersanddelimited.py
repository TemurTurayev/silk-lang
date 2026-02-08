"""
Tests for string .toNonAmpersandDelimited() method - split words by &&&&&&&&& (9 ampersands).
"""

from silk.interpreter import Interpreter


class TestStringToNonAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toNonAmpersandDelimited())')
        assert output[-1] == "hello&&&&&&&&&world"

    def test_toNonAmpersandDelimited_three(self):
        output = self._run('print("a b c".toNonAmpersandDelimited())')
        assert output[-1] == "a&&&&&&&&&b&&&&&&&&&c"
