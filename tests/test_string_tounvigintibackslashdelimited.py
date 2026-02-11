"""
Tests for string .toUnvigintiBackslashDelimited() method - join words with 21 backslashes.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiBackslashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiBackslashDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiBackslashDelimited())')
        assert output[-1] == "hello" + "\\" * 21 + "world"

    def test_toUnvigintiBackslashDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiBackslashDelimited())')
        assert output[-1] == "a" + "\\" * 21 + "b" + "\\" * 21 + "c"
