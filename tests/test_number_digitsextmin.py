"""
Tests for number .digitSextMin() method - min of each consecutive sextuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSextMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSextMin_basic(self):
        output = self._run('print(123456789012.digitSextMin())')
        # [min(1,2,3,4,5,6)=1, min(7,8,9,0,1,2)=0]
        assert output[-1] == "[1, 0]"

    def test_digitSextMin_remainder(self):
        output = self._run('print(54321098.digitSextMin())')
        # [min(5,4,3,2,1,0)=0, min(9,8)=8]
        assert output[-1] == "[0, 8]"
