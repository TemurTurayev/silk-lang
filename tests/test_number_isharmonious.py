"""
Tests for number .isHarmonious() method - check if harmonic mean of divisors is integer.
Also known as harmonic divisor number or Ore number.
Examples: 1, 6, 28, 140, 270, 496, ...
"""

from silk.interpreter import Interpreter


class TestNumberIsHarmonious:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isHarmonious_6(self):
        output = self._run('print(6.isHarmonious())')
        assert output[-1] == "true"

    def test_isHarmonious_5(self):
        output = self._run('print(5.isHarmonious())')
        assert output[-1] == "false"
