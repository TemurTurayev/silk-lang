"""
Tests for string .toDuovigintiBackslashDelimited() method - join words with 22 backslash chars.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiBackslashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiBackslashDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiBackslashDelimited())')
        assert output[-1] == "hello" + "\\" * 22 + "world"

    def test_toDuovigintiBackslashDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiBackslashDelimited())')
        assert output[-1] == "a" + "\\" * 22 + "b" + "\\" * 22 + "c"
