"""
Tests for number .digitSeptMax() method - max of each consecutive septuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptMax_basic(self):
        output = self._run('print(12345671234567.digitSeptMax())')
        # [max(1,2,3,4,5,6,7)=7, max(1,2,3,4,5,6,7)=7]
        assert output[-1] == "[7, 7]"

    def test_digitSeptMax_remainder(self):
        output = self._run('print(123456789.digitSeptMax())')
        # [max(1,2,3,4,5,6,7)=7, max(8,9)=9]
        assert output[-1] == "[7, 9]"
