"""
Tests for number .digitQuintProduct() method - product of each consecutive quintuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuintProduct_basic(self):
        output = self._run('print(1234512345.digitQuintProduct())')
        # [1*2*3*4*5=120, 1*2*3*4*5=120]
        assert output[-1] == "[120, 120]"

    def test_digitQuintProduct_remainder(self):
        output = self._run('print(1234523.digitQuintProduct())')
        # [1*2*3*4*5=120, 2*3=6]
        assert output[-1] == "[120, 6]"
