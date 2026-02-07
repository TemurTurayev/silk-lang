"""
Tests for number .digitProduct() method.
"""

from silk.interpreter import Interpreter


class TestNumberDigitProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitProduct_basic(self):
        output = self._run('print(234.digitProduct())')
        assert output[-1] == "24"

    def test_digitProduct_with_zero(self):
        output = self._run('print(102.digitProduct())')
        assert output[-1] == "0"

    def test_digitProduct_single(self):
        output = self._run('print(7.digitProduct())')
        assert output[-1] == "7"
