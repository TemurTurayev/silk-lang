"""
Tests for number .digitSeptMin() method - min of each consecutive septuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptMin_basic(self):
        output = self._run('print(12345671234567.digitSeptMin())')
        # [min(1,2,3,4,5,6,7)=1, min(1,2,3,4,5,6,7)=1]
        assert output[-1] == "[1, 1]"

    def test_digitSeptMin_remainder(self):
        output = self._run('print(123456789.digitSeptMin())')
        # [min(1,2,3,4,5,6,7)=1, min(8,9)=8]
        assert output[-1] == "[1, 8]"
