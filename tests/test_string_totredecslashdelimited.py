"""
Tests for string .toTredecSlashDelimited() method - join words with 13 slashes.
"""

from silk.interpreter import Interpreter


class TestStringToTredecSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTredecSlashDelimited_basic(self):
        output = self._run('print("hello world".toTredecSlashDelimited())')
        assert output[-1] == "hello/////////////world"

    def test_toTredecSlashDelimited_three(self):
        output = self._run('print("a b c".toTredecSlashDelimited())')
        assert output[-1] == "a/////////////b/////////////c"
