"""
Tests for number .digitSeptendecLCM() method - LCM of each consecutive 17-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptendecLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptendecLCM_basic(self):
        output = self._run('print(12312312312312312.digitSeptendecLCM())')
        # lcm(1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2) = 6
        assert output[-1] == "[6]"

    def test_digitSeptendecLCM_remainder(self):
        output = self._run('print(123123123123123124.digitSeptendecLCM())')
        # lcm(1,2,3,..)=6, lcm(4)=4
        assert output[-1] == "[6, 4]"
