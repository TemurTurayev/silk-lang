"""
Tests for number .digitUndetrigintProduct() method - product of each consecutive 29-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndetrigintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndetrigintProduct_basic(self):
        output = self._run('print(11111111111111111111111111111.digitUndetrigintProduct())')
        assert output[-1] == "[1]"

    def test_digitUndetrigintProduct_remainder(self):
        output = self._run('print(111111111111111111111111111113.digitUndetrigintProduct())')
        assert output[-1] == "[1, 3]"
