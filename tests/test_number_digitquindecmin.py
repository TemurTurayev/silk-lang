"""
Tests for number .digitQuindecMin() method - min of each consecutive 15-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuindecMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuindecMin_basic(self):
        output = self._run('print(123456789012345.digitQuindecMin())')
        # min(1,2,3,4,5,6,7,8,9,0,1,2,3,4,5) = 0
        assert output[-1] == "[0]"

    def test_digitQuindecMin_remainder(self):
        output = self._run('print(1234567890123457.digitQuindecMin())')
        # min(1..5)=0, min(7)=7
        assert output[-1] == "[0, 7]"
