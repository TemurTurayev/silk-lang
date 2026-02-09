"""
Tests for number .digitSeptentrigintMin() method - min of each consecutive 37-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptentrigintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptentrigintMin_basic(self):
        output = self._run('print(1111111111111111111111111111111111111.digitSeptentrigintMin())')
        assert output[-1] == "[1]"

    def test_digitSeptentrigintMin_remainder(self):
        output = self._run('print(22222222222222222222222222222222222221.digitSeptentrigintMin())')
        assert output[-1] == "[2, 1]"
