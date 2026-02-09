"""
Tests for number .digitDuotrigintProduct() method - product of each consecutive 32-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuotrigintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuotrigintProduct_basic(self):
        output = self._run('print(22222222222222222222222222222222.digitDuotrigintProduct())')
        assert output[-1] == "[4294967296]"

    def test_digitDuotrigintProduct_remainder(self):
        output = self._run('print(222222222222222222222222222222223.digitDuotrigintProduct())')
        assert output[-1] == "[4294967296, 3]"
