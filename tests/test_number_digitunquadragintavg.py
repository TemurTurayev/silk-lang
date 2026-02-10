"""
Tests for number .digitUnquadragintAvg() method - average of each consecutive 41-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUnquadragintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUnquadragintAvg_basic(self):
        output = self._run('print(11111111111111111111111111111111111111111.digitUnquadragintAvg())')
        assert output[-1] == "[1]"

    def test_digitUnquadragintAvg_remainder(self):
        output = self._run('print(111111111111111111111111111111111111111119.digitUnquadragintAvg())')
        assert output[-1] == "[1, 9]"
