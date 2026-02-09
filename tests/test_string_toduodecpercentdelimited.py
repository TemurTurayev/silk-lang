"""
Tests for string .toDuodecPercentDelimited() method - join words with 12 percent signs.
"""

from silk.interpreter import Interpreter


class TestStringToDuodecPercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuodecPercentDelimited_basic(self):
        output = self._run('print("hello world".toDuodecPercentDelimited())')
        assert output[-1] == "hello%%%%%%%%%%%%world"

    def test_toDuodecPercentDelimited_three(self):
        output = self._run('print("a b c".toDuodecPercentDelimited())')
        assert output[-1] == "a%%%%%%%%%%%%b%%%%%%%%%%%%c"
