"""
Tests for number .digitSumCubes() method - sum of cubes of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSumCubes:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSumCubes_basic(self):
        output = self._run('print(123.digitSumCubes())')
        # 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
        assert output[-1] == "36"

    def test_digitSumCubes_single(self):
        output = self._run('print(4.digitSumCubes())')
        assert output[-1] == "64"
