"""
Tests for number .digitTripleAvg() method - average of each consecutive triple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTripleAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTripleAvg_basic(self):
        output = self._run('print(123789.digitTripleAvg())')
        # [avg(1,2,3)=2, avg(7,8,9)=8]
        assert output[-1] == "[2, 8]"

    def test_digitTripleAvg_remainder(self):
        output = self._run('print(52847.digitTripleAvg())')
        # [avg(5,2,8)=5, avg(4,7)=5.5]
        assert output[-1] == "[5, 5.5]"
