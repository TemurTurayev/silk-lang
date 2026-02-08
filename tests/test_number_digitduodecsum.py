"""
Tests for number .digitDuodecSum() method - sum of each consecutive 12-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodecSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodecSum_basic(self):
        output = self._run('print(123456789012345678901234.digitDuodecSum())')
        # sum(1,2,3,4,5,6,7,8,9,0,1,2)=48, sum(3,4,5,6,7,8,9,0,1,2,3,4)=52
        assert output[-1] == "[48, 52]"

    def test_digitDuodecSum_single(self):
        output = self._run('print(123456789012.digitDuodecSum())')
        # sum(1,2,3,4,5,6,7,8,9,0,1,2)=48
        assert output[-1] == "[48]"
