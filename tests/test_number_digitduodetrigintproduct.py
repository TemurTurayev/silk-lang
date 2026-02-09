"""
Tests for number .digitDuodetrigintProduct() method - product of each consecutive 28-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodetrigintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodetrigintProduct_basic(self):
        output = self._run('print(1111111111111111111111111111.digitDuodetrigintProduct())')
        assert output[-1] == "[1]"

    def test_digitDuodetrigintProduct_remainder(self):
        output = self._run('print(22222222222222222222222222225.digitDuodetrigintProduct())')
        assert output[-1] == "[268435456, 5]"
