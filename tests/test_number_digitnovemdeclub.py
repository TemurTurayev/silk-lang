"""
Tests for number .digitNovemdecLCM() method - LCM of each consecutive 19-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitNovemdecLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitNovemdecLCM_basic(self):
        output = self._run('print(2468246824682468246.digitNovemdecLCM())')
        # lcm(2,4,6,8,2,4,6,8,2,4,6,8,2,4,6,8,2,4,6) = 24
        assert output[-1] == "[24]"

    def test_digitNovemdecLCM_remainder(self):
        output = self._run('print(24682468246824682465.digitNovemdecLCM())')
        # lcm(...)=24, lcm(5)=5
        assert output[-1] == "[24, 5]"
