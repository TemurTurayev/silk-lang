"""
Tests for string .toHashDelimited() method - split words by hash sign.
"""

from silk.interpreter import Interpreter


class TestStringToHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toHashDelimited_basic(self):
        output = self._run('print("hello world".toHashDelimited())')
        assert output[-1] == "hello#world"

    def test_toHashDelimited_three(self):
        output = self._run('print("a b c".toHashDelimited())')
        assert output[-1] == "a#b#c"
