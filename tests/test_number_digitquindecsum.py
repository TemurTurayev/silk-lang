"""
Tests for number .digitQuindecSum() method - sum of each consecutive 15-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuindecSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuindecSum_basic(self):
        output = self._run('print(123456789012345.digitQuindecSum())')
        # sum(1,2,3,4,5,6,7,8,9,0,1,2,3,4,5) = 60
        assert output[-1] == "[60]"

    def test_digitQuindecSum_remainder(self):
        output = self._run('print(1234567890123456.digitQuindecSum())')
        # sum(1..5)=60, sum(6)=6
        assert output[-1] == "[60, 6]"
