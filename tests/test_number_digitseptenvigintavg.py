"""
Tests for number .digitSeptenvigintAvg() method - average of each consecutive 27-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptenvigintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptenvigintAvg_basic(self):
        output = self._run('print(111111111111111111111111111.digitSeptenvigintAvg())')
        assert output[-1] == "[1]"

    def test_digitSeptenvigintAvg_remainder(self):
        output = self._run('print(222222222222222222222222222.digitSeptenvigintAvg())')
        assert output[-1] == "[2]"
