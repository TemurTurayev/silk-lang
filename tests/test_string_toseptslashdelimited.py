"""
Tests for string .toSeptSlashDelimited() method - split words by ///////.
"""

from silk.interpreter import Interpreter


class TestStringToSeptSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptSlashDelimited_basic(self):
        output = self._run('print("hello world".toSeptSlashDelimited())')
        assert output[-1] == "hello///////world"

    def test_toSeptSlashDelimited_three(self):
        output = self._run('print("a b c".toSeptSlashDelimited())')
        assert output[-1] == "a///////b///////c"
