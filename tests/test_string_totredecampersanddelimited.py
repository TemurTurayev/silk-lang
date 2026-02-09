"""
Tests for string .toTredecAmpersandDelimited() method - join words with 13 ampersands.
"""

from silk.interpreter import Interpreter


class TestStringToTredecAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTredecAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toTredecAmpersandDelimited())')
        assert output[-1] == "hello&&&&&&&&&&&&&world"

    def test_toTredecAmpersandDelimited_three(self):
        output = self._run('print("a b c".toTredecAmpersandDelimited())')
        assert output[-1] == "a&&&&&&&&&&&&&b&&&&&&&&&&&&&c"
