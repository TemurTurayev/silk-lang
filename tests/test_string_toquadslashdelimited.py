"""
Tests for string .toQuadSlashDelimited() method - split words by ////.
"""

from silk.interpreter import Interpreter


class TestStringToQuadSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuadSlashDelimited_basic(self):
        output = self._run('print("hello world".toQuadSlashDelimited())')
        assert output[-1] == "hello////world"

    def test_toQuadSlashDelimited_three(self):
        output = self._run('print("a b c".toQuadSlashDelimited())')
        assert output[-1] == "a////b////c"
