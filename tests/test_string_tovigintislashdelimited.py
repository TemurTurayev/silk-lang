"""
Tests for string .toVigintiSlashDelimited() method - join words with 20 slashes.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiSlashDelimited_basic(self):
        output = self._run('print("hello world".toVigintiSlashDelimited())')
        assert output[-1] == "hello" + "/" * 20 + "world"

    def test_toVigintiSlashDelimited_multi(self):
        output = self._run('print("a b c".toVigintiSlashDelimited())')
        assert output[-1] == "a" + "/" * 20 + "b" + "/" * 20 + "c"
