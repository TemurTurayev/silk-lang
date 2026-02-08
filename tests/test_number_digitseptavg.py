"""
Tests for number .digitSeptAvg() method - average of each consecutive septuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptAvg_basic(self):
        output = self._run('print(12345671234567.digitSeptAvg())')
        # [avg(1..7)=4, avg(1..7)=4]
        assert output[-1] == "[4, 4]"

    def test_digitSeptAvg_remainder(self):
        output = self._run('print(123456789.digitSeptAvg())')
        # [avg(1..7)=4, avg(8,9)=8.5]
        assert output[-1] == "[4, 8.5]"
