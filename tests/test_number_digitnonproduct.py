"""
Tests for number .digitNonProduct() method - product of each consecutive 9-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitNonProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitNonProduct_basic(self):
        output = self._run('print(123456789123456789.digitNonProduct())')
        # [1*2*3*4*5*6*7*8*9=362880, 1*2*3*4*5*6*7*8*9=362880]
        assert output[-1] == "[362880, 362880]"

    def test_digitNonProduct_remainder(self):
        output = self._run('print(12345678912.digitNonProduct())')
        # [1*2*3*4*5*6*7*8*9=362880, 1*2=2]
        assert output[-1] == "[362880, 2]"
