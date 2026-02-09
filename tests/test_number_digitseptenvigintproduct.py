"""
Tests for number .digitSeptenvigintProduct() method - product of each consecutive 27-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptenvigintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptenvigintProduct_basic(self):
        output = self._run('print(111111111111111111111111111.digitSeptenvigintProduct())')
        assert output[-1] == "[1]"

    def test_digitSeptenvigintProduct_remainder(self):
        output = self._run('print(2222222222222222222222222225.digitSeptenvigintProduct())')
        assert output[-1] == "[134217728, 5]"
