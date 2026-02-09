"""
Tests for number .digitQuindecMax() method - max of each consecutive 15-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuindecMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuindecMax_basic(self):
        output = self._run('print(123456789012345.digitQuindecMax())')
        # max(1,2,3,4,5,6,7,8,9,0,1,2,3,4,5) = 9
        assert output[-1] == "[9]"

    def test_digitQuindecMax_remainder(self):
        output = self._run('print(1234567890123457.digitQuindecMax())')
        # max(1..5)=9, max(7)=7
        assert output[-1] == "[9, 7]"
