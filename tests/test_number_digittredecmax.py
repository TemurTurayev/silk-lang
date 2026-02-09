"""
Tests for number .digitTredecMax() method - max of each consecutive 13-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTredecMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTredecMax_basic(self):
        output = self._run('print(1234567890123.digitTredecMax())')
        # max(1,2,3,4,5,6,7,8,9,0,1,2,3) = 9
        assert output[-1] == "[9]"

    def test_digitTredecMax_remainder(self):
        output = self._run('print(12345678901237.digitTredecMax())')
        # max(1..3)=9, max(7)=7
        assert output[-1] == "[9, 7]"
