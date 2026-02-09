"""
Tests for string .toDuodecAmpersandDelimited() method - split words by &&&&&&&&&&&& (12 ampersands).
"""

from silk.interpreter import Interpreter


class TestStringToDuodecAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuodecAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toDuodecAmpersandDelimited())')
        assert output[-1] == "hello&&&&&&&&&&&&world"

    def test_toDuodecAmpersandDelimited_three(self):
        output = self._run('print("a b c".toDuodecAmpersandDelimited())')
        assert output[-1] == "a&&&&&&&&&&&&b&&&&&&&&&&&&c"
