"""
Tests for string .toDoubleSlashDelimited() method - split words by //.
"""

from silk.interpreter import Interpreter


class TestStringToDoubleSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDoubleSlashDelimited_basic(self):
        output = self._run('print("hello world".toDoubleSlashDelimited())')
        assert output[-1] == "hello//world"

    def test_toDoubleSlashDelimited_three(self):
        output = self._run('print("a b c".toDoubleSlashDelimited())')
        assert output[-1] == "a//b//c"
