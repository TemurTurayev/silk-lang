"""
Tests for number .digitQuinvigintMin() method - min of each consecutive 25-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuinvigintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuinvigintMin_basic(self):
        output = self._run('print(1111111111111111111111111.digitQuinvigintMin())')
        assert output[-1] == "[1]"

    def test_digitQuinvigintMin_remainder(self):
        output = self._run('print(11111111111111111111111110.digitQuinvigintMin())')
        assert output[-1] == "[1, 0]"
