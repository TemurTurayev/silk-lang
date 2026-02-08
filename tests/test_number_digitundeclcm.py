"""
Tests for number .digitUndecLCM() method - LCM of each consecutive 11-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndecLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndecLCM_basic(self):
        output = self._run('print(12345612345.digitUndecLCM())')
        # lcm(1,2,3,4,5,6,1,2,3,4,5) = 60
        assert output[-1] == "[60]"

    def test_digitUndecLCM_remainder(self):
        output = self._run('print(123456123453.digitUndecLCM())')
        # lcm(1,2,3,4,5,6,1,2,3,4,5)=60, lcm(3)=3
        assert output[-1] == "[60, 3]"
