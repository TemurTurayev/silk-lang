"""
Tests for number .digitQuindecProduct() method - product of each consecutive 15-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuindecProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuindecProduct_basic(self):
        output = self._run('print(111111111111111.digitQuindecProduct())')
        # product(1*15) = 1
        assert output[-1] == "[1]"

    def test_digitQuindecProduct_remainder(self):
        output = self._run('print(1111111111111113.digitQuindecProduct())')
        # product(1*15)=1, product(3)=3
        assert output[-1] == "[1, 3]"
