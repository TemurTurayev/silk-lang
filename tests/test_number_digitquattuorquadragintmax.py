"""
Tests for number .digitQuattuorquadragintMax() method - max of each consecutive 44-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuorquadragintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuorquadragintMax_basic(self):
        output = self._run('print(11111111111111111111111111111111111111111111.digitQuattuorquadragintMax())')
        assert output[-1] == "[1]"

    def test_digitQuattuorquadragintMax_remainder(self):
        output = self._run('print(111111111111111111111111111111111111111111119.digitQuattuorquadragintMax())')
        assert output[-1] == "[1, 9]"
