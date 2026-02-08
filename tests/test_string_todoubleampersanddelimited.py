"""
Tests for string .toDoubleAmpersandDelimited() method - split words by &&.
"""

from silk.interpreter import Interpreter


class TestStringToDoubleAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDoubleAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toDoubleAmpersandDelimited())')
        assert output[-1] == "hello&&world"

    def test_toDoubleAmpersandDelimited_three(self):
        output = self._run('print("a b c".toDoubleAmpersandDelimited())')
        assert output[-1] == "a&&b&&c"
