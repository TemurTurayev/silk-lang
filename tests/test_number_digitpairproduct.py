"""
Tests for number .digitPairProduct() method - product of each consecutive pair of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitPairProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitPairProduct_basic(self):
        output = self._run('print(1234.digitPairProduct())')
        # [1*2, 3*4] = [2, 12]
        assert output[-1] == "[2, 12]"

    def test_digitPairProduct_odd(self):
        output = self._run('print(12345.digitPairProduct())')
        # [1*2, 3*4, 5] = [2, 12, 5]
        assert output[-1] == "[2, 12, 5]"
