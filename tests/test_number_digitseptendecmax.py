"""
Tests for number .digitSeptendecMax() method - max of each consecutive 17-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptendecMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptendecMax_basic(self):
        output = self._run('print(12345678912345678.digitSeptendecMax())')
        # max(1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8) = 9
        assert output[-1] == "[9]"

    def test_digitSeptendecMax_remainder(self):
        output = self._run('print(123456789123456783.digitSeptendecMax())')
        # max(1..8,9,1..8)=9, max(3)=3
        assert output[-1] == "[9, 3]"
