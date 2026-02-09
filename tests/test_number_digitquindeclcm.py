"""
Tests for number .digitQuindecLCM() method - LCM of each consecutive 15-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuindecLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuindecLCM_basic(self):
        output = self._run('print(123123123123123.digitQuindecLCM())')
        # lcm(1,2,3,1,2,3,1,2,3,1,2,3,1,2,3) = 6
        assert output[-1] == "[6]"

    def test_digitQuindecLCM_remainder(self):
        output = self._run('print(1231231231231234.digitQuindecLCM())')
        # lcm(1,2,3,..)=6, lcm(4)=4
        assert output[-1] == "[6, 4]"
