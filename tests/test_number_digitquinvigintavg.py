"""
Tests for number .digitQuinvigintAvg() method - avg of each consecutive 25-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuinvigintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuinvigintAvg_basic(self):
        output = self._run('print(1111111111111111111111111.digitQuinvigintAvg())')
        assert output[-1] == "[1]"

    def test_digitQuinvigintAvg_remainder(self):
        output = self._run('print(11111111111111111111111115.digitQuinvigintAvg())')
        assert output[-1] == "[1, 5]"
