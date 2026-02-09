"""
Tests for number .digitUntrigintProduct() method - product of each consecutive 31-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUntrigintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUntrigintProduct_basic(self):
        output = self._run('print(2222222222222222222222222222222.digitUntrigintProduct())')
        assert output[-1] == "[2147483648]"

    def test_digitUntrigintProduct_remainder(self):
        output = self._run('print(22222222222222222222222222222223.digitUntrigintProduct())')
        assert output[-1] == "[2147483648, 3]"
