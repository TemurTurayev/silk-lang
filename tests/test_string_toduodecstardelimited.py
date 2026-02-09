"""
Tests for string .toDuodecStarDelimited() method - split words by ************ (12 stars).
"""

from silk.interpreter import Interpreter


class TestStringToDuodecStarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuodecStarDelimited_basic(self):
        output = self._run('print("hello world".toDuodecStarDelimited())')
        assert output[-1] == "hello************world"

    def test_toDuodecStarDelimited_three(self):
        output = self._run('print("a b c".toDuodecStarDelimited())')
        assert output[-1] == "a************b************c"
