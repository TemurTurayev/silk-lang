"""
Tests for number .digitQuattuordecMin() method - min of each consecutive 14-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuordecMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuordecMin_basic(self):
        output = self._run('print(12345678901234.digitQuattuordecMin())')
        # min(1,2,3,4,5,6,7,8,9,0,1,2,3,4) = 0
        assert output[-1] == "[0]"

    def test_digitQuattuordecMin_remainder(self):
        output = self._run('print(123456789012347.digitQuattuordecMin())')
        # min(1..4)=0, min(7)=7
        assert output[-1] == "[0, 7]"
