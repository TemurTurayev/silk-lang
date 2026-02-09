"""
Tests for string .toNovemdecBackslashDelimited() method - join words with 19 backslashes.
"""

from silk.interpreter import Interpreter


class TestStringToNovemdecBackslashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNovemdecBackslashDelimited_basic(self):
        output = self._run('print("hello world".toNovemdecBackslashDelimited())')
        assert output[-1] == "hello" + "\\" * 19 + "world"

    def test_toNovemdecBackslashDelimited_multi(self):
        output = self._run('print("a b c".toNovemdecBackslashDelimited())')
        assert output[-1] == "a" + "\\" * 19 + "b" + "\\" * 19 + "c"
