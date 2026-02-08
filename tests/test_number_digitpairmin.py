"""
Tests for number .digitPairMin() method - min of each consecutive pair of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitPairMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitPairMin_basic(self):
        output = self._run('print(1234.digitPairMin())')
        # [min(1,2), min(3,4)] = [1, 3]
        assert output[-1] == "[1, 3]"

    def test_digitPairMin_odd(self):
        output = self._run('print(51627.digitPairMin())')
        # [min(5,1), min(6,2), 7] = [1, 2, 7]
        assert output[-1] == "[1, 2, 7]"
