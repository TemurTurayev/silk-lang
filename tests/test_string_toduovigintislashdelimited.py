"""
Tests for string .toDuovigintiSlashDelimited() method - join words with 22 slash chars.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiSlashDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiSlashDelimited())')
        assert output[-1] == "hello" + "/" * 22 + "world"

    def test_toDuovigintiSlashDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiSlashDelimited())')
        assert output[-1] == "a" + "/" * 22 + "b" + "/" * 22 + "c"
