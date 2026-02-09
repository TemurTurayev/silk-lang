"""
Tests for string .toUndecAmpersandDelimited() method - split words by &&&&&&&&&&& (11 ampersands).
"""

from silk.interpreter import Interpreter


class TestStringToUndecAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toUndecAmpersandDelimited())')
        assert output[-1] == "hello&&&&&&&&&&&world"

    def test_toUndecAmpersandDelimited_three(self):
        output = self._run('print("a b c".toUndecAmpersandDelimited())')
        assert output[-1] == "a&&&&&&&&&&&b&&&&&&&&&&&c"
