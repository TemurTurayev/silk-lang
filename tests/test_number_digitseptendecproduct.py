"""
Tests for number .digitSeptendecProduct() method - product of each consecutive 17-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptendecProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptendecProduct_basic(self):
        output = self._run('print(12111211121112111.digitSeptendecProduct())')
        # product(1,2,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1) = 16
        assert output[-1] == "[16]"

    def test_digitSeptendecProduct_remainder(self):
        output = self._run('print(121112111211121115.digitSeptendecProduct())')
        # product(...)=16, product(5)=5
        assert output[-1] == "[16, 5]"
