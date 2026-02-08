"""
Tests for number .digitUndecMin() method - min of each consecutive 11-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndecMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndecMin_basic(self):
        output = self._run('print(12345678901234567890123.digitUndecMin())')
        # [min(1,2,3,4,5,6,7,8,9,0,1)=0, min(2,3,4,5,6,7,8,9,0,1,2)=0, 3=3]
        assert output[-1] == "[0, 0, 3]"

    def test_digitUndecMin_single_group(self):
        output = self._run('print(12345678901.digitUndecMin())')
        # [min(1,2,3,4,5,6,7,8,9,0,1)=0]
        assert output[-1] == "[0]"
