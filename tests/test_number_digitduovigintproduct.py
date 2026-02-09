"""
Tests for number .digitDuovigintProduct() method - product of each consecutive 22-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuovigintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuovigintProduct_basic(self):
        output = self._run('print(2222222222222222222222.digitDuovigintProduct())')
        assert output[-1] == "[4194304]"

    def test_digitDuovigintProduct_remainder(self):
        output = self._run('print(22222222222222222222223.digitDuovigintProduct())')
        # product(2*22)=2^22=4194304, product(3)=3
        assert output[-1] == "[4194304, 3]"
