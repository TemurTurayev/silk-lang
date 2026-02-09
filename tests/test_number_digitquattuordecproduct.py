"""
Tests for number .digitQuattuordecProduct() method - product of each consecutive 14-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuordecProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuordecProduct_basic(self):
        output = self._run('print(11111111111111.digitQuattuordecProduct())')
        # product(1*14) = 1
        assert output[-1] == "[1]"

    def test_digitQuattuordecProduct_remainder(self):
        output = self._run('print(111111111111113.digitQuattuordecProduct())')
        # product(1*14)=1, product(3)=3
        assert output[-1] == "[1, 3]"
