"""
Tests for number .digitTredecAvg() method - average of each consecutive 13-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTredecAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTredecAvg_basic(self):
        output = self._run('print(1234567890123.digitTredecAvg())')
        # avg(1,2,3,4,5,6,7,8,9,0,1,2,3) = 51/13 ≈ 3.923...
        result = self._run('print(1234567890123.digitTredecAvg())')
        val = eval(result[-1])
        assert abs(val[0] - 51/13) < 0.001

    def test_digitTredecAvg_single_remainder(self):
        output = self._run('print(12345678901235.digitTredecAvg())')
        # avg(1..3)=51/13, avg(5)=5
        val = eval(output[-1])
        assert val[1] == 5
