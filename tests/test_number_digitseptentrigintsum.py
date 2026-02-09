"""
Tests for number .digitSeptentrigintSum() method - sum of each consecutive 37-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptentrigintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptentrigintSum_basic(self):
        output = self._run('print(1111111111111111111111111111111111111.digitSeptentrigintSum())')
        assert output[-1] == "[37]"

    def test_digitSeptentrigintSum_remainder(self):
        output = self._run('print(11111111111111111111111111111111111112.digitSeptentrigintSum())')
        assert output[-1] == "[37, 2]"
