"""
Tests for number .digitDuodequadragintProduct() method - product of each consecutive 38-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodequadragintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodequadragintProduct_basic(self):
        output = self._run('print(11111111111111111111111111111111111111.digitDuodequadragintProduct())')
        assert output[-1] == "[1]"

    def test_digitDuodequadragintProduct_remainder(self):
        output = self._run('print(222222222222222222222222222222222222223.digitDuodequadragintProduct())')
        assert output[-1] == "[" + str(2**38) + ", 3]"
