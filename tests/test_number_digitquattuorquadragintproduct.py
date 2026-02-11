"""
Tests for number .digitQuattuorquadragintProduct() method - product of each consecutive 44-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuorquadragintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuorquadragintProduct_basic(self):
        output = self._run('print(11111111111111111111111111111111111111111111.digitQuattuorquadragintProduct())')
        assert output[-1] == "[1]"

    def test_digitQuattuorquadragintProduct_remainder(self):
        output = self._run('print(111111111111111111111111111111111111111111112.digitQuattuorquadragintProduct())')
        assert output[-1] == "[1, 2]"
