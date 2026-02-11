"""
Tests for string .toUnvigintiAtDelimited() method - join words with 21 at signs.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiAtDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiAtDelimited())')
        assert output[-1] == "hello" + "@" * 21 + "world"

    def test_toUnvigintiAtDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiAtDelimited())')
        assert output[-1] == "a" + "@" * 21 + "b" + "@" * 21 + "c"
