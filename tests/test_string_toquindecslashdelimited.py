"""
Tests for string .toQuindecSlashDelimited() method - join words with 15 slashes.
"""

from silk.interpreter import Interpreter


class TestStringToQuindecSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuindecSlashDelimited_basic(self):
        output = self._run('print("hello world".toQuindecSlashDelimited())')
        assert output[-1] == "hello///////////////world"

    def test_toQuindecSlashDelimited_three(self):
        output = self._run('print("a b c".toQuindecSlashDelimited())')
        assert output[-1] == "a///////////////b///////////////c"
