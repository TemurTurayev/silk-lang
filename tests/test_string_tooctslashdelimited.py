"""
Tests for string .toOctSlashDelimited() method - split words by //////// (8 slashes).
"""

from silk.interpreter import Interpreter


class TestStringToOctSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctSlashDelimited_basic(self):
        output = self._run('print("hello world".toOctSlashDelimited())')
        assert output[-1] == "hello////////world"

    def test_toOctSlashDelimited_three(self):
        output = self._run('print("a b c".toOctSlashDelimited())')
        assert output[-1] == "a////////b////////c"
