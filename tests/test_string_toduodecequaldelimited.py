"""
Tests for string .toDuodecEqualDelimited() method - split words by ============ (12 equals).
"""

from silk.interpreter import Interpreter


class TestStringToDuodecEqualDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuodecEqualDelimited_basic(self):
        output = self._run('print("hello world".toDuodecEqualDelimited())')
        assert output[-1] == "hello============world"

    def test_toDuodecEqualDelimited_three(self):
        output = self._run('print("a b c".toDuodecEqualDelimited())')
        assert output[-1] == "a============b============c"
