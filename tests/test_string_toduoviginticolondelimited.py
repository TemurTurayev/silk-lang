"""
Tests for string .toDuovigintiColonDelimited() method - join words with 22 colon chars.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiColonDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiColonDelimited())')
        assert output[-1] == "hello" + ":" * 22 + "world"

    def test_toDuovigintiColonDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiColonDelimited())')
        assert output[-1] == "a" + ":" * 22 + "b" + ":" * 22 + "c"
