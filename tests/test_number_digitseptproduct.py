"""
Tests for number .digitSeptProduct() method - product of each consecutive septuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptProduct_basic(self):
        output = self._run('print(12345671234567.digitSeptProduct())')
        # [1*2*3*4*5*6*7=5040, 1*2*3*4*5*6*7=5040]
        assert output[-1] == "[5040, 5040]"

    def test_digitSeptProduct_remainder(self):
        output = self._run('print(123456789.digitSeptProduct())')
        # [1*2*3*4*5*6*7=5040, 8*9=72]
        assert output[-1] == "[5040, 72]"
