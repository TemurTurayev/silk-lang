"""
Tests for number .digitSexvigintProduct() method - product of each consecutive 26-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSexvigintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSexvigintProduct_basic(self):
        output = self._run('print(11111111111111111111111111.digitSexvigintProduct())')
        assert output[-1] == "[1]"

    def test_digitSexvigintProduct_remainder(self):
        output = self._run('print(111111111111111111111111113.digitSexvigintProduct())')
        assert output[-1] == "[1, 3]"
