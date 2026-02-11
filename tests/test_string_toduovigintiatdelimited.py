"""
Tests for string .toDuovigintiAtDelimited() method - join words with 22 at chars.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiAtDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiAtDelimited())')
        assert output[-1] == "hello" + "@" * 22 + "world"

    def test_toDuovigintiAtDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiAtDelimited())')
        assert output[-1] == "a" + "@" * 22 + "b" + "@" * 22 + "c"
