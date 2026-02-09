"""
Tests for number .digitTrevigintProduct() method - product of each consecutive 23-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrevigintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrevigintProduct_basic(self):
        output = self._run('print(22222222222222222222222.digitTrevigintProduct())')
        assert output[-1] == "[8388608]"

    def test_digitTrevigintProduct_remainder(self):
        output = self._run('print(222222222222222222222225.digitTrevigintProduct())')
        # product(2*23)=2^23=8388608, product(5)=5
        assert output[-1] == "[8388608, 5]"
