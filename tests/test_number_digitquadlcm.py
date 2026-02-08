"""
Tests for number .digitQuadLCM() method - LCM of each consecutive quadruple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuadLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuadLCM_basic(self):
        output = self._run('print(23463648.digitQuadLCM())')
        # [lcm(2,3,4,6)=12, lcm(3,6,4,8)=24]
        assert output[-1] == "[12, 24]"

    def test_digitQuadLCM_remainder(self):
        output = self._run('print(23465.digitQuadLCM())')
        # [lcm(2,3,4,6)=12, lcm(5)=5]
        assert output[-1] == "[12, 5]"
