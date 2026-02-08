"""
Tests for number .digitUndecProduct() method - product of each consecutive 11-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndecProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndecProduct_basic(self):
        output = self._run('print(1234567891112345678911.digitUndecProduct())')
        # [1*2*3*4*5*6*7*8*9*1*1=362880, 1*2*3*4*5*6*7*8*9*1*1=362880]
        assert output[-1] == "[362880, 362880]"

    def test_digitUndecProduct_remainder(self):
        output = self._run('print(1234567891112.digitUndecProduct())')
        # [1*2*3*4*5*6*7*8*9*1*1=362880, 1*2=2]
        assert output[-1] == "[362880, 2]"
