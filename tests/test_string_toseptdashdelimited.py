"""
Tests for string .toSeptDashDelimited() method - split words by -------.
"""

from silk.interpreter import Interpreter


class TestStringToSeptDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptDashDelimited_basic(self):
        output = self._run('print("hello world".toSeptDashDelimited())')
        assert output[-1] == "hello-------world"

    def test_toSeptDashDelimited_three(self):
        output = self._run('print("a b c".toSeptDashDelimited())')
        assert output[-1] == "a-------b-------c"
