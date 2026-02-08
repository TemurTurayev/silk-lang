"""
Tests for string .toQuintSlashDelimited() method - split words by /////.
"""

from silk.interpreter import Interpreter


class TestStringToQuintSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuintSlashDelimited_basic(self):
        output = self._run('print("hello world".toQuintSlashDelimited())')
        assert output[-1] == "hello/////world"

    def test_toQuintSlashDelimited_three(self):
        output = self._run('print("a b c".toQuintSlashDelimited())')
        assert output[-1] == "a/////b/////c"
