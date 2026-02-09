"""
Tests for number .digitDuodecMax() method - max of each consecutive 12-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodecMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodecMax_basic(self):
        output = self._run('print(123456789012345678901234.digitDuodecMax())')
        # max(1..9,0,1,2)=9, max(3..9,0,1,2,3,4)=9
        assert output[-1] == "[9, 9]"

    def test_digitDuodecMax_single(self):
        output = self._run('print(123456789012.digitDuodecMax())')
        assert output[-1] == "[9]"
