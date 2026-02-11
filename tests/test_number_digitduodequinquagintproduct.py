"""
Tests for number .digitDuodequinquagintProduct() method - product of each consecutive 48-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodequinquagintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodequinquagintProduct_basic(self):
        output = self._run('print(111111111111111111111111111111111111111111111111.digitDuodequinquagintProduct())')
        assert output[-1] == "[1]"

    def test_digitDuodequinquagintProduct_remainder(self):
        output = self._run('print(1111111111111111111111111111111111111111111111112.digitDuodequinquagintProduct())')
        assert output[-1] == "[1, 2]"
