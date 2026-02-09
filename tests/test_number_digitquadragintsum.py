"""
Tests for number .digitQuadragintSum() method - sum of each consecutive 40-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuadragintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuadragintSum_basic(self):
        output = self._run('print(1111111111111111111111111111111111111111.digitQuadragintSum())')
        assert output[-1] == "[40]"

    def test_digitQuadragintSum_remainder(self):
        output = self._run('print(11111111111111111111111111111111111111115.digitQuadragintSum())')
        assert output[-1] == "[40, 5]"
