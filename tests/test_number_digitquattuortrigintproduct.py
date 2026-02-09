"""
Tests for number .digitQuattuortrigintProduct() method - product of each consecutive 34-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuortrigintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuortrigintProduct_basic(self):
        output = self._run('print(2222222222222222222222222222222222.digitQuattuortrigintProduct())')
        assert output[-1] == "[" + str(2**34) + "]"

    def test_digitQuattuortrigintProduct_remainder(self):
        output = self._run('print(22222222222222222222222222222222225.digitQuattuortrigintProduct())')
        assert output[-1] == "[" + str(2**34) + ", 5]"
