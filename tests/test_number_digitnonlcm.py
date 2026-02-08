"""
Tests for number .digitNonLCM() method - LCM of each consecutive 9-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitNonLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitNonLCM_basic(self):
        output = self._run('print(123456789123456789.digitNonLCM())')
        # lcm(1,2,3,4,5,6,7,8,9) = 2520
        assert output[-1] == "[2520, 2520]"

    def test_digitNonLCM_remainder(self):
        output = self._run('print(12345678924.digitNonLCM())')
        # lcm(1..9)=2520; lcm(2,4)=4
        assert output[-1] == "[2520, 4]"
