"""
Tests for string .toNonDotDelimited() method - split words by ......... (9 dots).
"""

from silk.interpreter import Interpreter


class TestStringToNonDotDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonDotDelimited_basic(self):
        output = self._run('print("hello world".toNonDotDelimited())')
        assert output[-1] == "hello.........world"

    def test_toNonDotDelimited_three(self):
        output = self._run('print("a b c".toNonDotDelimited())')
        assert output[-1] == "a.........b.........c"
