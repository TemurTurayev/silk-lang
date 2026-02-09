"""
Tests for number .digitQuattuordecMax() method - max of each consecutive 14-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuordecMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuordecMax_basic(self):
        output = self._run('print(12345678901234.digitQuattuordecMax())')
        # max(1,2,3,4,5,6,7,8,9,0,1,2,3,4) = 9
        assert output[-1] == "[9]"

    def test_digitQuattuordecMax_remainder(self):
        output = self._run('print(123456789012347.digitQuattuordecMax())')
        # max(1..4)=9, max(7)=7
        assert output[-1] == "[9, 7]"
