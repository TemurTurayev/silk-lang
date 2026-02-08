"""
Tests for number .digitVariance() method - variance of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitVariance:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitVariance_equal(self):
        output = self._run('print(333.digitVariance())')
        assert output[-1] == "0"

    def test_digitVariance_varied(self):
        output = self._run('print(13.digitVariance())')
        # Var(1,3) = ((1-2)^2 + (3-2)^2)/2 = 1
        assert output[-1] == "1"
