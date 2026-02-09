"""
Tests for number .digitDuodetrigintMin() method - min of each consecutive 28-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodetrigintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodetrigintMin_basic(self):
        output = self._run('print(1111111111111111111111111111.digitDuodetrigintMin())')
        assert output[-1] == "[1]"

    def test_digitDuodetrigintMin_remainder(self):
        output = self._run('print(11111111111111111111111111119.digitDuodetrigintMin())')
        assert output[-1] == "[1, 9]"
