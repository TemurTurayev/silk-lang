"""
Tests for number .digitSkewness() method - skewness of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSkewness:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSkewness_symmetric(self):
        output = self._run('print(333.digitSkewness())')
        assert output[-1] == "0"

    def test_digitSkewness_asymmetric(self):
        output = self._run('print(135.digitSkewness())')
        # digits 1,3,5 => mean=3, std=sqrt(8/3), skew=0 (symmetric)
        assert output[-1] == "0"
