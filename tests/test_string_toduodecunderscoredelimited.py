"""
Tests for string .toDuodecUnderscoreDelimited() method - join words with 12 underscores.
"""

from silk.interpreter import Interpreter


class TestStringToDuodecUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuodecUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toDuodecUnderscoreDelimited())')
        assert output[-1] == "hello____________world"

    def test_toDuodecUnderscoreDelimited_three(self):
        output = self._run('print("a b c".toDuodecUnderscoreDelimited())')
        assert output[-1] == "a____________b____________c"
