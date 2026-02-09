"""
Tests for number .digitDuodecMin() method - min of each consecutive 12-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodecMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodecMin_basic(self):
        output = self._run('print(123456789012345678901234.digitDuodecMin())')
        # min(1..9,0,1,2)=0, min(3..9,0,1,2,3,4)=0
        assert output[-1] == "[0, 0]"

    def test_digitDuodecMin_no_zero(self):
        output = self._run('print(111111111111.digitDuodecMin())')
        assert output[-1] == "[1]"
