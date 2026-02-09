"""
Tests for number .digitDuodecLCM() method - LCM of each consecutive 12-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodecLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodecLCM_basic(self):
        output = self._run('print(123456123456.digitDuodecLCM())')
        # lcm(1,2,3,4,5,6,1,2,3,4,5,6) = 60
        assert output[-1] == "[60]"

    def test_digitDuodecLCM_remainder(self):
        output = self._run('print(1234561234563.digitDuodecLCM())')
        # lcm(1,2,3,4,5,6,1,2,3,4,5,6)=60, lcm(3)=3
        assert output[-1] == "[60, 3]"
