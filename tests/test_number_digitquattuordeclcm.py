"""
Tests for number .digitQuattuordecLCM() method - LCM of each consecutive 14-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuordecLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuordecLCM_basic(self):
        output = self._run('print(12312312312312.digitQuattuordecLCM())')
        # lcm(1,2,3,1,2,3,1,2,3,1,2,3,1,2) = 6
        assert output[-1] == "[6]"

    def test_digitQuattuordecLCM_remainder(self):
        output = self._run('print(123123123123124.digitQuattuordecLCM())')
        # lcm(1,2,3,..)=6, lcm(4)=4
        assert output[-1] == "[6, 4]"
