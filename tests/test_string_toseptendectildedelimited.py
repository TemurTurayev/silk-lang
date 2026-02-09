"""
Tests for string .toSeptendecTildeDelimited() method - join words with 17 tildes.
"""

from silk.interpreter import Interpreter


class TestStringToSeptendecTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptendecTildeDelimited_basic(self):
        output = self._run('print("hello world".toSeptendecTildeDelimited())')
        assert output[-1] == "hello" + "~" * 17 + "world"

    def test_toSeptendecTildeDelimited_three(self):
        output = self._run('print("a b c".toSeptendecTildeDelimited())')
        assert output[-1] == "a" + "~" * 17 + "b" + "~" * 17 + "c"
