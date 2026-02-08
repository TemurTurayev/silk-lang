"""
Tests for number .digitQuadSum() method - sum of each consecutive quadruple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuadSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuadSum_basic(self):
        output = self._run('print(12345678.digitQuadSum())')
        # [1+2+3+4=10, 5+6+7+8=26]
        assert output[-1] == "[10, 26]"

    def test_digitQuadSum_remainder(self):
        output = self._run('print(123456.digitQuadSum())')
        # [1+2+3+4=10, 5+6=11]
        assert output[-1] == "[10, 11]"
