"""
Tests for number .digitNovemdecProduct() method - product of each consecutive 19-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitNovemdecProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitNovemdecProduct_basic(self):
        output = self._run('print(1211121112111211121.digitNovemdecProduct())')
        # 19 digits: 1,2,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,2,1 => product = 2^5 = 32
        assert output[-1] == "[32]"

    def test_digitNovemdecProduct_remainder(self):
        output = self._run('print(12111211121112111215.digitNovemdecProduct())')
        # product(...)=32, product(5)=5
        assert output[-1] == "[32, 5]"
