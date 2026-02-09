"""
Tests for string .toSedecSlashDelimited() method - join words with 16 slashes.
"""

from silk.interpreter import Interpreter


class TestStringToSedecSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecSlashDelimited_basic(self):
        output = self._run('print("hello world".toSedecSlashDelimited())')
        assert output[-1] == "hello" + "/" * 16 + "world"

    def test_toSedecSlashDelimited_three(self):
        output = self._run('print("a b c".toSedecSlashDelimited())')
        assert output[-1] == "a" + "/" * 16 + "b" + "/" * 16 + "c"
