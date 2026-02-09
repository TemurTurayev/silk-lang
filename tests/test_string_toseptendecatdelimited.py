"""
Tests for string .toSeptendecAtDelimited() method - join words with 17 at signs.
"""

from silk.interpreter import Interpreter


class TestStringToSeptendecAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptendecAtDelimited_basic(self):
        output = self._run('print("hello world".toSeptendecAtDelimited())')
        assert output[-1] == "hello" + "@" * 17 + "world"

    def test_toSeptendecAtDelimited_three(self):
        output = self._run('print("a b c".toSeptendecAtDelimited())')
        assert output[-1] == "a" + "@" * 17 + "b" + "@" * 17 + "c"
