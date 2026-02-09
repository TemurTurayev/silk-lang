"""
Tests for number .digitSeptenvigintMax() method - max of each consecutive 27-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptenvigintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptenvigintMax_basic(self):
        output = self._run('print(111111111111111111111111111.digitSeptenvigintMax())')
        assert output[-1] == "[1]"

    def test_digitSeptenvigintMax_remainder(self):
        output = self._run('print(1111111111111111111111111119.digitSeptenvigintMax())')
        assert output[-1] == "[1, 9]"
