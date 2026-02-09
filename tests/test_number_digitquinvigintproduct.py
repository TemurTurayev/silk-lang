"""
Tests for number .digitQuinvigintProduct() method - product of each consecutive 25-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuinvigintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuinvigintProduct_basic(self):
        output = self._run('print(1111111111111111111111111.digitQuinvigintProduct())')
        assert output[-1] == "[1]"

    def test_digitQuinvigintProduct_remainder(self):
        output = self._run('print(11111111111111111111111113.digitQuinvigintProduct())')
        assert output[-1] == "[1, 3]"
