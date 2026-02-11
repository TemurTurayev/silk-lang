"""
Tests for number .digitTrequadragintMax() method - max of each consecutive 43-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrequadragintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrequadragintMax_basic(self):
        output = self._run('print(1111111111111111111111111111111111111111111.digitTrequadragintMax())')
        assert output[-1] == "[1]"

    def test_digitTrequadragintMax_remainder(self):
        output = self._run('print(11111111111111111111111111111111111111111119.digitTrequadragintMax())')
        assert output[-1] == "[1, 9]"
