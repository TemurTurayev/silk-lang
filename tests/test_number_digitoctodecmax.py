"""
Tests for number .digitOctodecMax() method - max of each consecutive 18-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitOctodecMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitOctodecMax_basic(self):
        output = self._run('print(123456789123456789.digitOctodecMax())')
        # max(1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9) = 9
        assert output[-1] == "[9]"

    def test_digitOctodecMax_remainder(self):
        output = self._run('print(1234567891234567893.digitOctodecMax())')
        # max(1..9,1..9)=9, max(3)=3
        assert output[-1] == "[9, 3]"
