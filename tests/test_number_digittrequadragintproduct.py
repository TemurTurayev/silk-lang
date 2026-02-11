"""
Tests for number .digitTrequadragintProduct() method - product of each consecutive 43-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrequadragintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrequadragintProduct_basic(self):
        output = self._run('print(2222222222222222222222222222222222222222222.digitTrequadragintProduct())')
        assert output[-1] == "[8796093022208]"

    def test_digitTrequadragintProduct_remainder(self):
        output = self._run('print(22222222222222222222222222222222222222222223.digitTrequadragintProduct())')
        assert output[-1] == "[8796093022208, 3]"
