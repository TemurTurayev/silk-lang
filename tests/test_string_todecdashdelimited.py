"""
Tests for string .toDecDashDelimited() method - split words by ---------- (10 dashes).
"""

from silk.interpreter import Interpreter


class TestStringToDecDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecDashDelimited_basic(self):
        output = self._run('print("hello world".toDecDashDelimited())')
        assert output[-1] == "hello----------world"

    def test_toDecDashDelimited_three(self):
        output = self._run('print("a b c".toDecDashDelimited())')
        assert output[-1] == "a----------b----------c"
