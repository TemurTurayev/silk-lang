"""
Tests for number .digitDuodecProduct() method - product of each consecutive 12-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodecProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodecProduct_basic(self):
        output = self._run('print(111111111111222222222222.digitDuodecProduct())')
        # product(1*12)=1, product(2*12)=4096
        assert output[-1] == "[1, 4096]"

    def test_digitDuodecProduct_remainder(self):
        output = self._run('print(1111111111113.digitDuodecProduct())')
        # product(1*12)=1, product(3)=3
        assert output[-1] == "[1, 3]"
