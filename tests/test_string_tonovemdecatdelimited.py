"""
Tests for string .toNovemdecAtDelimited() method - join words with 19 at signs.
"""

from silk.interpreter import Interpreter


class TestStringToNovemdecAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNovemdecAtDelimited_basic(self):
        output = self._run('print("hello world".toNovemdecAtDelimited())')
        assert output[-1] == "hello" + "@" * 19 + "world"

    def test_toNovemdecAtDelimited_three(self):
        output = self._run('print("a b c".toNovemdecAtDelimited())')
        assert output[-1] == "a" + "@" * 19 + "b" + "@" * 19 + "c"
