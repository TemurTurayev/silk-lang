"""
Tests for string .toSeptAmpersandDelimited() method - split words by &&&&&&&.
"""

from silk.interpreter import Interpreter


class TestStringToSeptAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toSeptAmpersandDelimited())')
        assert output[-1] == "hello&&&&&&&world"

    def test_toSeptAmpersandDelimited_three(self):
        output = self._run('print("a b c".toSeptAmpersandDelimited())')
        assert output[-1] == "a&&&&&&&b&&&&&&&c"
