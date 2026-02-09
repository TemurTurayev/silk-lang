"""
Tests for string .toVigintiTildeDelimited() method - join words with 20 tildes.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiTildeDelimited_basic(self):
        output = self._run('print("hello world".toVigintiTildeDelimited())')
        assert output[-1] == "hello" + "~" * 20 + "world"

    def test_toVigintiTildeDelimited_multi(self):
        output = self._run('print("a b c".toVigintiTildeDelimited())')
        assert output[-1] == "a" + "~" * 20 + "b" + "~" * 20 + "c"
