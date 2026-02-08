"""
Tests for number .digitOctProduct() method - product of each consecutive octuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitOctProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitOctProduct_basic(self):
        output = self._run('print(1234567812345678.digitOctProduct())')
        # [1*2*3*4*5*6*7*8=40320, 1*2*3*4*5*6*7*8=40320]
        assert output[-1] == "[40320, 40320]"

    def test_digitOctProduct_remainder(self):
        output = self._run('print(1234567890.digitOctProduct())')
        # [1*2*3*4*5*6*7*8=40320, 9*0=0]
        assert output[-1] == "[40320, 0]"
