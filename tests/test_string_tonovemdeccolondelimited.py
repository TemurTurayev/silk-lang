"""
Tests for string .toNovemdecColonDelimited() method - join words with 19 colons.
"""

from silk.interpreter import Interpreter


class TestStringToNovemdecColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNovemdecColonDelimited_basic(self):
        output = self._run('print("hello world".toNovemdecColonDelimited())')
        assert output[-1] == "hello" + ":" * 19 + "world"

    def test_toNovemdecColonDelimited_three(self):
        output = self._run('print("a b c".toNovemdecColonDelimited())')
        assert output[-1] == "a" + ":" * 19 + "b" + ":" * 19 + "c"
