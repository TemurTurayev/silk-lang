"""
Tests for string .toUnvigintiSlashDelimited() method - join words with 21 slashes.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiSlashDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiSlashDelimited())')
        assert output[-1] == "hello" + "/" * 21 + "world"

    def test_toUnvigintiSlashDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiSlashDelimited())')
        assert output[-1] == "a" + "/" * 21 + "b" + "/" * 21 + "c"
