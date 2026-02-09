"""
Tests for string .toOctodecBackslashDelimited() method - join words with 18 backslashes.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecBackslashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecBackslashDelimited_basic(self):
        output = self._run('print("hello world".toOctodecBackslashDelimited())')
        assert output[-1] == "hello" + "\\" * 18 + "world"

    def test_toOctodecBackslashDelimited_three(self):
        output = self._run('print("a b c".toOctodecBackslashDelimited())')
        assert output[-1] == "a" + "\\" * 18 + "b" + "\\" * 18 + "c"
