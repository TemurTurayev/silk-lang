"""
Tests for number .digitQuattuorquadragintLCM() method - LCM of each consecutive 44-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuorquadragintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuorquadragintLCM_basic(self):
        output = self._run('print(11111111111111111111111111111111111111111111.digitQuattuorquadragintLCM())')
        assert output[-1] == "[1]"

    def test_digitQuattuorquadragintLCM_remainder(self):
        output = self._run('print(22222222222222222222222222222222222222222222344.digitQuattuorquadragintLCM())')
        assert output[-1] == "[2, 12]"
