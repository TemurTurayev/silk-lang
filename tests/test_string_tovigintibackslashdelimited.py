"""
Tests for string .toVigintiBackslashDelimited() method - join words with 20 backslashes.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiBackslashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiBackslashDelimited_basic(self):
        output = self._run('print("hello world".toVigintiBackslashDelimited())')
        assert output[-1] == "hello" + "\\" * 20 + "world"

    def test_toVigintiBackslashDelimited_multi(self):
        output = self._run('print("a b c".toVigintiBackslashDelimited())')
        assert output[-1] == "a" + "\\" * 20 + "b" + "\\" * 20 + "c"
