"""
Tests for number .digitDecProduct() method - product of each consecutive 10-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDecProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDecProduct_basic(self):
        output = self._run('print(12345678911234567891.digitDecProduct())')
        # [1*2*3*4*5*6*7*8*9*1=362880, 1*2*3*4*5*6*7*8*9*1=362880]
        assert output[-1] == "[362880, 362880]"

    def test_digitDecProduct_remainder(self):
        output = self._run('print(123456789112.digitDecProduct())')
        # [1*2*3*4*5*6*7*8*9*1=362880, 1*2=2]
        assert output[-1] == "[362880, 2]"
