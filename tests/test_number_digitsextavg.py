"""
Tests for number .digitSextAvg() method - average of each consecutive sextuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSextAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSextAvg_basic(self):
        output = self._run('print(123456789012.digitSextAvg())')
        # [avg(1,2,3,4,5,6)=3.5, avg(7,8,9,0,1,2)=4.5]
        assert output[-1] == "[3.5, 4.5]"

    def test_digitSextAvg_remainder(self):
        output = self._run('print(12345636.digitSextAvg())')
        # [avg(1,2,3,4,5,6)=3.5, avg(3,6)=4.5]
        assert output[-1] == "[3.5, 4.5]"
