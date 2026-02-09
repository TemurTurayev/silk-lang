"""
Tests for number .digitTrigintProduct() method - product of each consecutive 30-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrigintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrigintProduct_basic(self):
        output = self._run('print(111111111111111111111111111111.digitTrigintProduct())')
        assert output[-1] == "[1]"

    def test_digitTrigintProduct_remainder(self):
        output = self._run('print(1111111111111111111111111111113.digitTrigintProduct())')
        assert output[-1] == "[1, 3]"
