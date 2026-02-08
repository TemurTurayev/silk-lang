"""
Tests for number .digitPairAvg() method - average of each consecutive pair of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitPairAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitPairAvg_basic(self):
        output = self._run('print(4268.digitPairAvg())')
        # [avg(4,2)=3, avg(6,8)=7]
        assert output[-1] == "[3, 7]"

    def test_digitPairAvg_odd(self):
        output = self._run('print(93615.digitPairAvg())')
        # [avg(9,3)=6, avg(6,1)=3.5, 5]
        assert output[-1] == "[6, 3.5, 5]"
