"""
Tests for number .digitTredecMin() method - min of each consecutive 13-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTredecMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTredecMin_basic(self):
        output = self._run('print(1234567890123.digitTredecMin())')
        # min(1,2,3,4,5,6,7,8,9,0,1,2,3) = 0
        assert output[-1] == "[0]"

    def test_digitTredecMin_remainder(self):
        output = self._run('print(12345678901237.digitTredecMin())')
        # min(1..3)=0, min(7)=7
        assert output[-1] == "[0, 7]"
