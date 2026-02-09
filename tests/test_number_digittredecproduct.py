"""
Tests for number .digitTredecProduct() method - product of each consecutive 13-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTredecProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTredecProduct_basic(self):
        output = self._run('print(1111111111111.digitTredecProduct())')
        # product(1*13) = 1
        assert output[-1] == "[1]"

    def test_digitTredecProduct_remainder(self):
        output = self._run('print(11111111111115.digitTredecProduct())')
        # product(1*13)=1, product(5)=5
        assert output[-1] == "[1, 5]"
