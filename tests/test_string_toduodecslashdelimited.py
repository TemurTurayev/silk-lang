"""
Tests for string .toDuodecSlashDelimited() method - join words with 12 slashes.
"""

from silk.interpreter import Interpreter


class TestStringToDuodecSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuodecSlashDelimited_basic(self):
        output = self._run('print("hello world".toDuodecSlashDelimited())')
        assert output[-1] == "hello////////////world"

    def test_toDuodecSlashDelimited_three(self):
        output = self._run('print("a b c".toDuodecSlashDelimited())')
        assert output[-1] == "a////////////b////////////c"
