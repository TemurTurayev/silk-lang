"""
Tests for number .digitQuintAvg() method - average of each consecutive quintuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuintAvg_basic(self):
        output = self._run('print(1234567890.digitQuintAvg())')
        # [avg(1,2,3,4,5)=3, avg(6,7,8,9,0)=6]
        assert output[-1] == "[3, 6]"

    def test_digitQuintAvg_remainder(self):
        output = self._run('print(1234536.digitQuintAvg())')
        # [avg(1,2,3,4,5)=3, avg(3,6)=4.5]
        assert output[-1] == "[3, 4.5]"
