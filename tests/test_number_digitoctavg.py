"""
Tests for number .digitOctAvg() method - average of each consecutive octuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitOctAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitOctAvg_basic(self):
        output = self._run('print(1234567812345678.digitOctAvg())')
        # [avg(1..8)=4.5, avg(1..8)=4.5]
        assert output[-1] == "[4.5, 4.5]"

    def test_digitOctAvg_remainder(self):
        output = self._run('print(1234567890.digitOctAvg())')
        # [avg(1..8)=4.5, avg(9,0)=4.5]
        assert output[-1] == "[4.5, 4.5]"
