"""
Tests for string .toAmpersandDelimited() method - split words by ampersand.
"""

from silk.interpreter import Interpreter


class TestStringToAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toAmpersandDelimited())')
        assert output[-1] == "hello&world"

    def test_toAmpersandDelimited_three(self):
        output = self._run('print("a b c".toAmpersandDelimited())')
        assert output[-1] == "a&b&c"
