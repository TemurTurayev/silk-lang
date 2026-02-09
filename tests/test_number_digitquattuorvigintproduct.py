"""
Tests for number .digitQuattuorvigintProduct() method - product of each consecutive 24-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuorvigintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuorvigintProduct_basic(self):
        output = self._run('print(222222222222222222222222.digitQuattuorvigintProduct())')
        assert output[-1] == "[16777216]"

    def test_digitQuattuorvigintProduct_remainder(self):
        output = self._run('print(2222222222222222222222225.digitQuattuorvigintProduct())')
        # product(2*24)=2^24=16777216, product(5)=5
        assert output[-1] == "[16777216, 5]"
