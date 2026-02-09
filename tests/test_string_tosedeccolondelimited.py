"""
Tests for string .toSedecColonDelimited() method - join words with 16 colons.
"""

from silk.interpreter import Interpreter


class TestStringToSedecColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecColonDelimited_basic(self):
        output = self._run('print("hello world".toSedecColonDelimited())')
        assert output[-1] == "hello" + ":" * 16 + "world"

    def test_toSedecColonDelimited_three(self):
        output = self._run('print("a b c".toSedecColonDelimited())')
        assert output[-1] == "a" + ":" * 16 + "b" + ":" * 16 + "c"
