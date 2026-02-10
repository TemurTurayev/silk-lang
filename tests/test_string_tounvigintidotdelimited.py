"""
Tests for string .toUnvigintiDotDelimited() method - join words with 21 dots.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiDotDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiDotDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiDotDelimited())')
        assert output[-1] == "hello" + "." * 21 + "world"

    def test_toUnvigintiDotDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiDotDelimited())')
        assert output[-1] == "a" + "." * 21 + "b" + "." * 21 + "c"
