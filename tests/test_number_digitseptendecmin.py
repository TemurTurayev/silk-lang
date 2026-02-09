"""
Tests for number .digitSeptendecMin() method - min of each consecutive 17-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptendecMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptendecMin_basic(self):
        output = self._run('print(12345678912345678.digitSeptendecMin())')
        # min(1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8) = 1
        assert output[-1] == "[1]"

    def test_digitSeptendecMin_remainder(self):
        output = self._run('print(123456789123456789.digitSeptendecMin())')
        # min(1..8,9,1..8)=1, min(9)=9
        assert output[-1] == "[1, 9]"
