"""
Tests for string .toDuovigintiTildeDelimited() method - join words with 22 tilde chars.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiTildeDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiTildeDelimited())')
        assert output[-1] == "hello" + "~" * 22 + "world"

    def test_toDuovigintiTildeDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiTildeDelimited())')
        assert output[-1] == "a" + "~" * 22 + "b" + "~" * 22 + "c"
