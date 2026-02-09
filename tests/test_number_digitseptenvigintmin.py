"""
Tests for number .digitSeptenvigintMin() method - min of each consecutive 27-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptenvigintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptenvigintMin_basic(self):
        output = self._run('print(111111111111111111111111111.digitSeptenvigintMin())')
        assert output[-1] == "[1]"

    def test_digitSeptenvigintMin_remainder(self):
        output = self._run('print(1111111111111111111111111119.digitSeptenvigintMin())')
        assert output[-1] == "[1, 9]"
