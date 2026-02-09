"""
Tests for string .toNovemdecSlashDelimited() method - join words with 19 slashes.
"""

from silk.interpreter import Interpreter


class TestStringToNovemdecSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNovemdecSlashDelimited_basic(self):
        output = self._run('print("hello world".toNovemdecSlashDelimited())')
        assert output[-1] == "hello///////////////////world"

    def test_toNovemdecSlashDelimited_multi(self):
        output = self._run('print("a b c".toNovemdecSlashDelimited())')
        assert output[-1] == "a///////////////////b///////////////////c"
