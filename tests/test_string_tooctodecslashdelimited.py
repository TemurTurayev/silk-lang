"""
Tests for string .toOctodecSlashDelimited() method - join words with 18 slashes.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecSlashDelimited_basic(self):
        output = self._run('print("hello world".toOctodecSlashDelimited())')
        assert output[-1] == "hello" + "/" * 18 + "world"

    def test_toOctodecSlashDelimited_three(self):
        output = self._run('print("a b c".toOctodecSlashDelimited())')
        assert output[-1] == "a" + "/" * 18 + "b" + "/" * 18 + "c"
