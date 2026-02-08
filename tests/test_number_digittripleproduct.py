"""
Tests for number .digitTripleProduct() method - product of each consecutive triple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTripleProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTripleProduct_basic(self):
        output = self._run('print(123456.digitTripleProduct())')
        # [1*2*3=6, 4*5*6=120]
        assert output[-1] == "[6, 120]"

    def test_digitTripleProduct_remainder(self):
        output = self._run('print(12345.digitTripleProduct())')
        # [1*2*3=6, 4*5=20]
        assert output[-1] == "[6, 20]"
