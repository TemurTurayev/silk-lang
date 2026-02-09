"""
Tests for number .digitSeptenvigintSum() method - sum of each consecutive 27-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptenvigintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptenvigintSum_basic(self):
        output = self._run('print(111111111111111111111111111.digitSeptenvigintSum())')
        assert output[-1] == "[27]"

    def test_digitSeptenvigintSum_remainder(self):
        output = self._run('print(1111111111111111111111111115.digitSeptenvigintSum())')
        assert output[-1] == "[27, 5]"
