"""
Tests for number .digitTrequadragintAvg() method - average of each consecutive 43-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrequadragintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrequadragintAvg_basic(self):
        output = self._run('print(1111111111111111111111111111111111111111111.digitTrequadragintAvg())')
        assert output[-1] == "[1]"

    def test_digitTrequadragintAvg_remainder(self):
        output = self._run('print(11111111111111111111111111111111111111111119.digitTrequadragintAvg())')
        assert output[-1] == "[1, 9]"
