"""
Tests for number .digitTrequadragintMin() method - min of each consecutive 43-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrequadragintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrequadragintMin_basic(self):
        output = self._run('print(1111111111111111111111111111111111111111111.digitTrequadragintMin())')
        assert output[-1] == "[1]"

    def test_digitTrequadragintMin_remainder(self):
        output = self._run('print(11111111111111111111111111111111111111111119.digitTrequadragintMin())')
        assert output[-1] == "[1, 9]"
