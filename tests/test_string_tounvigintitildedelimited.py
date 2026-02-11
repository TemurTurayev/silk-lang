"""
Tests for string .toUnvigintiTildeDelimited() method - join words with 21 tildes.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiTildeDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiTildeDelimited())')
        assert output[-1] == "hello" + "~" * 21 + "world"

    def test_toUnvigintiTildeDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiTildeDelimited())')
        assert output[-1] == "a" + "~" * 21 + "b" + "~" * 21 + "c"
