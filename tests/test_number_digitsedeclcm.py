"""
Tests for number .digitSedecLCM() method - LCM of each consecutive 16-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSedecLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSedecLCM_basic(self):
        output = self._run('print(1231231231231231.digitSedecLCM())')
        # lcm(1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1) = 6
        assert output[-1] == "[6]"

    def test_digitSedecLCM_remainder(self):
        output = self._run('print(12312312312312314.digitSedecLCM())')
        # lcm(1,2,3,..)=6, lcm(4)=4
        assert output[-1] == "[6, 4]"
