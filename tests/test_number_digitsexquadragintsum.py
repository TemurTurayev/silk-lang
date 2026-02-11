"""
Tests for number .digitSexquadragintSum() method - sum of each consecutive 46-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSexquadragintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSexquadragintSum_basic(self):
        output = self._run('print(1111111111111111111111111111111111111111111111.digitSexquadragintSum())')
        assert output[-1] == "[46]"

    def test_digitSexquadragintSum_remainder(self):
        output = self._run('print(11111111111111111111111111111111111111111111119.digitSexquadragintSum())')
        assert output[-1] == "[46, 9]"
