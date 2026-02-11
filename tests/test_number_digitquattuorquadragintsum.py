"""
Tests for number .digitQuattuorquadragintSum() method - sum of each consecutive 44-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuorquadragintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuorquadragintSum_basic(self):
        output = self._run('print(11111111111111111111111111111111111111111111.digitQuattuorquadragintSum())')
        assert output[-1] == "[44]"

    def test_digitQuattuorquadragintSum_remainder(self):
        output = self._run('print(111111111111111111111111111111111111111111119.digitQuattuorquadragintSum())')
        assert output[-1] == "[44, 9]"
