"""
Tests for string .toUndecSlashDelimited() method - split words by /////////// (11 slashes).
"""

from silk.interpreter import Interpreter


class TestStringToUndecSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecSlashDelimited_basic(self):
        output = self._run('print("hello world".toUndecSlashDelimited())')
        assert output[-1] == "hello///////////world"

    def test_toUndecSlashDelimited_three(self):
        output = self._run('print("a b c".toUndecSlashDelimited())')
        assert output[-1] == "a///////////b///////////c"
