"""
Tests for number .digitUnquadragintProduct() method - product of each consecutive 41-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUnquadragintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUnquadragintProduct_basic(self):
        output = self._run('print(11111111111111111111111111111111111111111.digitUnquadragintProduct())')
        assert output[-1] == "[1]"

    def test_digitUnquadragintProduct_remainder(self):
        output = self._run('print(222222222222222222222222222222222222222223.digitUnquadragintProduct())')
        assert output[-1] == "[" + str(2**41) + ", 3]"
