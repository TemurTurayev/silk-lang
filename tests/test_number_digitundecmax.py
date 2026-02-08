"""
Tests for number .digitUndecMax() method - max of each consecutive 11-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndecMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndecMax_basic(self):
        output = self._run('print(12345678901234567890123.digitUndecMax())')
        # [max(1,2,3,4,5,6,7,8,9,0,1)=9, max(2,3,4,5,6,7,8,9,0,1,2)=9, 3=3]
        assert output[-1] == "[9, 9, 3]"

    def test_digitUndecMax_single_group(self):
        output = self._run('print(12345678901.digitUndecMax())')
        # [max(1,2,3,4,5,6,7,8,9,0,1)=9]
        assert output[-1] == "[9]"
