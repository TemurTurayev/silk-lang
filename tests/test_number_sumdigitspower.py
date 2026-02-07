"""
Tests for number .sumOfDigitsPower(p) method.
"""

from silk.interpreter import Interpreter


class TestNumberSumOfDigitsPower:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_sumOfDigitsPower_basic(self):
        output = self._run('print(123.sumOfDigitsPower(2))')
        assert output[-1] == "14"

    def test_sumOfDigitsPower_cubes(self):
        output = self._run('print(153.sumOfDigitsPower(3))')
        assert output[-1] == "153"
