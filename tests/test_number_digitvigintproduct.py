"""
Tests for number .digitVigintProduct() method - product of each consecutive 20-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitVigintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitVigintProduct_basic(self):
        output = self._run('print(12111211121112111211.digitVigintProduct())')
        # 20 digits: 1,2,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,2,1,1 => product = 2^5 = 32
        assert output[-1] == "[32]"

    def test_digitVigintProduct_remainder(self):
        output = self._run('print(121112111211121112115.digitVigintProduct())')
        # product(...)=32, product(5)=5
        assert output[-1] == "[32, 5]"
