"""
Tests for number .digitSeptentrigintMax() method - max of each consecutive 37-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptentrigintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptentrigintMax_basic(self):
        output = self._run('print(1111111111111111111111111111111111111.digitSeptentrigintMax())')
        assert output[-1] == "[1]"

    def test_digitSeptentrigintMax_remainder(self):
        output = self._run('print(11111111111111111111111111111111111119.digitSeptentrigintMax())')
        assert output[-1] == "[1, 9]"
