"""
Tests for string .toQuattuordecSlashDelimited() method - join words with 14 slashes.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecSlashDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecSlashDelimited())')
        assert output[-1] == "hello//////////////world"

    def test_toQuattuordecSlashDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecSlashDelimited())')
        assert output[-1] == "a//////////////b//////////////c"
