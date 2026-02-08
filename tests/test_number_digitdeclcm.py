"""
Tests for number .digitDecLCM() method - LCM of each consecutive 10-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDecLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDecLCM_basic(self):
        output = self._run('print(12345678911234567891.digitDecLCM())')
        # lcm(1,2,3,4,5,6,7,8,9,1)=2520; lcm(1,2,3,4,5,6,7,8,9,1)=2520
        assert output[-1] == "[2520, 2520]"

    def test_digitDecLCM_remainder(self):
        output = self._run('print(123456789124.digitDecLCM())')
        # lcm(1,2,3,4,5,6,7,8,9,1)=2520; lcm(2,4)=4
        assert output[-1] == "[2520, 4]"
