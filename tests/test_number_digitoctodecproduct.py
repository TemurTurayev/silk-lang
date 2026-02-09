"""
Tests for number .digitOctodecProduct() method - product of each consecutive 18-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitOctodecProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitOctodecProduct_basic(self):
        output = self._run('print(121112111211121112.digitOctodecProduct())')
        # product(1,2,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,2) = 32
        assert output[-1] == "[32]"

    def test_digitOctodecProduct_remainder(self):
        output = self._run('print(1211121112111211125.digitOctodecProduct())')
        # product(...)=32, product(5)=5
        assert output[-1] == "[32, 5]"
