"""
Tests for number .digitSextProduct() method - product of each consecutive sextuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSextProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSextProduct_basic(self):
        output = self._run('print(123123123123.digitSextProduct())')
        # [1*2*3*1*2*3=36, 1*2*3*1*2*3=36]
        assert output[-1] == "[36, 36]"

    def test_digitSextProduct_remainder(self):
        output = self._run('print(12312324.digitSextProduct())')
        # [1*2*3*1*2*3=36, 2*4=8]
        assert output[-1] == "[36, 8]"
