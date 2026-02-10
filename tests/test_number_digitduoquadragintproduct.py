"""
Tests for number .digitDuoquadragintProduct() method - product of each consecutive 42-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuoquadragintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuoquadragintProduct_basic(self):
        output = self._run('print(222222222222222222222222222222222222222222.digitDuoquadragintProduct())')
        assert output[-1] == "[4398046511104]"

    def test_digitDuoquadragintProduct_remainder(self):
        output = self._run('print(2222222222222222222222222222222222222222223.digitDuoquadragintProduct())')
        assert output[-1] == "[4398046511104, 3]"
