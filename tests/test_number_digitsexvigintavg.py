"""
Tests for number .digitSexvigintAvg() method - average of each consecutive 26-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSexvigintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSexvigintAvg_basic(self):
        output = self._run('print(11111111111111111111111111.digitSexvigintAvg())')
        assert output[-1] == "[1]"

    def test_digitSexvigintAvg_remainder(self):
        output = self._run('print(222222222222222222222222222.digitSexvigintAvg())')
        assert output[-1] == "[2, 2]"
