"""
Tests for string .toUnvigintiAmpersandDelimited() method - join words with 21 ampersands.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiAmpersandDelimited())')
        assert output[-1] == "hello" + "&" * 21 + "world"

    def test_toUnvigintiAmpersandDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiAmpersandDelimited())')
        assert output[-1] == "a" + "&" * 21 + "b" + "&" * 21 + "c"
