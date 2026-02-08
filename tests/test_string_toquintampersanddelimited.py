"""
Tests for string .toQuintAmpersandDelimited() method - split words by &&&&&.
"""

from silk.interpreter import Interpreter


class TestStringToQuintAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuintAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toQuintAmpersandDelimited())')
        assert output[-1] == "hello&&&&&world"

    def test_toQuintAmpersandDelimited_three(self):
        output = self._run('print("a b c".toQuintAmpersandDelimited())')
        assert output[-1] == "a&&&&&b&&&&&c"
