"""
Tests for number .digitCubeSum() method - sum of cubes of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitCubeSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitCubeSum_basic(self):
        output = self._run('print(123.digitCubeSum())')
        assert output[-1] == "36"

    def test_digitCubeSum_single(self):
        output = self._run('print(3.digitCubeSum())')
        assert output[-1] == "27"
