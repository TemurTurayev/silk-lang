"""
Tests for string .toSextSlashDelimited() method - split words by //////.
"""

from silk.interpreter import Interpreter


class TestStringToSextSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSextSlashDelimited_basic(self):
        output = self._run('print("hello world".toSextSlashDelimited())')
        assert output[-1] == "hello//////world"

    def test_toSextSlashDelimited_three(self):
        output = self._run('print("a b c".toSextSlashDelimited())')
        assert output[-1] == "a//////b//////c"
