"""
Tests for number .digitUntrigintMin() method - min of each consecutive 31-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUntrigintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUntrigintMin_basic(self):
        output = self._run('print(1111111111111111111111111111111.digitUntrigintMin())')
        assert output[-1] == "[1]"

    def test_digitUntrigintMin_remainder(self):
        output = self._run('print(11111111111111111111111111111119.digitUntrigintMin())')
        assert output[-1] == "[1, 9]"
