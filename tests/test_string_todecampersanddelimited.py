"""
Tests for string .toDecAmpersandDelimited() method - split words by &&&&&&&&&& (10 ampersands).
"""

from silk.interpreter import Interpreter


class TestStringToDecAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toDecAmpersandDelimited())')
        assert output[-1] == "hello&&&&&&&&&&world"

    def test_toDecAmpersandDelimited_three(self):
        output = self._run('print("a b c".toDecAmpersandDelimited())')
        assert output[-1] == "a&&&&&&&&&&b&&&&&&&&&&c"
