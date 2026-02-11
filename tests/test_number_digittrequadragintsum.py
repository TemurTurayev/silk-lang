"""
Tests for number .digitTrequadragintSum() method - sum of each consecutive 43-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrequadragintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrequadragintSum_basic(self):
        output = self._run('print(1111111111111111111111111111111111111111111.digitTrequadragintSum())')
        assert output[-1] == "[43]"

    def test_digitTrequadragintSum_remainder(self):
        output = self._run('print(11111111111111111111111111111111111111111119.digitTrequadragintSum())')
        assert output[-1] == "[43, 9]"
