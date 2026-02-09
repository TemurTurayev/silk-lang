"""
Tests for number .digitQuintrigintProduct() method - product of each consecutive 35-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuintrigintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuintrigintProduct_basic(self):
        output = self._run('print(11111111111111111111111111111111111.digitQuintrigintProduct())')
        assert output[-1] == "[1]"

    def test_digitQuintrigintProduct_remainder(self):
        output = self._run('print(222222222222222222222222222222222225.digitQuintrigintProduct())')
        assert output[-1] == "[" + str(2**35) + ", 5]"
