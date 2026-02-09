"""
Tests for number .digitQuattuordecAvg() method - average of each consecutive 14-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuordecAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuordecAvg_basic(self):
        output = self._run('print(12345678901234.digitQuattuordecAvg())')
        # avg(1..4,5..9,0,1..4) = 55/14
        result = eval(output[-1])
        assert abs(result[0] - 55/14) < 0.001

    def test_digitQuattuordecAvg_remainder(self):
        output = self._run('print(123456789012345.digitQuattuordecAvg())')
        result = eval(output[-1])
        assert result[1] == 5
