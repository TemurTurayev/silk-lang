"""
Tests for string .toSeptendecSlashDelimited() method - join words with 17 slashes.
"""

from silk.interpreter import Interpreter


class TestStringToSeptendecSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptendecSlashDelimited_basic(self):
        output = self._run('print("hello world".toSeptendecSlashDelimited())')
        assert output[-1] == "hello" + "/" * 17 + "world"

    def test_toSeptendecSlashDelimited_three(self):
        output = self._run('print("a b c".toSeptendecSlashDelimited())')
        assert output[-1] == "a" + "/" * 17 + "b" + "/" * 17 + "c"
