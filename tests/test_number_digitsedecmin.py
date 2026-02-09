"""
Tests for number .digitSedecMin() method - min of each consecutive 16-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSedecMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSedecMin_basic(self):
        output = self._run('print(1234567812345678.digitSedecMin())')
        # min(1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8) = 1
        assert output[-1] == "[1]"

    def test_digitSedecMin_remainder(self):
        output = self._run('print(12345678123456789.digitSedecMin())')
        # min(1..8,1..8)=1, min(9)=9
        assert output[-1] == "[1, 9]"
