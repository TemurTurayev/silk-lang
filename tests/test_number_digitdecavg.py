"""
Tests for number .digitDecAvg() method - average of each consecutive 10-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDecAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDecAvg_basic(self):
        output = self._run('print(12345678901234567890.digitDecAvg())')
        # [avg(1..9,0)=4.5, avg(1..9,0)=4.5]
        assert output[-1] == "[4.5, 4.5]"

    def test_digitDecAvg_remainder(self):
        output = self._run('print(123456789024.digitDecAvg())')
        # [avg(1..9,0)=4.5, avg(2,4)=3]
        assert output[-1] == "[4.5, 3]"
