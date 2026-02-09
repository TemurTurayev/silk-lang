"""
Tests for number .digitSedecProduct() method - product of each consecutive 16-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSedecProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSedecProduct_basic(self):
        output = self._run('print(1211121112111211.digitSedecProduct())')
        # product(1,2,1,1,1,2,1,1,1,2,1,1,1,2,1,1) = 16
        assert output[-1] == "[16]"

    def test_digitSedecProduct_remainder(self):
        output = self._run('print(12111211121112115.digitSedecProduct())')
        # product(1,2,1,..)=16, product(5)=5
        assert output[-1] == "[16, 5]"
