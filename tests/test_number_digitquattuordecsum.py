"""
Tests for number .digitQuattuordecSum() method - sum of each consecutive 14-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuordecSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuordecSum_basic(self):
        output = self._run('print(12345678901234.digitQuattuordecSum())')
        # sum(1,2,3,4,5,6,7,8,9,0,1,2,3,4) = 55
        assert output[-1] == "[55]"

    def test_digitQuattuordecSum_remainder(self):
        output = self._run('print(123456789012345.digitQuattuordecSum())')
        # sum(1..4)=55, sum(5)=5
        assert output[-1] == "[55, 5]"
