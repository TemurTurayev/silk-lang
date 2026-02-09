"""
Tests for string .toVigintiAtDelimited() method - join words with 20 at signs.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiAtDelimited_basic(self):
        output = self._run('print("hello world".toVigintiAtDelimited())')
        assert output[-1] == "hello" + "@" * 20 + "world"

    def test_toVigintiAtDelimited_multi(self):
        output = self._run('print("a b c".toVigintiAtDelimited())')
        assert output[-1] == "a" + "@" * 20 + "b" + "@" * 20 + "c"
