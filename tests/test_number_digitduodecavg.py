"""
Tests for number .digitDuodecAvg() method - average of each consecutive 12-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodecAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodecAvg_basic(self):
        output = self._run('print(123456789012.digitDuodecAvg())')
        # avg(1..9,0,1,2) = 48/12 = 4
        assert output[-1] == "[4]"

    def test_digitDuodecAvg_remainder(self):
        output = self._run('print(1234567890125.digitDuodecAvg())')
        # avg(1..9,0,1,2)=4, avg(5)=5
        assert output[-1] == "[4, 5]"
