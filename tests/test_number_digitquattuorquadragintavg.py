"""
Tests for number .digitQuattuorquadragintAvg() method - average of each consecutive 44-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuorquadragintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuorquadragintAvg_basic(self):
        output = self._run('print(11111111111111111111111111111111111111111111.digitQuattuorquadragintAvg())')
        assert output[-1] == "[1]"

    def test_digitQuattuorquadragintAvg_remainder(self):
        output = self._run('print(111111111111111111111111111111111111111111119.digitQuattuorquadragintAvg())')
        assert output[-1] == "[1, 9]"
