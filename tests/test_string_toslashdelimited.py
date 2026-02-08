"""
Tests for string .toSlashDelimited() method - split words by forward slash.
"""

from silk.interpreter import Interpreter


class TestStringToSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSlashDelimited_basic(self):
        output = self._run('print("hello world".toSlashDelimited())')
        assert output[-1] == "hello/world"

    def test_toSlashDelimited_three(self):
        output = self._run('print("a b c".toSlashDelimited())')
        assert output[-1] == "a/b/c"
