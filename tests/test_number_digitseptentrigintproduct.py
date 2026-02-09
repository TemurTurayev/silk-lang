"""
Tests for number .digitSeptentrigintProduct() method - product of each consecutive 37-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptentrigintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptentrigintProduct_basic(self):
        output = self._run('print(1111111111111111111111111111111111111.digitSeptentrigintProduct())')
        assert output[-1] == "[1]"

    def test_digitSeptentrigintProduct_remainder(self):
        output = self._run('print(22222222222222222222222222222222222223.digitSeptentrigintProduct())')
        assert output[-1] == "[" + str(2**37) + ", 3]"
