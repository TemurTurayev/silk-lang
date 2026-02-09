"""
Tests for number .digitQuadragintMin() method - min of each consecutive 40-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuadragintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuadragintMin_basic(self):
        output = self._run('print(1111111111111111111111111111111111111111.digitQuadragintMin())')
        assert output[-1] == "[1]"

    def test_digitQuadragintMin_remainder(self):
        output = self._run('print(11111111111111111111111111111111111111110.digitQuadragintMin())')
        assert output[-1] == "[1, 0]"
