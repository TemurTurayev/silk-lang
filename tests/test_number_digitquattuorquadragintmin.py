"""
Tests for number .digitQuattuorquadragintMin() method - min of each consecutive 44-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuorquadragintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuorquadragintMin_basic(self):
        output = self._run('print(11111111111111111111111111111111111111111111.digitQuattuorquadragintMin())')
        assert output[-1] == "[1]"

    def test_digitQuattuorquadragintMin_remainder(self):
        output = self._run('print(111111111111111111111111111111111111111111119.digitQuattuorquadragintMin())')
        assert output[-1] == "[1, 9]"
