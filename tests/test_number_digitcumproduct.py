"""
Tests for number .digitCumProduct() method - cumulative product of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitCumProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitCumProduct_basic(self):
        output = self._run('print(1234.digitCumProduct())')
        assert output[-1] == "[1, 2, 6, 24]"

    def test_digitCumProduct_single(self):
        output = self._run('print(5.digitCumProduct())')
        assert output[-1] == "[5]"
