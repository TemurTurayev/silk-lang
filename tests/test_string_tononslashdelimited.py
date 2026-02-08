"""
Tests for string .toNonSlashDelimited() method - split words by ///////// (9 slashes).
"""

from silk.interpreter import Interpreter


class TestStringToNonSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonSlashDelimited_basic(self):
        output = self._run('print("hello world".toNonSlashDelimited())')
        assert output[-1] == "hello/////////world"

    def test_toNonSlashDelimited_three(self):
        output = self._run('print("a b c".toNonSlashDelimited())')
        assert output[-1] == "a/////////b/////////c"
