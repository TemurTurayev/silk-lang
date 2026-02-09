"""
Tests for number .digitOctodecLCM() method - LCM of each consecutive 18-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitOctodecLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitOctodecLCM_basic(self):
        output = self._run('print(246824682468246824.digitOctodecLCM())')
        # lcm(2,4,6,8,2,4,6,8,2,4,6,8,2,4,6,8,2,4) = 24
        assert output[-1] == "[24]"

    def test_digitOctodecLCM_remainder(self):
        output = self._run('print(2468246824682468245.digitOctodecLCM())')
        # lcm(...)=24, lcm(5)=5
        assert output[-1] == "[24, 5]"
