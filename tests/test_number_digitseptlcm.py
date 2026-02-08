"""
Tests for number .digitSeptLCM() method - LCM of each consecutive septuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptLCM_basic(self):
        output = self._run('print(12345671234567.digitSeptLCM())')
        # [lcm(1,2,3,4,5,6,7)=420, lcm(1,2,3,4,5,6,7)=420]
        assert output[-1] == "[420, 420]"

    def test_digitSeptLCM_remainder(self):
        output = self._run('print(123456789.digitSeptLCM())')
        # [lcm(1,2,3,4,5,6,7)=420, lcm(8,9)=72]
        assert output[-1] == "[420, 72]"
