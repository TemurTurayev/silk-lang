"""
Tests for number .digitUnvigintProduct() method - product of each consecutive 21-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUnvigintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUnvigintProduct_basic(self):
        output = self._run('print(111111111111111111111.digitUnvigintProduct())')
        assert output[-1] == "[1]"

    def test_digitUnvigintProduct_remainder(self):
        output = self._run('print(1111111111111111111115.digitUnvigintProduct())')
        # product(1*21)=1, product(5)=5
        assert output[-1] == "[1, 5]"
