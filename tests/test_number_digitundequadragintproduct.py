"""
Tests for number .digitUndequadragintProduct() method - product of each consecutive 39-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndequadragintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndequadragintProduct_basic(self):
        output = self._run('print(222222222222222222222222222222222222222.digitUndequadragintProduct())')
        assert output[-1] == "[" + str(2**39) + "]"

    def test_digitUndequadragintProduct_remainder(self):
        output = self._run('print(2222222222222222222222222222222222222223.digitUndequadragintProduct())')
        assert output[-1] == "[" + str(2**39) + ", 3]"
