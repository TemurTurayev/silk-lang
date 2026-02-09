"""
Tests for number .digitTrigintMin() method - min of each consecutive 30-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrigintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrigintMin_basic(self):
        output = self._run('print(111111111111111111111111111111.digitTrigintMin())')
        assert output[-1] == "[1]"

    def test_digitTrigintMin_remainder(self):
        output = self._run('print(1111111111111111111111111111119.digitTrigintMin())')
        assert output[-1] == "[1, 9]"
