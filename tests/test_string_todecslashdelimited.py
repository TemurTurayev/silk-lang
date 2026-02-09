"""
Tests for string .toDecSlashDelimited() method - split words by ////////// (10 slashes).
"""

from silk.interpreter import Interpreter


class TestStringToDecSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecSlashDelimited_basic(self):
        output = self._run('print("hello world".toDecSlashDelimited())')
        assert output[-1] == "hello//////////world"

    def test_toDecSlashDelimited_three(self):
        output = self._run('print("a b c".toDecSlashDelimited())')
        assert output[-1] == "a//////////b//////////c"
