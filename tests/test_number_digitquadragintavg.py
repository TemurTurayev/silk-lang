"""
Tests for number .digitQuadragintAvg() method - average of each consecutive 40-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuadragintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuadragintAvg_basic(self):
        output = self._run('print(2222222222222222222222222222222222222222.digitQuadragintAvg())')
        assert output[-1] == "[2]"

    def test_digitQuadragintAvg_remainder(self):
        output = self._run('print(22222222222222222222222222222222222222225.digitQuadragintAvg())')
        assert output[-1] == "[2, 5]"
